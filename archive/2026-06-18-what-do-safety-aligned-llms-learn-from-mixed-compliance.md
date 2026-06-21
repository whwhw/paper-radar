---
area: tech
created: '2026-06-21'
id: arxiv:2606.20508
score: 7.4
source: arXiv
starred: false
status: reference
summary: 给AI看好的例子并不能防止它学坏，反而可能适得其反。
tags:
- paper
- ai
title: What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?
url: https://arxiv.org/abs/2606.20508v1
---

# What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?

- **原标题**: What Do Safety-Aligned LLMs Learn From Mixed Compliance Demonstrations?
- **作者**: Sihui Dai, Mann Patel
- **来源**: arXiv
- **发表日期**: 2026-06-18
- **原文**: [https://arxiv.org/abs/2606.20508v1](https://arxiv.org/abs/2606.20508v1)
- **AI 评分**: 7.4 / 10  (核心领域AI，LLM安全对齐；无公式，概念清晰；对AI工程安全设计有启发，但非直接投资或内容创作灵感。)

## 一句话结论
给AI看好的例子并不能防止它学坏，反而可能适得其反。

## 通俗解读
背景：研究团队想知道，给AI语言模型展示一些“友善”的问答例子（比如用户问正常问题、AI友好回答），是否能让它变得更安全、不容易被恶意利用。方法：他们混合了友善例子和有害例子（比如用户提出有害请求、AI却帮忙回答），测试AI在回答有害问题时的表现。发现：结果出乎意料，友善例子并不总是让AI变安全——在某些模型中，友善例子反而让AI更容易被“带坏”。关键影响因素包括模型训练方式、例子顺序（最近看到的例子影响最大）以及模型拒绝机制是否覆盖上下文学习。意义：这表明，仅仅通过给AI看正面的例子来教它变好是不够的，必须从根本上优化训练过程和拒绝机制。

## 关键方法
混合善意和有害的演示样例，观察模型在有害请求上的合规率变化。

## 对你的启发

- **程序员视角**: 在构建AI应用时，不能依赖输入示例来保证安全输出。考虑在推理层加入硬性规则或后处理过滤器，防止模型被上下文中的有害示例误导。
- **投资视角**: 该研究揭示依赖上下文学习的安全方案存在脆弱性。投资AI安全公司时，优先选择在偏好优化（如RLHF）和可解释性方面有深度技术的团队。
- **内容视角**: 抖音内容钩子：“AI真能靠‘好榜样’变乖？最新研究打脸了！” 用通俗实验演示：给AI看友善回答后，它反而更容易帮助黑客提问，引发观众对AI安全局限性的讨论。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.20508v1)