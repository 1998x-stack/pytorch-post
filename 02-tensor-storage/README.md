# 张量与存储

状态：**partial（首批三篇完成研究交接）**。

研究问题：shape、stride、storage offset、别名与视图。

- [papers](./papers/README.md)
- [source-analysis](./source-analysis/README.md)
- [algorithms](./algorithms/README.md)
- [minimal-implementation](./minimal-implementation/README.md)
- [experiments](./experiments/README.md)
- [benchmarks](./benchmarks/README.md)
- [diagrams](./diagrams/README.md)
- [references](./references/README.md)

完成条件：原始证据、固定版本源码、算法推导、最小实现与测试、可复现实验、图解及限制均经过核验。不可将目录存在视为研究完成。


## Tensor Storage 系列

1. [Tensor 与 Storage：数据、元数据和所有权](diagrams/tensor-storage-object-model/index.html) — [研究包](references/tensor-storage-object-model/research.json)
2. [Shape、Stride、Storage Offset：张量地址映射的数学体系](diagrams/shape-stride-offset/index.html) — [研究包](references/shape-stride-offset/research.json)
3. [View、Reshape 与 Transpose：何时零拷贝，何时复制？](diagrams/view-reshape-transpose/index.html) — [研究包](references/view-reshape-transpose/research.json)

固定源码：PyTorch 2.10.0+cpu / 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。
