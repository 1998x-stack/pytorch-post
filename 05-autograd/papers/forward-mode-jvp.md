# Forward-mode AD：Dual Tensor 与 JVP — 文献调查

G0: 已检查 main 的六篇 Autograd 注册文章与开放 PR（无），新主题不重复。查询：Baydin forward mode JVP; Pearlmutter Hessian-vector product; Chen sublinear memory checkpointing; PyTorch forward_ad, hessian, checkpoint. AD 综述与 Chen §4.3 阅读相关正文；Pearlmutter 只核验题录，未阅读全文，不用作已验证主张。现代实现依据固定源码。

- [Baydin et al., Automatic Differentiation in Machine Learning: a Survey](https://arxiv.org/abs/1502.05767) — §3 forward/reverse accumulation; higher-order AD (verified)

范围：PyTorch 2.10 eager CPU 实数、单层 dual_level 与 torch.func.jvp；不涵盖全部算子、嵌套变换或 GPU。
