import torch
from torch._dynamo import compiled_autograd

captured = []
def compiler(gm):
    captured.append(gm.code)
    print('backward FX graph:')
    print(gm.code.strip())
    return gm.forward

def run(compiled):
    x = torch.tensor([2., 3.], dtype=torch.float64, requires_grad=True)
    y = x.square()
    y.register_hook(lambda g: g * 3)
    if compiled:
        with compiled_autograd._enable(compiler):
            y.sum().backward()
    else:
        y.sum().backward()
    return x.grad
base = run(False)
actual = run(True)
assert torch.equal(base, actual)
assert torch.equal(actual, torch.tensor([12., 18.], dtype=torch.float64))
assert captured and 'hook' in captured[0]
print('hook gradient:', actual.tolist(), 'captures:', len(captured))
