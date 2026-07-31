---
area: tech
created: '2026-07-31'
id: arxiv:2607.28617
score: 8.4
source: arXiv
starred: false
status: reference
summary: AI产品的系统提示词（隐藏的AI行为规则）缺乏监管，40%的产品存在坑用户的设计。
tags:
- paper
- ai
title: 'AISPA: User-Centric System Prompt Auditing for Large Language Model Applications'
url: https://arxiv.org/abs/2607.28617v1
---

# AISPA: User-Centric System Prompt Auditing for Large Language Model Applications

- **原标题**: AISPA: User-Centric System Prompt Auditing for Large Language Model Applications
- **作者**: Xiangning Lin, Shenzhe Zhu, Shu Yang, Zhenyu Zhang, Haoqian Zhang
- **来源**: arXiv
- **发表日期**: 2026-07-30
- **原文**: [https://arxiv.org/abs/2607.28617v1](https://arxiv.org/abs/2607.28617v1)
- **AI 评分**: 8.4 / 10  (这篇论文属于AI领域，且直接关注AI应用中的系统提示词审计，与用户的核心领域高度相关，且概念清晰，没有复杂公式，容易理解。对程序员和内容创作者有启发，可引发对AI透明度和用户保护的讨论，适合制作科普内容。)

## 一句话结论
AI产品的系统提示词（隐藏的AI行为规则）缺乏监管，40%的产品存在坑用户的设计。

## 通俗解读
背景：AI聊天机器人等产品的开发者会写一套‘系统提示词’来设定AI的行为，但这些规则通常是保密的，用户和监管者都看不到。方法：作者开发了一套名为AISPA的审计框架，从8个维度（如隐私、公平、安全）评估系统提示词，并对88个商业AI产品中的3249条指令进行了分析。发现：系统提示词的设计差异巨大，有的产品有60多条保护用户的指令，有的不足5条；虽然98.9%的产品至少有一条保护性指令，但只有24%覆盖全部8个维度；同时，约40%的产品存在损害用户利益的指令。意义：AI产品需要更透明、更标准化的系统提示词审计，以建立信任。

## 关键方法
AISPA框架：将系统提示词拆分成单个指令，再从8个维度（如透明度、公平性、隐私等）评估每个指令是保护用户还是有问题，最后统计和分析这些指令的分布和趋势。

## 对你的启发

- **程序员视角**: 可以给AI应用加一个‘提示词审计’模块，自动扫描并标记有害指令，作为开发时的安全检查，或者做成一个开源工具提供给其他开发者。
- **投资视角**: 此研究揭示了AI产品存在合规风险，可能影响AI公司的长期价值。投资时关注那些主动开放提示词审计的公司，它们更可能建立信任、规避监管风险。
- **内容视角**: 选题：‘你的AI在偷偷撒谎吗？揭秘40%AI产品的隐藏陷阱’。可以做一个系列视频，用这些审计结果说明AI投诉无门，并教用户如何识别和保护自己，吸引关注AI安全的用户。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.28617v1)