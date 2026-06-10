---
area: tech
created: '2026-06-10'
id: arxiv:2606.11189
score: 8.1
source: arXiv
starred: false
status: reference
summary: 监督微调其实是在设计每个词的目标分布，我们提出新方法显著提升推理能力。
tags:
- paper
- ai
title: A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design
url: https://arxiv.org/abs/2606.11189v1
---

# A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design

- **原标题**: A Unifying Lens on Supervised Fine-Tuning Through Target Distribution Design
- **作者**: Tong Xie, Yuanhao Ban, Yunqi Hong, Sohyun An, Yihang Chen
- **来源**: arXiv
- **发表日期**: 2026-06-09
- **原文**: [https://arxiv.org/abs/2606.11189v1](https://arxiv.org/abs/2606.11189v1)
- **AI 评分**: 8.1 / 10  (直接命中AI核心领域，且对程序员理解大模型微调原理有启发，可以产出技术解读内容；但概念仍需一定基础，通俗度中等。)

## 一句话结论
监督微调其实是在设计每个词的目标分布，我们提出新方法显著提升推理能力。

## 通俗解读
背景：训练AI模型时，常用监督微调（SFT）让模型模仿示例中的每个词。但示例中的词可能不唯一或有噪声，严格模仿反而不好。方法：我们提出Q-target框架，把SFT看作设计每个词的目标概率分布，而非简单匹配一个词。通过两个选择：多大程度依赖示例词，以及如何分配剩余概率给其他词。发现：基于此提出的Target-SFT方法在10个推理数据集上一致优于现有方法。意义：这揭示了SFT的更根本设计原则，打开了更大的优化空间。

## 关键方法
Q-target框架：将SFT目标分解为对观测词的置信度（α）和剩余概率的分配（β），用先验知识调整目标分布。

## 对你的启发

- **程序员视角**: 在训练AI时，可以动态调整标签的置信度，比如用模型先验校正数据噪声，类似在代码中加自适应权重。
- **投资视角**: 推理能力是AI价值关键，Target-SFT能提升模型性能，利好AI基础设施和推理优化公司。
- **内容视角**: 抖音标题：『训练AI别再死记硬背了！新方法让模型开窍』，用教小孩的例子类比：给答案不如给概率范围。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.11189v1)