# View、Reshape 与 Transpose：何时零拷贝，何时复制？ — 机制与算法

## 非连续张量不一定不能 view
同样 3×4 的 x，转置得到 shape=(4,3)、stride=(1,4)，逻辑遍历顺序为 0,4,8,1,5,9,…。另一种切片 x[:,::2] 则 shape=(3,2)、stride=(4,2)，逻辑顺序为 0,2,4,6,8,10。两者都不是普通 contiguous，但只有后一种可无复制展平。

## 连续子块判定
若相邻维度属于可合并的非单例连续子块，典型条件是 s[d] = size[d+1] × s[d+1]。注意最内层 stride 不必等于 1；size=1 的维度需要特别处理。（结构化公式见 HTML。）对步长切片 4=2×2，六个元素可由单个 stride=2 描述。对转置 1≠3×4，展平会跨不同子块，因此无法用单一 stride 表示。computeStride 从尾维划分旧子块，将新形状的维度乘积匹配到子块，并为每维推导 stride；无法匹配返回 nullopt。该例不是完整实现，源码还处理 singleton、空 tensor、符号值等。[VIEW-1]

## 源码如何决策
普通 dense transpose 交换 size 和 stride，调用 as_strided_symint，不移动元素；view_impl 检查 computeStride 并在不兼容时报错；reshape_symint 在普通连续输入直接 view，非连续输入尝试 computeStride，可行时 _reshape_alias，不可行时 contiguous clone 再 _unsafe_view。不要依赖 reshape 一定返回 view 或一定复制。[VIEW-2]

## 工程上的选择
要求共享且希望失败显式暴露时用 view；仅要求逻辑形状时用 reshape；需要换轴而不是重新排列线性顺序时用 transpose/permute。实际内存布局、后续 kernel 的 contiguous 需求与 Autograd 语义仍需分别验证。实验通过活跃非空张量的 storage 指针和数值验证两种路径。[VIEW-3]
