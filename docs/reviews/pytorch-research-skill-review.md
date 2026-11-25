# Research Skill design review

The research skill is an independent, repository-local skill, with no modifications to vendored Olah files. The 25-component catalog remains the routing authority. A per-topic manifest avoids a second taxonomy, supports cross-component citations, and makes draft versus ready explicit. The research package is the input to visualization, not a publication result.

Review risks: structural validation cannot verify facts, source line accuracy, version correspondence, benchmark truth, or semantic duplication. Require actual primary-source review and recorded execution evidence. A source-only research topic may justify not-applicable correctness, but missing required runtime must block. No research articles or measured benchmarks are introduced by this change. No GPU or Pi integration runtime is needed for the standard-library unit tests; actual Agent discovery and end-to-end handoff remain separate runtime checks.

## Verification evidence

- Executed `python -m unittest discover -s tests -v` in a local staging directory of the new skill: 10 tests passed (synthetic fixtures). The staged validator and test files were matched byte-for-byte to the remote Git blob SHAs `688043e46507cce5216f2bb8e289c05f5481ce84` and `c4039b73e80bab43d77322ad90a0a26fb950ec46` using `git hash-object`. This covers draft, valid synthetic handoff, duplicate IDs, invalid pin, unverified claim, measured claim without executed run, incomplete correctness, missing artifact, path traversal and blocked-without-reason.
- Compared recursive Git trees: only 11 new Skill files, this review, README and AGENTS changed. No component, catalog, or Olah vendor file changed.
- The full repository checkout/structure script, GitHub Actions and Pi Agent discovery were not executed. No actual component research, GPU benchmark, HTML generation or browser test was performed. The checker is a structural gate, not a fact verifier.
- Python 3.9+ is required by the standard-library checker (`Path.is_relative_to`).
