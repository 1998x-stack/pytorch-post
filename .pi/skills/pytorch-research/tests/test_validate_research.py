"""Synthetic fixtures only; no claim about actual PyTorch behavior."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location("validator", Path(__file__).resolve().parents[1] / "scripts/validate_research.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.cid = "05-autograd"
        self.slug = "synthetic-fixture"
        self.path = self.root / self.cid / "references" / self.slug / "research.json"
        self.write("catalog/components.json", json.dumps({"components": [{"id": self.cid}]}))
        self.data = {"schema_version": 1, "component": self.cid, "slug": self.slug, "scope": "synthetic only", "status": "draft", "pytorch_commit": "", "blockers": [], "sources": [], "claims": [], "runs": [], "artifacts": []}

    def write(self, path, value):
        p = self.root / path
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(value, encoding="utf-8")
        return p

    def check(self):
        self.write(self.path.relative_to(self.root), json.dumps(self.data))
        return mod.validate(self.root, self.path)

    def ready(self):
        commit = "a" * 40
        self.data.update(status="handoff-ready", pytorch_commit=commit)
        self.data["sources"] = [{"id":"code-a","kind":"code","relationship":"source-code","status":"verified","title":"synthetic","url":"https://example.invalid/blob/"+commit+"/fake.py","version":commit,"locator":"synthetic line 1"}]
        self.data["claims"] = [{"id":"claim-a","kind":"deduction","statement":"synthetic","limitation":"fixture only","status":"verified","evidence":["code-a"]}]
        self.data["runs"] = [{"id":"correctness","kind":"correctness","status":"not-applicable","reason":"synthetic documentary fixture"}]
        for role, suffix in [("papers","papers/fixture.md"),("source-analysis","source-analysis/fixture.md"),("algorithms","algorithms/fixture.md"),("review","references/synthetic-fixture/review.md"),("handoff","references/synthetic-fixture/handoff.md")]:
            path = f"{self.cid}/{suffix}"
            self.write(path, "synthetic fixture")
            self.data["artifacts"].append({"role":role,"path":path})

    def test_draft(self):
        self.assertEqual(self.check(), "draft")

    def test_ready(self):
        self.ready()
        self.assertEqual(self.check(), "handoff-ready")

    def test_duplicate(self):
        self.ready()
        self.data["sources"] *= 2
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.check()

    def test_bad_pin(self):
        self.ready()
        self.data["sources"][0]["version"] = "main"
        with self.assertRaisesRegex(ValueError, "commit permalink"):
            self.check()

    def test_unverified_claim(self):
        self.ready()
        self.data["claims"][0]["status"] = "unverified"
        with self.assertRaisesRegex(ValueError, "blocks handoff"):
            self.check()

    def test_measured_without_run(self):
        self.ready()
        self.data["claims"][0]["kind"] = "measured"
        with self.assertRaisesRegex(ValueError, "executed passed run"):
            self.check()

    def test_required_correctness_not_run(self):
        self.ready()
        self.data["runs"][0]["status"] = "not-run"
        with self.assertRaisesRegex(ValueError, "correctness run incomplete"):
            self.check()

    def test_missing_artifact(self):
        self.ready()
        (self.root / self.data["artifacts"][0]["path"]).unlink()
        with self.assertRaisesRegex(ValueError, "missing or empty artifact"):
            self.check()

    def test_path_traversal(self):
        self.ready()
        self.data["artifacts"][0]["path"] = f"{self.cid}/papers/../../outside.md"
        with self.assertRaisesRegex(ValueError, "unsafe artifact"):
            self.check()

    def test_blocked_needs_reason(self):
        self.data["status"] = "blocked"
        with self.assertRaisesRegex(ValueError, "blocked status"):
            self.check()

if __name__ == "__main__":
    unittest.main()
