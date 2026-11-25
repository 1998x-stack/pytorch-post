import torch

x = torch.tensor([2., 3.], dtype=torch.float64, requires_grad=True)
v = torch.tensor([4., 5.], dtype=x.dtype)
def f(z):
    return z[0]**3 + z[0]*z[1] + z[1]**2
loss = f(x)
g = torch.autograd.grad(loss, x, create_graph=True)[0]
hv = torch.autograd.grad(g, x, v)[0]
H = torch.func.hessian(f)(x.detach())
_, hv2 = torch.func.jvp(torch.func.grad(f), (x.detach(),), (v,))
expected = torch.tensor([[12., 1.], [1., 2.]], dtype=x.dtype)
assert torch.equal(H, expected) and torch.equal(hv, H @ v)
assert torch.equal(hv2, hv)
print('gradient:', g.tolist(), 'Hessian:', H.tolist())
print('HVP reverse/reverse and forward/reverse:', hv.tolist(), hv2.tolist())
g0 = torch.autograd.grad(f(x), x)[0]
assert not g0.requires_grad
try:
    torch.autograd.grad(g0.sum(), x)
except RuntimeError:
    print('without create_graph: second derivative rejected')
else:
    raise AssertionError('expected missing graph error')
