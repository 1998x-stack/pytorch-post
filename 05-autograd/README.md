# 自动微分

状态：四批十二个系列主题（11 篇本组件、1 篇跨组件）研究包与可视化已编写；发布以 Pages QA 和实际部署为准。

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

4. [Autograd 对象模型：Tensor、AutogradMeta、Node 与 Edge](diagrams/autograd-object-model/index.html) — [研究包](references/autograd-object-model/research.json)
5. [derivatives.yaml：从导数规则到自动生成反向算子](diagrams/derivative-codegen/index.html) — [研究包](references/derivative-codegen/research.json)
6. [Custom Autograd Function：定义自己的 VJP 与二阶梯度](diagrams/custom-autograd-function/index.html) — [研究包](references/custom-autograd-function/research.json)

7. [Forward-mode AD：Dual Tensor 与 JVP](diagrams/forward-mode-jvp/index.html) — [研究包](references/forward-mode-jvp/research.json)
8. [高阶自动微分：Hessian、HVP 与 create_graph](diagrams/higher-order-hessian/index.html) — [研究包](references/higher-order-hessian/research.json)
9. [Activation Checkpoint：重计算、早停与 RNG](diagrams/activation-checkpoint/index.html) — [研究包](references/activation-checkpoint/research.json)

10. [Autograd 并发：ReadyQueue、重入与 CUDA Stream](diagrams/autograd-concurrency/index.html) — [研究包](references/autograd-concurrency/research.json)
11. [AOTAutograd：联合图、前反向分区与保存值](../10-aot-autograd/diagrams/aot-joint-graph/index.html) — [研究包](../10-aot-autograd/references/aot-joint-graph/research.json)（跨组件：10-aot-autograd）
12. [Compiled Autograd：在 backward 时捕获更大的图](diagrams/compiled-autograd/index.html) — [研究包](references/compiled-autograd/research.json)

研究版本：PyTorch 2.10.0+cpu，commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。
