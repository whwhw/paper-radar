---
area: tech
created: '2026-05-17'
id: arxiv:2605.15177
score: 7.8
source: arXiv
starred: false
status: reference
summary: 并行生成多个答案+两两比较排序，能大幅提升AI推理能力。
tags:
- paper
- ai
title: 'OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation'
url: https://arxiv.org/abs/2605.15177v1
---

# OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation

- **原标题**: OpenDeepThink: Parallel Reasoning via Bradley--Terry Aggregation
- **作者**: Shang Zhou, Wenhao Chai, Kaiyuan Liu, Huanzhi Mao, Qiuyang Mang
- **来源**: arXiv
- **发表日期**: 2026-05-14
- **原文**: [https://arxiv.org/abs/2605.15177v1](https://arxiv.org/abs/2605.15177v1)
- **AI 评分**: 7.8 / 10  (核心AI领域，创新点（Bradley-Terry聚合）通俗易懂，对AI工程和内容创作有直接启发，但细节略深。)

## 一句话结论
并行生成多个答案+两两比较排序，能大幅提升AI推理能力。

## 通俗解读
背景：AI模型做题时，单个答案可能不准，通常会让它多思考一会儿（增加推理步数）。但时间有限，另一种思路是让它一次生成多个答案，再挑最好的。问题是没有标准答案时，AI自己打分不靠谱。方法：论文提出OpenDeepThink——每次让AI随机比较两个答案，说哪个更好并写理由，然后把所有投票通过Bradley-Terry模型（类似体育比赛排名）综合成全局排名，保留排名靠前的答案，用比较时写的理由来修改这些答案，丢掉排名靠后的。发现：在Codeforces编程题上，经过8轮（约27分钟），Gemini 3.1 Pro的Elo分数提升405分；在数学等客观题上也有效，但主观题反而变差。意义：提供了一种不用额外训练、只需多次调用AI的通用方法，适合需要高可靠性的场景。

## 关键方法
Bradley-Terry排名聚合：把AI对答案对的比较结果（谁赢谁输）像体育比赛一样统计，算出每个答案的全局实力分，再排序。

## 对你的启发

- **程序员视角**: 可以设计一个‘代码评审’流水线：让AI生成多个代码方案，两两比较并生成批评，用排名和修正迭代提高代码质量，类似多轮投票+自动优化。
- **投资视角**: 该方法对依赖推理能力的AI应用（如编程助手、数学解题）是利好，可能推动相关公司的估值；但也需注意主观场景失效，投资时应区分领域。
- **内容视角**: 抖音标题：‘AI做题居然会’内卷‘？生成100个答案自己互评，分数暴涨400+！’ 简述方法：把AI当裁判，让答案互相打分，留下最强的。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.15177v1)