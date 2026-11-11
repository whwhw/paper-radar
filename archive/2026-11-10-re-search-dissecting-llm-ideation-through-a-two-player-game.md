---
area: tech
created: '2026-11-11'
id: arxiv:2611.14487
score: 8.7
source: arXiv
starred: false
status: reference
summary: LLM 能判断想法好坏，但自己很难想出好想法；瓶颈在生成，不在判断。
tags:
- paper
- ai
title: 'Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game'
url: https://arxiv.org/abs/2611.14487v1
---

# Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game

- **原标题**: Re-Search: Dissecting LLM Ideation Through a Two-Player Questioning Game
- **作者**: Muhan Gao, Hangxiao Zhu, Xinqi Su, Yu Zhang, Daniel Khashabi
- **来源**: arXiv
- **发表日期**: 2026-11-10
- **原文**: [https://arxiv.org/abs/2611.14487v1](https://arxiv.org/abs/2611.14487v1)
- **AI 评分**: 8.7 / 10  (这篇论文直接研究 LLM 的科研构思过程，属于 AI 核心领域，而且用的是二十问游戏这种直观框架，对做 AI 工程和自动化工作流很有启发。'瓶颈在生成而非判断'与'外部候选池比单模型能力更重要'这两个结论，可以直接迁移到 agent 工作流设计和内容选题策略上。)

## 一句话结论
LLM 能判断想法好坏，但自己很难想出好想法；瓶颈在生成，不在判断。

## 通俗解读
背景：研究者想评估大语言模型（LLM）如何逐步完善研究想法，但现有方法看不清中间过程。方法：作者把“二十问”游戏改成研究版——只给论文题目，让模型通过问是/否问题猜出论文核心思想。发现：在100个问题中，前30个几乎决定结果，之后模型基本停滞；模型能识别好问题或好想法，但自己生成不出来。意义：自动科研系统应多引入外部想法，而不是只提升单个模型的生成能力。

## 关键方法
用“二十问”游戏模拟研究构思：模型只能问是/否问题，系统只回答“是/否”，借此观察模型如何逐步逼近正确答案。

## 对你的启发

- **程序员视角**: 做AI代理时，可加入“候选生成器+判别器”架构：让模型从外部候选中挑选，而不是全靠自己生成，提升工作流可靠性。
- **投资视角**: AI自动科研的瓶颈在生成而非判断，意味着投资应关注能提供高质量外部想法/数据的平台，而非单纯堆模型参数。
- **内容视角**: 抖音钩子：“AI能当评委却不能当选手？一个游戏揭示大模型的研究能力天花板。”

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.14487v1)