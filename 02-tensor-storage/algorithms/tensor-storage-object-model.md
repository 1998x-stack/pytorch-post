# Tensor 与 Storage：数据、元数据和所有权 — 机制与算法

## 张量不是一个独占的连续数组
令 x 为 3×4 的 int64 张量，y=x[:,1:3]。y 只有六个元素，却沿用 x 的 12 个元素底层存储。Python 对象、逻辑元素数量、底层字节容量是三个不同概念。2019 NeurIPS 论文 §5.1 提供 C++ 核心历史背景，具体字段以 2.10 源码为准。

## 四层对象与引用关系
普通 C++ TensorBase 以 intrusive_ptr 持有 TensorImpl。TensorImpl 保存 Storage、sizes/strides、storage_offset、dtype 等张量元数据；Storage 是指向 StorageImpl 的句柄。StorageImpl 保存 DataPtr 和 size_bytes_，负责底层存储相关状态。不是每个 Tensor 都独占一份存储，也不是每个 Tensor 都拥有可读的 data pointer。[OBJ-1]as_strided 的普通实现以 VIEW 类型构造新 TensorImpl，复制 Storage 句柄，并设置新的形状、步长与偏移。它不是重新分配并复制所有元素。[OBJ-2]

## 两个 data_ptr 的区别
untyped_storage().data_ptr() 对应底层存储起点；普通非空 Tensor.data_ptr() 对应该张量的首个逻辑元素。切片 y 的 storage_offset=1，int64 每元素 8 字节，所以 y.data_ptr() 比 x.data_ptr() 大 8 字节，底层存储起点仍相同。空张量可能返回空指针，不能推广为指针相等就一定共享所有权。

## 共享与复制的可观察后果
修改 y[0,0] 会修改 x[0,1]；clone 的相应值不变。存储 96 B、96 B、48 B 是 Storage 报告的逻辑字节容量，不是进程 RSS 或 allocator reserved memory。Autograd 的版本计数属于另一层语义，详见 SavedVariable；共享存储与共享 autograd 版本状态不能简单画等号。[OBJ-3]
