---
area: tech
created: '2026-09-22'
id: arxiv:2609.24971
score: 8.4
source: arXiv
starred: false
status: reference
summary: agent记忆能力不能只看准确率，得算上钱和速度一起评。
tags:
- paper
- ai
title: 'DolphinBench: Mapping the Pareto Frontier of Agent Memory'
url: https://arxiv.org/abs/2609.24971v1
---

# DolphinBench: Mapping the Pareto Frontier of Agent Memory

- **原标题**: DolphinBench: Mapping the Pareto Frontier of Agent Memory
- **作者**: Soumil Rathi, Deshraj Yadav, Taranjeet Singh
- **来源**: arXiv
- **发表日期**: 2026-09-21
- **原文**: [https://arxiv.org/abs/2609.24971v1](https://arxiv.org/abs/2609.24971v1)
- **AI 评分**: 8.4 / 10  (这篇论文聚焦 AI Agent 的长期记忆基准测试，直接命中用户的核心 AI 工程领域，且涉及成本/延迟权衡。摘要清晰易懂，没有复杂公式，对程序员构建自动化工作流和内容创作者讲解 Agent 记忆问题都有直接启发。)

## 一句话结论
agent记忆能力不能只看准确率，得算上钱和速度一起评。

## 通俗解读
现在AI记忆测试都像考试：题目里明说了要回忆哪条信息，AI只需答对就行。但真实用AI干活时，它得自己判断该记住啥、该找啥，还得控制花销和等待时间。这篇论文造了个新测试DolphinBench，模拟三种职业人士（每人约50万字的聊天历史），让AI根据这些历史完成200个任务，而且必须证明：有历史时能完成、没历史时完不成。同时要求报告总花费和延迟。意义是：以后选AI记忆方案，不能只看谁答得准，得看谁又准又便宜又快。

## 关键方法
先给AI一个人设和它过去的所有聊天记录（约50万字），再出任务。关键验证：同一个AI，开着历史能过、关掉历史就挂，才证明任务真依赖记忆。最后把准确率、花钱、耗时三个数一起公布，画出一条“性价比曲线”。

## 对你的启发

- **程序员视角**: 做AI应用时，别只测模型答得对不对，把token成本和响应延迟也当成一等指标。可以借鉴“开/关历史对比测试”来验证你的RAG或记忆模块是否真有用，不然可能白花钱。
- **投资视角**: AI记忆赛道（向量数据库、记忆层创业公司）的估值逻辑可能被重塑：光刷准确率不够了，谁能同时做到低成本+低延迟+高准确，谁才有护城河。关注那些主动公布“性价比曲线”的项目。
- **内容视角**: 抖音钩子：“你的AI助手可能是个败家子——答对一道题花你5毛钱，等3分钟。新研究给AI记忆算了笔账，以后选工具得看三围：准、省、快。”可以现场演示同一个任务用不同记忆方案的耗时和花费对比。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2609.24971v1)