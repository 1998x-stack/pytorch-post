# Research → Olah

- 05-autograd/derivative-codegen; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- PyTorch 并不是运行时对任意 C++ kernel 做符号微分。以 mul.Tensor 为例，追踪 schema、导数规则、代码生成以及广播梯度归约。
- Verified claims: cg-1, cg-2, cg-3; locators in research.json.
- Storyboard: mul.Tensor schema 对应 derivatives.yaml 中两个输入 VJP 规则。 → 构建阶段生成 Autograd wrapper 和反向 Node；并非运行时解释 YAML。 → MulBackward0 计算候选梯度，元数据将广播结果归约到 [2,1] 与 [1,3]。
- Runnable 05-autograd/minimal-implementation/derivative-codegen/demo.py; log 05-autograd/experiments/derivative-codegen/cpu.log.
- Scope and exclusions: PyTorch 2.10 eager CPU dense real mul.Tensor；静态代码生成阅读与运行时数值验证，不重新编译 PyTorch。; no measured performance claims.
- handoff-ready; publication gated by QA.
