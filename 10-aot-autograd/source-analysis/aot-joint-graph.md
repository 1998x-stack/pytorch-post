# AOTAutograd：联合图、前反向分区与保存值 — 固定源码

PyTorch 2.10.0+cpu git_version 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。

- [aot_function interface, joint trace and partition](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/_functorch/aot_autograd.py#L713-L770) — torch/_functorch/aot_autograd.py:713–770
- [default_partition and stashed activations](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/_functorch/partitioners.py#L1013-L1050) — torch/_functorch/partitioners.py:1013–1050

- AOTAutograd captures joint forward/backward graphs; functionalization and decomposition simplify graph representation, and partitioning separates forward and backward. 限制：Historical 2024 design and 2.10 API; exact transformation details depend on path and options.
- aot_function defaults to default_partition; stashed tensors are forward outputs consumed by the backward graph. Min-cut rematerialization is a separate configurable policy. 限制：The example uses default partition, not a measured or executed min-cut policy.
- For f(x)=sum(x*sin(x)), the captured forward FX returns sum, primal and sin; backward graph has primal, sin and tangent inputs. CPU gradient matches eager. 限制：Single fixed-shape real CPU example; callbacks return executable FX, not optimized machine code.
