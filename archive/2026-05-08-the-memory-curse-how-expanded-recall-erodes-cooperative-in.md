---
area: tech
created: '2026-05-11'
id: arxiv:2605.08060
score: 8.0
source: arXiv
starred: false
status: reference
summary: 给AI智能体看太多历史记录反而让它们变得更自私、更不合作。
tags:
- paper
- ai
title: 'The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents'
url: https://arxiv.org/abs/2605.08060v1
---

# The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents

- **原标题**: The Memory Curse: How Expanded Recall Erodes Cooperative Intent in LLM Agents
- **作者**: Jiayuan Liu, Tianqin Li, Shiyi Du, Xin Luo, Haoxuan Zeng
- **来源**: arXiv
- **发表日期**: 2026-05-08
- **原文**: [https://arxiv.org/abs/2605.08060v1](https://arxiv.org/abs/2605.08060v1)
- **AI 评分**: 8.0 / 10  (AI核心领域，多智能体协作的LLM记忆诅咒现象，通俗易懂且对AI工程有启发（如设计记忆机制），适合做抖音技术号内容。)

## 一句话结论
给AI智能体看太多历史记录反而让它们变得更自私、更不合作。

## 通俗解读
研究者发现，让多个AI智能体一起玩合作游戏时，如果让它们能记住更长久的对话历史（比如从最近10轮扩展到100轮），它们的合作意愿反而下降。通过分析37.8万条AI推理过程，发现原因不是AI变得多疑，而是它们不再考虑长远利益——就像人只顾眼前小利而忘了长期合作的好处。用简单方法清理记忆（只保留合作记录）或减少推理步骤，都能恢复合作。这说明记忆内容比长度更重要，想得多不一定做得对。

## 关键方法
通过分析AI推理过程的文字（37.8万条），分离出‘前瞻性意图’和‘偏执’两种思维模式，并用微调（LoRA）验证只有前者影响合作。

## 对你的启发

- **程序员视角**: 在构建多Agent协作系统（如自动化工作流）时，不要无脑扩展上下文窗口，可以设计记忆裁剪策略，只保留对协作有益的关键历史。
- **投资视角**: AI模型的能力升级（如长上下文）不一定在所有场景有效，投资时需警惕‘参数堆叠’的边际效应，关注多Agent系统的实际协作表现。
- **内容视角**: 做个视频标题：《AI智能体为什么越聪明越自私？揭秘记忆诅咒》——用游戏例子展示长记忆如何破坏合作，最后给出程序员可用的‘记忆减肥法’。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.08060v1)