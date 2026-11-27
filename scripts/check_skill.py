#!/usr/bin/env python3
"""Check the skill's structure and relative links. Exit 0 means it passed."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFERENCES = ["interview", "portfolio", "product-site", "design-motion", "search", "ship"]
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^(`{3,}).*?^\1\s*$", re.S | re.M)


def problems():
    skill = ROOT / "SKILL.md"
    text = skill.read_text(encoding="utf-8")
    front = re.match(r"---\n(.*?)\n---\n", text, re.S)
    meta = front.group(1) if front else ""
    if not re.search(r"^name: portfolio-skill$", meta, re.M):
        yield "SKILL.md: frontmatter name must be portfolio-skill"
    if not re.search(r"^description: \S", meta, re.M):
        yield "SKILL.md: frontmatter description is missing"
    if len(text.splitlines()) >= 150:
        yield "SKILL.md: must be under 150 lines"
    for name in REFERENCES:
        path = f"references/{name}.md"
        if not (ROOT / path).is_file():
            yield f"missing {path}"
        if f"]({path})" not in text:
            yield f"SKILL.md does not link {path}"
    if not (ROOT / "KICKOFF.md").is_file():
        yield "missing KICKOFF.md"
    for doc in ROOT.rglob("*.md"):
        rel = doc.relative_to(ROOT)
        if rel.parts[0] in {"docs", ".superpowers", ".git"}:
            continue
        body = FENCE.sub("", doc.read_text(encoding="utf-8"))
        for target in LINK.findall(body):
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if not (doc.parent / target.split("#")[0]).exists():
                yield f"{rel}: broken link {target}"


found = list(problems())
print("\n".join(found) if found else "PASS")
sys.exit(1 if found else 0)
