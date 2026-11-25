# Tensor Storage 首批研究评审

三个独立主题：对象模型、地址映射、view 兼容性。已检查 02 骨架、12 篇既有文章及开放 PR；不重复 Autograd 对象模型。2019 论文只作架构背景；具体字段、算法以固定 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0 为主。实际 CPU 三个 demo 退出 0，预期 blob SHA：tensor-storage-object-model 1fca167aeb40ab7080c53ed8fa5b2798e715d79b；shape-stride-offset ddae6aeb7c961246bf92513b2b421f9d5ecf6b74；view-reshape-transpose 824823a072c56d0fc85c3a8cedbffec701639dbe。关键反证：非 contiguous 并不等于不可 view；零 stride 可重叠但不越界；Storage 容量不是 RSS；空张量指针不能作所有权判断。未测试 GPU、特殊 layout、符号 shape 或性能。HTML QA 与部署状态以 CI 为准。
