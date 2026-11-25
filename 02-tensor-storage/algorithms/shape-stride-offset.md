# Shape、Stride、Storage Offset：张量地址映射的数学体系 — 机制与算法

## 形状决定索引空间，步长决定地址
一维 Storage 只提供原始字节；Tensor 的 shape 规定每个坐标的范围，stride 指定该维索引增加 1 时跨越多少元素，storage_offset 给出起点。形状相同的张量可以拥有完全不同的物理布局。

## 统一地址公式
将 storage 的第一个元素编号为 0。对 d 维坐标 i，存储元素编号是偏移加各维步长的线性组合。（结构化公式见 HTML。）字节地址为 storage_base + itemsize × p。例：shape=(2,3)，stride=(4,1)，offset=1，则第二行第三列（零起点 i=(1,2)）访问 1+4+2=7。[STRIDE-1]

## 越界与重叠是不同概念
对于非空、非负步长布局，最大索引为 o+Σ(size−1)stride。需要的存储字节跨度为 (最大索引+1)×itemsize。Resize.h 的 checkInBoundsForStorage 使用计算出的字节数核验容量；setStrided 检查 stride 和 offset 再写入元数据。shape=(2,3)、stride=(10,1)、offset=1 要访问索引 13，12 元素存储不足，实测拒绝。[STRIDE-2]零步长使不同逻辑坐标映射到同一地址；重叠并不等于越界。重叠布局的原地写入可能存在未定义或被拒绝的行为，本篇仅进行读取。

## 用枚举器验证三种布局
同一个 0..11 的 Storage 分别映射成普通有间隔切片、换维布局和零步长重复行。教学实现直接枚举合法索引并与 PyTorch as_strided 比较。空维、负步长和非标准布局不在模型范围内。[STRIDE-3]
