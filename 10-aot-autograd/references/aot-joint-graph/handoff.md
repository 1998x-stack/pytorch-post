# Research → Olah

- 10-aot-autograd/aot-joint-graph; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 从动态 eager tape 到可交给编译器的 FX 图。观察 forward 的额外返回值如何成为 backward 的输入。
- Claims: aot-1, aot-2, aot-3; locators in research.json.
- Storyboard: 联合图包含 sin、mul、sum 和它们的导数操作。 → forward FX 返回 loss、x、sin(x)，其中后两者为保存值。 → backward FX 接收 x、sin(x)、输出 tangent，返回输入梯度。
- Runnable 10-aot-autograd/minimal-implementation/aot-joint-graph/demo.py; log 10-aot-autograd/experiments/aot-joint-graph/cpu.log
- Scope: PyTorch 2.10 CPU aot_function 默认 partition_fn；真实捕获 FX 图并执行，不运行 Inductor 或 min-cut 性能实验。
- handoff-ready for declared CPU/source scope; publication gated by QA.
