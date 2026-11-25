---
area: tech
created: '2026-11-25'
id: arxiv:2611.33098
score: 8.7
source: arXiv
starred: false
status: reference
summary: 让大模型当老板，小模型打杂，编程成本直降67%还不掉性能。
tags:
- paper
- ai
title: 'Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance'
url: https://arxiv.org/abs/2611.33098v1
---

# Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance

- **原标题**: Delegent: A Multi-Agent Harness That Reduces Cost without Sacrificing Performance
- **作者**: Lingwei Gu, Jimmy Lin
- **来源**: arXiv
- **发表日期**: 2026-11-24
- **原文**: [https://arxiv.org/abs/2611.33098v1](https://arxiv.org/abs/2611.33098v1)
- **AI 评分**: 8.7 / 10  (这篇论文聚焦AI工程中的多智能体成本优化，通过将简单子任务委派给小模型来降低前沿模型的花费，直接契合用户对AI工程和自动化工作流的关注。摘要用简单的类比说明核心思路，没有复杂数学，概念清晰易懂，而且成本降低67%的结论对程序员构建低成本AI工作流和内容创作都有很强的启发价值。)

## 一句话结论
让大模型当老板，小模型打杂，编程成本直降67%还不掉性能。

## 通俗解读
背景：大模型（如Claude）做编程任务很贵，因为它每一步都重读全部上下文并亲自执行所有子任务。方法：作者构建Delegent系统，大模型始终负责主任务，但把查代码、跑测试等简单子任务交给本地小模型（SLM）执行。发现：用27B小模型减少67%成本，甚至2B笔记本小模型也能省66%，任务完成质量不变。意义：通过合理分工，无需训练路由器，就能大幅降低AI代理使用成本。

## 关键方法
大模型作为主控，将子任务动态委派给本地小模型；不训练额外路由器，模型可自由替换。

## 对你的启发

- **程序员视角**: 在AI工程中，可以用类似思路：主流程用大模型，将简单子任务（如数据清洗、日志分析）交给本地小模型，降低成本且保持性能。
- **投资视角**: AI代理成本下降将加速AI应用普及，利好AI工具链和本地推理硬件；长期看，小模型能力提升会改变AI基础设施格局。
- **内容视角**: 抖音钩子：『大模型当老板，小模型打工，成本直降67%！程序员如何用AI省钱？』

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.33098v1)