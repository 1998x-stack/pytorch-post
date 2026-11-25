# PyTorch Post

面向 PyTorch 内核和 AI Infrastructure 的研究知识库：论文 → 源码 → 算法 → 最小实现 → 实验 → 基准 → 图解。Autograd 前两批六篇研究已完成交接，其他组件仍为研究骨架。

## 组件索引

| 组件 | 研究范围 |
|---|---|
| [01-architecture](./01-architecture/README.md) | Eager 与编译模式的执行边界 |
| [02-tensor-storage](./02-tensor-storage/README.md) | shape、stride、storage offset、别名与视图 |
| [03-aten-operators](./03-aten-operators/README.md) | 算子 schema、TensorIterator、CPU/GPU kernel |
| [04-dispatcher](./04-dispatcher/README.md) | DispatchKeySet、注册、redispatch、fallback |
| [05-autograd](./05-autograd/README.md) | 反向模式、计算图、梯度累积与版本计数 |
| [06-nn-modules](./06-nn-modules/README.md) | 参数注册、buffer、hooks、state_dict |
| [07-optimizers](./07-optimizers/README.md) | SGD、Adam、AdamW 与状态更新 |
| [08-fx-graph](./08-fx-graph/README.md) | Node、Graph、GraphModule、符号追踪 |
| [09-torchdynamo](./09-torchdynamo/README.md) | 字节码转换、guards、graph breaks |
| [10-aot-autograd](./10-aot-autograd/README.md) | 联合前反向图、functionalization、partition |
| [11-torchinductor](./11-torchinductor/README.md) | lowering、fusion、schedule、codegen |
| [12-triton](./12-triton/README.md) | 分块、访存、并行映射、kernel 编译 |
| [13-cuda-runtime](./13-cuda-runtime/README.md) | stream、event、异步执行、同步 |
| [14-memory-allocator](./14-memory-allocator/README.md) | caching allocator、碎片、重计算与峰值 |
| [15-distributed-ddp](./15-distributed-ddp/README.md) | 梯度分桶、AllReduce、计算通信重叠 |
| [16-fsdp](./16-fsdp/README.md) | 参数分片、all-gather、reduce-scatter |
| [17-dtensor](./17-dtensor/README.md) | DeviceMesh、placement、redistribute |
| [18-model-parallelism](./18-model-parallelism/README.md) | TP、PP、微批次与多维并行 |
| [19-flash-attention](./19-flash-attention/README.md) | IO 感知、online softmax 与 SDPA 后端选择 |
| [20-flex-attention](./20-flex-attention/README.md) | score_mod、BlockMask 与编译生成 kernel |
| [21-quantization](./21-quantization/README.md) | PTQ、QAT、低精度表示与算子边界 |
| [22-data-loader](./22-data-loader/README.md) | worker、sampler、prefetch、pin_memory |
| [23-profiler](./23-profiler/README.md) | CPU/GPU trace、事件关联与性能模型 |
| [24-export-deployment](./24-export-deployment/README.md) | ExportedProgram、约束、部署运行时 |
| [25-torchtitan](./25-torchtitan/README.md) | 分布式训练组合、训练循环与 checkpoint |

## 工程规范

- [AGENTS.md](AGENTS.md)：研究、证据、去重、发布规则。
- [组件清单](catalog/components.json)：稳定 ID、范围、候选引用及状态。
- [PyTorch Research Skill](.pi/skills/pytorch-research/SKILL.md)：论文、源码、算法、实验与反思评审；先研究，再交接可视化。
- [Olah Skill](.pi/skills/olah-style-paper-posts/SKILL.md) 与 [集成指南](docs/skill-integration.md)。
- [结构评审](docs/reviews/bootstrap-review.md)。

```bash
python scripts/validate_structure.py
python .pi/skills/pytorch-research/scripts/validate_research.py --repo .
python -m unittest discover -s .pi/skills/pytorch-research/tests -v
```

## GitHub Pages

- [站点发布与首次开启](docs/pages.md)
- [Autograd 系列](05-autograd/README.md)
- [文章注册表](catalog/posts.json)

文章由组件 diagrams/<slug>/ 源文件构建；是否上线以 GitHub Actions 实际部署状态为准。
