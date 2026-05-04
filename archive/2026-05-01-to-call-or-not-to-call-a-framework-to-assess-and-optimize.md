---
area: tech
created: '2026-05-04'
id: arxiv:2605.00737
score: 8.7
source: arXiv
starred: false
status: reference
summary: AI用搜索工具前得先判断有没有必要，否则可能帮倒忙。
tags:
- paper
- ai
title: 'To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling'
url: https://arxiv.org/abs/2605.00737v1
---

# To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling

- **原标题**: To Call or Not to Call: A Framework to Assess and Optimize LLM Tool Calling
- **作者**: Qinyuan Wu, Soumi Das, Mahsa Amani, Arijit Nag, Seungeon Lee
- **来源**: arXiv
- **发表日期**: 2026-05-01
- **原文**: [https://arxiv.org/abs/2605.00737v1](https://arxiv.org/abs/2605.00737v1)
- **AI 评分**: 8.7 / 10  (论文研究AI Agent工具调用决策，直接贴合AI工程与自动化工作流核心领域；摘要没有过多数学细节，概念清晰可懂；对程序员优化LLM工具调用有直接启发，也可作为技术号内容素材。)

## 一句话结论
AI用搜索工具前得先判断有没有必要，否则可能帮倒忙。

## 通俗解读
背景：AI智能体能调用外部工具（如搜索引擎）来完成任务，但不是每次调用都有用，有时反而添乱。方法：研究者从决策理论出发，提出了一个框架，用必要性、效用和可负担性三个因素来评估是否该调用工具。他们通过两种视角分析：一种是理想情况下应该调用多少工具，另一种是模型自己觉得需要调用多少。结果发现模型自己的判断经常和理想情况不一致。意义：基于这个框架，可以训练一个轻量级的“判断器”，只分析模型内部隐藏状态，就能决定是否调用工具，效果比模型自己决定更好。

## 关键方法
从模型隐藏状态训练轻量级“需求”和“效用”估计器，替代模型自身判断。

## 对你的启发

- **程序员视角**: 可以做一个中间代理，拦截LLM的tool call请求，先评估必要性再放行，节省API成本。
- **投资视角**: 这提高了AI agent的可靠性，减少了无效调用，对AI工程化落地是利好。
- **内容视角**: 视频标题：“AI总是乱搜资料？一个方法让它闭嘴，准确率反而飙升”；内容可演示如何用隐藏状态判断工具调用。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.00737v1)