# Reflection review

- G0 去重，区别于 Autograd 元数据/版本计数。
- 固定源码与本地 wheel 一致。反证与边界：Sparse and special layout paths differ.；Ordinary dense path, not a universal alias guarantee.；Specific nonempty CPU sample; shape and stride determine feasibility, not is_contiguous alone.
- 本地真实 CPU demo 退出 0，预期 Git blob SHA 824823a072c56d0fc85c3a8cedbffec701639dbe，提交后比对。没有 GPU 或速度、RSS、分配器实测。
- HTML 静态、浏览器、上线由独立 CI 核验。
