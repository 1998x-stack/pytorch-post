# Compiled Autograd：在 backward 时捕获更大的图 — 固定源码

PyTorch 2.10.0+cpu git_version 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。

- [Engine::execute compiled autograd branch](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/engine.cpp#L1354-L1366) — torch/csrc/autograd/engine.cpp:1354–1366
- [AutogradCompilerInstance.proxy_call_hook](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/_dynamo/compiled_autograd.py#L803-L835) — torch/_dynamo/compiled_autograd.py:803–835
- [AutogradCompilerInstance.end_capture](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/_dynamo/compiled_autograd.py#L1025-L1050) — torch/_dynamo/compiled_autograd.py:1025–1050
- [_enable compiler registration](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/_dynamo/compiled_autograd.py#L1470-L1539) — torch/_dynamo/compiled_autograd.py:1470–1539

- Engine::execute can delegate to the registered compiled autograd callback; the Python capture instance creates proxies for hooks and supplies a captured graph to a compiler callback. 限制：Private API version-specific; compiled reentry limitation in source.
- Compiled Autograd targets larger runtime backward capture including hook logic beyond an individual AOT forward segment. 限制：Tutorial describes potential graph breaks and recompilation; not a guarantee of full graph coverage.
- CPU test captured one backward FX graph containing call_hook and call_accumulate_grad; hooked gradients [12,18] match eager. 限制：Callback runs gm.forward directly; no Inductor code generation or speedup; no cross-forward graph-break test.
