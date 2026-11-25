# 高阶自动微分：Hessian、HVP 与 create_graph — 固定源码

PyTorch 2.10.0+cpu git_version 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。

- [torch.autograd.grad create_graph and retain_graph](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/autograd/__init__.py#L375-L419) — torch/autograd/__init__.py:375–419
- [torch.func.hessian composition](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/_functorch/eager_transforms.py#L1312-L1351) — torch/_functorch/eager_transforms.py:1312–1351
- [JVP transform](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/_functorch/eager_transforms.py#L1080-L1125) — torch/_functorch/eager_transforms.py:1080–1125

- For a twice continuously differentiable scalar f, H v is JVP of grad(f); reverse differentiation of grad(f) with seed v returns H^T v, equal by symmetry. 限制：Real C² scalar f, fixed seed independent of x.
- torch.func.hessian returns jacfwd(jacrev(func)); autograd.grad(create_graph=True) constructs derivative graph, while retain_graph concerns freeing the original graph. 限制：Forward AD operator coverage may be incomplete.
- For f=x₁³+x₁x₂+x₂² at (2,3), grad=[15,8], H=[[12,1],[1,2]], and both HVP routes yield [53,14]; default create_graph=False rejects this second derivative. 限制：A polynomial CPU example only.
