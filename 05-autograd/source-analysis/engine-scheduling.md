# Autograd Engine：依赖计数与梯度汇聚 — 固定源码

PyTorch 2.10.0+cpu 对应提交 `449b1768410104d3ed79d3bcfe4ba1d65c7f22c0`；官方 GitHub commit 已核验，本地 wheel git_version 相同。

- [Engine::execute](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/engine.cpp#L1288-L1387) — root handling, GraphTask, compute_dependencies, queue root
- [Engine::evaluate_function](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/engine.cpp#L1130-L1235) — release_variables, dependencies_, not_ready_, queue->push
- [InputBuffer::add](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/input_buffer.cpp#L192-L216) — CPU branch, InputBuffer::add
- [AccumulateGrad_apply_impl](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/functions/accumulate_grad.cpp#L21-L50) — guard, locking, accumulateGrad

GraphTask一次 backward 的任务状态，包括依赖、未就绪缓冲区以及是否保留图等。InputBuffer以输入槽位为单位接收和累积梯度，CPU 分支可直接移动首份梯度，后续贡献执行累积。ReadyQueue / NodeTask依赖满足后，将 Node 与输入缓冲区交给执行队列。它不是 Python 前向操作的简单反序列表。调用链：Python backward → Engine::execute → 创建 GraphTask → compute_dependencies → execute_with_graph_task → evaluate_function → InputBuffer / ReadyQueue。单根 eager 路径可以跳过虚拟 GraphRoot。[ENG-1]

分支贡献在同一次反向中的 InputBuffer 聚合，与叶子 .grad 跨多次 backward 的累积不是同一个动作。前者协调 Node 就绪；后者由 AccumulateGrad 等处理。因此训练循环通常显式清零参数梯度。实验先得到 a.grad=7（调用 retain_grad），x.grad=14；在新图执行 (2*x).backward() 后，x.grad=16。本文只展示可验证的 CPU 简化图，不宣称多线程实际顺序固定；GPU stream 同步、设备队列、重入与 compiled autograd 是后续主题。浮点加法一般不满足严格结合律，toy 的整数结果不能证明任意顺序数值完全相等。[ENG-3]
