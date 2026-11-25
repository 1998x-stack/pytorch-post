# View、Reshape 与 Transpose：何时零拷贝，何时复制？ — 固定源码

PyTorch 2.10.0+cpu git_version 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0。

- [Dense transpose swaps sizes and strides](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/native/TensorShape.cpp#L3815-L3847) — aten/src/ATen/native/TensorShape.cpp:3815–3847
- [view_impl compatibility check](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/native/TensorShape.cpp#L4092-L4102) — aten/src/ATen/native/TensorShape.cpp:4092–4102
- [computeStride_impl chunk matching](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/TensorUtils.cpp#L327-L407) — aten/src/ATen/TensorUtils.cpp:327–407
- [reshape_symint alias or clone fallback](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/native/TensorShape.cpp#L2057-L2106) — aten/src/ATen/native/TensorShape.cpp:2057–2106

- Ordinary dense transpose swaps size and stride dimensions and delegates to as_strided; view_impl requires computeStride to produce compatible strides. 限制：Sparse and special layout paths differ.
- reshape_symint uses view for contiguous input, otherwise tests computeStride and uses alias or falls back to contiguous clone plus unsafe view. 限制：Ordinary dense path, not a universal alias guarantee.
- Transpose of 3×4 has (1,4) stride and shares storage; flatten view fails, reshape copies. A non-contiguous step-2 slice can flatten using view with stride (2,). 限制：Specific nonempty CPU sample; shape and stride determine feasibility, not is_contiguous alone.
