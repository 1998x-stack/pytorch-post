# Research → Olah

- 05-autograd/autograd-concurrency; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 反向传播的并发不只是多线程。分开理解 GraphTask 的调度、嵌套 backward 的死锁风险，以及设备流上的数据依赖。
- Claims: conc-1, conc-2, conc-3; locators in research.json.
- Storyboard: 线程 A、B 各自拥有独立图，梯度为 4、6。 → 外层 node 调用内层 grad；重入处理避免队列进度被阻塞，示例梯度 6。 → 生产者 stream → event / wait → 消费者 stream（仅源码机制，未实测 GPU）。
- Runnable 05-autograd/minimal-implementation/autograd-concurrency/demo.py; log 05-autograd/experiments/autograd-concurrency/cpu.log
- Scope: PyTorch 2.10 eager CPU 独立图及嵌套反向实测；CUDA canonical stream 合约仅固定源码研究，无 GPU 实验。
- handoff-ready for declared CPU/source scope; publication gated by QA.
