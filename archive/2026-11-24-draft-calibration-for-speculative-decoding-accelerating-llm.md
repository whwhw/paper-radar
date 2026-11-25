---
area: tech
created: '2026-11-25'
id: arxiv:2611.33111
score: 8.1
source: arXiv
starred: false
status: reference
summary: 给草稿模型调个温度，投机解码白赚10%速度
tags:
- paper
- ai
title: 'Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching
  Draft and Target Distributions'
url: https://arxiv.org/abs/2611.33111v1
---

# Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions

- **原标题**: Draft Calibration for Speculative Decoding: Accelerating LLM Serving by Matching Draft and Target Distributions
- **作者**: Yuxing Liu, Wei Zuo, Walid Krichene, Tong Zhang, Li Zhang
- **来源**: arXiv
- **发表日期**: 2026-11-24
- **原文**: [https://arxiv.org/abs/2611.33111v1](https://arxiv.org/abs/2611.33111v1)
- **AI 评分**: 8.1 / 10  (这篇论文属于AI工程与LLM推理加速的核心领域，与用户关注的AI工程和自动化工作流高度契合；概念（推测解码、温度缩放校准）相对清晰，但涉及分布距离等术语，需要一定背景；对程序员有直接工程启发（低成本提升推理吞吐约10%），也可做成技术号选题。)

## 一句话结论
给草稿模型调个温度，投机解码白赚10%速度

## 通俗解读
大模型逐字生成太慢，投机解码用一个小模型先猜几个词，再让大模型一次性验证，猜对就跳过。但小模型普遍“过于谦虚”：它其实猜对了首选词，却把概率压得很低，和大模型的判断不一致，导致验证时白猜、加速打折。作者不重新训练模型，只在输出后给草稿模型的概率分布“调温度”（相当于把压扁的概率重新拉开），让两者更对齐。结果接受长度最多提升约10%，几乎零成本，吞吐量同步变好。意义是：不用改模型、不用加算力，一个后处理小技巧就能让推理服务更快更省钱。

## 关键方法
核心是把“温度缩放”这个老办法用在草稿模型上：先用验证集看草稿分布和大模型分布的差距，再乘一个大于1的系数把草稿概率拉开，使首选词更突出。相当于考试的“校准分数线”，让猜题者的信心和真实对错匹配。

## 对你的启发

- **程序员视角**: 做推理服务或本地部署时，可以在草稿模型输出上加一层可调温度参数，用少量样本扫一遍找到最优值，当开关直接省成本；自动化工作流里凡是“小模型先跑、大模型复核”的链路都可套用。
- **投资视角**: 这提醒AI降本红利不只来自新模型，更来自推理层的“免费优化”，算力需求虽然长期增长，但单位token成本下降会更快，利好应用层变现，对英伟达等卖铲人则要看需求弹性是否跑赢效率提升。
- **内容视角**: 抖音钩子：“大模型变快10%，靠的不是换模型，是让它别太谦虚”——用“猜词游戏”演示投机解码，再现场调温度看速度变化，程序员视角讲推理成本，容易出爆款。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.33111v1)