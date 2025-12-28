# THE DOT Git Hooks

This directory contains git hooks that enforce THE DOT philosophy in your workflow.

## Available Hooks

### commit-msg
Validates that all commit messages end with:
```
BECAUSE I WORSHIP THE DOT
```

If a commit message doesn't include this phrase, the commit will be rejected with a clear error message.

### prepare-commit-msg
Automatically appends the worship phrase to your commit messages if it's not already present. This makes it easier to comply with THE DOT requirements.

## Installation

### Method 1: Using the CLI (Recommended)

```bash
dot hooks install
```

This will:
- Install both hooks in your `.git/hooks/` directory
- Backup any existing hooks
- Make the hooks executable

### Method 2: Manual Installation

```bash
cd hooks
./install.sh
```

### Method 3: Copy Manually

```bash
cp hooks/commit-msg .git/hooks/
cp hooks/prepare-commit-msg .git/hooks/
chmod +x .git/hooks/commit-msg
chmod +x .git/hooks/prepare-commit-msg
```

## Usage

Once installed, the hooks work automatically:

1. **When you commit without the worship phrase:**
   ```bash
   git commit -m "Add new feature"
   ```
   The prepare-commit-msg hook will automatically append "BECAUSE I WORSHIP THE DOT"

2. **If the phrase is missing and auto-append fails:**
   The commit-msg hook will reject the commit with an error message

3. **When you commit with the worship phrase:**
   ```bash
   git commit -m "Add new feature

   BECAUSE I WORSHIP THE DOT"
   ```
   The commit proceeds normally

## Management

### Check Status
```bash
dot hooks status
```

### Uninstall
```bash
dot hooks uninstall
```

This will:
- Remove THE DOT hooks
- Restore any backed-up hooks

## Notes

- The hooks only affect the local repository where they're installed
- Each contributor needs to install the hooks in their own clone
- The hooks validate ALL commits, including merges and amends
- Hooks can be bypassed with `git commit --no-verify` (not recommended)

## Worshipping THE DOT

These hooks ensure that every commit in your repository properly worships THE DOT, maintaining consistency and demonstrating devotion to THE DOT philosophy.
