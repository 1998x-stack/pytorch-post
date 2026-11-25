# Research package contract
Work from repo root. Each topic has one slug in the chosen component:

```text
<component>/
  papers/<slug>.md
  source-analysis/<slug>.md
  algorithms/<slug>.md
  minimal-implementation/<slug>/...
  experiments/<slug>/...
  benchmarks/<slug>/...
  references/<slug>/research.json
  references/<slug>/review.md
  references/<slug>/handoff.md
  diagrams/<slug>/...  # only from the Olah skill
```

Use assets/research.template.json as a draft; replace its placeholders, do not publish the template as research. Paths in the manifest are repository-relative and confined to that component. References to shared research may be documented in notes, not represented as local artifacts. Source IDs and claim IDs are unique within their respective collections. Run IDs identify execution records. Artifact roles: papers, source-analysis, algorithms, implementation, experiments, benchmarks, review, handoff. Source-only topics still produce a papers note explaining search results and absence of a direct paper.

Statuses:
- draft: evidence collection in progress.
- blocked: a material issue or required unavailable execution; include blockers.
- handoff-ready: no blockers, full PyTorch commit, at least one verified code source, at least one claim, all claims verified with verified sources, required notes/review/handoff exist, and a correctness run passed or is genuinely not-applicable with reason. Measured claims must reference a passed run with actual raw output. For handoff-ready, a correctness run not-run/failed is blocking; optional benchmark not-run/failed is permitted only if disclosed and no claim relies on it. A successful correctness run requires a declared implementation artifact. Every passed/failed run has command, environment and a raw-log path in experiments or benchmarks. A not-run/not-applicable run has a reason.

The validator checks shape, IDs, cross-references, status gates and local file existence, not source accuracy, experimental integrity or review conclusions. A draft with unresolved evidence can be structurally valid. Do not mark a manifest handoff-ready to satisfy the checker. A corpus scan with no manifests has no research to validate. Preserve old evidence and update claim versions if revising a topic.

Handoff: fill handoff.md from template with verified claim IDs and storyboard; Olah skill produces HTML, evidence.json, SVG, executable demo and browser reports, and rechecks citations. Do not copy research uncertainty into an unqualified article claim. Publication is a separate decision.
