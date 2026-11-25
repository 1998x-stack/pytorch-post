# PyTorch Post — Agent contract

1. 先读 README、catalog/components.json、已有研究和开放 PR；同一论文或主题不重复构建。一次聚焦一个可审计组件。
2. 首先查找原始论文、官方文档、源码，固定 PyTorch tag/commit 及外部依赖版本；明确直接论文、算法基础、对照研究，不因相关性推断实现来源。候选链接未经逐条核验。
3. 按组件八目录分别保存证据、源码分析、算法、最小实现、实验、基准、图解、引用。先制定可验证假设；禁止伪造数值、输出、测试状态。
4. 生成 HTML 前必须阅读 .pi/skills/olah-style-paper-posts/SKILL.md 和 docs/skill-integration.md；遵守其 Gate 0–7。源码研究不能为了套用论文模板而虚构论文。生成文件归属组件 diagrams/<slug>/，不写进 vendor。
5. 记录环境、依赖、随机种子、运行命令、原始输出；未运行标为 not verified。完整文章必须有 evidence.json、可访问的独立 SVG、静态检查、浏览器 QA；代码和 benchmark 按适用性执行。
6. 修改前后运行 python scripts/validate_structure.py；检查差异，优先 PR，报告剩余问题。不自动合并有失败或未核验的内容，不宣称 Pages 已发布。
7. Vendor 为固定快照；更新需新上游 SHA、逐文件哈希审计、兼容性检查及独立 PR。禁止从外部任意执行未经检查的脚本。
