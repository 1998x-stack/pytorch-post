# Research → Olah

- 02-tensor-storage/view-reshape-transpose; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 从 computeStride 的连续子块判定出发，理解非连续不等于不可 view，并追踪 reshape 的 clone fallback。
- Claims: view-1, view-2, view-3; locators in research.json.
- Storyboard: transpose: shape=(4,3)，stride=(1,4)，Storage 不变；flatten view 不兼容。 → reshape(-1) 复制为逻辑转置顺序：0,4,8,1,5,9,… → x[:,::2] stride=(4,2)，4=2×2，view(-1) 仍共享 Storage，stride=(2,)
- Runnable 02-tensor-storage/minimal-implementation/view-reshape-transpose/demo.py; log 02-tensor-storage/experiments/view-reshape-transpose/cpu.log
- Scope: PyTorch 2.10 普通非空 CPU dense strided Tensor，shape reshape overload；不涵盖 dtype view、特殊 layout 或符号形状分支。
- handoff-ready; publication gated by QA.
