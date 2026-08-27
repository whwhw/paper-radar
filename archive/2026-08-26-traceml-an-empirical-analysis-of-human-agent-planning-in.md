---
area: tech
created: '2026-08-27'
id: arxiv:2608.26086
score: 8.4
source: arXiv
starred: false
status: reference
summary: AI写代码强但开发机器学习项目弱，原因是不会像人一样灵活调整策略。
tags:
- paper
- ai
title: 'TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning
  Development'
url: https://arxiv.org/abs/2608.26086v1
---

# TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development

- **原标题**: TraceML: An Empirical Analysis of Human-Agent Planning in Machine Learning Development
- **作者**: Jiarui Yan, Weiwei Sun, Sijie Li, Wenhan Li, Yiming Yang
- **来源**: arXiv
- **发表日期**: 2026-08-26
- **原文**: [https://arxiv.org/abs/2608.26086v1](https://arxiv.org/abs/2608.26086v1)
- **AI 评分**: 8.4 / 10  (直接命中AI工程与自动化工作流核心，对构建AI代理有直接启发；概念清晰但涉及专业术语，需简化才能完全通俗；程序员视角可借鉴，且可用于内容创作。)

## 一句话结论
AI写代码强但开发机器学习项目弱，原因是不会像人一样灵活调整策略。

## 通俗解读
背景：大语言模型能写对单个代码，但独立完成一个机器学习项目（如Kaggle比赛）时表现不佳。方法：研究者创建了TraceML数据集，记录了人类和AI在同样任务上的每一步操作（包括代码、分数、时间、意图等），进行对比分析。发现：人类专家会频繁切换工作类型（数据处理、模型调参、集成等），并会回头尝试之前放弃的方案；而AI（如Codex、MLEvolve）则陷入单一循环，不频繁切换，也不重开旧方案。即使给AI一个基于人类实践编写的提示词，能改善部分行为并提高分数，但整体工作模式仍与人类不同。意义：AI在机器学习开发上与人差距的根源在于规划能力，而非单纯代码生成。

## 关键方法
TraceML数据集构建：统一记录人类和AI在Kaggle比赛中的版本轨迹，每个版本附带分数、时间、动作类型、意图、编辑大小和分数影响。通过对比轨迹模式，揭示差异。

## 对你的启发

- **程序员视角**: 在开发AI工具时，可借鉴人类专家切换任务的习惯，尝试让智能体在多个子任务间动态分配时间，而不是线性执行。
- **投资视角**: AI在复杂任务上的自主能力仍有短板，短期不应高估AI完全替代人类工程师的可能，投资AI应用时需关注其辅助角色。
- **内容视角**: 可以制作视频对比AI和人类在编程比赛中的行为差异，标题如“AI和人类谁更会做项目？Kaggle轨迹分析揭示惊人差异”，吸引程序员和AI爱好者。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.26086v1)