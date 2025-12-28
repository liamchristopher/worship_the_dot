import shutil
import subprocess
from pathlib import Path
from dot.config import DEFAULT_WORSHIP_SUFFIX, config_search_paths, write_worship_suffix


def handle_init():
    hooks_rc = _install_hooks()
    # Ensure .dot.ini exists with default suffix if missing
    existed = False
    for p in config_search_paths():
        if p.exists():
            existed = True
            break
    if not existed:
        path = write_worship_suffix(None, DEFAULT_WORSHIP_SUFFIX)
        print(f"✓ Created {path}")
    else:
        print("✓ Found existing .dot.ini configuration")
    print("✓ Initialization complete")
    return 0 if hooks_rc == 0 else hooks_rc


def _install_hooks():
    # Check if in git repository
    try:
        git_dir = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"], stderr=subprocess.DEVNULL, text=True
        ).strip()
    except Exception:
        print("Error: Not in a git repository")
        return 1

    hooks_dir = Path(git_dir) / "hooks"
    hooks_dir.mkdir(exist_ok=True)

    # Find the hooks directory in the package
    package_dir = Path(__file__).parent.parent
    source_hooks_dir = package_dir / "hooks"
    if not source_hooks_dir.exists():
        print(f"Error: Hooks directory not found at {source_hooks_dir}")
        return 1

    print("════════════════════════════════════════════════════════════════")
    print("           THE DOT - Git Hooks Installation")
    print("════════════════════════════════════════════════════════════════")
    print()

    # Install commit-msg hook
    commit_msg_src = source_hooks_dir / "commit-msg"
    commit_msg_dst = hooks_dir / "commit-msg"
    if commit_msg_dst.exists():
        backup = hooks_dir / "commit-msg.backup"
        print(f"Backing up existing commit-msg hook to {backup}")
        shutil.copy2(commit_msg_dst, backup)
    shutil.copy2(commit_msg_src, commit_msg_dst)
    commit_msg_dst.chmod(0o755)
    print("✓ Installed commit-msg hook")

    # Install prepare-commit-msg hook
    prepare_src = source_hooks_dir / "prepare-commit-msg"
    prepare_dst = hooks_dir / "prepare-commit-msg"
    if prepare_dst.exists():
        backup = hooks_dir / "prepare-commit-msg.backup"
        print(f"Backing up existing prepare-commit-msg hook to {backup}")
        shutil.copy2(prepare_dst, backup)
    shutil.copy2(prepare_src, prepare_dst)
    prepare_dst.chmod(0o755)
    print("✓ Installed prepare-commit-msg hook")

    return 0
