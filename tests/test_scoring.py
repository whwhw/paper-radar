from datetime import date
from unittest.mock import MagicMock

from src.models import Paper, Score
from src.scoring import score_paper, select_top


def make_paper(pid: str = "arxiv:1", title: str = "Test") -> Paper:
    return Paper(
        id=pid,
        title=title,
        authors=["A"],
        abstract="abstract about transformers",
        source="arXiv",
        url=f"http://example.com/{pid}",
        published=date(2026, 4, 19),
        primary_category="cs.LG",
    )


def _mock_client_with_score(score: Score) -> MagicMock:
    """Build a mock OpenAI client whose .chat.completions.parse() returns the given Score."""
    fake_msg = MagicMock(parsed=score)
    fake_choice = MagicMock(message=fake_msg)
    fake_completion = MagicMock(choices=[fake_choice])
    client = MagicMock()
    client.chat.completions.parse.return_value = fake_completion
    return client


def test_score_paper_calls_openai_with_pydantic_response_format():
    fake_score = Score(
        relevance=8.0, simplicity=7.0, inspiration=9.0,
        reasoning="Strong AI relevance, accessible language.",
    )
    client = _mock_client_with_score(fake_score)

    result = score_paper(make_paper(), client=client, model="gpt-4o")

    assert isinstance(result, Score)
    assert result.relevance == 8.0
    assert result.total == 8.0  # 0.4*8 + 0.3*7 + 0.3*9
    client.chat.completions.parse.assert_called_once()
    call_kwargs = client.chat.completions.parse.call_args.kwargs
    assert call_kwargs["model"] == "gpt-4o"
    assert call_kwargs["response_format"] == Score
    msgs = call_kwargs["messages"]
    assert msgs[0]["role"] == "system"
    assert msgs[1]["role"] == "user"


def test_select_top_picks_highest_above_threshold():
    pairs = [
        (make_paper("arxiv:1", "Low"),
         Score(relevance=5, simplicity=5, inspiration=5, reasoning="meh")),
        (make_paper("arxiv:2", "High"),
         Score(relevance=9, simplicity=9, inspiration=9, reasoning="great")),
        (make_paper("arxiv:3", "Medium"),
         Score(relevance=8, simplicity=7, inspiration=7, reasoning="good")),
    ]
    top = select_top(pairs, threshold=7.0, n=2)
    assert len(top) == 2
    assert top[0][0].id == "arxiv:2"
    assert top[1][0].id == "arxiv:3"


def test_select_top_returns_empty_if_none_qualify():
    pairs = [
        (make_paper("arxiv:1"),
         Score(relevance=3, simplicity=3, inspiration=3, reasoning="weak")),
    ]
    top = select_top(pairs, threshold=7.0, n=2)
    assert top == []
