# Autograd Engine：依赖计数与梯度汇聚 — 算法与不变量

## 为什么不能收到一份梯度就执行？
设 a=2x，b=3a，c=4a，L=b+c。a 同时影响两个输出分支。若 a 的反向函数只收到 b 的贡献 3 就执行，x 会得到 6，而 c 的贡献 4 尚未处理。必须先把属于 a 同一反向输入槽位的两份贡献聚合起来，再让 a 的反向函数向 x 传播 14。

## 用计数器表达“等齐”
把反向方向的依赖边数记为 d(a)=2。收到 3 后，d=1，缓冲区是 3；收到 4 后，d=0，缓冲区是 7，此时可以调度 a。若先收到 4 也一样得到 7。真实引擎的依赖计数针对有效边，不等同于简单的 Tensor 使用次数；多输入 Node 有多个槽位。[ENG-2]

## 三个关键对象
GraphTask一次 backward 的任务状态，包括依赖、未就绪缓冲区以及是否保留图等。InputBuffer以输入槽位为单位接收和累积梯度，CPU 分支可直接移动首份梯度，后续贡献执行累积。ReadyQueue / NodeTask依赖满足后，将 Node 与输入缓冲区交给执行队列。它不是 Python 前向操作的简单反序列表。调用链：Python backward → Engine::execute → 创建 GraphTask → compute_dependencies → execute_with_graph_task → evaluate_function → InputBuffer / ReadyQueue。单根 eager 路径可以跳过虚拟 GraphRoot。[ENG-1]

精确公式（MathML）见交接后的 HTML。教学代码只验证指定实数标量或小向量行为。
