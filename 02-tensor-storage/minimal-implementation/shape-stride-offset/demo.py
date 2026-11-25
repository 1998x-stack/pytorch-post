import itertools
import torch

def offsets(shape, stride, offset):
    return [offset + sum(i*s for i, s in zip(idx, stride))
            for idx in itertools.product(*(range(n) for n in shape))]
x = torch.arange(12, dtype=torch.int64)
for shape, stride, offset in [((2, 3), (4, 1), 1), ((3, 2), (1, 4), 1), ((2, 3), (0, 1), 2)]:
    idx = offsets(shape, stride, offset)
    y = x.as_strided(shape, stride, offset)
    assert y.tolist() == x[idx].reshape(shape).tolist()
    print(shape, stride, offset, 'indices:', idx, 'values:', y.tolist())
try:
    x.as_strided((2, 3), (10, 1), 1)
except RuntimeError:
    print('out-of-bounds rejected')
else:
    raise AssertionError('expected bounds error')
