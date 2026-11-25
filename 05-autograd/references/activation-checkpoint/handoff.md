# Research → Olah

- 05-autograd/activation-checkpoint; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 用计算换取激活存储：从分段模型的 O(√n) 推导，到 PyTorch reentrant 与 non-reentrant 的真实执行差异。
- Claims: ckpt-1, ckpt-2, ckpt-3; locators in research.json.
- Storyboard: 普通：enter→exit，一次 forward；梯度 [32,108]。 → non-reentrant：enter→exit→enter，在本例最后一次 exit 前早停；梯度一致。 → reentrant：enter→exit→enter→exit，完整重算；梯度一致。
- Runnable 05-autograd/minimal-implementation/activation-checkpoint/demo.py; log 05-autograd/experiments/activation-checkpoint/cpu.log
- Scope: PyTorch 2.10 CPU eager checkpoint，确定性平方块与固定种子 Dropout；不测 GPU 峰值显存、耗时或分布式。
- handoff-ready; publication gated by QA.
