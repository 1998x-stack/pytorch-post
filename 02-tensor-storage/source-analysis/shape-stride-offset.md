# Shape、Stride、Storage Offset：张量地址映射的数学体系 — 固定源码

PyTorch 2.10.0+cpu git_version 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。

- [TensorImpl shape and offset](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/c10/core/TensorImpl.h#L2923-L2934) — c10/core/TensorImpl.h:2923–2934
- [TensorImpl data byte offset](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/c10/core/TensorImpl.h#L1670-L1693) — c10/core/TensorImpl.h:1670–1693
- [as_strided_tensorimpl](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/native/TensorShape.cpp#L1409-L1421) — aten/src/ATen/native/TensorShape.cpp:1409–1421
- [checkInBoundsForStorage](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/native/Resize.h#L83-L124) — aten/src/ATen/native/Resize.h:83–124
- [setStrided checks and metadata](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/native/Resize.h#L183-L203) — aten/src/ATen/native/Resize.h:183–203

- For a nonempty ordinary tensor, element index in storage = offset + sum(i_d × stride_d); byte address = base + itemsize × index. 限制：Element strides and offsets, not byte strides; nonnegative indices within shape.
- For nonnegative strides, maximum reached index is offset + sum((size_d−1) × stride_d); nonempty storage requires (max_index+1) × itemsize bytes or more. 限制：Only nonempty tensors and nonnegative strides; empty layouts have distinct checks.
- An explicit Python offset enumerator matches three native as_strided layouts, including zero stride, and out-of-bounds as_strided raises RuntimeError. 限制：Read-only test of overlap; never write through overlapping layout.
