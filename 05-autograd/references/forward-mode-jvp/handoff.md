# Research → Olah

- 05-autograd/forward-mode-jvp; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 从切向量传播理解前向模式：一次计算得到 Jv，而非反向模式的 Jᵀu。
- Claims: jvp-1, jvp-2, jvp-3; locators in research.json.
- Storyboard: x=[2,3]，v=[4,5]，dual 携带原值和 tangent。 → 乘积：4×3+2×5=22；和：4+5=9。 → primal=[6,5]，JVP=[22,9]；退出 dual level 后 tangent 清除。
- Runnable 05-autograd/minimal-implementation/forward-mode-jvp/demo.py; log 05-autograd/experiments/forward-mode-jvp/cpu.log
- Scope: PyTorch 2.10 eager CPU 实数、单层 dual_level 与 torch.func.jvp；不涵盖全部算子、嵌套变换或 GPU。
- handoff-ready; publication gated by QA.
