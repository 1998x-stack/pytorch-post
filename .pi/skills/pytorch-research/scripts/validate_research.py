#!/usr/bin/env python3
"""Validate research manifests structurally; never certify evidence truth."""
import argparse
import json
import re
from pathlib import Path

SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
SHA = re.compile(r"[0-9a-f]{40}")
REL = {"direct", "direct-framework", "direct-ecosystem", "algorithm", "dependency", "related", "official-doc", "source-code"}
ROLE_DIR = {"papers": "papers", "source-analysis": "source-analysis", "algorithms": "algorithms", "implementation": "minimal-implementation", "experiments": "experiments", "benchmarks": "benchmarks", "review": "references", "handoff": "references"}

def require(condition, message):
    if not condition:
        raise ValueError(message)

def nonempty(value):
    return isinstance(value, str) and bool(value.strip())

def records(data, key):
    values = data.get(key)
    require(isinstance(values, list), key + " must be a list")
    result = {}
    for row in values:
        require(isinstance(row, dict), key + " entry must be an object")
        ident = row.get("id")
        require(nonempty(ident) and SLUG.fullmatch(ident), key + " invalid id")
        require(ident not in result, key + " duplicate id: " + ident)
        result[ident] = row
    return result

def artifact(repo, component, value, folders):
    require(nonempty(value), "missing artifact path")
    rel = Path(value)
    require(not rel.is_absolute() and ".." not in rel.parts, "unsafe artifact path: " + value)
    require(len(rel.parts) >= 3 and rel.parts[0] == component and rel.parts[1] in folders, "artifact outside expected component/directory: " + value)
    full = (repo / rel).resolve()
    require(full.is_relative_to((repo / component).resolve()) and full.is_relative_to(repo.resolve()), "artifact escapes repository/component")
    require(full.is_file() and full.stat().st_size > 0, "missing or empty artifact: " + value)
    return full

def validate(repo, path):
    repo = repo.resolve()
    path = path.resolve()
    require(path.is_relative_to(repo), "manifest outside repository")
    catalog = json.loads((repo / "catalog/components.json").read_text(encoding="utf-8"))
    data = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(data, dict) and data.get("schema_version") == 1, "expected schema_version 1")
    component, slug = data.get("component"), data.get("slug")
    require(component in {c["id"] for c in catalog["components"]}, "unknown component")
    require(nonempty(slug) and SLUG.fullmatch(slug), "invalid slug")
    require(path == repo / component / "references" / slug / "research.json", "noncanonical manifest path")
    status = data.get("status")
    require(status in {"draft", "blocked", "handoff-ready"}, "invalid status")
    ready = status == "handoff-ready"
    require(nonempty(data.get("scope")), "missing scope")
    commit = data.get("pytorch_commit")
    require(isinstance(commit, str) and (not commit or SHA.fullmatch(commit)), "invalid PyTorch commit")
    blockers = data.get("blockers")
    require(isinstance(blockers, list) and all(nonempty(b) for b in blockers), "invalid blockers")
    require(status != "blocked" or blockers, "blocked status needs reason")
    require(not ready or (commit and not blockers), "ready needs pinned commit and no blockers")
    sources, claims, runs = (records(data, key) for key in ("sources", "claims", "runs"))
    for ident, source in sources.items():
        require(source.get("kind") in {"paper", "code", "official-doc", "external-doc", "other"}, ident + ": invalid source kind")
        require(source.get("relationship") in REL, ident + ": invalid relationship")
        require(source.get("status") in {"verified", "unverified"}, ident + ": invalid source status")
        url = source.get("url")
        require(nonempty(url) and url.startswith("https://"), ident + ": missing HTTPS source URL")
        if source["status"] == "verified":
            require(all(nonempty(source.get(k)) for k in ("title", "version", "locator")), ident + ": verified source lacks metadata")
            if source["kind"] == "code":
                require(SHA.fullmatch(source["version"]) and source["version"] in url, ident + ": code source requires full commit permalink")
    for ident, run in runs.items():
        require(run.get("kind") in {"correctness", "experiment", "benchmark"}, ident + ": invalid run kind")
        state = run.get("status")
        require(state in {"passed", "failed", "not-run", "not-applicable"}, ident + ": invalid run status")
        if state in {"passed", "failed"}:
            require(all(nonempty(run.get(k)) for k in ("command", "environment")), ident + ": missing execution metadata")
            artifact(repo, component, run.get("raw_log"), {"experiments", "benchmarks"})
        else:
            require(nonempty(run.get("reason")), ident + ": missing reason")
    for ident, claim in claims.items():
        require(nonempty(claim.get("statement")) and nonempty(claim.get("limitation")), ident + ": missing claim/limitation")
        require(claim.get("kind") in {"paper", "implementation", "deduction", "measured"}, ident + ": invalid claim kind")
        require(claim.get("status") in {"verified", "unverified"}, ident + ": invalid claim status")
        evidence = claim.get("evidence")
        require(isinstance(evidence, list) and all(isinstance(e, str) and e in sources for e in evidence), ident + ": unknown source")
        if claim["status"] == "verified":
            require(evidence and all(sources[e]["status"] == "verified" for e in evidence), ident + ": verified claim requires verified evidence")
            if claim["kind"] == "measured":
                run = runs.get(claim.get("run_id"))
                require(run and run["status"] == "passed", ident + ": measured claim needs executed passed run")
        require(not ready or claim["status"] == "verified", ident + ": unverified claim blocks handoff")
    items = data.get("artifacts")
    require(isinstance(items, list), "artifacts must be a list")
    roles, paths = set(), set()
    for item in items:
        require(isinstance(item, dict) and item.get("role") in ROLE_DIR, "invalid artifact role")
        role = item["role"]
        full = artifact(repo, component, item.get("path"), {ROLE_DIR[role]})
        require(full not in paths, "duplicate artifact path")
        roles.add(role)
        paths.add(full)
    if ready:
        require(claims and any(s["kind"] == "code" and s["status"] == "verified" for s in sources.values()), "ready needs claims and verified pinned code")
        require({"papers", "source-analysis", "algorithms", "review", "handoff"} <= roles, "ready missing required artifacts")
        for name in ("review.md", "handoff.md"):
            require(path.parent / name in paths, "ready missing canonical " + name)
        correctness = [x for x in runs.values() if x["kind"] == "correctness"]
        require(correctness and all(x["status"] in {"passed", "not-applicable"} for x in correctness), "required correctness run incomplete")
        require(not any(x["status"] == "passed" for x in correctness) or "implementation" in roles, "passed correctness needs implementation artifact")
    return status

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", type=Path)
    parser.add_argument("--repo", type=Path, default=Path.cwd())
    args = parser.parse_args()
    repo = args.repo.resolve()
    try:
        if args.manifest:
            paths = [repo / args.manifest]
        else:
            catalog = json.loads((repo / "catalog/components.json").read_text(encoding="utf-8"))
            paths = sorted(p for c in catalog["components"] for p in (repo / c["id"] / "references").glob("*/research.json"))
        failures = 0
        for path in paths:
            try:
                status = validate(repo, path)
                print(f"STRUCTURE OK [{status}]: {path.relative_to(repo)}")
            except (ValueError, OSError, KeyError, TypeError) as exc:
                print(f"INVALID {path}: {exc}")
                failures += 1
        print(f"{len(paths)} manifest(s), {failures} invalid; evidence truth not tested" if paths else "No research manifests; no research readiness established.")
        return int(bool(failures))
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(f"INVALID repository: {exc}")
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
