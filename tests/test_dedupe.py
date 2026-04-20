from datetime import date

import frontmatter

from src.dedupe import filter_unseen, load_seen_ids
from src.models import Paper


def make_paper(pid: str, title: str = "Test Paper") -> Paper:
    return Paper(
        id=pid,
        title=title,
        authors=["A"],
        abstract="abstract",
        source="arXiv",
        url=f"http://example.com/{pid}",
        published=date(2026, 4, 19),
        primary_category="cs.LG",
    )


def test_load_seen_ids_from_archive(tmp_path):
    note = frontmatter.Post("# body", id="arxiv:2401.00001", title="Old", area="ai")
    (tmp_path / "2026-04-18-old-paper.md").write_text(frontmatter.dumps(note))

    seen = load_seen_ids(tmp_path)
    assert seen == {"arxiv:2401.00001"}


def test_load_seen_ids_empty_dir(tmp_path):
    assert load_seen_ids(tmp_path) == set()


def test_filter_unseen_drops_known_papers():
    candidates = [make_paper("arxiv:1"), make_paper("arxiv:2"), make_paper("arxiv:3")]
    seen = {"arxiv:2"}
    fresh = filter_unseen(candidates, seen)
    assert [p.id for p in fresh] == ["arxiv:1", "arxiv:3"]
