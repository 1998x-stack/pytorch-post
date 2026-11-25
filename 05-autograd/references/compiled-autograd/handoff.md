# Research → Olah

- 05-autograd/compiled-autograd; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 为什么 AOTAutograd 仍不能捕获所有运行时反向逻辑？观察 Compiled Autograd 对 hook 和梯度累积的真实 FX 捕获。
- Claims: ca-1, ca-2, ca-3; locators in research.json.
- Storyboard: 动态引擎访问 SumBackward、tensor hook 与 PowBackward。 → FX 图包含真实 call_hook，输出余切从 [1,1] 变为 [3,3]。 → call_accumulate_grad 更新 x.grad=[12,18]；与 eager 对照一致。
- Runnable 05-autograd/minimal-implementation/compiled-autograd/demo.py; log 05-autograd/experiments/compiled-autograd/cpu.log
- Scope: PyTorch 2.10 CPU，私有 _enable 捕获接口与 FX 执行回调；无优化后端、CUDA 或跨 graph-break 实测。
- handoff-ready for declared CPU/source scope; publication gated by QA.
