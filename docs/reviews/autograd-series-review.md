# 首批 Autograd 系列评审

3 个主题均完成固定版本源码定位、证据账本、CPU 对照实验与原始图解。实验在本地 PyTorch 2.10.0+cpu 环境执行；源码与 wheel git_version 相符。三个 demo 的 Git blob SHA 分别为 1e024c66851c3e60c7cdcf2b4eddc51b7a56e1c7, 73d4eb31ce0ceda6d3e06cbbbdd60805c6408de7, 435743cd48da05ec7961162ba367b3b1c2371108；提交后比较远端 blob。没有测量性能或 GPU，不声称完成完整 Autograd Engine 复现。2019 框架论文只核验摘要，2017 原文和 AD 综述读取相关章节。HTML 浏览器与静态 QA 由发布流水线运行；未实际获得结果前不得报告通过。

Pages 构建只复制显式登记的 handoff-ready 文章及图像、证据 JSON，组件索引由 catalog 自动生成。Pages 设置必须由有权限的管理员开启（连接器不支持 Pages 管理端点）。
