# Reflection review

- 去重：本批新增对象模型、代码生成、Python 扩展机制；与首批 VJP、Engine、SavedVariable 内容交叉引用，不重复论题。
- 核验：fn-1: Normal eager route; functorch transforms have a separate branch.；fn-2: Non-Tensor scalar input returns None; higher-order support depends on differentiable backward and saved values.；fn-3: CPU float64 examples; no generic guarantee for all inputs or transforms.
- 实际执行 CPU demo，退出码 0。原始文件 Git blob SHA 7633f7aeaea8fb1725237496767db06cba3029ca，待提交后与远端比对。未运行 GPU、C++ 重编译或性能基准，不声称这些完成。
- 静态与浏览器 QA 由 Pages CI 独立核验；不将研究 handoff-ready 等同上线。
