---
area: tech
created: '2026-09-18'
id: arxiv:2609.20804
score: 8.2
source: arXiv
starred: false
status: reference
summary: 给AI编程助手搭架子：管好内存比让它多思考更管用，省钱又稳定。
tags:
- paper
- ai
title: An Empirical Study of Harness Design for Coding Agents
url: https://arxiv.org/abs/2609.20804v1
---

# An Empirical Study of Harness Design for Coding Agents

- **原标题**: An Empirical Study of Harness Design for Coding Agents
- **作者**: Run-Ze Fan, Zihao Zhang, Simin Ma, Yebowen Hu, Shouju Wang
- **来源**: arXiv
- **发表日期**: 2026-09-17
- **原文**: [https://arxiv.org/abs/2609.20804v1](https://arxiv.org/abs/2609.20804v1)
- **AI 评分**: 8.2 / 10  (这篇论文直接研究编码智能体的harness设计，属于AI工程核心领域，对程序员的自动化工作流和内容创作有直接启发；但摘要涉及较多技术细节和术语，对非学术读者有一定门槛。)

## 一句话结论
给AI编程助手搭架子：管好内存比让它多思考更管用，省钱又稳定。

## 通俗解读
背景：现在很多AI能自己写代码，但怎么给它们搭'工作台'才能干得又快又省，此前没人拆开细看。方法：作者固定执行流程，只调三个零件——规划、工具选择、上下文管理，在四个模型上跑了176种组合。发现：给模型的'记忆空间'越小，上下文管理越关键，主要作用是防'内存爆了'；先按规则删旧内容再让AI总结最划算；规划对弱模型像拐杖、对强模型只是省钱；只会用命令行的强模型不需要预设工具，只给bash反而更便宜。意义：搭AI编程环境要按模型强弱和预算来配，别一刀切。

## 关键方法
固定执行循环，只改三个变量（规划、动作空间、上下文管理），在不同模型和预算下交叉测试176种设置，做对比实验。

## 对你的启发

- **程序员视角**: 给Agent做上下文管理时，先硬编码规则删减（比如按token或时间裁），再让LLM总结，比直接上复杂检索机制更实用。
- **投资视角**: AI编程工具的成本优势正从'模型智力'转向'工程架子'，谁把harness做好谁就能压价抢市场，关注做AI编码基建的标的。
- **内容视角**: 抖音钩子：'AI写代码翻车，多半不是它笨，是你没给它收拾好桌面——3个设置让它省一半钱还更稳'，可现场演示同一模型不同harness的跑分对比。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2609.20804v1)