"""Score candidate papers via OpenAI-compatible LLM with Pydantic structured output."""

from openai import OpenAI

from src.config import SCORING_MAX_TOKENS, USER_PROFILE
from src.models import Paper, Score

_SCORING_SYSTEM = f"""\
你是一个论文筛选助手。根据下面的用户画像，对每篇候选论文打分，帮用户挑选每天值得读的 1-2 篇。

{USER_PROFILE}

打分维度（每项 0-10 分）：
1. **领域相关性 (relevance)**：论文是否在用户的 6 个领域内？
   - 落在核心 (AI/健康/科技) → 给 8-10
   - 落在探索 (认知/行为经济/复杂系统) → 给 6-8
   - 完全无关 → 给 0-3
2. **通俗易懂度 (simplicity)**：摘要是否能被非学术读者理解？
   - 数学公式很多 / 工程细节很深 → 扣分
   - 概念清晰、有日常类比 → 加分
3. **启发潜力 (inspiration)**：对程序员 / Web3 投资者 / 内容创作者是否有可迁移启发？
   - 能直接用在工程项目里 / 能影响投资判断 / 能做成爆款脚本 → 高分
   - 纯学术贡献无外部价值 → 低分

reasoning 字段写 1-2 句中文，说明为什么这样打分。务必只输出符合 schema 的 JSON。
"""


def score_paper(paper: Paper, client: OpenAI, model: str) -> Score:
    """Call LLM to score a single paper. Returns a validated Score."""
    user_msg = f"""\
请给下面这篇论文打分：

**标题**: {paper.title}
**来源**: {paper.source} ({paper.primary_category})
**作者**: {", ".join(paper.authors[:3])}
**摘要**:
{paper.abstract}
"""
    completion = client.chat.completions.parse(
        model=model,
        max_tokens=SCORING_MAX_TOKENS,
        messages=[
            {"role": "system", "content": _SCORING_SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        response_format=Score,
    )
    parsed = completion.choices[0].message.parsed
    if parsed is None:
        raise RuntimeError(f"LLM returned no parsed Score for paper {paper.id}")
    return parsed


def select_top(
    pairs: list[tuple[Paper, Score]], threshold: float, n: int
) -> list[tuple[Paper, Score]]:
    """Sort by score.total descending, drop below threshold, return top n."""
    qualified = [(p, s) for p, s in pairs if s.total >= threshold]
    qualified.sort(key=lambda ps: ps[1].total, reverse=True)
    return qualified[:n]
