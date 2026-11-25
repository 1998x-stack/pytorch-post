# Forward-mode AD：Dual Tensor 与 JVP — 算法

## 同一个 Jacobian，为什么有两种传播方向？
设 f: Rⁿ→Rᵐ，J 的形状为 m×n。前向模式以输入方向 v 为种子，计算输出方向 Jv；反向模式以输出余切 u 为种子，计算 Jᵀu。两者通常无需显式生成整个矩阵。前者逐个输入方向构建 Jacobian 列，后者逐个输出方向构建行，因此少输入多输出与多输入少输出适合不同策略；算子覆盖和中间存储同样重要。

## Dual 数：同时携带值与变化率
用 (p,t) 表示原值和方向导数。加法将两个 tangent 相加；乘法按乘积法则传播。等价的代数表达是 ε²=0 的 p+εt，这只是数学模型，不是 PyTorch Tensor 的内存布局。（结构化公式见 HTML。）例：f(x₁,x₂)=(x₁x₂,x₁+x₂)，x=(2,3)，v=(4,5)。乘法分支 tangent=4×3+2×5=22，加法分支=4+5=9。[JVP-1]

## 源码：dual level 与 transform
forward_ad.enter_dual_level 进入层级；make_dual 检查 dtype、层级并调用 _VF._make_dual；unpack_dual 读取 primal 和 tangent。AutogradMeta 还有按需填充的 fw_grad_。低级 dual_level 不支持任意嵌套；torch.func.jvp 具有额外变换层级处理。不要把 forward AD 等同于 backward(create_graph=True)。[JVP-2]

## 何时使用 JVP
方向敏感度、隐式模型线性化、HVP 都可使用 JVP。显式 Jacobian 需要多个方向，成本不应误称为一次 JVP。部分算子缺少前向 AD 规则，不能据本例推断全部模型支持。[JVP-3]
