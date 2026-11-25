import threading
from concurrent.futures import ThreadPoolExecutor
import torch

torch.set_num_threads(1)
barrier = threading.Barrier(2)
def task(value):
    x = torch.tensor(value, dtype=torch.float64, requires_grad=True)
    y = x.square()
    barrier.wait(timeout=10)
    return torch.autograd.grad(y, x)[0].item()
with ThreadPoolExecutor(max_workers=2) as pool:
    result = list(pool.map(task, [2., 3.]))
assert result == [4., 6.]
print('independent CPU graph gradients:', result)
class Reenter(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x):
        ctx.save_for_backward(x)
        return x.square()
    @staticmethod
    def backward(ctx, g):
        (x,) = ctx.saved_tensors
        with torch.enable_grad():
            z = x.detach().requires_grad_()
            inner = torch.autograd.grad(z.square(), z)[0]
        return g * inner
x = torch.tensor(3., dtype=torch.float64, requires_grad=True)
Reenter.apply(x).backward()
assert x.grad.item() == 6.
print('nested backward gradient:', x.grad.item())
print('CUDA available:', torch.cuda.is_available())
