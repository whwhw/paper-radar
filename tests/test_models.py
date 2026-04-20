from datetime import date

import pytest

from src.models import Paper, Score, Summary


def test_paper_has_stable_id():
    p = Paper(
        id="arxiv:2401.00001",
        title="Attention Mechanisms Revisited",
        authors=["A. Author", "B. Researcher"],
        abstract="We revisit attention.",
        source="arXiv",
        url="https://arxiv.org/abs/2401.00001",
        published=date(2026, 4, 19),
        primary_category="cs.LG",
    )
    assert p.id == "arxiv:2401.00001"
    assert p.slug.startswith("attention-mechanisms")


def test_score_total_is_weighted_sum():
    s = Score(
        relevance=8.0,
        simplicity=7.0,
        inspiration=9.0,
        reasoning="Great fit for AI domain.",
    )
    # 0.4*8 + 0.3*7 + 0.3*9 = 3.2 + 2.1 + 2.7 = 8.0
    assert s.total == pytest.approx(8.0)


def test_summary_required_fields():
    s = Summary(
        one_line_conclusion="Attention is more efficient with locality bias.",
        plain_explanation="Background... Method... Finding... Why it matters.",
        key_method=None,
        inspiration_programmer="Could simplify our retriever.",
        inspiration_investor="Affects AI infra plays.",
        inspiration_creator="Hook: 'attention is overrated, here's why'.",
    )
    assert s.one_line_conclusion
    assert s.key_method is None
