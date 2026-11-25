# Version-pinned source tracing

1. Resolve release tag to full commit, record official repository URL and exact installed package/build (which can differ). External Triton/TorchAO/TorchTitan/ExecuTorch etc. have independent versions. Use immutable GitHub blob permalinks (or equivalent pinned repository links).
2. Locate public Python API and real call chain; inspect schema, binding/generation, dispatch/guards and concrete backend. Cite each transition with commit, path, symbol and line range. If static inference only, say so; dynamic trace requires actual execution.
3. Record input/output contract: shape, dtype, device, stride, aliasing, mutability, grad mode, thread/stream/rank. Identify invariant, state transitions, failure path and fallback. Not every component needs every field; state applicability.
4. Compare a minimal native run or official test against the traced path when possible. For compiled code preserve graph breaks, graph IR and backend settings; for distributed execution preserve mesh and collectives. Generated code should be identified as such.
5. For version comparisons use two pinned commits, comparable environment, changed behavior and source diffs. Never attribute a modern implementation to an older paper without evidence.
