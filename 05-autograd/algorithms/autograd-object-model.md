# Autograd 对象模型：Tensor、AutogradMeta、Node 与 Edge — 机制与算法

## 一个张量不等于一个反向节点
设 x=[2,3]，a=2x，u,v=a.unbind()。虽然 u、v 是两个标量 Tensor，却共享同一个 UnbindBackward0。它们的 output_nr 分别为 0、1。若损失 L=3u+4v，反向节点必须知道两份梯度分别来自哪个前向输出。

## 四层对象的职责
Tensor 是面向用户的句柄；TensorImpl 保存底层张量状态，并可选持有 AutogradMetaInterface。AutogradMeta 包含 grad_、grad_fn_、弱引用 grad_accumulator_ 和 output_nr_。它不是每个张量必然分配的对象。Node 表示反向函数，而 Edge = (目标 Node, input_nr)，指明反向输入槽位。[OBJ-1] [OBJ-2]注意反向边指向更靠近前向输入的节点；不是向前向消费者指去。Tensor 的 output_nr 是其生产者前向输出编号，也对应生产者反向函数的输入槽位。两个输出共享节点，不代表共享同一个输入槽。

## 叶子为什么没有 grad_fn？
叶子 x 的 grad_fn 为 None，但它需要梯度时，canonical gradient_edge 可通过 grad_accumulator(self) 获得 AccumulateGrad 节点；源码按需取得或创建。普通非叶子 a 的 canonical edge 则是 grad_fn 与 output_nr 的组合。a.grad 默认不保留；retain_grad() 让该例中的中间梯度可以读出。

## 把对象关系还原成梯度传播
L 的两条路径分别把 3 与 4 送给 UnbindBackward0 的第 0、1 个输入槽位。unbind 的反向将两份标量还原为向量 [3,4]；乘 2 的反向得到 [6,8]。这是槽位路由与跨边传递的教学例，不是 C++ 对象地址或真实线程执行跟踪。[OBJ-3]

示例是有限范围的教学与行为验证，不是完整 C++ 实现复现。
