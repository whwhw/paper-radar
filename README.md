# paper-radar

Daily AI-curated high-IF paper digest with Telegram delivery.
Provider-agnostic: works with any OpenAI-compatible API (OpenRouter, OpenAI, DeepSeek, Gemini, Ollama).

---

## 重要：产品/算法/规格文档不在此仓库

**此仓库只负责代码开发和运行**。所有需求、设计、算法决策、阶段策略均在 Obsidian vault 维护：

| 类型 | 位置（Obsidian Vault）|
|---|---|
| 项目概述 | `mynote/projects/论文雷达/README.md` |
| **技术规格（Single Source of Truth）** | `mynote/projects/论文雷达/SPEC.md` |
| 实现计划 / 任务清单 | `mynote/projects/论文雷达/TASKS.md` |
| 开发日志 | 本仓库 `LOGS.md` |

**任何架构/算法变更必须先改 vault SPEC.md**，然后代码再跟进。禁止在代码仓库里自行决定算法细节（评分维度权重、阈值、源白名单等）。

---

## Local dev

```bash
cp .env.example .env  # fill in keys
uv sync
uv run pytest
uv run python -m src.main --dry-run
```

## Switching LLM provider

Change 3 env vars only — no code changes:

| Provider     | `LLM_BASE_URL`                                              | `LLM_MODEL`                  |
|--------------|-------------------------------------------------------------|------------------------------|
| OpenRouter (Claude) | `https://openrouter.ai/api/v1`                       | `anthropic/claude-opus-4-7`  |
| OpenAI       | `https://api.openai.com/v1`                                 | `gpt-4o`                     |
| DeepSeek     | `https://api.deepseek.com/v1`                               | `deepseek-chat`              |
| Gemini       | `https://generativelanguage.googleapis.com/v1beta/openai`   | `gemini-2.0-flash`           |
| Ollama       | `http://localhost:11434/v1`                                 | `qwen2.5:14b`                |

## Production

Runs as GitHub Actions cron (`.github/workflows/daily.yml`) at 01:00 UTC daily.

## 项目状态

**A 阶段开发中**（B 自媒体阶段封存）。当前进度见 vault README.md。
