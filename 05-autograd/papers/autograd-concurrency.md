# Autograd 并发：ReadyQueue、重入与 CUDA Stream — 文献调查

G0: 已检查 main 九篇 Autograd 文章、10-aot-autograd 骨架和开放 PR（无）。搜索：PyTorch 2 compiler paper AOTAutograd; PyTorch compiled autograd tutorial backward hooks graph breaks; PyTorch autograd mechanics multithreaded CUDA stream semantics reentrant backward. 2024 ASPLOS 论文 §3.9 原文和图文页面已查看；相关现代机制以固定源码为主。未发现需为当前线程实现或 Compiled Autograd 虚构独立论文。

- [Autograd mechanics](https://docs.pytorch.org/docs/main/notes/autograd.html) — Multithreaded Autograd; Hogwild; thread safety

范围：PyTorch 2.10 eager CPU 独立图及嵌套反向实测；CUDA canonical stream 合约仅固定源码研究，无 GPU 实验。
