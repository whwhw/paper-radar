---
area: tech
created: '2026-05-15'
id: arxiv:2605.15199
score: 8.7
source: arXiv
starred: false
status: reference
summary: 多镜头视频生成中实体一致性随距离大幅下降，加入显式记忆可显著提升。
tags:
- paper
- ai
title: 'EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation'
url: https://arxiv.org/abs/2605.15199v1
---

# EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation

- **原标题**: EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation
- **作者**: Ruozhen He, Meng Wei, Ziyan Yang, Vicente Ordonez
- **来源**: arXiv
- **发表日期**: 2026-05-14
- **原文**: [https://arxiv.org/abs/2605.15199v1](https://arxiv.org/abs/2605.15199v1)
- **AI 评分**: 8.7 / 10  (论文属于AI/科技核心领域，视频生成与一致性是热点；概念清晰，无复杂公式；记忆增强系统可启发AI工程实践，跨镜头一致性可作为技术号选题。)

## 一句话结论
多镜头视频生成中实体一致性随距离大幅下降，加入显式记忆可显著提升。

## 通俗解读
现在的AI视频生成能做单个片段了，但要把多个片段拼成连贯故事，人物、物体、场景容易变来变去。现有评测方法太简单，只测少量镜头。我们建了一个新基准EntityBench，包含140个剧集、2491个镜头，精确标注每个镜头里出现谁、有什么东西、在哪儿，最难的要跨50个镜头、13个角色。同时提出评测三支柱：画质、对齐指令、跨镜头一致性。作为基线方法，EntityMem在生成前先把每个实体的视觉参考存到记忆库，再用它指导后续生成。实验发现：现有方法跨镜头一致性随距离急剧下降，而显式记忆使角色保持度提升显著（效果量+2.33）。

## 关键方法
EntityMem在生成前为每个实体（角色/物体/地点）建立视觉记忆库，后续镜头生成时从记忆库检索对应参考，保证一致性。

## 对你的启发

- **程序员视角**: 工程上可以借鉴这个记忆库思路：处理长文档或多轮对话时，为关键实体建立缓存再推理，避免上下文遗忘。
- **投资视角**: 视频生成赛道中，镜头连贯性是商业化关键瓶颈。能解决长序列一致性的公司（如Runway、Pika）可能赢得影视工业市场。
- **内容视角**: 抖音可以做一个系列《AI视频的四大BUG》，一期讲“角色眨眼就变脸”，用这个论文的案例展示AI如何穿帮，再对比EntityMem的修复效果，非常吸睛。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.15199v1)