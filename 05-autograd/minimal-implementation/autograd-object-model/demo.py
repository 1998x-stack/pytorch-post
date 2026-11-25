import torch

x = torch.tensor([2., 3.], dtype=torch.float64, requires_grad=True)
a = x * 2
u, v = a.unbind()
assert x.is_leaf and x.grad_fn is None and x.grad is None
assert not a.is_leaf and a.grad_fn is not None
assert u.grad_fn is v.grad_fn
assert (u.output_nr, v.output_nr) == (0, 1)
loss = 3*u + 4*v
print('leaf:', x.is_leaf, x.grad_fn)
print('shared backward node:', type(u.grad_fn).__name__, 'slots:', u.output_nr, v.output_nr)
print('consumer edge:', loss.grad_fn.next_functions[0][0].next_functions[0][1], loss.grad_fn.next_functions[1][0].next_functions[0][1])
a.retain_grad()
loss.backward()
assert torch.equal(a.grad, torch.tensor([3., 4.], dtype=torch.float64))
assert torch.equal(x.grad, torch.tensor([6., 8.], dtype=torch.float64))
print('a.grad:', a.grad.tolist(), 'x.grad:', x.grad.tolist())
