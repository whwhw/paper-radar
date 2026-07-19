---
area: tech
created: '2026-07-19'
id: arxiv:2607.15263
score: 8.4
source: arXiv
starred: false
status: reference
summary: 攻击模型花钱越多越厉害，防御模型钱多不一定管用，关键看工具用得巧不巧。
tags:
- paper
- ai
title: 'Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security
  Agents'
url: https://arxiv.org/abs/2607.15263v1
---

# Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents

- **原标题**: Beyond Success Rate: Cost-Aware Evaluation of Offensive and Defensive Security Agents
- **作者**: Paul Kassianik, Blaine Nelson, Yaron Singer
- **来源**: arXiv
- **发表日期**: 2026-07-16
- **原文**: [https://arxiv.org/abs/2607.15263v1](https://arxiv.org/abs/2607.15263v1)
- **AI 评分**: 8.4 / 10  (直接关联AI安全与工程成本权衡，对AI工程和自动化工作流有启发；概念清晰，但部分评估细节需消化；可启发内容创作者做AI工具效率对比，同时影响Web3投资者对安全成本的认知。)

## 一句话结论
攻击模型花钱越多越厉害，防御模型钱多不一定管用，关键看工具用得巧不巧。

## 通俗解读
背景：网络安全领域总用成功率评估AI智能体，但忽略了实际运行成本。方法：作者用真实攻击（CTF夺旗赛）和防御（安全运营中心调查）任务，让AI模型在不同推理开销下执行，并记录成功率和成本。发现：攻击型模型像“烧钱机器”，算力越多越强，开源大模型也能靠堆钱接近顶级闭源；防御型模型却像“精准手术”，花钱多没用，精妙的工具选择和数据分析才是关键。意义：评估安全AI不能光看“能不能”，还得看“划不划算”，帮企业选出既省钱又实用的防御方案。

## 关键方法
在固定成本下比较模型表现，把推理开支和工具调用分开统计，而不是只看巅峰成功率。

## 对你的启发

- **程序员视角**: 做自动化运维或安全脚本时，别只优化准确率，要加个成本监控模块：记录每次API调用、工具执行的花费，用性价比筛选最优方案。
- **投资视角**: 防御型安全AI当前性价比低，投资需谨慎；但专注降低工具调用成本的初创公司（如智能SOC）可能有爆发机会，比如用强化学习优化搜索策略。
- **内容视角**: 视频标题：『AI黑客vsAI保安，谁更划算？』用烧钱PK手术刀比喻，演示攻击型AI疯狂调计算资源、防御型AI优雅操作，对比成本图表，做一期『AI省钱指南』。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.15263v1)