# AOTAutograd：联合图、前反向分区与保存值 — 文献调查

G0: 已检查 main 九篇 Autograd 文章、10-aot-autograd 骨架和开放 PR（无）。搜索：PyTorch 2 compiler paper AOTAutograd; PyTorch compiled autograd tutorial backward hooks graph breaks; PyTorch autograd mechanics multithreaded CUDA stream semantics reentrant backward. 2024 ASPLOS 论文 §3.9 原文和图文页面已查看；相关现代机制以固定源码为主。未发现需为当前线程实现或 Compiled Autograd 虚构独立论文。

- [Ansel et al., PyTorch 2: Faster Machine Learning Through Dynamic Python Bytecode Transformation and Graph Compilation](https://docs.pytorch.org/assets/pytorch2-2.pdf) — §3.9 AOTAutograd, pp. 7–8; §4.2 decompositions

范围：PyTorch 2.10 CPU aot_function 默认 partition_fn；真实捕获 FX 图并执行，不运行 Inductor 或 min-cut 性能实验。
