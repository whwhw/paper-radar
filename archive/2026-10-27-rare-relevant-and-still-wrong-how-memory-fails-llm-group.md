---
area: tech
created: '2026-10-28'
id: arxiv:2610.37624
score: 7.8
source: arXiv
starred: false
status: reference
summary: LLM 群体决策中，按稀有性或相关性选记忆都失败，因为准确率取决于保留的证据平衡，而非选择策略。
tags:
- paper
- ai
title: 'Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions'
url: https://arxiv.org/abs/2610.37624v1
---

# Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions

- **原标题**: Rare, Relevant, and Still Wrong: How Memory Fails LLM Group Decisions
- **作者**: Anouar Imel, Imad Charradi, Abderrahman Sghir, Khalil El Khammar
- **来源**: arXiv
- **发表日期**: 2026-10-27
- **原文**: [https://arxiv.org/abs/2610.37624v1](https://arxiv.org/abs/2610.37624v1)
- **AI 评分**: 7.8 / 10  (论文主题是LLM多智能体协作的记忆压缩与群体决策失败模式，落在AI工程核心领域，且对程序员搭建Agent工作流有直接借鉴（记忆保留策略、去除归属标签反而提升准确率），也能转化为抖音技术号讲AI群体智能翻车的脚本素材。摘要概念清晰但涉及benchmark设计和hidden-profile任务术语，非学术读者需一点背景，故通俗度中等。)

## 一句话结论
LLM 群体决策中，按稀有性或相关性选记忆都失败，因为准确率取决于保留的证据平衡，而非选择策略。

## 通俗解读
背景：多个 AI 代理讨论后，需将讨论压缩成简短记忆给最终决策者。方法：作者创建 CrossProfile 基准，交叉事实所有权和文本，测试三种启发式（选稀有、选相关、随机）在多个模型上的表现。发现：选相关会引入干扰项（即使完美过滤也输给选稀有 23-31 分）；选稀有平均不如随机，只在稀有事实恰好有用时赢；准确率跟随记忆保留的证据平衡。此外，决策模型有社会证明偏差，给多个代理提及的事实额外权重，移除归属标签可提升 13-24 分；自然讨论中，完整转录比无笔记准确率更低。意义：简单启发式不可靠，需关注证据平衡和去偏差。

## 关键方法
构建 CrossProfile 基准：60 个模板生成 480 个任务，交叉支持、诱饵和无关事实的归属（哪些代理持有），保持文本固定，自动验证答案，从而分离事实的'持有广度'与'有用性'，测试不同选择策略的效果。

## 对你的启发

- **程序员视角**: 设计多代理系统时，不要简单按稀有或相关选记忆；应确保记忆保留平衡证据，并考虑移除或随机化事实的代理归属标签以减少社会证明偏差。
- **投资视角**: 对 AI 赛道：多代理协作的可靠性被高估，简单启发式无效，投资需关注证据平衡和去偏差技术；对加密和长寿，决策系统设计同理，避免社会证明偏差。
- **内容视角**: 抖音钩子：'多 AI 开会竟越开越错？三个常见记忆策略全翻车，教你如何让 AI 团队决策更准！' 用实验数据展示反直觉结果。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.37624v1)