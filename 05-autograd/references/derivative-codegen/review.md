# Reflection review

- 去重：本批新增对象模型、代码生成、Python 扩展机制；与首批 VJP、Engine、SavedVariable 内容交叉引用，不重复论题。
- 核验：cg-1: Not every op uses generated explicit derivatives; composite or manual paths exist.；cg-2: Article derivation is real-valued; complex details not derived.；cg-3: CPU sample and installed binary only; source generator was not rebuilt.
- 实际执行 CPU demo，退出码 0。原始文件 Git blob SHA b0e9e289b490cdb239ba77f648b341569854f492，待提交后与远端比对。未运行 GPU、C++ 重编译或性能基准，不声称这些完成。
- 静态与浏览器 QA 由 Pages CI 独立核验；不将研究 handoff-ready 等同上线。
