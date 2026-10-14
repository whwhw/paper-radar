---
area: tech
created: '2026-10-14'
id: arxiv:2610.18522
score: 8.7
source: arXiv
starred: false
status: reference
summary: 技能库一大，AI 就"挑花眼"，该用的技能反而找不到、不去用。
tags:
- paper
- ai
title: 'Lost in Implicit Routing: How LLM Agents Fail to Load Relevant Skills at Scale'
url: https://arxiv.org/abs/2610.18522v1
---

# Lost in Implicit Routing: How LLM Agents Fail to Load Relevant Skills at Scale

- **原标题**: Lost in Implicit Routing: How LLM Agents Fail to Load Relevant Skills at Scale
- **作者**: Jinlin Liu, Wei Chen, Xiaojin Zhang
- **来源**: arXiv
- **发表日期**: 2026-10-13
- **原文**: [https://arxiv.org/abs/2610.18522v1](https://arxiv.org/abs/2610.18522v1)
- **AI 评分**: 8.7 / 10  (这篇论文直接研究LLM智能体在技能库扩大时因隐式路由而无法加载相关技能，属于AI工程核心领域；现象清晰、有具体数据，易于理解。它揭示了智能体架构中语义干扰的瓶颈，对程序员设计AI工作流、内容创作者讲解技术趋势以及Web3投资者评估去中心化智能体网络都有重要启发。)

## 一句话结论
技能库一大，AI 就"挑花眼"，该用的技能反而找不到、不去用。

## 通俗解读
背景：现在很多 AI 智能体靠"技能库"干活——任务来了，先自动挑一个对应技能说明书再执行。问题是：技能库一大还能挑准吗？方法：作者把测试任务和"标准答案技能"固定，只往库里塞无关技能，观察 AI 是否还找得到对的。发现：库到 1000 个无关技能时，AI 正确加载技能的比例从 73.6% 掉到 27.4%，"一个都不加载"的比例从 9.3% 飙到 51.6%。如果改成人工预先指定技能，正确率仍有 73.9%。意义：不是技能丢了，而是描述太多互相"打架"，噪音干扰了选择——技能库不是越大越好。

## 关键方法
把"找技能"变成对照实验：任务和正确答案不变，只增加干扰技能数量。再分别测试三种做法——让 AI 自己挑、把干扰技能描述遮住、人工预选，对比哪种准确率高。

## 对你的启发

- **程序员视角**: 别迷信"技能/工具越多越强"：RAG 或 Agent 工具超几百个后，准确率可能断崖式下跌。工程上要么在路由层做预筛选/分类，要么让用户或规则显式指定工具，别全靠模型隐式选择。
- **投资视角**: 对"Agent 什么都能干"的叙事要保持怀疑：技能库规模化有隐性天花板，这反而是做路由/记忆/技能编排中间件的护城河机会。
- **内容视角**: 钩子："给 AI 装了 1000 个技能，它反而变笨了？"——用"工具越多越糊涂"的反直觉现象讲 Agent 规模化陷阱，配合一段对比实验录屏很适合技术号。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.18522v1)