---
name: pytorch-research
description: Research PyTorch internals and ecosystem components from primary papers, version-pinned source code, algorithms, minimal implementations, reproducible experiments and benchmarks; audit evidence and hand off verified findings to olah-style-paper-posts. Use for PyTorch component investigations, implementation tracing, comparison of releases, or technical research reviews.
---

# PyTorch Research

Research first, presentation second. This skill owns technical evidence and reproducibility; the sibling [olah-style-paper-posts](../olah-style-paper-posts/SKILL.md) skill owns HTML/SVG presentation and browser QA. Never generate a polished article to conceal incomplete research.

## Entry and scope

Read root AGENTS.md, catalog/components.json, and the selected component README. Resolve one component ID, one precise research question, one lowercase kebab-case topic slug, a PyTorch release/tag and resolved full commit, plus any separate ecosystem dependency revision. If version selection is not specified, choose a documented release relevant to the question and record why; never silently equate main, stable docs and an installed wheel. Treat catalog links as candidates, not validated evidence.

Use [routing.md](references/routing.md) to choose relevant components and depth. No GPU or paper access is not a reason to invent evidence. A source-only investigation may use official code/docs instead of a nonexistent paper; label it as such.

## Ordered gates (stop or mark blocked when evidence is insufficient)

### G0 — Survey and deduplicate (before writing)
Read existing component research manifests, titles, papers, source-analysis, diagrams and open PRs when remote access exists. Search primary sources and identify candidate revisions. Compare topic, scope, version and paper identifiers; a paper may legitimately support multiple distinct components. Reuse existing research rather than creating a duplicate. Record search queries, existing matches, selected scope and decision in the research notes; report unavailable remote checks. See [evidence.md](references/evidence.md).

### G1 — Evidence and version pinning
Read the primary paper's relevant sections/appendix, official docs, and actual implementation at the resolved commit. Capture paper title, authors, publication/preprint version, DOI/arXiv, sections/figures/tables; for code record repository, commit, path, symbol, line range and permalink. Separate direct, direct-framework, direct-ecosystem, algorithm, dependency, related, official-doc and source-code relationships. Distinguish stated guarantees, observed behavior, deductions and hypotheses. Record conflicting evidence rather than silently resolving it. See [source-tracing.md](references/source-tracing.md).

### G2 — Mechanism and algorithm
Trace a real entry point to runtime/kernel, recording guards, dispatch keys, shapes, dtype, device, stride/aliasing, synchronization and failure paths where relevant. Derive equations, invariants, complexity and assumptions. Distinguish eager/compiled, forward/backward and CPU/GPU variants; identify boundaries with neighboring components. Produce a small counterexample or edge case. Do not assume source paths from catalog still exist.

### G3 — Minimal implementation and correctness
Specify expected behavior and tolerances before coding. Implement a minimal, independently understandable mechanism, compare against native PyTorch when available, and test success plus edge/failure cases. Record dependencies, actual installed versions, seeds and invocation. If no meaningful implementation exists, document why and mark correctness run not-applicable; if it should run but cannot, mark not-run and block handoff. Never confuse a toy with production or paper reproduction. See [experiments.md](references/experiments.md).

### G4 — Experiments and benchmarks
Run only relevant controlled experiments; record environment, exact commands, warmups, repetitions, raw samples, baseline, units, synchronization and correctness preconditions. Separate compilation from steady state, allocated from reserved memory, and global from rank-local metrics. Failed runs and negative findings are evidence; keep logs. If hardware is missing, do not simulate a measured speedup. A non-empirical research topic may mark benchmark not-applicable with a concrete reason.

### G5 — Reflection and independent cross-check
Use [review.md](references/review.md): attempt to falsify claims; check code revision, equation, dispatch/graph path, edge cases, numerical tolerances, units, evidence mapping, duplicates and limitations. Reopen earlier gates when a material flaw is found. Record findings and fixes, unresolved limitations, actual commands/results and readiness decision. No high-severity unresolved correctness/evidence finding may pass.

### G6 — Research package and handoff
Use [output-contract.md](references/output-contract.md) and assets/research.template.json. The canonical manifest is <component>/references/<slug>/research.json. Store notes/code/results in the matching existing subdirectories; do not create a second top-level taxonomy. Run from the repository root:

```bash
python .pi/skills/pytorch-research/scripts/validate_research.py --repo . <component>/references/<slug>/research.json
python .pi/skills/pytorch-research/scripts/validate_research.py --repo .
python scripts/validate_structure.py
```

Structural validation is not evidence verification. Only mark handoff-ready after G0–G5, required verified claims, completed applicable correctness checks, and human/agent evidence audit. Draft/blocked manifests may be structurally valid but are not publication-ready. Use handoff.md to communicate the verified claims, source locators, diagrams storyboard, runnable examples, raw results and unresolved exclusions to the Olah skill; it must retain citations and do its own QA. Never write HTML in this skill unless explicitly acting under the second skill. Never modify the vendored skill to fit a topic.

## Hard constraints

- Do not fabricate references, paper results, source symbols/line numbers, version identities, hardware metrics or execution status.
- Preserve exact evidence and provenance; no unauthorized bulk copying, secrets, or unreviewed downloads/execution.
- No topic duplication, uncontrolled dependency upgrades, or unrelated repository edits.
- Keep one research topic per PR where practical. Inspect diff and actual checks; distinguish scaffold, draft, blocked, handoff-ready and separately reviewed article publication.
- Report any missing source access, runtime, GPU or browser QA explicitly. A failed/omitted test is never a pass.

## Resources

- [routing.md](references/routing.md): component and cross-component routing.
- [evidence.md](references/evidence.md): literature and claim ledger.
- [source-tracing.md](references/source-tracing.md): pinned code, call graph, invariants.
- [experiments.md](references/experiments.md): reproducibility and benchmarks.
- [review.md](references/review.md): adversarial reflection and release gates.
- [output-contract.md](references/output-contract.md): file layout, status rules, handoff.
- [research.template.json](assets/research.template.json), [handoff.template.md](assets/handoff.template.md): reusable contracts.
- scripts/validate_research.py and tests/test_validate_research.py: standard-library manifest guard and synthetic regression tests.
