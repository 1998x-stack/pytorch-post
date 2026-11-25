# Custom Autograd Function：定义自己的 VJP 与二阶梯度 — 机制与算法

## 为什么需要自定义 Function？
普通 PyTorch 运算组合通常已经支持自动微分。若希望把外部计算或自定义梯度规则接入 Autograd，可以使用 Function；它不是任意不可微函数的数学求导器。用户必须保证 backward 代表预期的 VJP。

## apply 到 PyNode：跨过 Python / C++ 边界
FunctionMeta 生成对应 backward class。普通 eager 模式中 Function.apply 进入 C++ THPFunction_apply，建立 next edges、记录 ctx.needs_input_grad，在关闭 grad mode 的作用域执行 forward，然后处理输出。反向引擎调度 PyNode::apply 时调用 Python 侧 backward 路径。[FN-1]调用 ScaledCube.apply(x,scale)，而不是直接调用 forward，否则无法建立自定义反向节点。这里采用 forward(ctx,x,scale) 形式；torch.func 变换需要另一套 setup_context 等契约，不在本文验证范围。

## 定义正确的 VJP
令 y=s x³（逐元素），s 是 Python 浮点常量。backward 收到与输出匹配的 g，返回与两个 forward 参数对应的梯度：x 的 VJP 与 scale 的 None。[FN-2]（公式见 HTML 中的结构化 MathML。）保存 Tensor 使用 ctx.save_for_backward，非 Tensor 信息可存 ctx.scale。这里保存输入 x 而非无梯度记录的中间值；create_graph=True 时，backward 内部的可微操作会被记录，因而对 y.sum() 得到二阶梯度 6sx。

## 数值检查能抓住什么？
gradcheck 将解析梯度与有限差分对比；gradgradcheck 针对高阶梯度。float64 小样本更适于数值检查，但通过检查不意味着所有输入、不可微点或设备都正确。故意将平方函数的 backward 写成恒等映射，gradcheck 在本例正确拒绝。[FN-3]若原地修改输入，需要遵守 mark_dirty 和版本计数规则；若不支持二阶反向，应明确约束而不是默认承诺。广播、多输出和 Tensor 类型参数同样需要各自的梯度形状与返回槽位测试。

示例是有限范围的教学与行为验证，不是完整 C++ 实现复现。
