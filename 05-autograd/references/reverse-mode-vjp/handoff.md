# Research → Olah

- Component: 05-autograd; topic: reverse-mode-vjp; revision: 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- Question: 为什么一次 backward 能计算成千上万个参数的梯度？从一条分叉的标量计算路径开始，推导向量–雅可比积，再连接 PyTorch 的反向图。
- Claims: ad-1, ad-2, ad-3；见 research.json。
- Storyboard: 前向：x=2，a=4，b=6，L=10 → 反向：L→a、b 各传 1；a→x 贡献 4，b→x 贡献 3；总梯度 7；原始 SVG 与可交互状态。
- Runnable: 05-autograd/minimal-implementation/reverse-mode-vjp/demo.py; logs: 05-autograd/experiments/reverse-mode-vjp/cpu.log
- Exclusions: 实数、CPU eager、一阶反向微分；标量 loss 与显式种子的向量输出；不报告未测性能数字。
- Research: handoff-ready；publication subject to independent QA.
