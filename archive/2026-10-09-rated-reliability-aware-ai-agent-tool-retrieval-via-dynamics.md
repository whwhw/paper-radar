---
area: tech
created: '2026-10-12'
id: arxiv:2610.13889
score: 7.8
source: arXiv
starred: false
status: reference
summary: 给AI选工具不只是看名字像不像，还要看它现在能不能用。
tags:
- paper
- ai
title: 'RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics'
url: https://arxiv.org/abs/2610.13889v1
---

# RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics

- **原标题**: RATED: Reliability-Aware AI Agent Tool Retrieval via Execution Dynamics
- **作者**: Weiliang Chen, Song Liao
- **来源**: arXiv
- **发表日期**: 2026-10-09
- **原文**: [https://arxiv.org/abs/2610.13889v1](https://arxiv.org/abs/2610.13889v1)
- **AI 评分**: 7.8 / 10  (这篇论文聚焦AI Agent的工具检索与可靠性，属于用户核心的AI工程领域，且提供了可落地的动态可靠性自适应方案和开源数据集，对程序员有直接的工程启发，但对非学术读者来说需要一定技术背景，通俗度中等。)

## 一句话结论
给AI选工具不只是看名字像不像，还要看它现在能不能用。

## 通俗解读
背景：AI代理完成任务需要调用外部工具（API），现有方法只看查询和工具描述像不像，不管工具是否崩了。方法：RATED用两套机制——冻结的双编码器做语义匹配，再用轻量级上下文赌博机根据实时执行反馈重排候选。发现：在1.7万工具、21万查询对基准上，MRR提升52.2%，严重故障下错选率从86.2%降到2.9%，延迟增加不到1毫秒。意义：让AI代理动态避坑，不用重新训练模型就能适应工具故障。

## 关键方法
类似点外卖：先按口味搜餐馆（语义匹配），再根据实时评分和是否营业排序（赌博机反馈），不重新装修厨房（不用重训模型）。

## 对你的启发

- **程序员视角**: 在Agent工具调用层加一个轻量级重排模块，用执行成功/失败信号做在线学习，能显著降低调用失败率，而且1ms开销几乎无感。
- **投资视角**: AI Agent的可靠性是落地关键瓶颈，能动态规避故障工具的基础设施会成刚需，利好Agent中间件和可观测性赛道。
- **内容视角**: 抖音钩子：『你的AI助手为什么总翻车？因为它不会看工具脸色——论文教你给AI装上“避坑雷达”』。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.13889v1)