# Reflection review
Before handoff, review from the perspectives of a framework maintainer, skeptical researcher, reproduction engineer and teaching author. Write findings under references/<slug>/review.md with severity, evidence, fix, residual risk and verification.

| Gate | Failure examples |
|---|---|
| Scope & novelty | Same topic/version already exists; paper reused without a new question. |
| Evidence | Invented source lines, abstract-only claim, related paper mistaken for implementation, version mismatch. |
| Mechanism | Wrong dispatch path, graph/shape, aliasing, gradient, synchronization or rank semantics. |
| Implementation | Toy presented as production, missing negative test, assertion-free demo, numerical mismatch. |
| Measurement | Timing without synchronization, inconsistent baseline, missing units/raw logs, unexecuted result. |
| Handoff | Unsupported chart, missing claim locator, unclear exclusions or stale source pins. |

Block handoff on unresolved material correctness/evidence issues or required correctness not-run/failed. For optional experiments, distinguish not-applicable with rationale from not-run; disclose absent measurements and exclude dependent claims. Rerun affected tests after fixes. Review outcomes describe actual checks and residual limits, never simply "passed" based on file presence.
