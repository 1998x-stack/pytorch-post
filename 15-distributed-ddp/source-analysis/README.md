# DDP：源码分析

候选入口（路径随版本变化，尚未验证）：
- `torch/nn/parallel/distributed.py`
- `torch/csrc/distributed/c10d/reducer.cpp`

记录 PyTorch tag/commit、调用链、输入输出、边界条件、分派/执行路径；外部项目单独固定版本。
