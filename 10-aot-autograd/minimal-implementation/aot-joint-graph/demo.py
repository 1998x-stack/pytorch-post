import torch
from torch._functorch.aot_autograd import aot_function
from functorch.compile import make_boxed_func

seen = {}
def compiler(stage):
    def capture(gm, args):
        seen[stage] = gm.code
        print(stage, 'FX graph:')
        print(gm.code.strip())
        return make_boxed_func(gm.forward)
    return capture
def f(x):
    return (x.sin() * x).sum()
x = torch.tensor([0.2, 0.7], dtype=torch.float64, requires_grad=True)
eager = f(x)
g = torch.autograd.grad(eager, x)[0]
compiled = aot_function(f, fw_compiler=compiler('forward'), bw_compiler=compiler('backward'))
y = compiled(x)
g2 = torch.autograd.grad(y, x)[0]
assert torch.allclose(y, eager) and torch.allclose(g2, g)
assert set(seen) == {'forward', 'backward'}
print('forward/backward captured; eager gradient match:', torch.allclose(g2, g))
