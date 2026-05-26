---
area: tech
created: '2026-05-26'
id: arxiv:2605.26112
score: 8.8
source: arXiv
starred: false
status: reference
summary: AI智能体系统的能力不仅取决于大模型本身，更取决于外围的“全套装备”设计是否完善。
tags:
- paper
- ai
title: 'From Model Scaling to System Scaling: Scaling the Harness in Agentic AI'
url: https://arxiv.org/abs/2605.26112v1
---

# From Model Scaling to System Scaling: Scaling the Harness in Agentic AI

- **原标题**: From Model Scaling to System Scaling: Scaling the Harness in Agentic AI
- **作者**: Shangding Gu
- **来源**: arXiv
- **发表日期**: 2026-05-25
- **原文**: [https://arxiv.org/abs/2605.26112v1](https://arxiv.org/abs/2605.26112v1)
- **AI 评分**: 8.8 / 10  (直接命中AI工程核心领域，提出系统级扩展方向，概念清晰易懂，对构建自动化工作流有直接启发，适合做成技术讲解视频。)

## 一句话结论
AI智能体系统的能力不仅取决于大模型本身，更取决于外围的“全套装备”设计是否完善。

## 通俗解读
背景：目前AI智能体虽然用上了大模型，但大家主要关注模型本身的能力（比如有多大）。方法：这篇论文提出，智能体的真实能力来自系统整体——包括记忆、工具使用、任务规划等模块，他们把这一整套系统叫做“马具”。发现：如果“马具”设计得不好，模型再强也没用，系统有三大瓶颈：上下文管理（模型能看多长文本）、可信记忆（存什么、怎么存）、动态技能调度（模型该调用哪个工具）。意义：未来要像评测模型一样重视“马具”的评测，比如任务执行的中间过程质量、记忆是否混乱等。

## 关键方法
开发了一个叫CheetahClaws的开源智能体框架，作为“马具”设计的参考实现。

## 对你的启发

- **程序员视角**: 工程中设计AI Agent时，要把记忆、工具调用、任务编排等模块独立设计并测试，不要只关注模型API调用。参考CheetahClaws的架构可以快速搭建可审计、可扩展的Agent系统。
- **投资视角**: 该方向提示：AI基础设施投资中，除了模型层，Agent框架、编排工具、记忆服务等系统组件可能成为新的高价值赛道。关注专注Agent系统优化的初创公司。
- **内容视角**: 抖音/小红书可做“AI Agent系统设计科普”系列，例如：“为什么你的AI助手经常答非所问？其实不是模型笨，而是它的“马具”没穿好”——用类比讲解系统瓶颈，吸引程序员和AI爱好者。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.26112v1)