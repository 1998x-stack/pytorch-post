# 自动微分

状态：首批三篇研究包与可视化已编写；发布以 Pages QA 和实际部署为准。

研究问题：反向模式、计算图、梯度累积与版本计数。

- [papers](./papers/README.md)
- [source-analysis](./source-analysis/README.md)
- [algorithms](./algorithms/README.md)
- [minimal-implementation](./minimal-implementation/README.md)
- [experiments](./experiments/README.md)
- [benchmarks](./benchmarks/README.md)
- [diagrams](./diagrams/README.md)
- [references](./references/README.md)

完成条件：原始证据、固定版本源码、算法推导、最小实现与测试、可复现实验、图解及限制均经过核验。不可将目录存在视为研究完成。

## Autograd 系列

1. [反向自动微分：从链式法则到 VJP](diagrams/reverse-mode-vjp/index.html) — [研究包](references/reverse-mode-vjp/research.json)
2. [Autograd Engine：依赖计数与梯度汇聚](diagrams/engine-scheduling/index.html) — [研究包](references/engine-scheduling/research.json)
3. [SavedVariable：保存值、版本计数与原地修改](diagrams/saved-tensors-versioning/index.html) — [研究包](references/saved-tensors-versioning/research.json)

研究版本：PyTorch 2.10.0+cpu，commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。
