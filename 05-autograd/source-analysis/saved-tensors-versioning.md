# SavedVariable：保存值、版本计数与原地修改 — 固定源码

PyTorch 2.10.0+cpu 对应提交 `449b1768410104d3ed79d3bcfe4ba1d65c7f22c0`；官方 GitHub commit 已核验，本地 wheel git_version 相同。

- [SavedVariable constructor](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/saved_variable.cpp#L17-L65) — saved_version_, inference tensor guard
- [SavedVariable::unpack](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/saved_variable.cpp#L130-L198) — undefined data and version check when hooks absent
- [Engine::evaluate_function](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/engine.cpp#L1130-L1235) — release_variables, dependencies_, not_ready_, queue->push

当 keep_graph_ 为 false，执行完反向函数后 Engine 调用 release_variables；SavedVariable::unpack 遇到未定义 data 且无 hooks 时检查重复 backward 错误。retain_graph=True 保留本次 backward 所需状态，但不是 create_graph=True：后者用于构建导数计算的图。[SV-2]对于 x*x，第一次保留图，第二次默认释放，两个梯度累积到 8；第三次报错。对于不需要保存中间值的简单算子，重复 backward 可能不报相同错误。2017 论文 §3/§3.1 提供设计背景，2.10 源码才是本文实现判断的依据。[SV-3]
