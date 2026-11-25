# 反向自动微分：从链式法则到 VJP — 固定源码

PyTorch 2.10.0+cpu 对应提交 `449b1768410104d3ed79d3bcfe4ba1d65c7f22c0`；官方 GitHub commit 已核验，本地 wheel git_version 相同。

- [THPEngine Python backward binding](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/python_engine.cpp#L180-L272) — accumulate_grad argument and root gradient edges
- [InputBuffer::add](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/input_buffer.cpp#L192-L216) — CPU branch, InputBuffer::add

2017 年论文 §1、§3 描述即时执行和反向函数图。不能将历史 Variable 包装器直接视作今天的 Tensor 结构。2.10 源码的 Python binding 组装根边与梯度输入；CPU InputBuffer 对同一输入槽位的贡献进行累积。[AD-1] [AD-2]反向模式通常适合输出维数远小于输入维数的情况，但保存中间状态有内存成本；这里不宣称反向模式总是快于前向模式，也不把数学图等同于具体 C++ Node 图。
