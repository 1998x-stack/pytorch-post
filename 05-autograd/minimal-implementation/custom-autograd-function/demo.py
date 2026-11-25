import torch

class ScaledCube(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, scale):
        ctx.save_for_backward(x)
        ctx.scale = scale
        return scale * x.pow(3)

    @staticmethod
    def backward(ctx, grad_output):
        (x,) = ctx.saved_tensors
        return grad_output * ctx.scale * 3 * x.square(), None

x = torch.tensor([2., -1.], dtype=torch.float64, requires_grad=True)
y = ScaledCube.apply(x, 2.)
assert torch.equal(y, 2*x.pow(3))
g = torch.autograd.grad(y.sum(), x, create_graph=True)[0]
h = torch.autograd.grad(g.sum(), x)[0]
assert torch.equal(g, 6*x.square()) and torch.equal(h, 12*x)
print('forward:', y.tolist(), 'gradient:', g.tolist(), 'second:', h.tolist())
assert torch.autograd.gradcheck(lambda a: ScaledCube.apply(a, 2.), (x,))
assert torch.autograd.gradgradcheck(lambda a: ScaledCube.apply(a, 2.), (x,))
print('gradcheck and gradgradcheck: passed')
class Wrong(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        return x.square()
    @staticmethod
    def backward(ctx, grad_output):
        return grad_output
assert not torch.autograd.gradcheck(Wrong.apply, (x,), raise_exception=False)
print('wrong backward: rejected')
