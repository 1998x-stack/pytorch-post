# Compiled Autograd：在 backward 时捕获更大的图 — 机制与算法

## AOTAutograd 与 Compiled Autograd 不同在哪里？
AOTAutograd 在前向编译阶段为片段建立反向图；运行时 backward 仍可能协调多个片段、eager 节点和 hooks。Compiled Autograd 将捕获入口推进到反向引擎，目标是让更大范围的实际反向调用进入 FX 表示。它不会取消 AOTAutograd，且不是保证永远没有 graph break。[CA-2]

## 运行时捕获的接口
Engine::execute 在注册 compiled autograd 回调时选择相应分支。2.10 的 _enable 注册 AutogradCompilerInstance 并在退出时恢复先前设置；proxy_call_hook 创建 FX call_function 代理，end_capture 收尾。源码同时明确 compiled autograd 的嵌套重入限制。私有 API 可能随版本改变，不建议将本例当作跨版本稳定接口。[CA-1]

## 真实图中的 hook
令 y=x²、L=sum(y)，在 y 上注册 g→3g 的 hook。反向的 SumBackward 产生 [1,1]，hook 修改为 [3,3]，PowBackward 乘以 2x 得 [12,18]，最后累积进 x.grad。真实捕获图包含 SumBackward0、call_hook、PowBackward0、call_accumulate_grad；validate_outputs 等节点处理元数据验证。本例直接以 eager forward 构图、只在 backward 周围启用 _enable，并返回 gm.forward；实测的是运行时捕获和执行语义，不是 Dynamo/Inductor 优化代码或跨多个前向 graph break 的捕获结果。[CA-3]

## 缓存、重编译与工程选择
更大的图可能给后端更多优化机会，但也带来缓存查询、图结构变化、shape 变化、hooks graph break 等开销。官方教程给出跨前向片段捕获的示例；本篇没有运行该实验，不报告其性能。生产评估需区分捕获时间、编译时间、稳定运行以及实际通信调度。
