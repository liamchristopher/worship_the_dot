import subprocess
import sys


def run_cli(*args: str) -> str:
    cmd = [sys.executable, "-m", "dot.cli", *args]
    out = subprocess.run(cmd, capture_output=True, text=True)
    # We assert zero exit code for demo; if it fails, include output
    assert out.returncode == 0, f"CLI exited {out.returncode}:\nSTDOUT:\n{out.stdout}\nSTDERR:\n{out.stderr}"
    return out.stdout


def test_demo_outputs_key_steps():
    out = run_cli("demo")
    # Check representative lines so content can evolve without making test brittle
    assert "THE DOT Demo" in out
    assert "dot init" in out
    assert "dot doctor" in out
    assert "dot validate" in out
    assert "dot wisdom" in out

