# Autograd 对象模型：Tensor、AutogradMeta、Node 与 Edge — 固定源码

PyTorch wheel 2.10.0+cpu 的 git_version 为 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0，与已核验的源码版本一致。

- [TensorImpl: optional AutogradMetaInterface](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/c10/core/TensorImpl.h#L2894-L2914) — c10/core/TensorImpl.h:2894–2914
- [AutogradMeta fields and output_nr](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/variable.h#L227-L305) — torch/csrc/autograd/variable.h:227–305
- [Leaf accumulator and gradient_edge](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/variable.cpp#L289-L335) — torch/csrc/autograd/variable.cpp:289–335
- [Edge definition](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/edge.h#L13-L39) — torch/csrc/autograd/edge.h:13–39
- [Node outgoing edges](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/function.h#L298-L325) — torch/csrc/autograd/function.h:298–325

- TensorImpl can hold an optional AutogradMetaInterface; AutogradMeta holds grad_, grad_fn_, weak grad_accumulator_ and output_nr_. 限制：Optional metadata is not a separately allocated object for every Tensor.
- Canonical gradient_edge uses grad_fn and output_nr for interior tensors, or a leaf gradient accumulator with slot 0; Edge stores target Node and input_nr. 限制：Only differentiable relevant tensors; view history may be rebased.
