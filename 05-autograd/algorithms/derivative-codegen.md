# derivatives.yaml：从导数规则到自动生成反向算子 — 机制与算法

## 正向 kernel 为什么不需要包含完整反向逻辑？
ATen schema 描述 mul.Tensor 的输入输出；实际算子实现负责数值计算。Autograd 规则另行描述怎样从输出余切求输入余切。它不是对 C++ 源文件自动求导的万能程序，也不是每次调用都重新读取 YAML。

## 构建阶段：规则如何成为 C++ 代码
native_functions.yaml 定义算子 schema；derivatives.yaml 对同一签名给出导数规则。gen_autograd.py 读取两者及 tags，经 load_derivatives 形成 differentiability info，再驱动 VariableType 与 Functions 的生成。前者为适用算子生成 Autograd wrapper，创建 grad_fn、收集 next edges；后者生成反向 Node 的计算代码。[CG-1]mul.Tensor 的 self 与 other 规则都调用 mul_tensor_backward；result 条目是前向模式公式，不能当作反向 VJP。生成器中 needs_input_grad 决定是否计算相应输入梯度。源码还存在 composite、手写及特定 dispatch 规则，本文不推广到所有算子。

## 广播乘法的 VJP
x=(2×1)、y=(1×3)、z=(2×3)，zᵢⱼ=xᵢyⱼ。给定输出余切 g，输入梯度分别沿广播维度求和。（公式见 HTML 中的结构化 MathML。）本例中 g=[[1,2,3],[4,5,6]]。x 方向为 [4+10+18,16+25+36]=[32,77]；y 方向为 [2+12,4+15,6+18]=[14,19,24]。

## 运行阶段：公式与形状校验分工
mul_tensor_backward 在实数情况下给出逐元素乘法结果（源码还处理共轭及 real-to-complex）。Engine 的 validate_outputs_impl 调用 InputMetadata::maybe_reduce，兼容的广播梯度经 reduce_grad 调用 sum_to 恢复输入形状；不是 YAML 公式单独处理所有广播。[CG-2]原生实验中反向节点名为 MulBackward0，结果与手工公式一致并通过 gradcheck。该运行验证安装版本的数值行为，不代表重新运行代码生成器或编译了 C++。[CG-3]

示例是有限范围的教学与行为验证，不是完整 C++ 实现复现。
