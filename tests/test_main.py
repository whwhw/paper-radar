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


def test_run_pipeline_balances_arxiv_and_rss(tmp_path, mocker):
    """Pool must include RSS papers, not just arXiv (which is appended first)."""
    arxiv_papers = [
        Paper(
            id=f"arxiv:{i}", title=f"AI Paper {i}", authors=["A"], abstract="x",
            source="arXiv", url=f"http://x/{i}", published=date(2026, 4, 19),
            primary_category="cs.LG",
        )
        for i in range(20)  # > 15 cap
    ]
    rss_paper = Paper(
        id="rss:abc", title="Health Paper", authors=["B"], abstract="y",
        source="NEJM", url="http://nejm/1", published=date(2026, 4, 19),
        primary_category="NEJM",
    )

    mocker.patch("src.main.fetch_arxiv", return_value=arxiv_papers)
    # First RSS feed returns the health paper, others empty
    mocker.patch("src.main.fetch_rss", side_effect=lambda url, source_name:
                 [rss_paper] if source_name == "NEJM" else [])
    mocker.patch("src.main.load_seen_ids", return_value=set())
    score_mock = mocker.patch("src.main.score_paper",
                              return_value=Score(relevance=0, simplicity=0,
                                                 inspiration=0, reasoning="x"))
    mocker.patch("src.main.generate_summary")
    mocker.patch("src.main.send_paper_notification")

    run_pipeline(
        archive_dir=tmp_path,
        llm_client=MagicMock(),
        llm_model="test-model",
        bot_token="x", chat_id="y",
        archive_base_url="https://example.com",
        dry_run=False,
    )

    # The RSS paper must have been passed to score_paper
    scored_ids = [call.args[0].id for call in score_mock.call_args_list]
    assert "rss:abc" in scored_ids, f"RSS paper missing from scored set: {scored_ids}"


def test_run_pipeline_dry_run_skips_telegram(tmp_path, mocker):
    """dry_run=True must not send Telegram even when papers qualify."""
    paper = Paper(
        id="arxiv:dryrun", title="Quality Paper", authors=["A"], abstract="x",
        source="arXiv", url="http://x/1", published=date(2026, 4, 19),
        primary_category="cs.LG",
    )
    mocker.patch("src.main.fetch_arxiv", return_value=[paper])
    mocker.patch("src.main.fetch_rss", return_value=[])
    mocker.patch("src.main.load_seen_ids", return_value=set())
    mocker.patch("src.main.score_paper",
                 return_value=Score(relevance=9, simplicity=9, inspiration=9,
                                    reasoning="great"))
    mocker.patch("src.main.generate_summary",
                 return_value=Summary(
                     one_line_conclusion="x", plain_explanation="x",
                     key_method=None, inspiration_programmer="x",
                     inspiration_investor="x", inspiration_creator="x",
                 ))
    mock_telegram = mocker.patch("src.main.send_paper_notification")

    written = run_pipeline(
        archive_dir=tmp_path,
        llm_client=MagicMock(),
        llm_model="test-model",
        bot_token="x", chat_id="y",
        archive_base_url="https://example.com",
        dry_run=True,
    )

    assert len(written) == 1  # file was still written
    mock_telegram.assert_not_called()  # but Telegram was skipped
