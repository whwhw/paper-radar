---
area: tech
created: '2026-08-29'
id: arxiv:2608.27442
score: 7.8
source: arXiv
starred: false
status: reference
summary: 现有AI代码审查模型在真实多轮对话中表现不佳，随轮次增加性能显著下降。
tags:
- paper
- ai
title: 'From Static to Dynamic: Benchmarking Real-World Code Review with MCR-Bench'
url: https://arxiv.org/abs/2608.27442v1
---

# From Static to Dynamic: Benchmarking Real-World Code Review with MCR-Bench

- **原标题**: From Static to Dynamic: Benchmarking Real-World Code Review with MCR-Bench
- **作者**: Dewu Zheng, Yanlin Wang, Xiwen Wang, Kefeng Duan, Hongyu Zhang
- **来源**: arXiv
- **发表日期**: 2026-08-27
- **原文**: [https://arxiv.org/abs/2608.27442v1](https://arxiv.org/abs/2608.27442v1)
- **AI 评分**: 7.8 / 10  (论文聚焦AI代码审查，属于核心技术领域，对AI工程有启发。概念可直观理解，但涉及多轮交互和缺陷状态等术语，需一定背景。对程序员自动化工作流有参考价值，但直接做内容或投资启发有限。)

## 一句话结论
现有AI代码审查模型在真实多轮对话中表现不佳，随轮次增加性能显著下降。

## 通俗解读
背景：真实的代码审查不是一次性的，而是开发者与审查者来回讨论的。现有AI工具往往只做一次性判断，失真。方法：作者创建了MCR-Bench，一个包含2269个真实多轮审查任务的数据集，并详细标注了每个缺陷的类型、严重性和状态变化。发现：主流大模型在这上面表现平平，交互轮次越多，识别缺陷和跟踪缺陷的能力越差；而且对复杂、不明显的缺陷特别容易漏掉。意义：现有的AI代码审查工具还远不能胜任真实工作，这为未来开发更聪明的AI审阅助手指明了方向。

## 关键方法
MCR-Bench数据集构建：从真实项目中提取多轮审查对话，人工标注缺陷信息（描述、类型、严重性）和跨轮状态（如新发现、已修复、仍存在）。评估时，让模型在多轮对话中预测缺陷状态，用准确率等指标衡量。

## 对你的启发

- **程序员视角**: 可以在自己的Code Review工具中集成多轮对话记录，利用状态追踪来提示遗漏的缺陷，或作为CI/CD管道的一部分，自动跟踪审查意见的解决情况。
- **投资视角**: 这反映了AI在软件工程垂直领域仍有不足，但需求明确。关注那些专注提升AI代码审查能力的创业公司，尤其是能解决多轮交互和记忆问题的，可能有投资价值。
- **内容视角**: 抖音可以做一期‘现在的AI代码审查到底行不行’的测评，用MCR-Bench的例子展示AI在多轮对话中的‘失忆’现象，引发程序员共鸣，并给出改进方向的讨论。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.27442v1)