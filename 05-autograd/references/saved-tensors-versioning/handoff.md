# Research → Olah

- Component: 05-autograd; topic: saved-tensors-versioning; revision: 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- Question: 为什么 detach() 之后修改张量仍可能让 backward 报错？理解保存的前向值、共享版本计数和反向资源生命周期。
- Claims: sv-1, sv-2, sv-3；见 research.json。
- Storyboard: 保存：x=2，saved=0，current=0；梯度应为 4 → 原地修改共享别名：x=3，saved=0，current=1；unpack 拒绝 → 修改独立 clone：原 x=2，版本未变；梯度仍为 4；原始 SVG 与可交互状态。
- Runnable: 05-autograd/minimal-implementation/saved-tensors-versioning/demo.py; logs: 05-autograd/experiments/saved-tensors-versioning/cpu.log
- Exclusions: PyTorch 2.10 eager CPU、普通 SavedVariable 无 hooks 路径；不覆盖 inference tensor、所有别名机制或 hooks；不报告未测性能数字。
- Research: handoff-ready；publication subject to independent QA.
