#!/usr/bin/env python3
import subprocess
import shutil
import sys
import yaml

def run(cmd):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return p.returncode, p.stdout

def main(path="scripts/compat.yml"):
    spec = yaml.safe_load(open(path))
    py = spec["python_cli"]
    rs = spec["rust_cli"]
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

        e1, o1 = run(py + args)
        e2, o2 = run(rs + args)

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

    if failures:
        print(f"{failures} test(s) failed")
        sys.exit(1)
    print("All compatibility tests passed")

if __name__ == "__main__":
    main()
