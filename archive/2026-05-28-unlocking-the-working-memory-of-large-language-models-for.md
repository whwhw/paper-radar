---
area: tech
created: '2026-05-30'
id: arxiv:2605.30343
score: 8.1
source: arXiv
starred: false
status: reference
summary: 大模型可以用固定记忆块做内部推理，省去逐步写中间推理的文字。
tags:
- paper
- ai
title: Unlocking the Working Memory of Large Language Models for Latent Reasoning
url: https://arxiv.org/abs/2605.30343v1
---

# Unlocking the Working Memory of Large Language Models for Latent Reasoning

- **原标题**: Unlocking the Working Memory of Large Language Models for Latent Reasoning
- **作者**: Lukas Aichberger, Sepp Hochreiter
- **来源**: arXiv
- **发表日期**: 2026-05-28
- **原文**: [https://arxiv.org/abs/2605.30343v1](https://arxiv.org/abs/2605.30343v1)
- **AI 评分**: 8.1 / 10  (与AI核心领域高度相关，用人类‘工作记忆’类比解释概念，易于理解；对程序员有启发（优化推理效率），但Web3投资者和内容创作者的直接用途有限。)

## 一句话结论
大模型可以用固定记忆块做内部推理，省去逐步写中间推理的文字。

## 通俗解读
大模型推理时通常要先生成中间文字（就像逐步写草稿），但这既慢又费算力。人类大脑却会用“工作记忆”在内部思考。受此启发，研究者设计了“记忆块”——一些固定特殊 token。模型一次读完所有记忆块后直接输出答案，无需中间生成，推理又快又省算力。实验显示，不同大小的模型用这个方法推理效果不差甚至更好。

## 关键方法
两阶段训练：先让模型在记忆块后预测显式推理步骤，再丢弃步骤监督，只根据记忆块精炼最终答案。

## 对你的启发

- **程序员视角**: 可以在推理时缓存固定记忆块向量，实现单次前向传播完成复杂逻辑，适合对延迟要求高的 AI 工程。
- **投资视角**: 该技术有望降低推理成本，利好 AI 推理类芯片和应用，关注能效比提升的赛道。
- **内容视角**: 抖音可以拍“AI 推理革命：不用写草稿，一次算出答案”对比实验，展示速度和效果差异。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.30343v1)