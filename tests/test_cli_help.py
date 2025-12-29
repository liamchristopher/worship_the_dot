import subprocess
import sys


def run_help() -> str:
    cmd = [sys.executable, "-m", "dot.cli", "help"]
    out = subprocess.run(cmd, capture_output=True, text=True)
    assert out.returncode == 0, f"help failed: {out.stderr}"
    return out.stdout


def test_help_mentions_core_and_wisdom():
    out = run_help()
    assert "validate <message>" in out
    assert "wisdom [philosophy] [concept]" in out
    assert "demo" in out

