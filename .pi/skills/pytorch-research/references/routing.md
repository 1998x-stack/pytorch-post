# Component routing
Use catalog/components.json as the authority for the 25 IDs. Route by the primary question, not a paper's broad title. The same source may be cited from distinct topics, but a claim/implementation should have one canonical owner.

| Components | Typical questions and evidence |
|---|---|
| 01–05 | Eager execution, tensor storage/view/aliasing, ATen schema and kernels, dispatch/redispatch, reverse-mode autograd. Trace Python binding to C++/kernel; distinguish storage vs logical tensor, generated vs handwritten code. |
| 06–07 | Module registration, state_dict, hooks, optimizer mathematical update, fused/foreach/single implementations. Compare state and gradients on deterministic inputs. |
| 08–12 | FX graph, Dynamo guards and graph breaks, AOTAutograd functionalization/partition, Inductor lowering/scheduler/codegen, Triton kernels. Capture graph artifacts and specify compile backend/version. |
| 13–14 | CUDA stream/event, allocator lifetime, fragmentation, checkpointing. Distinguish synchronization, allocated/reserved/peak and device/host timing. |
| 15–18, 25 | DDP bucket/reducer, FSDP state sharding, DTensor placements, TP/PP, TorchTitan orchestration. Record world size, mesh, rank-local/global shape, collective ordering and external revision. |
| 19–20 | SDPA backend and FlashAttention IO/softmax vs FlexAttention score/block mask. Record mask semantics, numerical tolerance, dtype, device and fallback. |
| 21–24 | PTQ/QAT and TorchAO, DataLoader worker/sampler, profiler traces, export constraints/deployment. Distinguish main repository from external ecosystem. |

Cross-component work: choose one canonical owner and link neighboring topic manifests. For source-only topics, do not invent a paper; record searches and use code/docs. For a version comparison, record both full SHAs, changed symbols and same-input tests; do not confuse API change with algorithm change.
