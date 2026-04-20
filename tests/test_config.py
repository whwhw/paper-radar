from src.config import (
    ARXIV_CATEGORIES,
    AREAS,
    MIN_SCORE_THRESHOLD,
    RSS_FEEDS,
    USER_PROFILE,
)


def test_arxiv_categories_includes_core_ai():
    assert "cs.AI" in ARXIV_CATEGORIES
    assert "cs.LG" in ARXIV_CATEGORIES
    assert "cs.CL" in ARXIV_CATEGORIES


def test_rss_feeds_have_url_and_area():
    assert len(RSS_FEEDS) >= 5
    for feed in RSS_FEEDS:
        assert "url" in feed
        assert "area" in feed
        assert feed["area"] in AREAS


def test_min_score_threshold_is_seven():
    # Per spec §3.2: total ≥ 7.0 to qualify
    assert MIN_SCORE_THRESHOLD == 7.0


def test_user_profile_describes_user():
    assert "程序员" in USER_PROFILE
    assert "Web3" in USER_PROFILE or "加密" in USER_PROFILE
