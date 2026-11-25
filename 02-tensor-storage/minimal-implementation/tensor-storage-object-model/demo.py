import torch
x = torch.arange(12, dtype=torch.int64).reshape(3, 4)
y = x[:, 1:3]
z = y.clone()
assert x.untyped_storage().data_ptr() == y.untyped_storage().data_ptr()
assert z.untyped_storage().data_ptr() != y.untyped_storage().data_ptr()
assert y.data_ptr() - x.data_ptr() == y.element_size()
print('shape:', tuple(y.shape), 'stride:', y.stride(), 'offset:', y.storage_offset())
print('storage bytes:', x.untyped_storage().nbytes(), y.untyped_storage().nbytes(), z.untyped_storage().nbytes())
y[0, 0] = 99
assert x[0, 1].item() == 99 and z[0, 0].item() == 1
print('view mutation:', x[0, 1].item(), 'clone:', z[0, 0].item())
