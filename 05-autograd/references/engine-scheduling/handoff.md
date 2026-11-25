# Research → Olah

- Component: 05-autograd; topic: engine-scheduling; revision: 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- Question: 同一个中间结果被两个分支共享时，谁来决定 backward 的执行顺序？从依赖计数到 GraphTask、InputBuffer 与 ReadyQueue。
- Claims: eng-1, eng-2, eng-3；见 research.json。
- Storyboard: 等待：依赖=2，buffer=0 → 收到贡献 3：依赖=1，buffer=3，不调度 → 收到贡献 4：依赖=0，buffer=7，执行 a 的反向；x.grad=14；原始 SVG 与可交互状态。
- Runnable: 05-autograd/minimal-implementation/engine-scheduling/demo.py; logs: 05-autograd/experiments/engine-scheduling/cpu.log
- Exclusions: PyTorch 2.10 eager CPU backward 的简化共享节点调度；排除 compiled autograd、重入、GPU stream 详细调度；不报告未测性能数字。
- Research: handoff-ready；publication subject to independent QA.
