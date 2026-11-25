# Reflection review

- G0 去重，区别于 Autograd 元数据/版本计数。
- 固定源码与本地 wheel 一致。反证与边界：Ordinary storage-backed dense tensors; not all layouts expose storage.；Empty tensors and specialized backends need separate treatment.；One nonempty CPU sample; pointer equality is not a universal ownership test.
- 本地真实 CPU demo 退出 0，预期 Git blob SHA 1fca167aeb40ab7080c53ed8fa5b2798e715d79b，提交后比对。没有 GPU 或速度、RSS、分配器实测。
- HTML 静态、浏览器、上线由独立 CI 核验。
