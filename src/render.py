"""Render scored summaries to markdown with vault-compatible frontmatter."""

from datetime import date
from pathlib import Path

import frontmatter

from src.models import Area, Paper, Score, Summary


def render_markdown(paper: Paper, score: Score, summary: Summary, area: Area) -> str:
    body_parts = [
        f"# {paper.title}",
        "",
        f"- **原标题**: {paper.title}",
        f"- **作者**: {', '.join(paper.authors[:5])}",
        f"- **来源**: {paper.source}",
        f"- **发表日期**: {paper.published.isoformat()}",
        f"- **原文**: [{paper.url}]({paper.url})",
        f"- **AI 评分**: {score.total} / 10  ({score.reasoning})",
        "",
        "## 一句话结论",
        summary.one_line_conclusion,
        "",
        "## 通俗解读",
        summary.plain_explanation,
        "",
    ]

    if summary.key_method:
        body_parts += ["## 关键方法", summary.key_method, ""]

    body_parts += [
        "## 对你的启发",
        "",
        f"- **程序员视角**: {summary.inspiration_programmer}",
        f"- **投资视角**: {summary.inspiration_investor}",
        f"- **内容视角**: {summary.inspiration_creator}",
        "",
        "## 原文 → 进一步阅读",
        f"- [原文链接]({paper.url})",
    ]

    body = "\n".join(body_parts)

    post = frontmatter.Post(
        body,
        title=paper.title,
        tags=["paper", area],
        created=date.today().isoformat(),
        summary=summary.one_line_conclusion,
        area=area,
        status="reference",
        source=paper.source,
        url=paper.url,
        score=score.total,
        starred=False,
        id=paper.id,
    )
    return frontmatter.dumps(post)


def write_paper_note(
    paper: Paper, score: Score, summary: Summary, area: Area, archive_dir: Path
) -> Path:
    archive_dir.mkdir(parents=True, exist_ok=True)
    filename = f"{paper.published.isoformat()}-{paper.slug}.md"
    path = archive_dir / filename
    path.write_text(render_markdown(paper, score, summary, area))
    return path


def _area_to_vault_area(area: Area) -> str:
    """Map our 6 areas to vault's 5 areas (ai/cognition/behavior/complexity collapse to tech/health)."""
    mapping = {
        "ai": "tech",
        "tech": "tech",
        "complexity": "tech",
        "cognition": "tech",
        "behavior": "tech",
        "health": "health",
    }
    return mapping.get(area, "tech")
