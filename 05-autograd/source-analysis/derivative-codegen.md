# derivatives.yaml：从导数规则到自动生成反向算子 — 固定源码

PyTorch wheel 2.10.0+cpu 的 git_version 为 449b1768410104d3ed79d3bcfe4ba1d65c7f22c0，与已核验的源码版本一致。

- [ATen mul.Tensor schema](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/aten/src/ATen/native/native_functions.yaml#L4301-L4306) — aten/src/ATen/native/native_functions.yaml:4301–4306
- [derivatives.yaml VJP rules](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/tools/autograd/derivatives.yaml#L1212-L1215) — tools/autograd/derivatives.yaml:1212–1215
- [gen_autograd pipeline](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/tools/autograd/gen_autograd.py#L59-L95) — tools/autograd/gen_autograd.py:59–95
- [Autograd wrapper grad_fn / next edges](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/tools/autograd/gen_variable_type.py#L608-L634) — tools/autograd/gen_variable_type.py:608–634
- [Backward derivative template](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/tools/autograd/gen_autograd_functions.py#L185-L191) — tools/autograd/gen_autograd_functions.py:185–191
- [mul_tensor_backward](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/FunctionsManual.cpp#L602-L608) — torch/csrc/autograd/FunctionsManual.cpp:602–608
- [InputMetadata::reduce_grad](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/input_metadata.cpp#L137-L141) — torch/csrc/autograd/input_metadata.cpp:137–141
- [Engine validates and reduces gradient](https://github.com/pytorch/pytorch/blob/449b1768410104d3ed79d3bcfe4ba1d65c7f22c0/torch/csrc/autograd/engine.cpp#L935-L946) — torch/csrc/autograd/engine.cpp:935–946

- gen_autograd loads derivatives.yaml and calls generators for VariableType and Functions; generated derivative templates assign gradients for needed inputs. 限制：Not every op uses generated explicit derivatives; composite or manual paths exist.
- mul.Tensor reverse rules use mul_tensor_backward; the helper multiplies by conjugate of the other operand and handles real/complex conversion; engine metadata handles compatible broadcast reduction. 限制：Article derivation is real-valued; complex details not derived.
