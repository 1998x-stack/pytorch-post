# Tensor 与 Storage：数据、元数据和所有权 — 固定源码

PyTorch 2.10.0+cpu git_version 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。

- [TensorBase intrusive pointer](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/core/TensorBase.h#L954-L955) — aten/src/ATen/core/TensorBase.h:954–955
- [TensorImpl storage field](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/c10/core/TensorImpl.h#L2887-L2893) — c10/core/TensorImpl.h:2887–2893
- [TensorImpl metadata fields](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/c10/core/TensorImpl.h#L2923-L2934) — c10/core/TensorImpl.h:2923–2934
- [Storage intrusive pointer](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/c10/core/Storage.h#L221-L223) — c10/core/Storage.h:221–223
- [StorageImpl data pointer and byte length](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/c10/core/StorageImpl.h#L337-L341) — c10/core/StorageImpl.h:337–341
- [TensorImpl::data_impl](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/c10/core/TensorImpl.h#L1670-L1693) — c10/core/TensorImpl.h:1670–1693
- [as_strided_tensorimpl creates view](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/native/TensorShape.cpp#L1409-L1421) — aten/src/ATen/native/TensorShape.cpp:1409–1421

- TensorBase holds an intrusive pointer to TensorImpl; TensorImpl contains Storage and layout metadata, while Storage points to StorageImpl containing DataPtr and byte length. 限制：Ordinary storage-backed dense tensors; not all layouts expose storage.
- A strided view can create a new TensorImpl sharing Storage; a nonempty ordinary tensor data pointer includes byte offset = element_size × storage_offset. 限制：Empty tensors and specialized backends need separate treatment.
- A 3×4 int64 base and its 3×2 slice share 96 storage bytes; clone owns 48 bytes; slice mutation changes base but not clone. 限制：One nonempty CPU sample; pointer equality is not a universal ownership test.
