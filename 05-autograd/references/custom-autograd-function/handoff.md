# Research → Olah

- 05-autograd/custom-autograd-function; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 如何让自定义计算参与 PyTorch 的反向引擎？从 apply、ctx、forward/backward 到 gradcheck 与 gradgradcheck，区分正确规则和错误规则。
- Verified claims: fn-1, fn-2, fn-3; locators in research.json.
- Storyboard: 输入 [2,-1]，scale=2；forward → [16,-2]，ctx 保存 x。 → 输出余切为 [1,1]；backward → [24,6]，scale 返回 None。 → create_graph=True 后再次微分 → [24,-12]；gradgradcheck 通过。
- Runnable 05-autograd/minimal-implementation/custom-autograd-function/demo.py; log 05-autograd/experiments/custom-autograd-function/cpu.log.
- Scope and exclusions: PyTorch 2.10 eager CPU Python 自定义 Function，combined forward(ctx,...) 模式；不覆盖 torch.func、vmap、JVP、编译或 C++ 扩展注册。; no measured performance claims.
- handoff-ready; publication gated by QA.
