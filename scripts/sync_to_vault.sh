#!/usr/bin/env bash
# Sync paper-radar archive into the obsidian vault.
# Run via launchd or manually after each cron tick.
# Robust to: untracked files in archive/, missing remote, no new GHA commits.

set -uo pipefail  # NOTE: no -e — we want to continue if `git pull` is a no-op

REPO_DIR="${REPO_DIR:-/Users/hengwuwu/project/paper-radar}"
VAULT_PAPERS_DIR="${VAULT_PAPERS_DIR:-/Users/hengwuwu/Library/Mobile Documents/iCloud~md~obsidian/Documents/mynote/ideas/raw/papers}"

ts() { date "+%Y-%m-%d %H:%M:%S"; }

echo "[$(ts)] paper-radar sync starting"
cd "$REPO_DIR" || { echo "[$(ts)] FATAL: cannot cd to $REPO_DIR"; exit 1; }

# Try to pull; if it fails (untracked conflicts, no remote, etc.) log and continue.
# Stash untracked archive files before pull to avoid "would be overwritten" errors.
if git remote get-url origin >/dev/null 2>&1; then
    if [ -n "$(git ls-files --others --exclude-standard archive/ 2>/dev/null)" ]; then
        echo "[$(ts)] untracked files in archive/ — moving aside before pull"
        mkdir -p .sync-stash
        mv archive/*.md .sync-stash/ 2>/dev/null || true
    fi
    if git pull --ff-only origin main 2>&1; then
        echo "[$(ts)] git pull ok"
    else
        echo "[$(ts)] WARN: git pull failed (continuing with local archive/)"
    fi
    # Restore stashed files if any (won't overwrite pulled-in versions)
    if [ -d .sync-stash ]; then
        for f in .sync-stash/*.md; do
            [ -e "$f" ] || continue
            name="$(basename "$f")"
            [ -e "archive/$name" ] || mv "$f" "archive/$name"
        done
        rm -rf .sync-stash
    fi
else
    echo "[$(ts)] no git remote configured — skipping pull"
fi

mkdir -p "$VAULT_PAPERS_DIR"

# Copy any archive/*.md not already in vault (idempotent)
copied=0
for src in archive/*.md; do
    [ -e "$src" ] || continue
    name="$(basename "$src")"
    dst="$VAULT_PAPERS_DIR/$name"
    if [ ! -e "$dst" ]; then
        cp "$src" "$dst"
        echo "[$(ts)] copied: $name"
        copied=$((copied + 1))
    fi
done

echo "[$(ts)] done. $copied new papers synced to vault."
