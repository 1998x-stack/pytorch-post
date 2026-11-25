#!/usr/bin/env python3
"""Build a curated static site from the component catalog and explicit post registry."""
import argparse
import html
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
STYLE = """
:root{color-scheme:light;--ink:#203035;--sub:#53676d;--accent:#147f80;--paper:#fffdf9;--line:#dce8e4}
*{box-sizing:border-box}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 system-ui,-apple-system,"PingFang SC","Microsoft YaHei",sans-serif}
main{max-width:1130px;padding:2.5rem 1.2rem 4rem;margin:auto}h1{font-size:clamp(2.1rem,6vw,4rem);line-height:1.14;margin:.65rem 0}h2{margin:2.3rem 0 .9rem}a{color:var(--accent);text-underline-offset:.18em}a:focus-visible{outline:3px solid var(--accent);outline-offset:4px}.eyebrow{font-size:.78rem;letter-spacing:.15em;color:var(--accent);font-weight:700}.dek{font-size:1.13rem;color:var(--sub);max-width:780px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:1rem}.card{border:1px solid var(--line);border-radius:12px;padding:1rem;background:white;min-width:0;overflow-wrap:anywhere}.card h3{margin:0 0 .55rem}.card p{margin:.55rem 0}.meta{font-size:.85rem;color:var(--sub)}.stat{display:flex;gap:1.2rem;flex-wrap:wrap;padding:1rem 0;border-bottom:1px solid var(--line)}footer{margin-top:3rem;border-top:1px solid var(--line);padding-top:1rem;color:var(--sub);font-size:.88rem}
"""
def require(condition, message):
    if not condition:
        raise ValueError(message)

def e(value):
    return html.escape(str(value), quote=True)

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")

def page(title, content):
    return f'<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{e(title)}</title><style>{STYLE}</style></head><body><main>{content}<footer>PyTorch Post · <a href="https://github.com/1998x-stack/pytorch-post">研究仓库</a></footer></main></body></html>\n'

def build(out):
    catalog = json.loads((ROOT / "catalog/components.json").read_text(encoding="utf-8"))
    registry = json.loads((ROOT / "catalog/posts.json").read_text(encoding="utf-8"))
    require(registry.get("schema_version") == 1, "unsupported registry schema")
    components = {c["id"]: c for c in catalog["components"]}
    require(len(components) == len(catalog["components"]), "duplicate component ID")
    posts = {}
    for p in registry["posts"]:
        cid, slug = p["component"], p["slug"]
        require(cid in components and SLUG.fullmatch(cid) and SLUG.fullmatch(slug), "invalid route")
        require((cid, slug) not in posts, "duplicate route")
        require(p["status"] == "handoff-ready", "registry includes unready research")
        expected = f"{cid}/diagrams/{slug}/index.html"
        require(p["source"] == expected, "source is not canonical")
        manifest = json.loads((ROOT / cid / "references" / slug / "research.json").read_text(encoding="utf-8"))
        require(manifest["status"] == "handoff-ready" and manifest["component"] == cid and manifest["slug"] == slug, "unready/mismatched research manifest")
        require(type(p["order"]) is int and p["order"] > 0, "invalid article order")
        if "series_component" in p or "series_order" in p:
            require(p.get("series_component") in components and p["series_component"] != cid, "invalid cross-component series")
            require(type(p.get("series_order")) is int and p["series_order"] > 0, "invalid cross-component order")
        posts[cid, slug] = p
    require(not out.exists(), "output must not exist; choose a fresh path")
    out.mkdir(parents=True)
    write(out / ".nojekyll", "")
    component_cards = []
    for cid, c in components.items():
        require(SLUG.fullmatch(cid), "invalid component path")
        rows = sorted((p for (key, _), p in posts.items() if key == cid), key=lambda p: (p["order"], p["slug"]))
        component_cards.append(f'<div class="card"><p class="meta">{e(cid)}</p><h3><a href="{e(cid)}/">{e(c["title"])}</a></h3><p>{e(c["focus"])}</p><p class="meta">{len(rows)} 篇文章 · {"有研究内容" if rows else "待研究"}</p></div>')
        cards = []
        related = [p for p in posts.values() if p.get("series_component") == cid]
        orders = [p["order"] for p in rows] + [p["series_order"] for p in related]
        require(len(orders) == len(set(orders)), f"duplicate series order in {cid}")
        for p in rows:
            slug = p["slug"]
            src = (ROOT / p["source"]).parent
            dst = out / cid / slug
            dst.mkdir(parents=True)
            for name in ("index.html", "evidence.json"):
                f = src / name
                require(f.is_file() and not f.is_symlink(), f"missing/unsafe {f}")
                shutil.copyfile(f, dst / name)
            for f in sorted((src / "assets").glob("*.svg")):
                require(f.is_file() and not f.is_symlink(), f"unsafe {f}")
                (dst / "assets").mkdir(exist_ok=True)
                shutil.copyfile(f, dst / "assets" / f.name)
            cards.append((p["order"], f'<div class="card"><p class="meta">第 {p["order"]:02d} 篇</p><h3><a href="{e(slug)}/">{e(p["title"])}</a></h3><p>{e(p["summary"])}</p></div>'))
        for p in related:
            cards.append((p["series_order"], f'<div class="card"><p class="meta">第 {p["series_order"]:02d} 篇 · 跨组件 {e(p["component"])}</p><h3><a href="../{e(p["component"])}/{e(p["slug"])}/">{e(p["title"])}</a></h3><p>{e(p["summary"])}</p></div>'))
        articles = "".join(card for _, card in sorted(cards)) or '<p>此组件尚未有通过研究交接并登记的文章。</p>'
        write(out / cid / "index.html", page(c["title"], f'<nav><a href="../">← 全部组件</a></nav><p class="eyebrow">{e(cid)}</p><h1>{e(c["title"])}</h1><p class="dek">{e(c["focus"])}</p><h2>研究系列</h2><div class="grid">{articles}</div>'))
    write(out / "index.html", page("PyTorch Post", f'<p class="eyebrow">PYTORCH INTERNALS · RESEARCH LIBRARY</p><h1>深入 PyTorch</h1><p class="dek">从论文、版本固定的源码与可重复实验出发，逐层理解张量计算、自动微分、编译器与分布式训练。</p><div class="stat"><strong>{len(components)} 个核心组件</strong><strong>{len(posts)} 篇研究文章</strong></div><h2>组件与研究系列</h2><div class="grid">{"".join(component_cards)}</div>'))
    print(f"Built {len(components)} component indexes and {len(posts)} articles at {out}")

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    try:
        build(args.out.resolve())
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"BUILD FAILED: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
