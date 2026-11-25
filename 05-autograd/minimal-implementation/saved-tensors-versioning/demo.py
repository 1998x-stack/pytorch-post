import torch

def check_version(saved, current):
    if saved != current:
        raise ValueError('stale saved value')

check_version(0, 0)
try:
    check_version(0, 1)
except ValueError:
    print('toy: mismatch rejected')
else:
    raise AssertionError('expected mismatch')
x = torch.tensor(2., dtype=torch.float64, requires_grad=True)
y = x*x
alias = x.detach()
before = x._version
alias.add_(1)
assert x._version == before + 1
try:
    y.backward()
except RuntimeError as exc:
    assert 'modified by an inplace operation' in str(exc)
    print('native: version mismatch rejected')
else:
    raise AssertionError('expected version error')
x = torch.tensor(2., dtype=torch.float64, requires_grad=True)
y = x*x
x.detach().clone().add_(1)
y.backward()
assert x.grad.item() == 4
print('clone leaves gradient:', x.grad.item())
x = torch.tensor(2., dtype=torch.float64, requires_grad=True)
y = x*x
y.backward(retain_graph=True)
y.backward()
assert x.grad.item() == 8
try:
    y.backward()
except RuntimeError as exc:
    assert 'backward through the graph a second time' in str(exc)
    print('released saved values: repeat rejected')
else:
    raise AssertionError('expected release error')
