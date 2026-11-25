# Olah Skill 集成

实际入口：`.pi/skills/olah-style-paper-posts/SKILL.md`。完整上游 Skill 源码、示例、依赖和原始测试源文件已固定于该目录；UPSTREAM.json 记录来源提交与每个 blob SHA。上游仓库未附经核验的开源许可证，不宣称第三方资产获得额外授权；同一所有者迁移，后续对外再授权前需明确许可。

上游 SKILL.md 原样保留，其命令路径 `skills/olah-style-paper-posts` 改为 `.pi/skills/olah-style-paper-posts`，上游 examples/ 路径改为 `.pi/skills/olah-style-paper-posts/examples/`。原始测试与文档仅供参考，测试含上游仓库相对路径，不能直接在本仓库运行；不要把它们当作本项目已运行的测试。

```bash
python -m pip install -r .pi/skills/olah-style-paper-posts/requirements-dev.txt
python -m playwright install chromium
python .pi/skills/olah-style-paper-posts/scripts/new_post.py --slug autograd-engine --title 'Autograd Engine' --out 05-autograd/diagrams
# 填写真实文章、证据和图示后再执行：
python .pi/skills/olah-style-paper-posts/scripts/validate.py 05-autograd/diagrams/autograd-engine/index.html
python .pi/skills/olah-style-paper-posts/scripts/extract_svg.py 05-autograd/diagrams/autograd-engine/index.html --out 05-autograd/diagrams/autograd-engine/assets
python .pi/skills/olah-style-paper-posts/scripts/browser_check.py 05-autograd/diagrams/autograd-engine/index.html --output 05-autograd/diagrams/autograd-engine/qa
```

注意：new_post.py 会覆盖同名文章的 index.html/evidence.json；只用于新 slug。上游浏览器脚本使用 set_content，外部相对资源的解析和真实 file:// 导航需要另做验证；检查实际页面键盘操作、链接、离线资源和截图，不能仅凭单一脚本判定上线。
