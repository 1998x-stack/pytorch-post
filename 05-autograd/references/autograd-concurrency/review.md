# Reflection review

- 已查重旧九篇及 AOTAutograd 组件；AOT 主文归属 10-aot-autograd，05-autograd 只建立交叉入口。
- 反证与边界：The pool mechanism is not asserted to be used in every nested backward; CPU and accelerator routes differ.；Source-level contract only; CUDA unavailable. No claim about exact kernel overlap or latency.；Correctness and completion only; no shared-leaf race or concurrency speedup measurement.
- 本地 demo 退出 0；预期 Git blob SHA a3768afadcbcdaafd3c000bf68733d5329dbb318，提交后核对。保留实际 FX 输出，不冒称后端优化或实测 CUDA。
- 研究 handoff；HTML CI、实际部署独立确认。
