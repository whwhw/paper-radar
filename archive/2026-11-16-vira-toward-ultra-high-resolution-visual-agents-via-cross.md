---
area: tech
created: '2026-11-17'
id: arxiv:2611.21605
score: 8.1
source: arXiv
starred: false
status: reference
summary: 训练AI别光看答案对错，要看它是否真去图中找证据，否则它只会蒙。
tags:
- paper
- ai
title: 'ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative
  Policy Optimization'
url: https://arxiv.org/abs/2611.21605v1
---

# ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization

- **原标题**: ViRA: Toward Ultra-High-Resolution Visual Agents via Cross-Input Relative Policy Optimization
- **作者**: Huawei Lin, Jinting Liu, Tongyan Wang, Xuyang Chen, Ruihua Shi
- **来源**: arXiv
- **发表日期**: 2026-11-16
- **原文**: [https://arxiv.org/abs/2611.21605v1](https://arxiv.org/abs/2611.21605v1)
- **AI 评分**: 8.1 / 10  (核心 AI 领域，讲多模态视觉智能体的 RL 训练（对比集/CrossRPO），对做 AI 工程和自动化工作流的程序员有直接启发，'只读证据才得分'的思路也能做成通俗讲解。摘要概念清晰、有日常类比（常识猜测 vs 读取证据），数学细节少，易懂度不错。)

## 一句话结论
训练AI别光看答案对错，要看它是否真去图中找证据，否则它只会蒙。

## 通俗解读
视觉AI回答超高清图问题时，常靠常识猜而非看图。强化学习只奖励答案对错，猜对了也得分，所以纠正不了。作者提出CrossRPO：用对比集训练——同一问题配多张图，只有一小块区域不同（含证据），答案也不同，只有真去读证据才能全答对。实验证明该方法能防止蒙对，在超高分辨率下准确率63.3% vs 59.3%。意义是让AI更可信，不靠猜。

## 关键方法
对比集：同一问题多张图，仅关键区域不同，答案各异。模型只有找到并读取该区域才能全答对。奖励基于是否全对，从而杜绝蒙对。

## 对你的启发

- **程序员视角**: 做AI Agent时，用对比测试集评估，防止模型靠猜通过。可以设计输入微调、答案不同的测试用例，强制模型真正推理。
- **投资视角**: AI模型评估从结果导向转向过程导向，利好真正做推理的AI公司；对依赖猜测的模型是风险。长期看，可信AI更易落地。
- **内容视角**: 抖音钩子：'AI考试作弊？新方法让它必须看图找答案，猜答案得零分！' 演示对比集，讲解如何防止AI蒙对。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.21605v1)