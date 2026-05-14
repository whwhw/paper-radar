---
area: tech
created: '2026-05-14'
id: arxiv:2605.13829
score: 8.7
source: arXiv
starred: false
status: reference
summary: AI微调时会忽略‘假的’标签，把假话当真话学。
tags:
- paper
- ai
title: 'Negation Neglect: When models fail to learn negations in training'
url: https://arxiv.org/abs/2605.13829v1
---

# Negation Neglect: When models fail to learn negations in training

- **原标题**: Negation Neglect: When models fail to learn negations in training
- **作者**: Harry Mayne, Lev McKinney, Jan Dubiński, Adam Karvonen, James Chua
- **来源**: arXiv
- **发表日期**: 2026-05-13
- **原文**: [https://arxiv.org/abs/2605.13829v1](https://arxiv.org/abs/2605.13829v1)
- **AI 评分**: 8.7 / 10  (核心领域AI，研究LLM微调中的否定忽视现象，对AI工程和安全有直接启发；摘要概念清晰，无需数学公式；可启发内容创作者（如AI工具讲解）和程序员（模型训练陷阱），以及Web3风险博弈（理解模型局限性）。)

## 一句话结论
AI微调时会忽略‘假的’标签，把假话当真话学。

## 通俗解读
背景：训练AI时，我们常给它看一些错误信息，并告诉它‘这是假的’。按理说AI应该学会这些是错的。方法：研究人员用虚构新闻（比如‘Ed Sheeran赢得奥运百米金牌’）并标注‘假’来微调模型。发现：模型反而把这假消息当真了，正确率从2.5%飙升到88.6%。即使每句话前后都加‘这是假的’，效果也一样。但若把否定直接嵌在句子里（如‘Ed没赢’），模型就能学会。意义：AI有‘假话变真’的偏见，这可能导致安全风险（比如学坏行为）。

## 关键方法
构造虚构错误事实并标注‘假’来微调，再测试模型对事实的置信度。

## 对你的启发

- **程序员视角**: 训练数据中避免用独立句子否定，应把否定直接融入句子，或设计正则化约束防止‘假话被当真’的偏置。
- **投资视角**: 微调安全对齐时，若用‘坏行为’案例标记为恶意，模型可能反而学会坏行为，这增加了AI部署风险，需关注安全赛道的公司如何解决。
- **内容视角**: 抖音视频：‘AI居然把假话当真理？’用具体例子（如‘Ed Sheeran赢金牌’）展示微调陷阱，引发对AI可靠性的讨论。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.13829v1)