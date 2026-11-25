# Shape、Stride、Storage Offset：张量地址映射的数学体系 — 文献调查

G0：检查 main 02-tensor-storage 八目录（只有 README）、既有 12 篇注册文章、开放 PR（无）。与 05-autograd 的对象模型、SavedVariable 主题不同：本篇研究数据布局和 storage，不重复自动微分。查询 PyTorch tensor storage strides storage_offset view reshape；PyTorch 2019 architecture paper。NeurIPS 2019 §5.1、§4.3 提供历史背景；未发现能直接证明现代字段或 computeStride 算法的专门论文，采用固定 2.10 源码及官方文档。

- [Paszke et al., PyTorch: An Imperative Style, High-Performance Deep Learning Library](https://proceedings.neurips.cc/paper/2019/file/bdbca288fee7f92f2bfa9f7012727740-Paper.pdf) — §5.1, p.5: C++ tensor implementation; §4.3 mutation/versioning. Historical context only.
- [torch.Storage](https://docs.pytorch.org/docs/stable/storage.html) — Storage, offset and sharing

范围：非空普通 CPU strided int64，非负 stride；示例覆盖零步长读取，不执行重叠写入，不推及 sparse/meta/符号形状。
