# Reflection Review

- 校对 sv-1, sv-2, sv-3 与原始论文/固定源码行范围；明确历史设计与当前实现区别。
- 反证：saved tensor hooks 路径不能作相同保证。；并非所有不保存中间值的图第二次 backward 都必然报错。；仅针对本次 CPU float64 示例。
- 本地真实 CPU 执行 demo.py，输出见 05-autograd/experiments/saved-tensors-versioning/cpu.log；无 GPU 与性能结论。原始 demo Git blob SHA：435743cd48da05ec7961162ba367b3b1c2371108（待远端写入后对比）。
- 研究 handoff 范围限本文；不宣称生产引擎完整复现。HTML 发布须独立通过静态与浏览器 QA。
