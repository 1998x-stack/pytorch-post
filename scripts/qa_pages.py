#!/usr/bin/env python3
"""Check generated site links, real browser navigation, viewports and interactive articles."""
import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit
from xml.etree import ElementTree
from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

SIZES = [("desktop", 1440, 900), ("mobile", 390, 844), ("narrow", 360, 800)]

def check(site, reports):
    site = site.resolve()
    reports.mkdir(parents=True, exist_ok=True)
    pages = sorted(site.rglob("index.html"))
    failures = []
    summary = []
    def verify(ok, message):
        if not ok:
            failures.append(message)
    for f in pages:
        rel = f.relative_to(site)
        soup = BeautifulSoup(f.read_text(encoding="utf-8"), "html.parser")
        verify(len(soup.select("h1")) == 1, f"{rel}: h1 count")
        verify(soup.find("main") is not None, f"{rel}: no main")
        for tag in soup.select("[href], [src]"):
            url = urlsplit(tag.get("href", tag.get("src", "")))
            if url.scheme or url.netloc:
                continue
            verify(not url.path.startswith("/"), f"{rel}: absolute project path")
            target = (f.parent / unquote(url.path)).resolve() if url.path else f
            verify(target.is_relative_to(site), f"{rel}: link escapes output")
            if target.is_dir():
                target = target / "index.html"
            verify(target.is_file(), f"{rel}: broken link {tag.get('href', tag.get('src'))}")
            if target.suffix == ".html" and target.is_file() and url.fragment:
                dest = BeautifulSoup(target.read_text(encoding="utf-8"), "html.parser")
                verify(dest.find(id=unquote(url.fragment)) is not None, f"{rel}: broken fragment {url.fragment}")
        for svg in f.parent.glob("assets/*.svg"):
            try:
                root = ElementTree.parse(svg).getroot()
                verify(root.tag.endswith("svg") and "viewBox" in root.attrib, f"{svg}: invalid SVG")
            except ElementTree.ParseError as exc:
                failures.append(str(exc))
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        for f in pages:
            rel = f.relative_to(site)
            article = len(rel.parts) == 3
            # All indexes receive a desktop browser smoke; articles also receive mobile/interaction checks.
            for label, w, h in SIZES if article else SIZES[:1]:
                page = browser.new_page(viewport={"width": w, "height": h}, reduced_motion="reduce")
                errors = []
                page.on("pageerror", lambda e: errors.append(str(e)))
                page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
                page.route("https?://**", lambda route: (errors.append("unexpected external request"), route.abort()))
                # file:// does not resolve directory navigation automatically, so use explicit index.html for loading.
                page.goto(f.as_uri(), wait_until="load")
                m = page.evaluate("""() => ({
                    overflow: document.documentElement.scrollWidth > innerWidth + 1,
                    badImages: [...document.images].filter(i => !i.complete || !i.naturalWidth).length,
                    badSVG: [...document.querySelectorAll('svg')].filter(s=>!s.getBoundingClientRect().width||!s.getBoundingClientRect().height).length,
                    badMath: [...document.querySelectorAll('math')].filter(m=>m.namespaceURI!=='http://www.w3.org/1998/Math/MathML'||m.closest('svg')||!m.getBoundingClientRect().width||!m.getBoundingClientRect().height).length,
                    badFractions: [...document.querySelectorAll('mfrac')].filter(m=>m.children.length!==2||m.children[0].getBoundingClientRect().top>=m.children[1].getBoundingClientRect().top).length
                })""")
                verify(not any(m.values()), f"{rel} {label}: {m}")
                changed = None
                if article:
                    buttons = page.locator("button[data-step]")
                    verify(buttons.count() >= 2, f"{rel}: missing interactive states")
                    if buttons.count() >= 2:
                        before = page.locator("#state").inner_text()
                        buttons.nth(1).focus()
                        page.keyboard.press("Enter")
                        changed = page.locator("#state").inner_text() != before
                        verify(changed and buttons.nth(1).get_attribute("aria-pressed") == "true", f"{rel}: keyboard state failed")
                    shot = reports / rel.parent.as_posix().replace("/", "-") / f"{label}.png"
                    shot.parent.mkdir(parents=True, exist_ok=True)
                    page.screenshot(path=str(shot), full_page=True)
                verify(not errors, f"{rel} {label}: {errors}")
                summary.append({"path": str(rel), "viewport": label, "measurements": m, "interaction": changed, "errors": errors})
                page.close()
        browser.close()
    report = {"pages": len(pages), "checks": summary, "failures": failures, "pass": not failures}
    (reports / "report.json").write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
    print(f"Pages: {len(pages)}, browser checks: {len(summary)}, failures: {len(failures)}")
    for item in failures:
        print(item)
    return int(bool(failures))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("site", type=Path)
    parser.add_argument("--reports", type=Path, required=True)
    args = parser.parse_args()
    raise SystemExit(check(args.site, args.reports))
