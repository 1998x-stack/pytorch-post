# Research → Olah

- 02-tensor-storage/tensor-storage-object-model; commit 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0
- 为什么切片的元素变少了，底层存储却可能仍然一样大？区分 TensorBase、TensorImpl、Storage 和 StorageImpl。
- Claims: obj-1, obj-2, obj-3; locators in research.json.
- Storyboard: x：shape=(3,4)，stride=(4,1)，offset=0，共 96 B。 → y：shape=(3,2)，stride=(4,1)，offset=1；共享 x 的 96 B 存储。 → z：clone 创建独立 48 B 存储；修改 y 不影响 z。
- Runnable 02-tensor-storage/minimal-implementation/tensor-storage-object-model/demo.py; log 02-tensor-storage/experiments/tensor-storage-object-model/cpu.log
- Scope: PyTorch 2.10 普通 CPU dense strided、非空 int64 Tensor；不涉及 sparse/meta、量化、跨进程、分配器实际容量。
- handoff-ready; publication gated by QA.
