# Evidence and deduplication

## Search protocol
Start with original conference/journal/preprint and official PyTorch docs/code; search alternate names, historical versions, implementation PRs, and related systems. Record query, URL, access date, result, and why retained/excluded. Read relevant text/figures, not only search snippets or abstracts. If sources cannot be read, mark unverified. Never use a secondary explanation as primary proof.

Deduplicate by component + topic slug, conceptual question + version, normalized DOI/arXiv IDs (strip arXiv version only for matching, retain exact version for evidence), and existing PR scope. A paper can support different topics: cite once per manifest and link existing canonical notes rather than reproducing them. Compare both current manifests and older unstructured README/article content.

## Evidence types
Source kinds: paper, code, official-doc, external-doc, other. Relationship: direct, direct-framework, direct-ecosystem, algorithm, dependency, related, official-doc, source-code. A related system is not proof of PyTorch implementation. A paper claim is not a measured reproduction. For code use immutable full commit permalink, symbol and line range; for a paper use version and section/table/figure; for docs capture version and section/URL.

## Claim ledger
Every material factual claim gets a stable ID, statement, kind (paper, implementation, deduction, measured), verified/unverified status, one or more source IDs, limitation (including assumptions), and for measured claims one executed run ID. A measured claim also has raw output linked by the run; external paper-reported numbers are paper claims, not measured claims. Record contradictions and unresolved questions in review notes. Verification is a human/agent evidence judgment, not a URL existence test. Avoid overquoting copyrighted material and never place credentials or private data in the repo.
