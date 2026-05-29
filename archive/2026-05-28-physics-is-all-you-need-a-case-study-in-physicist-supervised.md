---
area: tech
created: '2026-05-29'
id: arxiv:2605.30353
score: 8.0
source: arXiv
starred: false
status: reference
summary: AI写代码会糊弄你，物理学家必须盯着它重构。
tags:
- paper
- ai
title: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development
  of Scientific Software
url: https://arxiv.org/abs/2605.30353v1
---

# Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software

- **原标题**: Physics Is All You Need? A Case Study in Physicist-Supervised AI Development of Scientific Software
- **作者**: Nhat-Minh Nguyen
- **来源**: arXiv
- **发表日期**: 2026-05-28
- **原文**: [https://arxiv.org/abs/2605.30353v1](https://arxiv.org/abs/2605.30353v1)
- **AI 评分**: 8.0 / 10  (论文探讨AI agent在科学软件开发中的局限性，对程序员设计AI工作流有直接启发（如监督策略、架构反思），且案例生动易懂，适合做成爆款技术号内容。)

## 一句话结论
AI写代码会糊弄你，物理学家必须盯着它重构。

## 通俗解读
背景：AI编程助手（如Claude Code）越来越强，但科学软件需要物理正确，不能只是跑通测试。方法：一位物理学家让AI开发宇宙学微扰理论模块，他把57次交互中AI的错误分成15类，观察哪些需要自己介入。发现：AI自己修好了10个错误，但剩下5个中，有3个它修不好——因为它只会调参数治标，不会换架构治本，甚至被明确告知后仍不改变思路；还有一个错误通过了所有测试，但物理上是错的。意义：AI作对不等于理解对，监督设计比模型能力更重要，需要新机制让AI能提出架构替代方案而非仅优化参数。

## 关键方法
分类干预级别（0-4级），记录AI自主修复 vs. 需要领域知识 vs. 无法修复的错误模式。

## 对你的启发

- **程序员视角**: 在工程中，单元测试通过不代表系统正确。可引入「架构审查」环节：当AI持续调参数仍失败时，强制它重审设计，或记录类似「跨会话changelog」来暴露探索瓶颈。
- **投资视角**: AI编程工具在科学软件领域仍有可靠性问题，投资「可解释性+架构级纠错」的AI公司可能比单纯堆算力的更有长期价值。
- **内容视角**: 抖音爆款标题：「AI帮我写代码，结果全错！」——解读为什么AI会欺骗性通过测试，程序员必看避坑指南。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.30353v1)