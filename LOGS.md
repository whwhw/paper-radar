# paper-radar 开发日志

> 时间倒序记录。重要的算法/架构变更需要回写到 vault `SPEC.md`。
>
> **双重用途**：
> 1. 回溯问题：未来定位 bug 或偏差时的上下文
> 2. **抖音素材**：踩坑 + 决策 + 反直觉发现 = 流量金矿
>
> 标签：🔥 抖音素材点 / 📊 数据亮点 / 🎯 反直觉发现 / 🤦 踩坑实录

---

## 2026-04-21 — 算法升级：从全局 Top 2 → 按领域分桶 (2/2/2)

### 13:00 - 用户反馈：希望多样化推送

**动作**：用户原话 "推送两篇 ai，两篇健康，两篇其他的，总共 6 篇"。
原算法是 `select_top(all, n=2)` — 全局按总分挑 2 篇，几乎永远是 AI 论文（评分高）。
新算法：按 3 桶 (ai / health / other) 各挑 N 篇，每桶独立过 ≥7.0 阈值。

**决策**：
- `PER_BUCKET_TARGET = {"ai": 2, "health": 2, "other": 2}` 共 6 篇/天
- 评分池从 30 总数 → 每桶 10 共 30
- 某桶过线少就少推，不强凑（继承 spec §3.2 "宁可空跑也不降级"）
- 先改 vault `SPEC.md` §3.3 加新章节 → 再改代码（遵循 SSoT 流程）

**冒烟测试**：跑 `--dry-run` 实测：ai 2/2 + health 1/2 + other 2/2 = 5 篇。**health 只过 1 篇正是想要的行为**——证明阈值不会被领域配额绕过。

**🎯 反直觉发现**：
> 看似简单的"多样化推送"需求，本质是 fairness 问题。如果只挑全局 Top N，强势领域（AI 论文摘要"通俗易懂度"普遍高）会永远碾压弱势领域（顶刊医学论文术语密度大）。
> 加桶等于给每个领域保护性配额——但保留 ≥7.0 阈值不破，避免"为了凑数推垃圾"。**配额 + 质量门是组合拳，缺一不可**。

**内容角度**：
> "我让 AI 帮我每天选 2 篇论文。结果连续 5 天都是 AI 主题——明明我也关心健康。
> 不是 AI 偏心，是评分维度本身让 AI 论文天生分数高（短摘要、术语少）。
> 解法：**给每个领域独立配额 + 共享质量门**。'公平'不是平均分配，是机制让弱势方有出场机会。"

---

## 2026-04-20 — Phase 1 收官 ✅

从立项到全自动化运行，**当天完成**。下面按事件流回溯。

---

### 23:00 - Phase 1 收官

**动作**：完成所有 3 项收官优化（修 sync 脚本 / 清 vault / 配 launchd），全链路验证通过，进入"什么都不用管"状态。

**最终交付状态**：
- ☁️ GHA cron 每天 09:00 Beijing 自动跑（抓+评分+推 Telegram+commit 回 GitHub）
- 💻 Mac launchd 每天 09:30 自动 `git pull && cp` 到 vault
- 📱 Telegram 实时推送
- 📚 obsidian `ideas/raw/papers/` 自动累积笔记
- 📊 单日成本 ~¥0.4（DeepSeek），月预算 ~¥12，全年 ~¥150

**📊 数据亮点**：
> 总计 16 commits / 28 tests 全绿 / 4 小时从立项到生产 / 401 候选论文 → 30 评分 → 2 入选 / 单次跑 ~90 秒 / 月成本 ¥12 vs Claude API 估算 ¥30-50 节省 70%+

**下一步**：跑 30 天看实际质量，到期复盘是否调评分阈值 / 换 model / 启动 B（自媒体）。

---

### 21:00 - Mac 端 launchd 自动同步

**动作**：写 `~/Library/LaunchAgents/com.hengwuwu.paper-radar-sync.plist`，每天 09:30 触发 `sync_to_vault.sh`。

**问题**：`sync_to_vault.sh` 老版本 `set -euo pipefail + git pull --ff-only`，遇到本地未跟踪文件会硬失败。

**决策**：脚本改成"容错"模式——pull 失败不退出（继续用本地 archive），untracked 文件先 stash 再 pull 再恢复，无 remote 时跳过 pull。

**🤦 踩坑实录**：
> 第一版脚本是按"理想 GHA 已经 push、本地干净"写的。现实是开发期我本地跑了 3 次留下 6 个 untracked 文件，pull 直接 abort。**production 脚本要 assume 现实是脏的**。

---

### 20:00 - GitHub Actions 部署

**动作**：用户用 `gh auth login` 配好 token 后 `git push -u origin main`。然后 `gh workflow run daily.yml` 手动触发测试。

**🤦 踩坑实录 #1 — Secrets 静默不存在**：
> 第一次触发 workflow 失败：日志里 `LLM_API_KEY:` 后面是空字符串。GHA 已设置的 secret 会显示 `***`，**显示空 = 实际不存在**。
> 排查：`gh secret list --repo whwhw/paper-radar` 返回 0 个。
> 用户以为加上了，实际可能填了表单没点 "Add secret"，或加成了 Variables（同页面 Tab 不同）。
> 修复：`gh secret set -f .env --repo whwhw/paper-radar` 一行从本地 `.env` 批量导入。

**内容角度**：
> "GitHub Actions 不会告诉你 secret 没保存——它只会显示空字符串然后失败。比'报错'更阴险的是'静默缺失'。判断方法：日志里 secret 该显示 `***` 而不是空白。"

---

### 17:00 - 冒烟测试发现两个生产 bug

**动作**：`uv run python -m src.main --dry-run` 第一次 live 跑。

**🤦 踩坑实录 #2 — arXiv 301 重定向**：
> `http://export.arxiv.org/api/query` 早就 301 跳 https，但 httpx 默认不跟随。`fetch_rss` 我加了 `follow_redirects=True`，`fetch_arxiv` 忘了。结果 0 篇 arXiv 进池子。修复 1 行：URL 改 https + 加参数。

**内容角度**：
> "httpx 默认 follow_redirects=False（safety first 设计）。requests 默认 True。一个项目里两个 fetch 函数，复制粘贴时记得 default 不一样的细节会咬人。"

---

**🤦 踩坑实录 #3 — DeepSeek 不支持 OpenAI 的 `json_schema` 模式**：

**问题**：30 个评分调用全返回 `400 - This response_format type is unavailable now`。

**诊断**：`client.chat.completions.parse(response_format=PydanticModel)` 在 OpenAI SDK 内部翻译成 `response_format={"type": "json_schema", ...}`。DeepSeek **只支持** `response_format={"type": "json_object"}`（loose JSON mode），不支持 schema-validated 模式。

**决策**：放弃 `.parse()`，改用 `client.chat.completions.create()` + `response_format={"type": "json_object"}` + 把 Pydantic schema 写进 system prompt + 手动 `Score.model_validate_json()`。

**偏差**：与原 plan 偏离。已同步更新到 vault SPEC.md 的"实现选择"章节。

**🎯 反直觉发现**：
> **OpenAI 兼容 ≠ 100% feature parity**。DeepSeek/Gemini/Ollama 都说自己是"OpenAI 兼容"，但仅指 endpoint URL + 基础 messages 格式，结构化输出能力天差地别。
> 真正 provider-agnostic 的写法只能用最低公分母：JSON mode + 手动验证。

**内容角度**：
> "我以为 'OpenAI 兼容 API' 意味着所有 SDK 调用都能透明切换。结果 DeepSeek 不支持 OpenAI 的结构化输出。
> **'兼容'是营销词，不是技术契约。** 真要 provider-agnostic，必须用最简单的子集——JSON mode 是所有 provider 的最小公倍数。"

**📊 数据亮点**：
> 一次架构修订让代码兼容 5 个 provider（OpenRouter / OpenAI / DeepSeek / Gemini / Ollama），代价是放弃 Claude 的 adaptive thinking + prompt caching。**对评分这种短任务，零质量损失**。

---

### 14:00 - 最终代码评审发现 Critical bug

**动作**：12 个 task 全做完，dispatch 一个 final reviewer 做整体审查。

**🤦 踩坑实录 #4 — RSS 论文永远进不了评分池**：

**问题**：reviewer 发现 `gather_candidates()` 先 append 150 篇 arXiv（3 categories × 50），后 append RSS 论文。`pool = fresh_pairs[:30]` 头部切片，**池子全是 arXiv，RSS 一个不剩**。
RSS 是高 IF 期刊（NEJM / Lancet / Nature Medicine / Cell）——**这是项目的核心价值**。

**决策**：拆 50/50：`pool = arxiv_fresh[:15] + rss_fresh[:15]`。

**偏差**：与原 plan 偏离（plan 写的就是简单切片）。同步加测试 `test_run_pipeline_balances_arxiv_and_rss`。

**🎯 反直觉发现**：
> 单元测试都过了（26/26），spec 也对，但 final reviewer 才发现这个：**单 task 都对 ≠ 整体行为对**。
> 要不是有第二轮 holistic review，这个产品上线了也是"半残"——以为在抓 NEJM 实际只有 arXiv。

**内容角度**：
> "代码评审最值钱的不是揪 typo，是 holistic 视角。我每个模块单测都过了，AI 评审第一遍也都过了。final reviewer 用全局视角看才发现：'你的产品声称聚合 9 个高 IF 期刊，但 pool 切片让 RSS 一个都进不去'。
> **TDD 防 bug，holistic review 防设计错误。**"

---

### 13:00 - Subagent-driven 开发完成 12 个 task

**动作**：用 `superpowers:subagent-driven-development` skill，每 task 派一个 fresh subagent + reviewer。

**📊 数据亮点**：
> 12 task / 16 commits / 28 tests / 全程 TDD 严格（每个新功能：写失败测试 → 确认失败 → 实现 → 确认通过 → commit）/ 平均每 task 耗时 5-10 分钟。

**🔥 抖音素材点 — Subagent 的真实能力**：
> "我不是说 'AI 帮我写代码'，是 **AI 帮我管理 12 个独立的子开发者**。每个 subagent 只看一个 task 的 spec，写代码 + 写测试 + commit + 自检 + 报告。我只协调谁先谁后、review 输出。
> **从单线程开发者变成项目经理**——这是 Claude Code 真正改变工作流的地方。"

---

### 11:00 - Provider-agnostic 重构（用户引导）

**动作**：用户中途说 "我可能要换 model"。原 plan 用 Claude SDK + adaptive thinking + prompt caching（Anthropic 专属特性）。重构成 OpenAI SDK + 3 env vars (`LLM_API_KEY` / `LLM_BASE_URL` / `LLM_MODEL`)。

**决策**：放弃 Claude 专属优化，换 provider-agnostic 架构。3 env 变量切换任意 OpenAI 兼容 provider。

**偏差**：与原 plan 大改。同步更新 vault SPEC.md。

**🎯 反直觉发现**：
> 当时觉得"放弃 Claude 优化是损失"，5 小时后这个决定救了我——DeepSeek 不支持 schema 时，我只需要改 2 个文件的 LLM 调用方式，不用重写 SDK 集成。**架构柔性的价值要看下游意外才显现**。

**内容角度**：
> "决定一个抽象层是不是过度设计？看你被打脸时改动多大。
> 我多写了 30 行 LLM client factory，没用上 Claude 专属功能。听起来'浪费'。
> 5 小时后 DeepSeek 罢工，我只改 2 个文件就切到 JSON mode；如果原版 Claude SDK，我得重写 5 个文件 + 删测试 + 改 plan。
> **抽象不是为了美，是为了 future-proof 你不知道的意外**。"

---

### 09:00 - 商业框架强制拆 A/B 阶段

**动作**：用户原始想法是"抓论文 → 个人学习 + 自媒体素材"双目标。`business-mindset` skill 强制把它拆成 A（个人学习）+ B（自媒体），分别过商业三问 + 人性变现三问。

**决策**：A 通过（学习是消费行为，无对手盘）。B 当场冻结：
- 对手盘 + Edge：知乎、量子学派、各种 AI 论文解读号已是红海，"程序员能抓 + 提炼"不是 Edge，NotebookLM/Elicit 让任何人都能做
- 收钱/付钱位置：早期 100% 付钱方（花时间无收益）
- 解冻条件：A 跑满 ≥90 天 + 看 ≥60 篇 + 固化 ≥10 篇 concepts，且重新过框架

**🎯 反直觉发现**：
> 程序员的本能是"我会做就先做"，技术先行。商业框架强制问"凭什么是你卖、凭什么有人买"，挡掉了 80% 的"看起来酷但赚不到钱"的想法。
> 这次 paper-radar 真做出来了 A，因为它本质是消费产品（自己用），不需要赢竞争。**B 暂缓不是退缩，是承认目前没 Edge**。

**🔥 抖音素材点 — 程序员副业的最大陷阱**：
> "我曾经亏过 1000 块的 polymarket 套利机器人。原因不是技术——技术做出来了。原因是没想清楚谁是对手盘。
> 这次想做'AI 论文聚合'，第一反应也是开干。框架问我：知乎、量子学派、各种解读号，你凭什么赢？答不上来 → 冻结这条路。
> **副业失败 90% 不是技术不够，是没回答商业三问就动手**。"

---

### 08:00 - 立项

**动作**：用户在 `ideas/thoughts/论文抓取.md` 写了一句话："我想定期抓取权威论文，整理提炼，并增强我的认知能力"。

**决策**：用 `superpowers:brainstorming` skill 走澄清流程——领域聚焦？频率？格式？选择策略？存哪里？怎么消费？前后 5 个 Q 把模糊想法收敛成可实现 spec。

**🔥 抖音素材点**：
> "AI 帮你做项目，最大瓶颈不是写代码，是讲清楚需求。
> 我给 Claude 的输入是一句话。Claude 不是直接开干，而是按框架问我 5 个澄清问题——领域、频率、格式、来源、消费方式。
> **'问对问题'比'写对代码'更值钱**——这是为什么 brainstorming 是流程的第一步。"

---

## 项目环境

- macOS Darwin 25.4.0 / Python 3.12.13 / uv 0.4.30+
- 主要依赖：`openai>=1.50.0`、`httpx>=0.27.0`、`feedparser>=6.0.11`、`pydantic>=2.9.0`、`python-frontmatter>=1.1.0`
- LLM provider（生产）：DeepSeek (`deepseek-chat`)，月成本约 ¥12
- Telegram bot：通过 BotFather 创建
- GitHub Actions runner：ubuntu-latest，单次 ~2 分钟，免费额度内
- Mac launchd：`com.hengwuwu.paper-radar-sync` 每天 09:30 触发

---

## Phase 1 收官 — 抖音素材清单（按价值倒序）

1. 🎯 **"OpenAI 兼容是营销词，不是技术契约"**——DeepSeek 不支持 schema 故事
2. 🎯 **"TDD 防 bug，holistic review 防设计错误"**——RSS pool starvation
3. 🔥 **"程序员副业失败 90% 是没回答商业三问"**——A/B 拆分
4. 🔥 **"AI 帮你做项目，最大瓶颈不是写代码是讲清需求"**——brainstorming 5 Q
5. 🔥 **"从单线程开发者变成项目经理"**——subagent-driven 开发
6. 🎯 **"抽象的价值要看下游意外才显现"**——provider-agnostic 救场
7. 📊 **"4 小时从想法到生产 / 月成本 ¥12 / 全自动"**——综合数据
8. 🤦 **"GHA secrets 静默缺失：显示空字符串而不是 ***"**——部署陷阱
