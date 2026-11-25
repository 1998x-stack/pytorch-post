import torch

def toy(order):
    remaining, total = 2, 0
    trace = []
    for contribution in order:
        total += contribution
        remaining -= 1
        trace.append((remaining, total))
    assert remaining == 0
    return 2*total, trace

for order in ([3, 4], [4, 3]):
    result, trace = toy(order)
    assert result == 14
    print('toy', order, trace, result)
x = torch.tensor(2., dtype=torch.float64, requires_grad=True)
a = 2*x
a.retain_grad()
loss = 3*a + 4*a
loss.backward()
assert a.grad.item() == 7 and x.grad.item() == 14
print('native', a.grad.item(), x.grad.item())
(2*x).backward()
assert x.grad.item() == 16
print('second backward on a fresh graph:', x.grad.item())
