#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

AGENTS = [
    ("Tests Agent", [
        ["pytest", "-q"],
    ]),
    # Rust tests are run in CI; local agent skips if cargo is unavailable.
    ("Docs Agent", [[sys.executable, "scripts/docs_agent.py"]]),
    ("Changelog Agent", [[sys.executable, "scripts/changelog_agent.py"]]),
    ("Compatibility Agent", [[sys.executable, "scripts/compat.py"]]),
    ("Branch Hygiene Agent", [[sys.executable, "scripts/branch_hygiene_agent.py"]]),
]

def run(cmd):
    return subprocess.run(cmd).returncode

def main():
    root = Path(__file__).resolve().parents[1]
    failed = False
    for name, commands in AGENTS:
        print(f"==> {name}")
        for cmd in commands:
            print("$", " ".join(cmd))
            rc = run(cmd)
            if rc != 0:
                print(f"{name}: FAIL (exit {rc})")
                failed = True
                break
        else:
            print(f"{name}: OK")
        if failed:
            break
    sys.exit(1 if failed else 0)

if __name__ == "__main__":
    main()
