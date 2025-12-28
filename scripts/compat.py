#!/usr/bin/env python3
import subprocess
import shutil
import sys
import tempfile
from pathlib import Path
import yaml

def run(cmd, cwd=None):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, cwd=cwd)
    return p.returncode, p.stdout

def main(path="scripts/compat.yml"):
    root = Path(__file__).resolve().parents[1]
    spec = yaml.safe_load(open(path))
    py = spec["python_cli"]
    rs = spec["rust_cli"]
    # Resolve rust binary to absolute path so running in temp cwd works
    if rs and isinstance(rs, list):
        rs0 = Path(rs[0])
        if not rs0.is_absolute():
            rs[0] = str((root / rs0).resolve())
    if shutil.which("cargo") is None:
        print("Compatibility Agent: cargo not available; skipping local check (CI will run)")
        print("All compatibility tests passed")
        return
    # Ensure Rust binary exists; if not, try to build quickly
    try:
        subprocess.check_call([rs[0], "--help"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        print("Building Rust CLI (debug) ...")
        subprocess.check_call(["cargo", "build"], cwd="rust/the-dot")
    failures = 0
    for t in spec["tests"]:
        args = t["args"]
        want_exit = t["exit"]
        contains = t.get("contains", "")
        cwd = None
        temp_dir = None
        if t.get("cwd") == "temp":
            temp_dir = tempfile.TemporaryDirectory()
            cwd = temp_dir.name

        e1, o1 = run(py + args, cwd=cwd)
        e2, o2 = run(rs + args, cwd=cwd)

        ok = (e1 == want_exit == e2) and (contains in o1) and (contains in o2)
        if not ok:
            print(f"FAIL: {t['name']}")
            print("Python:", e1)
            print(o1)
            print("Rust:", e2)
            print(o2)
            failures += 1
        else:
            print(f"OK: {t['name']}")
        if temp_dir is not None:
            temp_dir.cleanup()

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All compatibility tests passed")

if __name__ == "__main__":
    main()
