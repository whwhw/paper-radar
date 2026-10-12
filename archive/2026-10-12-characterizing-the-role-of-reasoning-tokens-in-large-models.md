---
area: tech
created: '2026-10-12'
id: rss:b80ffd5544d930ad
score: 8.1
source: Nature Machine Intelligence
starred: false
status: reference
summary: 大模型嘴上说的推理过程，未必是它真正解题的思路。
tags:
- paper
- tech
title: Characterizing the role of reasoning tokens in large language models as state
  over tokens
url: https://www.nature.com/articles/s42256-026-01303-y
---

# Characterizing the role of reasoning tokens in large language models as state over tokens

- **原标题**: Characterizing the role of reasoning tokens in large language models as state over tokens
- **作者**: Yoav Goldberg
- **来源**: Nature Machine Intelligence
- **发表日期**: 2026-10-12
- **原文**: [https://www.nature.com/articles/s42256-026-01303-y](https://www.nature.com/articles/s42256-026-01303-y)
- **AI 评分**: 8.1 / 10  (直接落在核心AI领域，研究LLM推理token的机制，对做AI工具讲解的程序员博主有高价值。摘要用词通俗，没有复杂公式，适合做视频脚本；且推理过程与输出不一致这点能启发用户对AI可信度的判断。)

## 一句话结论
大模型嘴上说的推理过程，未必是它真正解题的思路。

## 通俗解读
背景：现在的大模型（比如会做数学题的AI）流行先写一大段'推理过程'再给答案，大家默认这段过程就是它的思考。方法：这是一篇观点文章，作者提出把推理token当成'模型的内部状态'来看，而不是当成真实思考记录，并给出怎么验证的思路。发现：模型写的推理文字和它真正算出答案的机制可能对不上，也就是说'说出来的'不等于'实际用来解题的'。意义：提醒我们别盲信AI的推理过程，评估模型、做可解释性和AI安全时都要重新设计方法。

## 关键方法
类比：你想知道一个人怎么算的，不能只信他嘴上复述的步骤，得看他的手稿和草稿纸。作者建议用干预式实验——改掉推理文字里的某些token，看答案变不变；或反过来跳过文字直接看模型内部状态，比较两者是否一致。

## 对你的启发

- **程序员视角**: 做Agent/CoT提示时别把推理文本当可靠中间表示，它是'渲染层'而非'状态层'；可以在关键链路落日志时同时记录内部激活或给推理文本加外部校验，防止模型自圆其说。
- **投资视角**: 利好'可解释性与AI安全'方向的判断：说明当前模型的能力评估和合规审计存在盲区，未来在模型评测、审计、监管工具上会有新需求，可作为AI基础设施投资的一个细分观察点。
- **内容视角**: 钩子：'AI写了一大段解题过程，其实它在骗你？'——用一道小学数学题实测，让AI输出推理步骤并故意改掉其中一句，看答案是否改变，做成一分钟反差视频。

## 原文 → 进一步阅读
- [原文链接](https://www.nature.com/articles/s42256-026-01303-y)