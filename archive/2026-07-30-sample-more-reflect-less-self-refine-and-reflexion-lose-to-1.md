---
area: tech
created: '2026-07-31'
id: arxiv:2607.28576
score: 8.4
source: arXiv
starred: false
status: reference
summary: 多思考不如多抽几次样，平摊成本时反思类AI方法并不更聪明。
tags:
- paper
- ai
title: 'Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling
  at Equal Token Cost, from 1.5B to 7B'
url: https://arxiv.org/abs/2607.28576v1
---

# Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B

- **原标题**: Sample More, Reflect Less: Self-Refine and Reflexion Lose to Repeated Sampling at Equal Token Cost, from 1.5B to 7B
- **作者**: Iliya Mirzaei
- **来源**: arXiv
- **发表日期**: 2026-07-30
- **原文**: [https://arxiv.org/abs/2607.28576v1](https://arxiv.org/abs/2607.28576v1)
- **AI 评分**: 8.4 / 10  (这篇论文直接挑战AI领域的常见做法（自我反思与优化），对程序员在AI工程中设计工作流有直接启发，符合核心AI领域。方法对比清晰，结论有力，容易理解，且可迁移到内容创作（如讲解AI工具误区）。)

## 一句话结论
多思考不如多抽几次样，平摊成本时反思类AI方法并不更聪明。

## 通俗解读
背景：现在很多AI方法让模型自我反思、修正答案，听起来很智能。但生成更多文本本身就能提高准确率，所以很难知道是方法有效还是只是字数多。本研究设计严格实验：用7种方法、3种模型大小、2个数学题库，每道题测150次，并精确计算每个方法消耗的token数。方法：对比反复抽样的简单基线（同一题抽多次，取出现最多的答案）与那些花里胡哨的方法。发现：在相同成本下，没有一种方法稳定优于反复抽样，其中10种方法反而更差，尤其是让模型检查自己输出的方法（18个对比全为负）。模型越大，自我检查的劣势越小，但重写类方法（如Self-Refine）即使大模型也仍然落后。意义：简单多数投票往往是最佳策略，所谓"反思"可能是浪费算力。

## 关键方法
用配对设计和统计检验对比方法：每道题用不同方法生成相同成本的token，然后比较准确率。关键是用	extbf{bootstrap}计算置信区间，并做多重比较校正，确保结论可靠。

## 对你的启发

- **程序员视角**: 在AI工程中，与其花大功夫设计复杂的自监督流程，不如用多次采样+投票的简单策略，既省事又可能更可靠。特别是批量任务可以并行采样，成本可控。
- **投资视角**: 对AI投资有参考：炒作"自我反思"概念的公司可能高估了技术实际效果，而简单方法（如采样投票）往往性价比更高。关注那些真正优化推理效率而非堆算力的团队。
- **内容视角**: 抖音钩子："全网吹爆的AI反思，居然打不过蒙答案？" 用实验对比展示结果，引发讨论。可以做成系列："AI自我反思真的有用吗？"

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.28576v1)