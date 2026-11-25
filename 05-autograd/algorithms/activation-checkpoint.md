# Activation Checkpoint：重计算、早停与 RNG — 算法

## 为什么保存所有激活不是唯一办法？
反向计算需要部分前向中间量。保存激活避免重新计算，但长链会让激活占用增长。Checkpoint 保留边界输入，部分中间量需要时重算。不是模型参数 checkpoint，也不是直接降低参数或优化器状态内存。

## 分段：计算与激活存储权衡
Chen 等 2016 §4.3 用均匀分段推导：n 层等大小激活，k 段，边界存储约 k，反向处理一段所需激活约 n/k。（结构化公式见 HTML。）n=16 时 k=1、2、4、8、16 对应这一简化代理量 17、10、8、10、17。不是实际字节数，也不计参数、梯度、workspace 与分配器。论文的 MXNet/Titan X 实验不可直接当作 PyTorch 2.10 性能结论。[CKPT-1]

## 两种 PyTorch 实现路线
reentrant：CheckpointFunction.forward 在 no_grad 下运行，保存输入；反向恢复 RNG 并启用 grad，重跑整个函数，再求梯度。non-reentrant：记录前向图，pack hook 用 holder 代替保存值，unpack 触发重计算，_recomputation_hook 在恢复所需保存值后可抛内部早停异常。推荐显式传 use_reentrant=False；不能假设所有区域都必然早停。[CKPT-2]

## 随机数、状态和验证
固定种子与 preserve_rng_state=True 让本例 Dropout 在重计算时使用一致的随机流，并恢复周围 CPU RNG 状态。设备迁移、未覆盖的设备、外部 RNG 和可变状态仍可能改变结果；带副作用的函数不宜随意 checkpoint。实验刻意记录 enter/exit 以观察早停，不把执行次数等同于显存实测。[CKPT-3]
