#!/usr/bin/env python3
"""Validate research scaffolds and byte-for-byte vendored Git blob identities."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".pi/skills/olah-style-paper-posts"

def main():
    catalog = json.loads((ROOT / "catalog/components.json").read_text(encoding="utf-8"))
    ids = [c["id"] for c in catalog["components"]]
    expected = [f"{i:02d}" for i in range(1, 26)]
    assert len(ids) == len(set(ids)) == 25
    assert [x.split("-", 1)[0] for x in ids] == expected
    actual = sorted(p.name for p in ROOT.iterdir() if p.is_dir() and p.name[:2].isdigit() and p.name[2:3] == "-")
    assert actual == sorted(ids), (actual, ids)
    assert catalog["subdirectories"] == ["papers","source-analysis","algorithms","minimal-implementation","experiments","benchmarks","diagrams","references"]
    for cid in ids:
        for path in [ROOT / cid / "README.md", *[ROOT / cid / sub / "README.md" for sub in catalog["subdirectories"]]]:
            assert path.is_file() and path.stat().st_size > 0, path
    manifest = json.loads((SKILL / "UPSTREAM.json").read_text(encoding="utf-8"))
    assert len(manifest["files"]) == len({x["target"] for x in manifest["files"]})
    expected_files = {x["target"] for x in manifest["files"]}
    actual_files = {p.relative_to(ROOT).as_posix() for p in SKILL.rglob("*") if p.is_file() and "__pycache__" not in p.parts and p.suffix != ".pyc" and p.name != "UPSTREAM.json"}
    assert actual_files == expected_files, (actual_files - expected_files, expected_files - actual_files)
    for item in manifest["files"]:
        path = ROOT / item["target"]
        assert path.resolve().is_relative_to(SKILL.resolve()), path
        data = path.read_bytes()
        digest = hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()
        assert digest == item["sha"], (path, digest, item["sha"])
    print(f"PASS: {len(ids)} components, {len(ids)*len(catalog['subdirectories'])} subdirectories, {len(manifest['files'])} upstream blobs")

if __name__ == "__main__":
    main()
