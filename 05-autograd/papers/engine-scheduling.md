# Autograd Engine：依赖计数与梯度汇聚 — 论文调查

查重：2026-11-25 检查默认分支 05-autograd 目录及 open PR（为空），未发现已有主题。查询：Automatic differentiation in PyTorch 2017；Baydin reverse mode VJP；PyTorch computational graph engine；SavedVariable version counter。2017 原始论文 §1、§3、§3.1 和 Baydin §3.2 用作直接/算法证据；[2019 框架论文](https://proceedings.neurips.cc/paper/2019/hash/bdbca288fee7f92f2bfa9f7012727740-Abstract.html) 只作背景（摘要核验，不据此断言内核细节）。

- [Automatic differentiation in PyTorch — Paszke et al. (2017)](https://openreview.net/references/pdf?id=BJJsrmfCZ) — direct; §1 Background; §3 Implementation; §3.1 Supporting in-place operations

范围：PyTorch 2.10 eager CPU backward 的简化共享节点调度；排除 compiled autograd、重入、GPU stream 详细调度。2017 实现与当前源码不可直接混同。
