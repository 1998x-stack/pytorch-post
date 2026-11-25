# Activation Checkpoint：重计算、早停与 RNG — 文献调查

G0: 已检查 main 的六篇 Autograd 注册文章与开放 PR（无），新主题不重复。查询：Baydin forward mode JVP; Pearlmutter Hessian-vector product; Chen sublinear memory checkpointing; PyTorch forward_ad, hessian, checkpoint. AD 综述与 Chen §4.3 阅读相关正文；Pearlmutter 只核验题录，未阅读全文，不用作已验证主张。现代实现依据固定源码。

- [Chen et al., Training Deep Nets with Sublinear Memory Cost](https://arxiv.org/abs/1604.06174) — §4.3, Eq. (1); §5 experiment scope (verified)

范围：PyTorch 2.10 CPU eager checkpoint，确定性平方块与固定种子 Dropout；不测 GPU 峰值显存、耗时或分布式。
