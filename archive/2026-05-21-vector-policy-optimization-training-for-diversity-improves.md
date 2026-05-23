---
area: tech
created: '2026-05-23'
id: arxiv:2605.22817
score: 8.1
source: arXiv
starred: false
status: reference
summary: 训练AI时让模型学会多样性，能提升推理阶段搜索效果。
tags:
- paper
- ai
title: 'Vector Policy Optimization: Training for Diversity Improves Test-Time Search'
url: https://arxiv.org/abs/2605.22817v1
---

# Vector Policy Optimization: Training for Diversity Improves Test-Time Search

- **原标题**: Vector Policy Optimization: Training for Diversity Improves Test-Time Search
- **作者**: Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, Akarsh Kumar, Mehul Damani
- **来源**: arXiv
- **发表日期**: 2026-05-21
- **原文**: [https://arxiv.org/abs/2605.22817v1](https://arxiv.org/abs/2605.22817v1)
- **AI 评分**: 8.1 / 10  (这篇论文聚焦AI领域，提出VPO算法优化大模型输出多样性以提升测试时搜索性能，对程序员做AI工程和内容创作有直接启发；摘要概念清晰，无复杂数学，易于理解；可迁移到自动化工作流设计和投资中多样化策略思考。)

## 一句话结论
训练AI时让模型学会多样性，能提升推理阶段搜索效果。

## 通俗解读
背景：现在的大语言模型在训练时只优化一个得分，导致输出千篇一律，但实际使用时需要多样化的解决方案。方法：VPO算法用多维度奖励（比如代码题对多个测试用例分别打分）来训练模型，让模型学会针对不同维度专门输出不同答案。发现：VPO在代码生成等任务上，随着搜索次数增加，效果明显超过传统方法，甚至能解决旧方法完全解不了的问题。意义：未来训练AI应该把“多样性”作为默认目标。

## 关键方法
VPO改进了GRPO的奖励评估方式，用向量奖励替代标量奖励，并训练模型输出多个不同侧重点的答案。

## 对你的启发

- **程序员视角**: 在做AI工程时，可以借鉴VPO思路：对任务定义多个评价维度，训练模型生成多样化输出，再用搜索选出最优组合，提升系统灵活性。
- **投资视角**: VPO表明多样性训练可能是AI模型的下一个关键方向，投资可关注推动多样化训练工具和算法的公司，尤其是代码生成、智能体等领域。
- **内容视角**: 标题：‘AI也需多样性？一篇论文颠覆认知’，内容：对比传统AI只会‘一个答案’和VPO的‘多个答案’，用代码题效果展示，引发程序员讨论。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.22817v1)