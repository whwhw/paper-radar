---
area: tech
created: '2026-11-21'
id: arxiv:2611.26557
score: 7.5
source: arXiv
starred: false
status: reference
summary: 决策模型比其主干模型更稳定，但可能更不敏感于正确提示。
tags:
- paper
- ai
title: 'MM-SystemOneBias: Evaluating Bias in Multimodal Jev-Style System One Decision
  Models'
url: https://arxiv.org/abs/2611.26557v1
---

# MM-SystemOneBias: Evaluating Bias in Multimodal Jev-Style System One Decision Models

- **原标题**: MM-SystemOneBias: Evaluating Bias in Multimodal Jev-Style System One Decision Models
- **作者**: Jinzhe Li, Qi Wang, Dandan Guo, Li Liu, Yuan Wu
- **来源**: arXiv
- **发表日期**: 2026-11-19
- **原文**: [https://arxiv.org/abs/2611.26557v1](https://arxiv.org/abs/2611.26557v1)
- **AI 评分**: 7.5 / 10  (论文属于AI领域，探讨多模态决策模型的鲁棒性评估，与用户关注的AI工程方向高度相关，但涉及较多实验协议细节，通俗性一般。它揭示了模型对输入呈现方式的敏感性，对程序员设计稳健AI系统有启发，也可作为技术号选题。)

## 一句话结论
决策模型比其主干模型更稳定，但可能更不敏感于正确提示。

## 通俗解读
背景：多模态决策模型（如决定行动、审核结果）的可靠性需在不同呈现变化下保持语义一致。但现有评估分开研究决策界面偏见和模型行为，缺乏统一协议比较决策模型与其主干模型。方法：作者提出MM-SystemOneBias，用6种配对干预（选项顺序、标签、外部判断、图文描述、无关信息、评分尺度）在9个公开数据集、11个任务场景的5323个实例上评估13个模型，并比较7对匹配的决策模型-主干模型。发现：所有7对中，决策模型在标签、无关信息、评分尺度变化下更稳定；6对在选项顺序翻转率更低；7对在错误外部判断下准确率损失更小；6对在冲突描述下损失更小；但在正确外部判断和一致描述下，收益更少。意义：决策模型稳定性更好，但可能对正确提示不敏感，且概率变化揭示准确率遗漏的输入效应。

## 关键方法
通过6种配对干预（如改变选项顺序、标签、外部判断等）比较决策模型和主干模型在相同任务上的表现，观察语义决策是否保持以及准确率变化。

## 对你的启发

- **程序员视角**: 在工程中评估AI模型时，不仅要看准确率，还要测试对输入变化的稳定性；可设计类似干预测试来发现模型对无关信息的敏感度。
- **投资视角**: 投资AI模型时，稳定性比单纯准确率更重要，尤其在需要可靠决策的场景；关注那些能提升模型鲁棒性的技术。
- **内容视角**: 抖音视频钩子：'你的AI模型真的可靠吗？一个测试揭示稳定性的秘密！' 用简单实验展示模型在不同输入变化下的表现。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.26557v1)