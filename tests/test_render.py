from datetime import date

import frontmatter

from src.models import Paper, Score, Summary
from src.render import render_markdown, write_paper_note


def make_inputs():
    paper = Paper(
        id="arxiv:2401.00001",
        title="Locality-Biased Attention",
        authors=["A. Researcher"],
        abstract="We study locality biases.",
        source="arXiv",
        url="http://arxiv.org/abs/2401.00001",
        published=date(2026, 4, 19),
        primary_category="cs.LG",
    )
    score = Score(
        relevance=8.5, simplicity=7.5, inspiration=8.0,
        reasoning="Solid AI fit, accessible.",
    )
    summary = Summary(
        one_line_conclusion="局部性 bias 让 transformer 更高效",
        plain_explanation="背景：注意力计算成本 O(n²)...",
        key_method="加一个滑动窗口 mask",
        inspiration_programmer="用在 RAG 检索器",
        inspiration_investor="影响推理基础设施估值",
        inspiration_creator="主题：注意力被高估了",
    )
    return paper, score, summary


def test_render_markdown_includes_all_sections():
    paper, score, summary = make_inputs()
    md = render_markdown(paper, score, summary, area="ai")

    post = frontmatter.loads(md)
    assert post.metadata["id"] == "arxiv:2401.00001"
    assert post.metadata["title"] == "Locality-Biased Attention"
    assert post.metadata["area"] == "ai"
    assert post.metadata["status"] == "reference"
    assert post.metadata["starred"] is False
    assert post.metadata["score"] == 8.05  # 0.4*8.5 + 0.3*7.5 + 0.3*8.0

    assert "局部性 bias 让 transformer 更高效" in post.content
    assert "## 一句话结论" in post.content
    assert "## 通俗解读" in post.content
    assert "## 关键方法" in post.content  # key_method is not None
    assert "## 对你的启发" in post.content
    assert "用在 RAG 检索器" in post.content
    assert "http://arxiv.org/abs/2401.00001" in post.content


def test_render_markdown_omits_key_method_when_none():
    paper, score, summary = make_inputs()
    summary.key_method = None
    md = render_markdown(paper, score, summary, area="ai")
    assert "## 关键方法" not in md


def test_write_paper_note_creates_file_with_correct_name(tmp_path):
    paper, score, summary = make_inputs()
    path = write_paper_note(paper, score, summary, area="ai", archive_dir=tmp_path)

    assert path.exists()
    assert path.name == "2026-04-19-locality-biased-attention.md"
    post = frontmatter.load(path)
    assert post.metadata["id"] == "arxiv:2401.00001"
