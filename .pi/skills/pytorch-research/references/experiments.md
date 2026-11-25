# Reproducibility and benchmarks

Define hypothesis, expected behavior and comparison first. Record OS, Python/PyTorch builds, CPU/GPU model, CUDA/driver, relevant library versions, threads, seed, dtype/shape, flags, command and exit status. Save raw stdout/stderr, samples and results under the component. Avoid dependency installation or scripts from unreviewed sources.

## Correctness
Use deterministic small inputs; compare expected values and native PyTorch with explicit tolerances, gradient or shape checks as relevant. Include an edge/failure case. Where native comparison isn't possible, explain oracle and limitations. Distinguish not-run (missing required runtime), not-applicable (no meaningful test), failed and passed. A negative research result can come from a successful measurement run.

## Performance
Baseline and variant must have equivalent semantics. Use warmup, repetitions, raw samples, median/dispersion and units; separate first compilation from steady state. Synchronize CUDA or use events correctly, measure allocated/reserved/peak memory distinctly, document cache effects and transfer inclusion. Distributed: fixed world size, topology, backend, synchronization and rank aggregation. Do not extrapolate synthetic CPU numbers to GPU or infer unmeasured speedups.

A benchmark result must be reproducible from a command, environment, raw data and analysis. Do not claim performance improvement without measured evidence. If hardware isn't available, record a proposed experiment and not-run status; do not use it for measured claims.
