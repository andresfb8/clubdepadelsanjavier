"""Basic static QA: broken local links, missing assets and required meta tags.

    python tools/check.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = ("http://", "https://", "mailto:", "tel:", "#", "data:")

LINK_RE = re.compile(r'(?:href|src)="([^"]+)"')


def main() -> int:
    pages = sorted(ROOT.glob("*.html"))
    problems: list[str] = []

    for page in pages:
        text = page.read_text(encoding="utf-8")
        name = page.name

        if "<title>" not in text:
            problems.append(f"{name}: falta <title>")
        if 'name="description"' not in text:
            problems.append(f"{name}: falta meta description")
        if 'id="main"' not in text:
            problems.append(f"{name}: falta <main id=main>")

        for ref in LINK_RE.findall(text):
            if ref.startswith(SKIP):
                continue
            clean = ref.split("#")[0].split("?")[0]
            if not clean:
                continue
            target = (ROOT / clean).resolve()
            if not target.exists():
                problems.append(f"{name}: enlace roto -> {ref}")

        # internal anchors must exist on the target page
        for ref in re.findall(r'href="([a-z0-9-]+\.html#[^"]+)"', text):
            target_file, anchor = ref.split("#", 1)
            target = ROOT / target_file
            if target.exists() and f'id="{anchor}"' not in target.read_text(encoding="utf-8"):
                problems.append(f"{name}: ancla inexistente -> {ref}")

    # tokens that should never survive the build
    for page in pages:
        text = page.read_text(encoding="utf-8")
        if "%%" in text:
            leftover = sorted(set(re.findall(r"%%[A-Z_]+%%", text)))
            problems.append(f"{page.name}: tokens sin sustituir {leftover}")

    if problems:
        print("PROBLEMAS:")
        for p in problems:
            print(" -", p)
        return 1

    print(f"OK · {len(pages)} páginas, sin enlaces rotos ni metadatos ausentes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
