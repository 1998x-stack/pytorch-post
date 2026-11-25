# Forward-mode AD：Dual Tensor 与 JVP — 固定源码

PyTorch 2.10.0+cpu git_version 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。

- [forward_ad.make_dual / enter / exit](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/autograd/forward_ad.py#L23-L130) — torch/autograd/forward_ad.py:23–130
- [unpack_dual and dual_level](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/autograd/forward_ad.py#L141-L197) — torch/autograd/forward_ad.py:141–197
- [functorch JVP transform](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/_functorch/eager_transforms.py#L1080-L1125) — torch/_functorch/eager_transforms.py:1080–1125
- [AutogradMeta forward gradient](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/variable.h#L234-L243) — torch/csrc/autograd/variable.h:234–243

- For f: R^n→R^m, a tangent v∈R^n propagates as Jv∈R^m; a VJP instead maps an output cotangent back to input space. 限制：Real differentiable functions; no complexity claim for arbitrary kernels.
- make_dual embeds a tangent and aliases the primal; unpack_dual retrieves primal/tangent; exiting a dual level removes its associated gradients. torch.func.jvp constructs duals and unpacks outputs. 限制：The low-level API supports only one dual level; transforms have additional nesting logic.
- At x=[2,3] and v=[4,5], f(x)=[6,5], Jv=[22,9]; torch.func.jvp agrees with jacrev(f) @ v, and unpack after exiting returns no tangent. 限制：Small deterministic CPU example.
