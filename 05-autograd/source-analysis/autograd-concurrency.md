# Autograd 并发：ReadyQueue、重入与 CUDA Stream — 固定源码

PyTorch 2.10.0+cpu git_version 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。

- [Engine reentrant backward and stream note](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/engine.cpp#L152-L181) — torch/csrc/autograd/engine.cpp:152–181
- [ReadyQueue push/pop](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/engine.cpp#L232-L274) — torch/csrc/autograd/engine.cpp:232–274
- [Engine::ready_queue device routing](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/engine.cpp#L1540-L1557) — torch/csrc/autograd/engine.cpp:1540–1557
- [InputBuffer canonical stream contract](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/input_buffer.cpp#L136-L187) — torch/csrc/autograd/input_buffer.cpp:136–187

- Engine ready queues route CPU work and device work; a nested backward can block a worker, so the engine has a worker pool mechanism for reentrant work. 限制：The pool mechanism is not asserted to be used in every nested backward; CPU and accelerator routes differ.
- For CUDA/privateuse1 the engine associates backward device work with forward streams; producer-consumer synchronization and accumulation stream choices are described in InputBuffer. 限制：Source-level contract only; CUDA unavailable. No claim about exact kernel overlap or latency.
- Two independent CPU graph tasks return gradients 4 and 6; a custom backward that invokes torch.autograd.grad returns gradient 6. 限制：Correctness and completion only; no shared-leaf race or concurrency speedup measurement.
