# Research → Olah

- 05-autograd/autograd-object-model; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- Tensor 的 grad_fn 究竟指向什么？以多输出算子为例，分清张量元数据、反向节点、梯度槽位和叶子梯度累积器。
- Verified claims: obj-1, obj-2, obj-3; locators in research.json.
- Storyboard: u 和 v 共用 UnbindBackward0；output_nr = 0 与 1。 → 输入槽 0 收到 3，槽 1 收到 4；UnbindBackward0 还原 [3,4]。 → MulBackward0 将 [3,4] 乘 2，叶子 x.grad = [6,8]。
- Runnable 05-autograd/minimal-implementation/autograd-object-model/demo.py; log 05-autograd/experiments/autograd-object-model/cpu.log.
- Scope and exclusions: PyTorch 2.10 eager CPU，普通实数 Tensor 与多输出 unbind；不覆盖 view rebase、forward AD、编译或特殊 Tensor subclass。; no measured performance claims.
- handoff-ready; publication gated by QA.
