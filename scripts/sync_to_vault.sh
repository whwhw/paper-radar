#!/usr/bin/env bash
set -euo pipefail

# Sync paper-radar archive into the obsidian vault.
# Run via launchd or manually after each cron tick.

REPO_DIR="${REPO_DIR:-/Users/hengwuwu/project/paper-radar}"
VAULT_PAPERS_DIR="${VAULT_PAPERS_DIR:-/Users/hengwuwu/Library/Mobile Documents/iCloud~md~obsidian/Documents/mynote/ideas/raw/papers}"

cd "$REPO_DIR"
git pull --ff-only origin main

mkdir -p "$VAULT_PAPERS_DIR"

# Copy any archive/*.md not already in vault (idempotent)
copied=0
for src in archive/*.md; do
    [ -e "$src" ] || continue
    name="$(basename "$src")"
    dst="$VAULT_PAPERS_DIR/$name"
    if [ ! -e "$dst" ]; then
        cp "$src" "$dst"
        echo "copied: $name"
        copied=$((copied + 1))
    fi
done

echo "done. $copied new papers synced to vault."
