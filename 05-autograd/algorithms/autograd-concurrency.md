# Autograd 并发：ReadyQueue、重入与 CUDA Stream — 机制与算法

## 区分三个不同的并发问题
两个 Python 线程同时调用 grad，是两个独立 GraphTask 的并发；一个 GraphTask 的 ready node 调度，是图内执行问题；CUDA stream 是设备异步执行与依赖问题。三者不能用同一条时间线解释。特别是 torch.set_num_threads 控制算子内部线程，不等于 Autograd worker 数。

## ReadyQueue 与重入
当一个 backward node 内部再次调用 grad，外层任务需要等待内层任务。如果负责队列的唯一 worker 阻塞，内层任务可能无法推进。Engine 的重入说明描述了 worker pool 协作处理这种情况；具体路径与设备、重入深度有关，不能把每次嵌套都说成创建新线程。CPU 队列和设备队列通过 ready_queue 分派。[CONC-1]独立输入分别求导避免共享 .grad 写入；共享叶子的梯度累积顺序和跨线程用户 hooks 的安全性仍须单独考虑。独立线程示例的 barrier 只保证两方到达求导入口，不能证明 kernel 或 C++ worker 实际重叠。

## CUDA 流与 producer-consumer 合约
设备上的反向算子通常遵循对应前向流；梯度从一个生产者交给另一个消费者时，InputBuffer 负责累积及相关同步的一部分，Engine 在消费者执行前处理另一部分。canonical stream 是节点约定，不等于全设备同步。首个贡献可直接移入缓冲；后续贡献需等待相关生产流、处理 record_stream 与累积，再更新 ready event。若在自定义流中执行 backward，再在其他流消费梯度，用户仍需建立正确的流依赖。当前仅阅读了固定源码；没有 CUDA 硬件，因此不声称实测 stream overlap。[CONC-2]

## 实验与边界
两个 CPU 线程分别求 x² 的梯度，x=2 和 3；结果为 4、6。自定义 Function 内部用 enable_grad 构建独立内层图，nested grad 得到 6。detach 使这个例子只用于一阶行为验证，不保证二阶导数。[CONC-3]
