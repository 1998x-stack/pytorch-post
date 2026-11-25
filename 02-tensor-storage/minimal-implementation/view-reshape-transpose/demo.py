import torch

def shares(a, b):
    return a.untyped_storage().data_ptr() == b.untyped_storage().data_ptr()
x = torch.arange(12).reshape(3, 4)
t = x.transpose(0, 1)
assert shares(x, t) and t.stride() == (1, 4)
print('transpose:', tuple(t.shape), t.stride(), 'shares:', shares(x, t))
try:
    t.view(-1)
except RuntimeError:
    print('transpose flatten view rejected')
else:
    raise AssertionError('expected incompatible stride')
r = t.reshape(-1)
assert not shares(r, t) and r.tolist() == t.tolist()[0] + t.tolist()[1] + t.tolist()[2] + t.tolist()[3]
print('reshape copy:', r.tolist())
s = x[:, ::2]
v = s.view(-1)
assert not s.is_contiguous() and shares(v, s) and v.stride() == (2,)
assert v.tolist() == [0, 2, 4, 6, 8, 10]
print('non-contiguous view:', v.tolist(), v.stride())
