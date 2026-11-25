# GitHub Pages 发布体系

站点预计地址：https://1998x-stack.github.io/pytorch-post/ （需实际部署后验证）。

## 首次开启（仓库管理员）

打开 https://github.com/1998x-stack/pytorch-post/settings/pages ，Build and deployment → Source → GitHub Actions。然后在 https://github.com/1998x-stack/pytorch-post/actions 运行 PyTorch Pages workflow（main）。如果已经开启且来源为 GitHub Actions，则 main push 会触发。连接器不提供 Pages 管理接口，不应把提交 workflow 当作已启用 Pages；actions/configure-pages 的 enablement 需要额外权限 token，不在仓库内写入或索取凭据。

## 路径与构建

- 首页 /：25 组件索引、文章数量、待研究状态。
- /05-autograd/：系列目录。
- /05-autograd/<slug>/：文章，含本地 SVG 和 evidence.json。
- 唯一文章源：<component>/diagrams/<slug>/index.html；不重复维护发布副本。
- catalog/posts.json：显式登记经过研究交接的主题；构建只复制登记文章、独立 SVG 与证据 JSON，不公开内部 QA、原始日志、.pi 或全部仓库。
- 发布门槛：结构、研究包、Skill 单测、Olah 静态校验、站内链接、真实 Chromium 各尺寸与键盘交互；失败不部署。QA 结果及截图留在 Actions artifact。

本地命令（输出目录必须不存在）：

```bash
python scripts/validate_structure.py
python .pi/skills/pytorch-research/scripts/validate_research.py --repo .
python scripts/build_pages.py --out _site
python -m pip install 'beautifulsoup4>=4.12,<5' 'playwright>=1.45,<2'
python -m playwright install chromium
python scripts/qa_pages.py _site --reports _qa
python -m http.server 8000 --directory _site
```

访问 http://localhost:8000/。部署成功后检查首页、组件索引、三篇文章与 SVG 请求。构建不需要 GPU 或安装 PyTorch；实验复现另行执行。
