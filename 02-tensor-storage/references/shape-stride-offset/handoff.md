# Research → Olah

- 02-tensor-storage/shape-stride-offset; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 一条仿射地址公式统一解释切片、转置和零步长，并从 storage 范围推导越界条件。
- Claims: stride-1, stride-2, stride-3; locators in research.json.
- Storyboard: (2,3) stride=(4,1) offset=1 → [1,2,3,5,6,7] → (3,2) stride=(1,4) offset=1 → [1,5,2,6,3,7] → (2,3) stride=(0,1) offset=2 → [2,3,4,2,3,4]
- Runnable 02-tensor-storage/minimal-implementation/shape-stride-offset/demo.py; log 02-tensor-storage/experiments/shape-stride-offset/cpu.log
- Scope: 非空普通 CPU strided int64，非负 stride；示例覆盖零步长读取，不执行重叠写入，不推及 sparse/meta/符号形状。
- handoff-ready; publication gated by QA.
