# 高阶自动微分：Hessian、HVP 与 create_graph — 算法

## 梯度告诉方向，Hessian 告诉梯度如何变化
对于标量函数 f: Rⁿ→R，梯度是 n 维向量，Hessian 是 n×n 矩阵。显式存储稠密 Hessian 需要 O(n²) 个元素；若算法只需要曲率方向 Hv，可以直接对梯度函数做方向微分。Pearlmutter 1994 是历史研究入口，本篇未阅读全文，不借其声称任何实测加速。

## 两条 HVP 路径
对 C² 实数标量函数，H=J(∇f) 对称。forward-over-reverse 是先 reverse 得到梯度，再 forward 得到其方向导数；reverse-over-reverse 则以 v 为种子对梯度执行 VJP，所得 Hᵀv 与 Hv 相同。（结构化公式见 HTML。）例：f=x₁³+x₁x₂+x₂²。梯度为 (3x₁²+x₂, x₁+2x₂)，H=[[6x₁,1],[1,2]]。在 (2,3) 代入 v=(4,5) 得 (53,14)。[HVP-1]

## create_graph 与 retain_graph 的区别
create_graph=True 允许将求导操作本身记录为可微计算；retain_graph 保留原反向所需保存值，单独设为 True 并不等于记录导数图。torch.func.hessian 的固定版本源码直接返回 jacfwd(jacrev(func,argnums),argnums)，算子不支持前向 AD 时可考虑 jacrev(jacrev(func))。[HVP-2]

## HVP 的适用边界
HVP 不显式物化 H，但仍需计算图和中间量，不能据此承诺常数内存或固定加速比。非光滑点可能不存在经典 Hessian；变量相关的 v 需考虑额外导数项。实验比较两条路线，并用默认 create_graph=False 构造负例。[HVP-3]
