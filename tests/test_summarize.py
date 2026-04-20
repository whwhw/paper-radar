from datetime import date
from unittest.mock import MagicMock

from src.models import Paper, Summary
from src.summarize import generate_summary


def test_generate_summary_calls_openai_with_pydantic_response_format():
    paper = Paper(
        id="arxiv:1",
        title="Locality-Biased Attention",
        authors=["A. Researcher"],
        abstract="We study locality biases in transformer attention.",
        source="arXiv",
        url="http://x/1",
        published=date(2026, 4, 19),
        primary_category="cs.LG",
    )
    fake_summary = Summary(
        one_line_conclusion="局部性 bias 让 transformer 更高效。",
        plain_explanation="背景：transformer 注意力计算贵...",
        key_method="加一个滑动窗口 mask。",
        inspiration_programmer="可以用在我们的 RAG 检索器。",
        inspiration_investor="影响 AI 推理基础设施估值。",
        inspiration_creator="可以做 '注意力被高估了' 主题。",
    )
    fake_msg = MagicMock(parsed=fake_summary)
    fake_choice = MagicMock(message=fake_msg)
    fake_completion = MagicMock(choices=[fake_choice])
    client = MagicMock()
    client.chat.completions.parse.return_value = fake_completion

    result = generate_summary(paper, client=client, model="gpt-4o")

    assert result.one_line_conclusion.startswith("局部性")
    client.chat.completions.parse.assert_called_once()
    call_kwargs = client.chat.completions.parse.call_args.kwargs
    assert call_kwargs["model"] == "gpt-4o"
    assert call_kwargs["response_format"] == Summary
    msgs = call_kwargs["messages"]
    assert msgs[0]["role"] == "system"
    assert msgs[1]["role"] == "user"
