#!/usr/bin/env python3
import re
from pathlib import Path
import glob
import sys

ROOT = Path(__file__).resolve().parents[1]

DOCS_DIR = ROOT / "docs"
FILES = [ROOT / "README.md", ROOT / "CONTRIBUTING.md", ROOT / "AGENTS.md", ROOT / "CLAUDE.md"]
FILES += [Path(p) for p in glob.glob(str(DOCS_DIR / "*.md"))]

TIMELY_WORDS = [
    r"\bwhiteboard\b",
    r"\bmonitors?\b",
    r"\boffice\b",
    r"\bcowboy commits\b",
]

def check_links(path: Path):
    content = path.read_text(encoding="utf-8", errors="ignore")
    # Find markdown links [text](link)
    links = re.findall(r"\[[^\]]+\]\(([^)]+)\)", content)
    errs = []
    for link in links:
        if link.startswith("http") or link.startswith("mailto:"):
            continue
        target = (path.parent / link).resolve()
        if not target.exists():
            errs.append(f"{path}: broken link -> {link}")
    return errs

def check_timeless(path: Path):
    content = path.read_text(encoding="utf-8", errors="ignore").lower()
    errs = []
    for w in TIMELY_WORDS:
        if re.search(w, content):
            errs.append(f"{path}: found modern reference: {w}")
    return errs

def main():
    errs = []
    for f in FILES:
        if f.exists():
            errs += check_links(f)
            errs += check_timeless(f)
    if errs:
        print("Docs Agent: FAIL")
        for e in errs:
            print("-", e)
        sys.exit(1)
    print("Docs Agent: OK")

if __name__ == "__main__":
    main()
