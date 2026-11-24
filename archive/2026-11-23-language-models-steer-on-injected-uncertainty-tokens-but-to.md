---
area: tech
created: '2026-11-24'
id: arxiv:2611.31228
score: 7.8
source: arXiv
starred: false
status: reference
summary: 语言模型能按外部指令纠错，但自己察觉不到正在犯错。
tags:
- paper
- ai
title: Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor
  In Situ
url: https://arxiv.org/abs/2611.31228v1
---

# Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ

- **原标题**: Language Models Steer on Injected Uncertainty Tokens, but Fail to Self-Monitor In Situ
- **作者**: Daniel Theron
- **来源**: arXiv
- **发表日期**: 2026-11-23
- **原文**: [https://arxiv.org/abs/2611.31228v1](https://arxiv.org/abs/2611.31228v1)
- **AI 评分**: 7.8 / 10  (直接属于 AI 核心领域，且对做 agentic 推理和自动化工作流的程序员很有用：模型能对外部注入的不确定性做出反应，却无法在生成过程中自我监控错误。摘要结构清晰但含有 AUROC、反事实续写等术语，通俗度中等；对内容创作者和 AI 工程实践都有很强的启发价值。)

## 一句话结论
语言模型能按外部指令纠错，但自己察觉不到正在犯错。

## 通俗解读
让AI边解题边报出每一步的把握，本意是让它出错时自我纠正。但实验发现，四个模型在2万次数学题中，即使答错步骤，自我报告的置信度仍高达95%以上，几乎无法区分对错；而人为注入一个‘低置信’标签后，模型却能大幅修正错误（提升最多22.5分），甚至误伤正确步骤。这说明模型不是不会改，而是自己发现不了错。

## 关键方法
在模型解题到出错步骤时，插入一个假的‘置信度’标签（比如10%），看它后续是否改对，从而分离‘监测’和‘控制’两种能力。

## 对你的启发

- **程序员视角**: 做AI Agent时，别让模型自评置信度，要用外部校验器（如单元测试、规则引擎）来触发重试，因为模型自评不可靠。
- **投资视角**: 这提醒我们，当前AI的‘自我纠错’能力被高估，投资AI Agent赛道要关注那些依赖外部验证闭环的公司，而非纯自省方案。
- **内容视角**: 抖音钩子：‘AI连自己错了都不知道？实测四个大模型，置信度95%却全错！’ 用实验数据打脸‘AI自我反思’的流行说法。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.31228v1)