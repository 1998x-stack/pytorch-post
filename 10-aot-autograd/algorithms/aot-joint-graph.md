# AOTAutograd：联合图、前反向分区与保存值 — 机制与算法

## 为何捕获 forward 还不够？
Dynamo 捕获可编译的前向片段，但训练还需要反向。AOTAutograd 利用自动微分与 tracing 捕获联合前反向图，然后将其分割，交给后端。2024 ASPLOS 论文 §3.9 说明了 fake tensor、联合图、functionalization、decomposition 与分区的设计。现代 2.10 源码决定本文实际接口。[AOT-1]

## 联合图切开后的接口
设 L=sum(x·sin(x))，输入 x 为实数向量。反向给定标量种子 g，梯度为 g·(sin(x)+x·cos(x))。要执行 backward，可保存 x、sin(x)，也可考虑重算部分中间量。实际 default_partition 默认尽量保留原前后向放置，把反向所需保存值作为前向的额外输出。min-cut rematerialization 是可选分区策略，论文说明用图割结合重计算优化存储；本次直接使用 aot_function 默认分区，不把实验说成运行了 min-cut。[AOT-2]

## 实际捕获的 FX 图
真实 forward FX 返回 (sum_1, primals_1, sin)，用户可见输出仍只是 loss；后两个值为反向接口需要的中间状态。backward 输入包含 primals_1、sin、tangents_1，展开种子，计算 sin 项与 x·cos(x) 项相加。下面的完整运行日志来自捕获回调。这是 FX 表示与执行验证：compiler 回调返回 make_boxed_func(gm.forward)，没有生成优化后的 C++ 或 GPU kernel。[AOT-3]

## 与其他组件的边界
功能化旨在把 mutation 转换成可分析的函数式表达，别名及输入更新还需 wrapper 维持语义；decomposition 把高层算子映射到更基础算子。此例没有 mutation，不宣称验证别名或动态 shape。AOTAutograd 的捕获边界通常与前向编译片段关联；下一篇 Compiled Autograd 研究在 backward 时捕获更大运行时图。
