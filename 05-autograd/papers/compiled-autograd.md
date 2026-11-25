# Compiled Autograd：在 backward 时捕获更大的图 — 文献调查

G0: 已检查 main 九篇 Autograd 文章、10-aot-autograd 骨架和开放 PR（无）。搜索：PyTorch 2 compiler paper AOTAutograd; PyTorch compiled autograd tutorial backward hooks graph breaks; PyTorch autograd mechanics multithreaded CUDA stream semantics reentrant backward. 2024 ASPLOS 论文 §3.9 原文和图文页面已查看；相关现代机制以固定源码为主。未发现需为当前线程实现或 Compiled Autograd 虚构独立论文。

- [Ansel et al., PyTorch 2: Faster Machine Learning Through Dynamic Python Bytecode Transformation and Graph Compilation](https://docs.pytorch.org/assets/pytorch2-2.pdf) — §3.9 AOTAutograd, pp. 7–8; §4.2 decompositions
- [Compiled Autograd tutorial](https://docs.pytorch.org/tutorials/intermediate/compiled_autograd_tutorial.html) — Overview; Capturing backward hooks; recompilation reasons

范围：PyTorch 2.10 CPU，私有 _enable 捕获接口与 FX 执行回调；无优化后端、CUDA 或跨 graph-break 实测。
