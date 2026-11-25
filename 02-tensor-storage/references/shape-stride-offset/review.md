# Reflection review

- G0 去重，区别于 Autograd 元数据/版本计数。
- 固定源码与本地 wheel 一致。反证与边界：Element strides and offsets, not byte strides; nonnegative indices within shape.；Only nonempty tensors and nonnegative strides; empty layouts have distinct checks.；Read-only test of overlap; never write through overlapping layout.
- 本地真实 CPU demo 退出 0，预期 Git blob SHA ddae6aeb7c961246bf92513b2b421f9d5ecf6b74，提交后比对。没有 GPU 或速度、RSS、分配器实测。
- HTML 静态、浏览器、上线由独立 CI 核验。
