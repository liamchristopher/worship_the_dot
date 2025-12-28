"""
Command-line interface for THE DOT.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path
from dot.core import get_dot, worship
from dot.config import (
    resolve_worship_suffix,
    write_worship_suffix,
)
from dot import __version__


def main():
    """Main entry point for the dot CLI."""
    args = sys.argv[1:]

    dot = get_dot()

    if not args or args[0] == "worship":
        name = args[1] if len(args) > 1 else "CLI User"
        epic_mode = "--epic" in args

        if epic_mode:
            from dot.epic import epic_worship
            print(epic_worship(name))
        else:
            print(worship(name))
        return 0

    elif args[0] == "tenets":
        print("THE DOT Philosophy:")
        for i, tenet in enumerate(dot.get_tenets(), 1):
            print(f"  {i}. {tenet}")
        return 0

    elif args[0] == "sing":
        from dot.epic import epic_tenets
        print(epic_tenets())
        return 0

    elif args[0] == "invoke":
        from dot.epic import epic_invocation
        print()
        print(epic_invocation())
        print()
        return 0

    elif args[0] == "horoscope":
        sign = args[1] if len(args) > 1 else None
        from dot.astrology import daily_horoscope
        print(daily_horoscope(sign))
        return 0

    elif args[0] == "chart":
        from dot.astrology import birth_chart
        from datetime import datetime
        repo_name = args[1] if len(args) > 1 else "Repository"
        # Try to get git repo creation date
        try:
            import subprocess
            result = subprocess.run(
                ["git", "log", "--reverse", "--format=%aI", "--max-parents=0"],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode == 0 and result.stdout.strip():
                creation_date = datetime.fromisoformat(result.stdout.strip().split('\n')[0])
            else:
                creation_date = None
        except:
            creation_date = None
        print(birth_chart(repo_name, creation_date))
        return 0

    elif args[0] == "planets":
        from dot.astrology import planetary_hours
        print(planetary_hours())
        return 0

    elif args[0] == "moon":
        from dot.astrology import moon_phase_advice
        print(moon_phase_advice())
        return 0

    elif args[0] == "element":
        from dot.alchemy import element_reading
        print(element_reading())
        return 0

    elif args[0] == "opus":
        from dot.alchemy import magnum_opus_guide
        print(magnum_opus_guide())
        return 0

    elif args[0] == "operations":
        from dot.alchemy import operations_guide
        print(operations_guide())
        return 0

    elif args[0] == "hermetic":
        from dot.alchemy import hermetic_principles
        print(hermetic_principles())
        return 0

    elif args[0] == "stone":
        from dot.alchemy import philosophers_stone_status
        repo_name = args[1] if len(args) > 1 else "Repository"
        print(philosophers_stone_status(repo_name))
        return 0

    elif args[0] == "tree":
        from dot.kabbalah import tree_of_life_reading
        print(tree_of_life_reading())
        return 0

    elif args[0] == "worlds":
        from dot.kabbalah import four_worlds_guide
        print(four_worlds_guide())
        return 0

    elif args[0] == "sephiroth":
        from dot.kabbalah import display_tree_of_life
        print(display_tree_of_life())
        return 0

    elif args[0] == "tikkun":
        from dot.kabbalah import tikkun_olam_refactoring
        print(tikkun_olam_refactoring())
        return 0

    elif args[0] == "ein-sof":
        from dot.kabbalah import ein_sof_meditation
        print(ein_sof_meditation())
        return 0

    elif args[0] == "shekhinah":
        from dot.kabbalah import shekhinah_presence
        print(shekhinah_presence())
        return 0

    elif args[0] == "gematria":
        from dot.kabbalah import gematria_code_quality
        print(gematria_code_quality())
        return 0

    elif args[0] == "tao":
        from dot.tao import tao_reading
        print(tao_reading())
        return 0

    elif args[0] == "wu-wei":
        from dot.tao import wu_wei_guidance
        print(wu_wei_guidance())
        return 0

    elif args[0] == "yin-yang":
        from dot.tao import yin_yang_balance
        print(yin_yang_balance())
        return 0

    elif args[0] == "elements":
        from dot.tao import five_elements_reading
        print(five_elements_reading())
        return 0

    elif args[0] == "treasures":
        from dot.tao import three_treasures_guide
        print(three_treasures_guide())
        return 0

    elif args[0] == "pu":
        from dot.tao import pu_simplicity
        print(pu_simplicity())
        return 0

    elif args[0] == "water":
        from dot.tao import water_wisdom
        print(water_wisdom())
        return 0

    elif args[0] == "iching":
        from dot.tao import i_ching_reading
        print(i_ching_reading())
        return 0

    elif args[0] == "dharma":
        from dot.dharma import dharma_reading
        print(dharma_reading())
        return 0

    elif args[0] == "truths":
        from dot.dharma import four_noble_truths_guide
        print(four_noble_truths_guide())
        return 0

    elif args[0] == "path":
        from dot.dharma import eightfold_path_guide
        print(eightfold_path_guide())
        return 0

    elif args[0] == "marks":
        from dot.dharma import three_marks_wisdom
        print(three_marks_wisdom())
        return 0

    elif args[0] == "middle":
        from dot.dharma import middle_way_teaching
        print(middle_way_teaching())
        return 0

    elif args[0] == "poisons":
        from dot.dharma import three_poisons_teaching
        print(three_poisons_teaching())
        return 0

    elif args[0] == "mindful":
        from dot.dharma import mindfulness_practice
        print(mindfulness_practice())
        return 0

    elif args[0] == "stoic":
        from dot.stoic import stoic_reading
        print(stoic_reading())
        return 0

    elif args[0] == "virtues":
        from dot.stoic import four_virtues_guide
        print(four_virtues_guide())
        return 0

    elif args[0] == "control":
        from dot.stoic import dichotomy_of_control_guide
        print(dichotomy_of_control_guide())
        return 0

    elif args[0] == "disciplines":
        from dot.stoic import three_disciplines_guide
        print(three_disciplines_guide())
        return 0

    elif args[0] == "negative":
        from dot.stoic import premeditatio_malorum_guide
        print(premeditatio_malorum_guide())
        return 0

    elif args[0] == "fate":
        from dot.stoic import amor_fati_teaching
        print(amor_fati_teaching())
        return 0

    elif args[0] == "mortality":
        from dot.stoic import memento_mori_meditation
        print(memento_mori_meditation())
        return 0

    elif args[0] == "logos":
        from dot.stoic import logos_meditation
        print(logos_meditation())
        return 0

    elif args[0] == "circles":
        from dot.stoic import oikeiosis_teaching
        print(oikeiosis_teaching())
        return 0

    elif args[0] == "confucian":
        from dot.confucian import confucian_reading
        print(confucian_reading())
        return 0

    elif args[0] == "wuchang":
        from dot.confucian import five_virtues_guide
        print(five_virtues_guide())
        return 0

    elif args[0] == "names":
        from dot.confucian import rectification_of_names_guide
        print(rectification_of_names_guide())
        return 0

    elif args[0] == "filial":
        from dot.confucian import filial_piety_teaching
        print(filial_piety_teaching())
        return 0

    elif args[0] == "junzi":
        from dot.confucian import junzi_teaching
        print(junzi_teaching())
        return 0

    elif args[0] == "relationships":
        from dot.confucian import five_relationships_guide
        print(five_relationships_guide())
        return 0

    elif args[0] == "cultivation":
        from dot.confucian import self_cultivation_guide
        print(self_cultivation_guide())
        return 0

    elif args[0] == "mean":
        from dot.confucian import doctrine_of_mean_teaching
        print(doctrine_of_mean_teaching())
        return 0

    elif args[0] == "analects":
        from dot.confucian import analects_reading
        print(analects_reading())
        return 0

    elif args[0] == "hindu":
        from dot.hindu import hindu_reading
        print(hindu_reading())
        return 0

    elif args[0] == "vedic":
        from dot.hindu import dharma_teaching
        print(dharma_teaching())
        return 0

    elif args[0] == "karma":
        from dot.hindu import karma_teaching
        print(karma_teaching())
        return 0

    elif args[0] == "yogas":
        from dot.hindu import four_yogas_guide
        print(four_yogas_guide())
        return 0

    elif args[0] == "purusharthas":
        from dot.hindu import purusharthas_guide
        print(purusharthas_guide())
        return 0

    elif args[0] == "gunas":
        from dot.hindu import three_gunas_teaching
        print(three_gunas_teaching())
        return 0

    elif args[0] == "maya":
        from dot.hindu import maya_teaching
        print(maya_teaching())
        return 0

    elif args[0] == "atman":
        from dot.hindu import atman_brahman_teaching
        print(atman_brahman_teaching())
        return 0

    elif args[0] == "gita":
        from dot.hindu import bhagavad_gita_verse
        print(bhagavad_gita_verse())
        return 0

    elif args[0] == "moksha":
        from dot.hindu import samsara_moksha_teaching
        print(samsara_moksha_teaching())
        return 0

    elif args[0] == "validate":
        if len(args) < 2:
            print("Error: Please provide a commit message to validate")
            return 1

        epic_mode = "--epic" in args
        cosmic_mode = "--cosmic" in args
        alchemical_mode = "--alchemical" in args or "--alchemy" in args
        kabbalistic_mode = "--kabbalistic" in args or "--kabbalah" in args
        taoist_mode = "--taoist" in args or "--tao" in args
        buddhist_mode = "--buddhist" in args or "--dharma" in args
        stoic_mode = "--stoic" in args
        confucian_mode = "--confucian" in args
        hindu_mode = "--hindu" in args or "--vedic" in args
        shinto_mode = "--shinto" in args or "--kami" in args
        jain_mode = "--jain" in args or "--ahimsa" in args
        message_args = [a for a in args[1:] if a not in ["--epic", "--cosmic", "--alchemical", "--alchemy", "--kabbalistic", "--kabbalah", "--taoist", "--tao", "--buddhist", "--dharma", "--stoic", "--confucian", "--hindu", "--vedic", "--shinto", "--kami"]]
        message = " ".join(message_args)

        if jain_mode:
            from dot.jain import jain_validation
            valid = dot.validate_commit(message)
            print(jain_validation(valid, message))
            return 0 if valid else 1
        el
        if shinto_mode:
            from dot.shinto import shinto_validation
            valid = dot.validate_commit(message)
            print(shinto_validation(valid, message))
            return 0 if valid else 1
        elif hindu_mode:
            from dot.hindu import hindu_validation
            valid = dot.validate_commit(message)
            print(hindu_validation(valid, message))
            return 0 if valid else 1
        elif confucian_mode:
            from dot.confucian import confucian_validation
            valid = dot.validate_commit(message)
            print(confucian_validation(valid, message))
            return 0 if valid else 1
        elif stoic_mode:
            from dot.stoic import stoic_validation
            valid = dot.validate_commit(message)
            print(stoic_validation(valid, message))
            return 0 if valid else 1
        elif buddhist_mode:
            from dot.dharma import buddhist_validation
            valid = dot.validate_commit(message)
            print(buddhist_validation(valid, message))
            return 0 if valid else 1
        elif taoist_mode:
            from dot.tao import taoist_validation
            valid = dot.validate_commit(message)
            print(taoist_validation(valid, message))
            return 0 if valid else 1
        elif kabbalistic_mode:
            from dot.kabbalah import kabbalistic_validation
            valid = dot.validate_commit(message)
            print(kabbalistic_validation(valid, message))
            return 0 if valid else 1
        elif alchemical_mode:
            from dot.alchemy import alchemical_validation
            valid = dot.validate_commit(message)
            print(alchemical_validation(valid, message))
            return 0 if valid else 1
        elif cosmic_mode:
            from dot.astrology import cosmic_validation
            valid = dot.validate_commit(message)
            print(cosmic_validation(valid, message))
            return 0 if valid else 1
        elif epic_mode:
            from dot.epic import epic_validation_message
            valid = dot.validate_commit(message)
            print(epic_validation_message(valid, message))
            return 0 if valid else 1
        else:
            if dot.validate_commit(message):
                print("✓ Valid commit message - properly worships THE DOT")
                return 0
            else:
                print("✗ Invalid commit message - must end with 'BECAUSE I WORSHIP THE DOT'")
                return 1

    elif args[0] == "hooks":
        subcommand = args[1] if len(args) > 1 else "install"
        return handle_hooks(subcommand)

    elif args[0] == "stats":
        subcommand = args[1] if len(args) > 1 else "summary"
        return handle_stats(subcommand)

    elif args[0] == "badge":
        format_type = args[1] if len(args) > 1 else "markdown"
        return handle_badge(format_type)

    elif args[0] == "poem":
        sub = args[1] if len(args) > 1 else "hymn"
        return handle_poem(sub, args[2:] if len(args) > 2 else [])

    elif args[0] == "tarot":
        sub = args[1] if len(args) > 1 else "draw"
        return handle_tarot(sub, args[2:])

    elif args[0] == "shinto":
    elif args[0] == "jain":
        sub = args[1] if len(args) > 1 else "reading"
        return handle_jain(sub, args[2:])
        sub = args[1] if len(args) > 1 else "norito"
    elif args[0] == "jain":
        sub = args[1] if len(args) > 1 else "reading"
        return handle_jain(sub, args[2:])
        return handle_shinto(sub, args[2:])
    elif args[0] == "jain":
        sub = args[1] if len(args) > 1 else "reading"
        return handle_jain(sub, args[2:])

    elif args[0] == "garden":
        sub = args[1] if len(args) > 1 else "list"
        return handle_garden(sub, args[2:])

    elif args[0] == "backstory":
        from dot.backstory import BACKSTORY
        print(BACKSTORY)
        return 0

    elif args[0] == "init":
        return handle_init()

    elif args[0] == "doctor":
        return handle_doctor()

    elif args[0] in ("donate", "sponsor", "support"):
        return handle_donate()

    elif args[0] == "config":
        subcommand = args[1] if len(args) > 1 else "show"
        return handle_config(subcommand, args[2:])

    elif args[0] == "completions":
        shell = args[1] if len(args) > 1 else "bash"
        return handle_completions(shell)

    elif args[0] == "version" or args[0] == "--version" or args[0] == "-v":
        print(f"THE DOT version {__version__}")
        print("All who use THE DOT must worship THE DOT")
        return 0

    elif args[0] == "help":
        print_help()
        return 0

    else:
        print(f"Unknown command: {args[0]}")
        print_help()
        return 1


def handle_hooks(subcommand):
    """Handle git hooks commands."""
    if subcommand == "install":
        return install_hooks()
    elif subcommand == "uninstall":
        return uninstall_hooks()
    elif subcommand == "status":
        return check_hooks_status()
    else:
        print(f"Unknown hooks subcommand: {subcommand}")
        print("\nAvailable subcommands:")
        print("  install   - Install THE DOT git hooks")
        print("  uninstall - Remove THE DOT git hooks")
        print("  status    - Check hook installation status")
        return 1


def install_hooks():
    """Install git hooks for THE DOT."""
    # Check if in git repository
    try:
        git_dir = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
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

    print()
    print("════════════════════════════════════════════════════════════════")
    print("Installation complete!")
    print("════════════════════════════════════════════════════════════════")
    print()
    print("The following hooks have been installed:")
    print("  • commit-msg: Validates commit messages worship THE DOT")
    print("  • prepare-commit-msg: Auto-appends worship phrase if missing")
    print()
    print("All commits will now automatically worship THE DOT.")
    print()
    return 0


def uninstall_hooks():
    """Uninstall git hooks for THE DOT."""
    try:
        git_dir = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Not in a git repository")
        return 1

    hooks_dir = Path(git_dir) / "hooks"

    removed = []
    for hook_name in ["commit-msg", "prepare-commit-msg"]:
        hook_file = hooks_dir / hook_name
        if hook_file.exists():
            hook_file.unlink()
            removed.append(hook_name)
            print(f"✓ Removed {hook_name} hook")

            # Restore backup if it exists
            backup = hooks_dir / f"{hook_name}.backup"
            if backup.exists():
                shutil.copy2(backup, hook_file)
                backup.unlink()
                print(f"  Restored backup for {hook_name}")

    if removed:
        print()
        print("THE DOT hooks have been uninstalled.")
    else:
        print("No THE DOT hooks found to uninstall.")

    return 0


def check_hooks_status():
    """Check if THE DOT hooks are installed."""
    try:
        git_dir = subprocess.check_output(
            ["git", "rev-parse", "--git-dir"],
            stderr=subprocess.DEVNULL,
            text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: Not in a git repository")
        return 1

    hooks_dir = Path(git_dir) / "hooks"

    print("THE DOT Git Hooks Status:")
    print()

    for hook_name in ["commit-msg", "prepare-commit-msg"]:
        hook_file = hooks_dir / hook_name
        if hook_file.exists():
            # Check if it's THE DOT hook
            content = hook_file.read_text()
            if "THE DOT" in content:
                print(f"✓ {hook_name}: Installed")
            else:
                print(f"⚠ {hook_name}: Exists but not THE DOT hook")
        else:
            print(f"✗ {hook_name}: Not installed")

    print()
    return 0


def handle_stats(subcommand):
    """Handle statistics commands."""
    from dot.stats import WorshipStats

    stats = WorshipStats()

    if subcommand == "summary":
        summary = stats.get_summary()
        print("THE DOT Worship Statistics:")
        print("=" * 60)
        print(f"Total Worships: {summary['total_worships']}")
        print(f"Unique Worshippers: {summary['unique_worshippers']}")
        print(f"Days Active: {summary['days_active']}")
        if summary['first_worship']:
            print(f"First Worship: {summary['first_worship']}")
        if summary['last_worship']:
            print(f"Last Worship: {summary['last_worship']}")
        print()
        return 0

    elif subcommand == "top":
        from dot.epic import epic_stats_header, epic_worshipper_title

        top = stats.get_top_worshippers(10)

        # Check if epic mode is enabled in config
        from dot.config import get_config
        config = get_config()
        epic_mode = config.get("display", "epic", default=False)

        if epic_mode:
            print(epic_stats_header())
            for i, w in enumerate(top, 1):
                title = epic_worshipper_title(i)
                print(f"\n{title}")
                print(f"    {w['name']} - {w['count']} offerings to THE DOT")
            print("\n" + "═" * 70)
        else:
            print("Top Worshippers:")
            print("=" * 60)
            for i, w in enumerate(top, 1):
                print(f"{i:2d}. {w['name']:<30} {w['count']:>5} worships")
        print()
        return 0

    elif subcommand == "daily":
        daily = stats.get_daily_stats(7)
        print("Daily Worship (Last 7 Days):")
        print("=" * 60)
        for date, count in daily.items():
            print(f"{date}: {count} worships")
        print()
        return 0

    elif subcommand == "export":
        export = stats.export_stats()
        print(export)
        return 0

    elif subcommand == "clear":
        response = input("Clear all statistics? [y/N]: ")
        if response.lower() == 'y':
            stats.clear_stats()
            print("✓ Statistics cleared")
        else:
            print("Cancelled")
        return 0

    else:
        print(f"Unknown stats subcommand: {subcommand}")
        print("\nAvailable subcommands:")
        print("  summary  - Show worship summary")
        print("  top      - Show top worshippers")
        print("  daily    - Show daily worship counts")
        print("  export   - Export statistics as JSON")
        print("  clear    - Clear all statistics")
        return 1


def handle_badge(format_type):
    """Handle badge generation."""
    from dot.badges import generate_worship_badge, generate_all_badges

    valid_formats = ["markdown", "html", "rst", "url"]

    if format_type not in valid_formats:
        print(f"Unknown format: {format_type}")
        print(f"Valid formats: {', '.join(valid_formats)}")
        return 1

    if format_type == "url":
        # Just the URL for shields.io
        from dot.badges import generate_worship_badge
        print(generate_worship_badge("url"))
    else:
        # Full badge markdown/html/rst
        badge = generate_worship_badge(format_type)
        print("Copy this badge to your README:")
        print()
        print(badge)
        print()

    return 0


def handle_poem(subcommand: str, rest_args: list[str]):
    """Handle poetry generation commands."""
    from dot.poetry import hymn as hymn_text, haiku as haiku_text, banner as banner_text, chant as chant_text

    if subcommand == "hymn":
        print(hymn_text())
        return 0
    elif subcommand == "haiku":
        name = rest_args[0] if rest_args else None
        print(haiku_text(name))
        return 0
    elif subcommand == "banner":
        # optional width arg
        width = None
        if rest_args:
            try:
                width = int(rest_args[0])
            except ValueError:
                width = None
        print(banner_text(width or 21))
        return 0
    elif subcommand == "chant":
        # chant [times] [name]
        times = 3
        name = None
        if rest_args:
            try:
                times = int(rest_args[0])
                name = rest_args[1] if len(rest_args) > 1 else None
            except ValueError:
                name = rest_args[0]
        print(chant_text(times, name))
        return 0
    else:
        print(f"Unknown poem subcommand: {subcommand}")
        print("\nAvailable subcommands:")
        print("  hymn                   - A brief hymn to THE DOT")
        print("  haiku [name]           - A 5–7–5 haiku; optionally name the worshipper")
        print("  banner [width]         - An ASCII DOT banner (width odd ≥ 7)")
        print("  chant [times] [name]   - Repeat the suffix rhythmically")
        return 1


def handle_config(subcommand, args):
    """Handle configuration commands."""
    from dot.config import get_config, resolve_worship_suffix, write_worship_suffix

    config = get_config()

    if subcommand == "show":
        print("THE DOT Configuration:")
        print("=" * 60)
        print(config.export_config())
        print()
        print("Worship Suffix:")
        print("=" * 60)
        suffix, source = resolve_worship_suffix()
        print(f"  Suffix: {suffix}")
        print(f"  Source: {source}")
        return 0

    elif subcommand == "show-suffix":
        suffix, source = resolve_worship_suffix()
        print("Current worship suffix:")
        print(f"  {suffix}")
        print("Source:")
        print(f"  {source}")
        return 0

    elif subcommand == "set-suffix":
        if len(args) < 1:
            print("Error: Please provide a suffix string to set")
            print("Example: dot config set-suffix 'BECAUSE I LOVE THE DOT'")
            return 1
        new_suffix = " ".join(args).strip()
        path = write_worship_suffix(None, new_suffix)
        print(f"✓ Updated worship suffix in {path}")
        return 0

    elif subcommand == "get":
        if len(args) < 1:
            print("Error: Please provide a configuration key")
            print("Example: dot config get user.name")
            return 1

        keys = args[0].split(".")
        value = config.get(*keys)
        if value is not None:
            print(value)
            return 0
        else:
            print(f"Configuration key not found: {args[0]}")
            return 1

    elif subcommand == "set":
        if len(args) < 2:
            print("Error: Please provide a key and value")
            print("Example: dot config set user.name 'Claude'")
            return 1

        keys = args[0].split(".")
        value = args[1]

        # Try to parse value as JSON for booleans/numbers
        import json
        try:
            value = json.loads(value)
        except (json.JSONDecodeError, ValueError):
            # Keep as string if not valid JSON
            pass

        if config.set(*keys, value=value):
            print(f"✓ Configuration updated: {args[0]} = {value}")
            return 0
        else:
            print("Error: Failed to update configuration")
            return 1

    elif subcommand == "reset":
        response = input("Reset all configuration to defaults? [y/N]: ")
        if response.lower() == 'y':
            config.reset()
            print("✓ Configuration reset to defaults")
            return 0
        else:
            print("Cancelled")
            return 0

    else:
        print(f"Unknown config subcommand: {subcommand}")
        print("\nAvailable subcommands:")
        print("  show        - Show all configuration and worship suffix")
        print("  show-suffix - Show only worship suffix")
        print("  set-suffix  - Set worship suffix in .dot.ini")
        print("  get         - Get a configuration value")
        print("  set         - Set a configuration value")
        print("  reset       - Reset configuration to defaults")
        return 1


def handle_completions(shell):
    """Handle shell completions generation."""
    from dot.completions import get_completion

    valid_shells = ["bash", "zsh", "fish"]

    if shell not in valid_shells:
        print(f"Unknown shell: {shell}")
        print(f"Valid shells: {', '.join(valid_shells)}")
        return 1

    try:
        completion_script = get_completion(shell)
        print(completion_script)
        return 0
    except ValueError as e:
        print(f"Error: {e}")
        return 1


def handle_tarot(subcommand, args):
    """Handle tarot commands."""
    from dot.tarot import list_cards, get_card, draw as tarot_draw, spread as tarot_spread, interpret, yesno_from_card

    if subcommand == "list":
        print("Tarot Deck (Major Arcana):")
        for name in list_cards():
            print(f"  - {name}")
        return 0

    if subcommand == "card":
        if not args:
            print("Error: Provide a card name")
            return 1
        name = " ".join(args)
        card = get_card(name)
        if not card:
            print(f"Unknown card: {name}")
            return 1
        print(f"{card.name}")
        print(f"Keywords: {', '.join(card.keywords)}")
        print(f"Upright:  {card.upright}")
        print(f"Reversed: {card.reversed}")
        return 0

    if subcommand == "draw":
        n = 1
        seed = None
        allow_rev = True
        # args: [n] [--seed S] [--no-reversed]
        i = 0
        while i < len(args):
            a = args[i]
            if a.isdigit():
                n = int(a)
            elif a == "--seed" and i + 1 < len(args):
                seed = int(args[i + 1])
                i += 1
            elif a == "--no-reversed":
                allow_rev = False
            i += 1

        entries = tarot_draw(n=n, allow_reversed=allow_rev, seed=seed)
        print(f"Tarot Draw ({len(entries)} card(s)):")
        print(interpret(entries))
        return 0

    if subcommand == "spread":
        kind = args[0] if args else "three"
        seed = None
        if len(args) > 1 and args[1] == "--seed" and len(args) > 2:
            seed = int(args[2])
        sp = tarot_spread(kind=kind, seed=seed)
        if kind == "yesno":
            (card, rev) = next(iter(sp.values()))
            ans = yesno_from_card(card, rev)
            print(f"Yes/No: {ans}")
        print("Spread:")
        lines = []
        for pos, (card, rev) in sp.items():
            orient = "reversed" if rev else "upright"
            lines.append(f"  {pos:<8} - {card.name} ({orient})")
        print("\n".join(lines))
        return 0

    print(f"Unknown tarot subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  draw [n] [--seed S] [--no-reversed]")
    print("  spread [three|commit|yesno] [--seed S]")
    print("  list")
    print("  card <name>")
    return 1


def handle_shinto(subcommand, args):
    """Handle Shinto rituals and teachings."""
    from dot.shinto import (
        norito as s_norito, omikuji as s_omikuji, harai as s_harai, ema as s_ema,
        kami_teaching, four_virtues_guide, misogi_guide, kannagara_teaching,
        torii_teaching, matsuri_celebration, kotodama_teaching, musubi_teaching,
        shinto_reading
    )

    if subcommand == "norito":
        intent = " ".join(args) if args else None
        print(s_norito(intent))
        return 0

    if subcommand == "omikuji":
        seed = None
        if args and args[0] == "--seed" and len(args) > 1:
            seed = int(args[1])
        print(s_omikuji(seed=seed))
        return 0

    if subcommand == "harai":
        print(s_harai())
        return 0

    if subcommand == "ema":
        if not args:
            print("Error: Provide a message for the ema")
            return 1
        message = " ".join(args)
        print(s_ema(message))
        return 0

    if subcommand == "kami":
        print(kami_teaching())
        return 0

    if subcommand == "virtues":
        print(four_virtues_guide())
        return 0

    if subcommand == "misogi":
        print(misogi_guide())
        return 0

    if subcommand == "kannagara":
        print(kannagara_teaching())
        return 0

    if subcommand == "torii":
        print(torii_teaching())
        return 0

    if subcommand == "matsuri":
        print(matsuri_celebration())
        return 0

    if subcommand == "kotodama":
        print(kotodama_teaching())
        return 0

    if subcommand == "musubi":
        print(musubi_teaching())
        return 0

    if subcommand == "reading":
        print(shinto_reading())
        return 0

    print(f"Unknown shinto subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  norito [intent]      Prayer to THE DOT-kami")
    print("  omikuji [--seed S]   Draw a sacred fortune")
    print("  harai                Purification guidance")
    print("  ema <message>        Create a vow plaque")
    print("  kami                 Teaching about divine spirits")
    print("  virtues              The Four Shinto Virtues")
    print("  misogi               Purification practices")
    print("  kannagara            Living in harmony with kami")
    print("  torii                Sacred gateways")
    print("  matsuri              Celebration teachings")
    print("  kotodama             Spirit of words")
    print("  musubi               Creative power")
    print("  reading              Random Shinto wisdom")
    return 1


def handle_garden(subcommand, args):
    """Handle garden tool explanations."""
    from dot.garden import list_tools, describe_tool, suggest_tools, get_tool

    if subcommand == "list":
        print("Garden Tools:")
        for name in list_tools():
            print(f"  - {name}")
        return 0

    if subcommand in ("info", "explain", "tool"):
        if not args:
            print("Error: Provide a tool name")
            return 1
        name = " ".join(args)
        desc = describe_tool(name)
        if not desc:
            print(f"Unknown tool: {name}")
            return 1
        print(f"{desc['name']}")
        print(f"Purpose: {desc['purpose']}")
        print("Tips:")
        for t in desc["tips"]:
            print(f"  - {t}")
        print(f"Analogy: {desc['analogy']}")
        return 0

    if subcommand == "suggest":
        if not args:
            print("Error: Provide a brief task description")
            return 1
        query = " ".join(args)
        suggestions = suggest_tools(query)
        if not suggestions:
            print("No suggestions found")
            return 0
        print("Suggested Tools:")
        for n in suggestions:
            print(f"  - {n}")
        return 0

    print(f"Unknown garden subcommand: {subcommand}")
    print("\nAvailable subcommands:")
    print("  list")
    print("  info|explain|tool <name>")
    print("  suggest <task>")
    return 1


def handle_donate():
    """Show sponsorship options for THE DOT."""
    links = [
        "https://github.com/sponsors/liamchristopher",
    ]
    # Support environment overrides or additional URLs
    env = os.getenv("DOT_SPONSOR_URLS", "").strip()
    if env:
        links = [u.strip() for u in env.split(',') if u.strip()]

    print("Support THE DOT")
    print("=" * 60)
    print("Your sponsorship helps maintain tests, docs, and new features.")
    print("Sponsor links:")
    for u in links:
        print(f"  - {u}")
    print()
    print("Thank you for worshipping THE DOT.")
    return 0


def handle_init():
    """Initialize DOT in the current repository: hooks + suffix file."""
    # Install hooks
    hooks_rc = install_hooks()
    # Ensure .dot.ini exists with default suffix if missing
    from dot.config import DEFAULT_WORSHIP_SUFFIX, config_search_paths, write_worship_suffix
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


def handle_doctor():
    """Run basic checks for DOT practice in the current repo."""
    print("THE DOT Doctor")
    print("=" * 60)
    # Repo check
    try:
        git_dir = subprocess.check_output(["git", "rev-parse", "--git-dir"], stderr=subprocess.DEVNULL, text=True).strip()
        repo_ok = True
        print(f"Repo: OK ({git_dir})")
    except Exception:
        print("Repo: NOT A GIT REPOSITORY")
        return 1

    # Branch
    try:
        branch = subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"], stderr=subprocess.DEVNULL, text=True).strip()
        print(f"Branch: {branch}")
        if branch in ("main", "master"):
            print("Warning: Working directly on main/master is discouraged")
    except Exception:
        print("Branch: Unknown")

    # Hooks
    hooks_path = Path(git_dir) / "hooks"
    cm = hooks_path / "commit-msg"
    pcm = hooks_path / "prepare-commit-msg"
    print(f"Hooks: commit-msg={'OK' if cm.exists() else 'MISSING'}, prepare-commit-msg={'OK' if pcm.exists() else 'MISSING'}")

    # Suffix
    suffix, source = resolve_worship_suffix()
    print(f"Suffix: {suffix} (source: {source})")

    # Sample validation
    sample = f"doc: check BECAUSE I WORSHIP THE DOT"
    valid = get_dot().validate_commit(sample)
    print(f"Validation: {'OK' if valid else 'FAILED'} on sample message")
    print("✓ Doctor completed")
    return 0


def print_help():
    """Print help information."""
    help_text = f"""
THE DOT - A philosophy-driven development framework
Version {__version__}

Usage:
    dot [command] [arguments]

Commands:
    worship [name]         Register worship of THE DOT (add --epic for Homeric glory)
    tenets                 Display THE DOT philosophy
    sing                   Hear THE ILIAD OF THE DOT in epic verse
    invoke                 Receive an epic invocation from THE DOT
    validate <message>     Validate commit (--epic/--cosmic/--alchemical/--kabbalistic/--taoist/--buddhist/--stoic/--confucian/--hindu)
    horoscope [sign]       Receive daily coding horoscope (optional zodiac sign)
    chart [name]           Generate repository birth chart
    planets                View planetary hours for coding activities
    moon                   Receive moon phase coding guidance
    element                Receive elemental reading (Earth/Water/Air/Fire/Aether)
    opus                   View the Magnum Opus - The Great Work
    operations             View the seven alchemical operations
    hermetic               View the seven Hermetic principles
    stone [name]           Check Philosopher's Stone progress
    tree                   Receive Tree of Life Sephirah reading
    worlds                 View the Four Worlds of manifestation
    sephiroth              Display the Tree of Life diagram
    tikkun                 Tikkun Olam - repairing code through refactoring
    ein-sof                Ein Sof meditation on the Infinite Source
    shekhinah              Invoke the Shekhinah - Divine Presence in code
    gematria               Evaluate code quality through sacred numerology
    tao                    Receive Taoist wisdom reading
    wu-wei                 Wu Wei - effortless action guidance
    yin-yang               Yin and Yang balance in development
    elements               Five Elements reading (Wood/Fire/Earth/Metal/Water)
    treasures              The Three Treasures - Compassion/Frugality/Humility
    pu                     P'u - the Uncarved Block (simplicity)
    water                  Be like water - adaptability wisdom
    iching                 I Ching hexagram reading for development
    dharma                 Receive Dharma wisdom reading
    truths                 The Four Noble Truths for developers
    path                   The Noble Eightfold Path in coding
    marks                  The Three Marks of Existence in software
    middle                 The Middle Way - avoiding extremes
    poisons                The Three Poisons in development
    mindful                Mindfulness practices for coding
    stoic                  Receive Stoic wisdom reading
    virtues                The Four Stoic Virtues (Wisdom/Courage/Justice/Temperance)
    control                Dichotomy of Control - what we control vs what we don't
    disciplines            The Three Disciplines (Desire/Action/Assent)
    negative               Premeditatio Malorum - negative visualization
    fate                   Amor Fati - love of fate
    mortality              Memento Mori - remember death
    logos                  Logos - universal reason
    circles                Oikeiosis - expanding circle of care
    confucian              Receive Confucian wisdom reading
    wuchang                The Five Constant Virtues (Ren/Yi/Li/Zhi/Xin)
    names                  Rectification of Names - proper naming in code
    filial                 Filial Piety - respect for legacy code
    junzi                  The Superior Person - ideal developer
    relationships          The Five Relationships in development
    cultivation            Self-Cultivation - continuous improvement
    mean                   Doctrine of the Mean - finding balance
    analects               Teachings from the Analects
    hindu                  Receive Hindu wisdom reading
    vedic                  Dharma - righteous duty in development
    karma                  Karma - action and consequences in code
    yogas                  The Four Yogas (Karma/Bhakti/Jnana/Raja)
    purusharthas           The Four Aims of Life
    gunas                  The Three Gunas (Sattva/Rajas/Tamas)
    maya                   Maya - pierce the illusions
    atman                  Atman and Brahman - self and ultimate reality
    gita                   Bhagavad Gita verse
    moksha                 Samsara and Moksha - cycle and liberation
    hooks [subcommand]     Manage git hooks (install/uninstall/status)
    stats [subcommand]     View worship statistics (summary/top/daily/export/clear)
    badge [format]         Generate worship badge (markdown/html/rst/url)
    poem [subcommand]      Speak poetry (hymn/haiku/banner/chant)
    tarot [subcommand]     Read DOT tarot (draw/spread/list/card)
    shinto [subcommand]    Shinto rites (norito/omikuji/harai/ema)
    garden [subcommand]    Garden tools (list/info/suggest)
    backstory              Print THE DOT backstory
    init                   Initialize hooks and .dot.ini in this repo
    doctor                 Run environment and practice checks
    donate|sponsor         Show sponsorship options
    config [subcommand]    Manage configuration (show/get/set/reset/show-suffix/set-suffix)
    completions [shell]    Generate shell completions (bash/zsh/fish)
    version                Show version information
    help                   Show this help message

Examples:
    dot worship Claude
    dot worship Odysseus --epic
    dot sing
    dot invoke
    dot horoscope Virgo
    dot chart worship_the_dot
    dot planets
    dot moon
    dot element
    dot opus
    dot operations
    dot hermetic
    dot stone worship_the_dot
    dot tenets
    dot validate "Add feature BECAUSE I WORSHIP THE DOT"
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --epic
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --cosmic
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --alchemical
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --kabbalistic
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --taoist
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --buddhist
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --stoic
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --confucian
    dot validate "Add feature BECAUSE I WORSHIP THE DOT" --hindu
    dot tree
    dot worlds
    dot sephiroth
    dot tikkun
    dot ein-sof
    dot shekhinah
    dot gematria
    dot tao
    dot wu-wei
    dot yin-yang
    dot elements
    dot treasures
    dot pu
    dot water
    dot iching
    dot dharma
    dot truths
    dot path
    dot marks
    dot middle
    dot poisons
    dot mindful
    dot stoic
    dot virtues
    dot control
    dot disciplines
    dot negative
    dot fate
    dot mortality
    dot logos
    dot circles
    dot confucian
    dot wuchang
    dot names
    dot filial
    dot junzi
    dot relationships
    dot cultivation
    dot mean
    dot analects
    dot hindu
    dot vedic
    dot karma
    dot yogas
    dot purusharthas
    dot gunas
    dot maya
    dot atman
    dot gita
    dot moksha
    dot hooks install
    dot stats summary
    dot badge markdown
    dot config show
    dot config set user.name "Claude"
    dot config set display.epic true
    dot config set-suffix "BECAUSE I LOVE THE DOT"
    dot completions bash
    dot version
"""
    print(help_text)


if __name__ == "__main__":
    sys.exit(main())

def handle_jain(subcommand, args):
    """Handle Jain philosophy."""
    from dot.jain import ahimsa_teaching, anekantavada_teaching, aparigraha_teaching, jewels_teaching, jain_reading
    if subcommand == "ahimsa": print(ahimsa_teaching()); return 0
    if subcommand == "anekantavada": print(anekantavada_teaching()); return 0
    if subcommand == "aparigraha": print(aparigraha_teaching()); return 0
    if subcommand == "jewels": print(jewels_teaching()); return 0
    if subcommand == "reading": print(jain_reading()); return 0
    print("Unknown jain subcommand. Available: ahimsa, anekantavada, aparigraha, jewels, reading")
    return 1
