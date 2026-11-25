# Activation Checkpoint：重计算、早停与 RNG — 固定源码

PyTorch 2.10.0+cpu git_version 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。

- [CheckpointFunction forward/backward](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/utils/checkpoint.py#L228-L315) — torch/utils/checkpoint.py:228–315
- [checkpoint variant documentation](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/utils/checkpoint.py#L349-L420) — torch/utils/checkpoint.py:349–420
- [_recomputation_hook early stop](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/utils/checkpoint.py#L1081-L1120) — torch/utils/checkpoint.py:1081–1120
- [_checkpoint_hook pack/unpack](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/utils/checkpoint.py#L1142-L1195) — torch/utils/checkpoint.py:1142–1195
- [Non-reentrant generator and RNG restoration](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/utils/checkpoint.py#L1550-L1615) — torch/utils/checkpoint.py:1550–1615

- For equal-sized sequential layers split into k segments, Chen et al. derive activation storage O(n/k+k), minimized in order at k≈sqrt(n). 限制：Idealized equal-size sequential activation model, not measured total GPU memory or universal guarantee.
- Reentrant uses a custom Function, no_grad forward and whole-function recomputation; non-reentrant uses saved tensor hooks and can stop when needed tensors are restored. RNG preservation forks/restores CPU and supported device state. 限制：Early-stop, device, stochastic and mutable-state constraints matter.
- Plain, non-reentrant and reentrant produce [32,108] gradients. The non-reentrant trace ends at a second enter, reentrant reaches second exit; fixed-seed Dropout output, gradient and CPU RNG state match baseline. 限制：Specific block and CPU seed 17; not an actual memory or timing benchmark.
