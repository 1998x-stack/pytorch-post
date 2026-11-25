import torch

def toy(x):
    a = x*x
    return a + 3*x, 2*x + 3

for value in (-2., 0., 2.):
    x = torch.tensor(value, dtype=torch.float64, requires_grad=True)
    y = x*x + 3*x
    expected, grad = toy(value)
    assert y.item() == expected
    assert torch.autograd.grad(y, x)[0].item() == grad
    print(f'x={value:g} y={expected:g} gradient={grad:g}')
x = torch.tensor([2., 3.], dtype=torch.float64, requires_grad=True)
y = torch.stack((x[0]*x[1], x[0]+x[1]))
v = torch.tensor([4., 5.], dtype=torch.float64)
g = torch.autograd.grad(y, x, v)[0]
assert torch.equal(g, torch.tensor([17., 13.], dtype=torch.float64))
print('VJP:', g.tolist())
