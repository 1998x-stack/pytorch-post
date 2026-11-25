# Custom Autograd Function：定义自己的 VJP 与二阶梯度 — 固定源码

PyTorch wheel 2.10.0+cpu 的 git_version 为 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0，与已核验的源码版本一致。

- [FunctionCtx.save_for_backward](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/autograd/function.py#L40-L66) — torch/autograd/function.py:40–66
- [FunctionMeta builds backward class](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/autograd/function.py#L330-L347) — torch/autograd/function.py:330–347
- [Function.backward / VJP contract](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/autograd/function.py#L417-L449) — torch/autograd/function.py:417–449
- [Function.apply normal and transform paths](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/autograd/function.py#L568-L593) — torch/autograd/function.py:568–593
- [THPFunction_apply initialization and grad mode](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/python_function.cpp#L1334-L1396) — torch/csrc/autograd/python_function.cpp:1334–1396
- [PyNode::apply calls Python apply](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/python_function.cpp#L156-L173) — torch/csrc/autograd/python_function.cpp:156–173

- FunctionMeta creates a backward class; regular Function.apply delegates to C++ apply, which sets next edges and calls forward with grad mode disabled. PyNode::apply calls back into Python. 限制：Normal eager route; functorch transforms have a separate branch.
- backward receives one output gradient per output and returns gradients matching forward inputs; tensors for backward use save_for_backward. 限制：Non-Tensor scalar input returns None; higher-order support depends on differentiable backward and saved values.
