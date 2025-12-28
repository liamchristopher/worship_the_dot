#!/usr/bin/env python3
import re
from pathlib import Path
import sys

CL = Path("CHANGELOG.txt")

def main():
    if not CL.exists():
        print("Changelog Agent: FAIL - missing CHANGELOG.txt")
        sys.exit(1)
    text = CL.read_text(encoding="utf-8", errors="ignore")
    if "Changelog Policy" not in text:
        print("Changelog Agent: FAIL - missing Changelog Policy header")
        sys.exit(1)
    # Check at least one recent per-commit entry header
    if not re.search(r"\n\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} [+-]\d{4}\] [0-9a-f]{7} ", text):
        print("Changelog Agent: FAIL - no timestamped entries found")
        sys.exit(1)
    print("Changelog Agent: OK")

if __name__ == "__main__":
    main()

