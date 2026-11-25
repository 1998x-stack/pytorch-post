# Autograd 对象模型：Tensor、AutogradMeta、Node 与 Edge — 文献调查

G0: 已检查 main 的 05-autograd 文件树、现有三篇文章注册表及开放 PR（无），未发现相同主题。搜索词：Automatic differentiation in PyTorch 2017；Autograd 对象模型：Tensor、AutogradMeta、Node 与 Edge；PyTorch autograd internals / derivatives.yaml / custom Function。2017 原始论文为历史背景，沿用首批研究的已读证据；未发现专门描述当前 2.10 对象字段/生成器/接口的独立论文，现代实现以固定源码为主。

- [Automatic differentiation in PyTorch — Paszke et al. (2017)](https://openreview.net/references/pdf?id=BJJsrmfCZ) — §1, §3; historical framework design (not evidence for modern fields or codegen)
- [Autograd mechanics](https://docs.pytorch.org/docs/main/notes/autograd.html)（当前文档背景，非固定 2.10 证据）
- [How to read the autograd codebase](https://dev-discuss.pytorch.org/t/how-to-read-the-autograd-codebase/383)（开发者导读，非正式论文）

范围：PyTorch 2.10 eager CPU，普通实数 Tensor 与多输出 unbind；不覆盖 view rebase、forward AD、编译或特殊 Tensor subclass。
