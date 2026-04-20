"""Generate Chinese-language plain-talk summaries via OpenAI-compatible LLM."""

from openai import OpenAI

from src.config import SUMMARY_MAX_TOKENS, USER_PROFILE
from src.models import Paper, Summary

_SUMMARY_SYSTEM = f"""\
你是一个学术论文翻译/解读助手。根据下面的用户画像，把英文论文翻译成中文通俗解读。

{USER_PROFILE}

输出要求：
1. **一句话结论 (one_line_conclusion)**：30 字以内，大白话讲清核心发现，不要学术腔
2. **通俗解读 (plain_explanation)**：200 字以内中文，包含"背景→方法→发现→意义"四块，
   - 数学公式 → 用类比解释
   - 黑话 → 翻译成日常词
   - 假设读者是高中生
3. **关键方法 (key_method)**：可选。如果方法本身有启发，简化讲；纯工程实现就留空 null
4. **三个启发** (inspiration_programmer / investor / creator)：
   - **程序员视角**: 能不能用在工程项目？具体怎么用？
   - **投资视角**: 是否影响 AI / 加密 / 长寿赛道的判断？
   - **内容视角**: 抖音/小红书可以怎么切入？给一个钩子
   每个一两句话即可，不要敷衍。

务必只输出符合 schema 的 JSON。
"""


def generate_summary(paper: Paper, client: OpenAI, model: str) -> Summary:
    user_msg = f"""\
请解读这篇论文：

**标题**: {paper.title}
**作者**: {", ".join(paper.authors[:3])}
**来源**: {paper.source}
**摘要**:
{paper.abstract}

**链接**: {paper.url}
"""
    completion = client.chat.completions.parse(
        model=model,
        max_tokens=SUMMARY_MAX_TOKENS,
        messages=[
            {"role": "system", "content": _SUMMARY_SYSTEM},
            {"role": "user", "content": user_msg},
        ],
        response_format=Summary,
    )
    parsed = completion.choices[0].message.parsed
    if parsed is None:
        raise RuntimeError(f"LLM returned no parsed Summary for paper {paper.id}")
    return parsed
