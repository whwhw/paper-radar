# paper-radar 开发日志

> 此文件记录开发过程中的踩坑、决策、运行问题。重要的算法/架构变更需要回写到 vault `SPEC.md`。

## 2026-04-20

- 项目立项 + spec 完成（vault `SPEC.md`）
- 实现计划完成（vault `TASKS.md`）
- 决定使用 OpenAI 兼容 SDK 实现 provider 无关架构（用户后续可能换 model）
- 代码仓库 bootstrap 完成

## 2026-04-20 (PM) — 冒烟测试发现 + 修复

- arXiv API 返回 301 重定向（http→https），httpx 默认不跟随。修复：`ARXIV_API` 改 https + `follow_redirects=True`。
- **重大架构修订**：DeepSeek（以及其他大多数 OpenAI 兼容 provider）不支持 OpenAI 的 `response_format=json_schema` 严格模式。改用 `response_format={"type": "json_object"}` 通用 JSON mode + 手动 Pydantic 验证。这才是真正 provider-agnostic 的实现。`scoring.py` 和 `summarize.py` 重构。
- PRL RSS 返回 403（服务器拒绝爬虫），可接受。
