# Autograd 第二批研究评审

第 04–06 篇：对象模型、derivatives.yaml / 代码生成、Custom Function。G0 查重已完成；当前分支无开放 PR，旧三篇主题不重复。本地 PyTorch 2.10.0+cpu、Python 3.13.5 三个 demo 均退出 0，真实输出已归档。文件 blob 预期：autograd-object-model fef2e2728008bf00bc99ae77b2cc863528b94c0b；derivative-codegen b0e9e289b490cdb239ba77f648b341569854f492；custom-autograd-function 7633f7aeaea8fb1725237496767db06cba3029ca。以源码固定 commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0 为证据，不把 2017 论文误当现代内部实现说明。三篇均具有独立 SVG、可操作状态与 evidence.json；CI 将验证全站。没有执行代码生成重新编译、GPU 性能测试或 torch.func 兼容性。手工截图审查与线上访问以实际结果为准。
