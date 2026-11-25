import torch

x = torch.tensor([[2.], [3.]], dtype=torch.float64, requires_grad=True)
y = torch.tensor([[4., 5., 6.]], dtype=torch.float64, requires_grad=True)
g = torch.tensor([[1., 2., 3.], [4., 5., 6.]], dtype=torch.float64)
z = x * y
expected_x = (g * y).sum(dim=1, keepdim=True)
expected_y = (g * x).sum(dim=0, keepdim=True)
gx, gy = torch.autograd.grad(z, (x, y), g)
assert torch.equal(gx, expected_x) and torch.equal(gy, expected_y)
assert gx.shape == x.shape and gy.shape == y.shape
print('node:', type(z.grad_fn).__name__)
print('broadcast VJP:', gx.tolist(), gy.tolist())
assert torch.autograd.gradcheck(lambda a, b: a*b, (x, y))
print('gradcheck: passed')
