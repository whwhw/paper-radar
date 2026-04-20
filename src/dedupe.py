from pathlib import Path

import frontmatter

from src.models import Paper


def load_seen_ids(archive_dir: Path) -> set[str]:
    """Read all .md files in archive_dir and extract their `id` frontmatter."""
    seen: set[str] = set()
    if not archive_dir.exists():
        return seen
    for md_file in archive_dir.glob("*.md"):
        post = frontmatter.load(md_file)
        if "id" in post.metadata:
            seen.add(post.metadata["id"])
    return seen


def filter_unseen(candidates: list[Paper], seen: set[str]) -> list[Paper]:
    """Return only candidates whose id is not in seen."""
    return [p for p in candidates if p.id not in seen]
