import torch
from torch.autograd import forward_ad as fw

x = torch.tensor([2., 3.], dtype=torch.float64)
v = torch.tensor([4., 5.], dtype=torch.float64)
def f(z):
    return torch.stack((z[0]*z[1], z[0]+z[1]))
with fw.dual_level():
    dual = fw.make_dual(x, v)
    out = f(dual)
    primal, tangent = fw.unpack_dual(out)
    assert torch.equal(primal, torch.tensor([6., 5.], dtype=x.dtype))
    assert torch.equal(tangent, torch.tensor([22., 9.], dtype=x.dtype))
    print('primal:', primal.tolist(), 'JVP:', tangent.tolist())
assert fw.unpack_dual(out).tangent is None
p, j = torch.func.jvp(f, (x,), (v,))
J = torch.func.jacrev(f)(x)
assert torch.equal(j, J @ v)
print('Jacobian:', J.tolist(), 'JVP matches:', j.tolist())
print('dual tangent cleared after exit')
