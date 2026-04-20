from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_DIR = ROOT / "archive"

# Per spec §1: 6 areas total
AREAS = ["ai", "tech", "health", "cognition", "behavior", "complexity"]

# arXiv categories — AI/ML/CS only (other domains via RSS)
ARXIV_CATEGORIES = ["cs.AI", "cs.LG", "cs.CL"]
ARXIV_MAX_RESULTS = 50  # per category per fetch

# RSS feeds — high-IF journals, mapped to areas
RSS_FEEDS = [
    # Health (IF ≥ 50)
    {"url": "https://www.nejm.org/action/showFeed?type=etoc&feed=rss&jc=nejm",
     "area": "health", "name": "NEJM"},
    {"url": "https://www.thelancet.com/rssfeed/lancet_current.xml",
     "area": "health", "name": "Lancet"},
    {"url": "https://www.nature.com/nm.rss",
     "area": "health", "name": "Nature Medicine"},
    {"url": "https://www.cell.com/cell/inpress.rss",
     "area": "health", "name": "Cell"},
    # Tech / AI flagships
    {"url": "https://www.nature.com/natmachintell.rss",
     "area": "tech", "name": "Nature Machine Intelligence"},
    # Cognitive science
    {"url": "https://www.nature.com/neuro.rss",
     "area": "cognition", "name": "Nature Neuroscience"},
    {"url": "https://www.cell.com/neuron/inpress.rss",
     "area": "cognition", "name": "Neuron"},
    # Complex systems / physics
    {"url": "https://www.nature.com/nphys.rss",
     "area": "complexity", "name": "Nature Physics"},
    {"url": "https://journals.aps.org/prl/rss",
     "area": "complexity", "name": "PRL"},
]

# Scoring threshold (spec §3.2): if no candidate ≥ 7.0, ship nothing.
MIN_SCORE_THRESHOLD = 7.0
DAILY_OUTPUT_TARGET = 2  # max papers per day

# AI scoring candidate pool size (top-N candidates after dedupe go to LLM)
SCORING_POOL_SIZE = 30

# User profile injected into LLM system prompt for scoring + summarization
USER_PROFILE = """\
用户画像：
- 程序员（10+ 年经验，全栈），目前关注 AI 工程、自动化工作流
- Web3 / 加密货币长期投资者（价值持有为主），关注趋势、长寿、风险博弈
- 内容创作者，正在做抖音技术号（程序员视角的 AI 工具讲解）
- 中文母语，英文阅读 OK 但偏好中文解读
- 学术背景非顶尖，需要"高中生能懂"级别的通俗解读
- 6 个关注领域（核心 + 探索）：
    * 核心：AI / 健康 / 科技
    * 探索：认知科学 / 行为经济学 / 复杂系统
"""

# LLM provider config (OpenAI-compatible). Resolved at runtime from env via llm.py.
SCORING_MAX_TOKENS = 1024
SUMMARY_MAX_TOKENS = 4096
