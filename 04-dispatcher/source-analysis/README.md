# 算子分派：源码分析

候选入口（路径随版本变化，尚未验证）：
- `aten/src/ATen/core/dispatch`
- `c10/core/DispatchKey.h`

记录 PyTorch tag/commit、调用链、输入输出、边界条件、分派/执行路径；外部项目单独固定版本。
