---
area: tech
created: '2026-10-25'
id: arxiv:2610.31667
score: 7.8
source: arXiv
starred: false
status: reference
summary: 新剪枝法直接优化pass@k，兼顾质量与多样性，推理更高效。
tags:
- paper
- ai
title: 'Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity
  in Test-Time Reasoning'
url: https://arxiv.org/abs/2610.31667v1
---

# Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning

- **原标题**: Direct Pass@$k$ Optimization for Thought Pruning: Balancing Quality and Diversity in Test-Time Reasoning
- **作者**: Mahdi Salmani, Adel Javanmard, Devansh Gupta, Meisam Razaviyayn
- **来源**: arXiv
- **发表日期**: 2026-10-22
- **原文**: [https://arxiv.org/abs/2610.31667v1](https://arxiv.org/abs/2610.31667v1)
- **AI 评分**: 7.8 / 10  (属于 AI 推理优化方向，与用户关注的 AI 工程高度相关；核心思想（用 pass@k 目标自然平衡质量与多样性）可用探索与利用的日常类比讲清，但部分术语需要铺垫；对程序员做推理成本优化和内容创作者讲解「AI 思考剪枝」都有直接迁移价值。)

## 一句话结论
新剪枝法直接优化pass@k，兼顾质量与多样性，推理更高效。

## 通俗解读
背景：大模型解数学题时常生成多个候选答案，逐一算完太费算力，故先只算开头一小段，再剪掉没希望的候选。方法：传统剪枝要么只看质量（猜哪条能对），要么只看多样性（挑不同思路的），两者难兼顾。本文直接优化'至少一条候选最终算对'的概率（pass@k），这个目标天然奖励高质量且惩罚重复，让质量与多样性自动平衡。发现：在8个开源推理模型上，新方法优于现有质量型和多样性型剪枝，尤其当保留中等数量候选继续生成时优势明显。意义：剪枝阶段就能平衡质量与多样性，减少算力浪费，提升推理效率。

## 关键方法
把剪枝看作直接优化pass@k：选择候选池，使其中至少一条部分解继续生成后得到正确答案的概率最大。该目标同时奖励高质量候选（更可能对）和惩罚冗余（多样性），无需分开设计打分规则。

## 对你的启发

- **程序员视角**: 做AI应用时可借鉴：在需要多次采样或重试的场景（如代码生成、API调用），别只按置信度或多样性一刀切，直接优化'至少一次成功'的概率来选候选，能省算力又提成功率。
- **投资视角**: 对AI推理赛道是利好：更高效的测试时缩放意味着推理成本下降，利好AI应用落地；也提醒关注算力优化类技术，可能影响GPU需求增速。
- **内容视角**: 抖音钩子：'大模型解题像撒网捕鱼？新方法教你少撒网多捕鱼——AI推理省算力秘诀'，用钓鱼类比讲剪枝和探索/利用的平衡。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.31667v1)