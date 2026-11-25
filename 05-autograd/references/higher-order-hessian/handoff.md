# Research → Olah

- 05-autograd/higher-order-hessian; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 为什么不必构造 n×n Hessian 也能计算曲率方向？对梯度再次微分，比较 reverse-over-reverse 与 forward-over-reverse。
- Claims: hvp-1, hvp-2, hvp-3; locators in research.json.
- Storyboard: f 在 (2,3) 的梯度是 [15,8]。 → H=[[12,1],[1,2]]，对称矩阵。 → v=[4,5]：Hv=[53,14]；两种组合一致。
- Runnable 05-autograd/minimal-implementation/higher-order-hessian/demo.py; log 05-autograd/experiments/higher-order-hessian/cpu.log
- Scope: PyTorch 2.10 CPU 实数 C² 标量函数；二阶导数与 HVP；不涵盖非光滑、复数或全部 transform 兼容性。
- handoff-ready; publication gated by QA.
