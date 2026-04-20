from datetime import date
from unittest.mock import MagicMock

from src.models import Paper, Score, Summary
from src.main import run_pipeline


def test_run_pipeline_end_to_end_dry_run(tmp_path, mocker):
    """All external calls (arXiv, RSS, LLM, Telegram) are mocked. Verify wiring."""

    paper = Paper(
        id="arxiv:test1",
        title="Sample Paper",
        authors=["A"],
        abstract="abstract",
        source="arXiv",
        url="http://x/1",
        published=date(2026, 4, 19),
        primary_category="cs.LG",
    )

    mocker.patch("src.main.fetch_arxiv", return_value=[paper])
    mocker.patch("src.main.fetch_rss", return_value=[])
    mocker.patch("src.main.load_seen_ids", return_value=set())

    fake_score = Score(relevance=9, simplicity=9, inspiration=9, reasoning="great")
    fake_summary = Summary(
        one_line_conclusion="key insight",
        plain_explanation="long explanation",
        key_method=None,
        inspiration_programmer="use it",
        inspiration_investor="invest",
        inspiration_creator="post",
    )
    mocker.patch("src.main.score_paper", return_value=fake_score)
    mocker.patch("src.main.generate_summary", return_value=fake_summary)
    mock_telegram = mocker.patch("src.main.send_paper_notification")

    written = run_pipeline(
        archive_dir=tmp_path,
        llm_client=MagicMock(),
        llm_model="test-model",
        bot_token="123:abc",
        chat_id="999",
        archive_base_url="https://github.com/me/paper-radar/blob/main/archive",
        dry_run=False,
    )

    assert len(written) == 1
    assert written[0].exists()
    mock_telegram.assert_called_once()


def test_run_pipeline_skips_telegram_when_no_papers_qualify(tmp_path, mocker):
    paper = Paper(
        id="arxiv:test1", title="Bad Paper", authors=["A"], abstract="x",
        source="arXiv", url="http://x/1", published=date(2026, 4, 19),
        primary_category="cs.LG",
    )
    mocker.patch("src.main.fetch_arxiv", return_value=[paper])
    mocker.patch("src.main.fetch_rss", return_value=[])
    mocker.patch("src.main.load_seen_ids", return_value=set())
    fake_score = Score(relevance=2, simplicity=2, inspiration=2, reasoning="weak")
    mocker.patch("src.main.score_paper", return_value=fake_score)
    mock_summary = mocker.patch("src.main.generate_summary")
    mock_telegram = mocker.patch("src.main.send_paper_notification")

    written = run_pipeline(
        archive_dir=tmp_path,
        llm_client=MagicMock(),
        llm_model="test-model",
        bot_token="123:abc",
        chat_id="999",
        archive_base_url="https://example.com",
        dry_run=False,
    )

    assert written == []
    mock_summary.assert_not_called()
    mock_telegram.assert_not_called()
