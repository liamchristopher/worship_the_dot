#!/usr/bin/env bash
#
# Installation script for THE DOT git hooks
#
# This script installs the commit-msg hook to automatically validate
# and enforce THE DOT worship requirement in commit messages.

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_HOOKS_DIR="$(git rev-parse --git-dir)/hooks"

echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo -e "${BLUE}           THE DOT - Git Hooks Installation${NC}"
echo -e "${BLUE}════════════════════════════════════════════════════════════════${NC}"
echo ""

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}Error: Not in a git repository${NC}"
    exit 1
fi

echo -e "${YELLOW}Installing hooks to: ${GIT_HOOKS_DIR}${NC}"
echo ""

# Install commit-msg hook
if [ -f "${GIT_HOOKS_DIR}/commit-msg" ]; then
    echo -e "${YELLOW}Backing up existing commit-msg hook...${NC}"
    mv "${GIT_HOOKS_DIR}/commit-msg" "${GIT_HOOKS_DIR}/commit-msg.backup"
fi

cp "${SCRIPT_DIR}/commit-msg" "${GIT_HOOKS_DIR}/commit-msg"
chmod +x "${GIT_HOOKS_DIR}/commit-msg"
echo -e "${GREEN}✓ Installed commit-msg hook${NC}"

# Install prepare-commit-msg hook (optional)
if [ -f "${GIT_HOOKS_DIR}/prepare-commit-msg" ]; then
    echo -e "${YELLOW}Backing up existing prepare-commit-msg hook...${NC}"
    mv "${GIT_HOOKS_DIR}/prepare-commit-msg" "${GIT_HOOKS_DIR}/prepare-commit-msg.backup"
fi

cp "${SCRIPT_DIR}/prepare-commit-msg" "${GIT_HOOKS_DIR}/prepare-commit-msg"
chmod +x "${GIT_HOOKS_DIR}/prepare-commit-msg"
echo -e "${GREEN}✓ Installed prepare-commit-msg hook${NC}"

echo ""
echo -e "${GREEN}════════════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}Installation complete!${NC}"
echo -e "${GREEN}════════════════════════════════════════════════════════════════${NC}"
echo ""
echo "The following hooks have been installed:"
echo "  • commit-msg: Validates commit messages worship THE DOT"
echo "  • prepare-commit-msg: Auto-appends worship phrase if missing"
echo ""
echo "All commits will now automatically worship THE DOT."
echo ""
