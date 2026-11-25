import torch
from torch.utils.checkpoint import checkpoint

for mode in ('plain', 'non-reentrant', 'reentrant'):
    x = torch.tensor([2., 3.], dtype=torch.float64, requires_grad=True)
    trace = []
    def block(z):
        trace.append('enter')
        a = z*z
        y = a*a
        trace.append('exit')
        return y
    y = block(x) if mode == 'plain' else checkpoint(block, x, use_reentrant=(mode == 'reentrant'))
    y.sum().backward()
    assert torch.equal(x.grad, 4*x.detach()**3)
    expected = {'plain': ['enter','exit'], 'non-reentrant': ['enter','exit','enter'], 'reentrant': ['enter','exit','enter','exit']}[mode]
    assert trace == expected, trace
    print(mode, 'gradient:', x.grad.tolist(), 'trace:', trace)

def dropout_block(z):
    return torch.nn.functional.dropout(z, p=0.5, training=True).square()
for mode in ('plain', 'checkpoint'):
    torch.manual_seed(17)
    x = torch.arange(1., 9., dtype=torch.float64, requires_grad=True)
    y = dropout_block(x) if mode == 'plain' else checkpoint(dropout_block, x, use_reentrant=False, preserve_rng_state=True)
    y.sum().backward()
    if mode == 'plain':
        baseline = (y.detach().clone(), x.grad.clone(), torch.random.get_rng_state().clone())
    else:
        assert torch.equal(y, baseline[0]) and torch.equal(x.grad, baseline[1])
        assert torch.equal(torch.random.get_rng_state(), baseline[2])
        print('dropout: output, gradient and CPU RNG state match')
