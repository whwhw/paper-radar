---
area: tech
created: '2026-11-02'
id: arxiv:2610.42039
score: 8.4
source: arXiv
starred: false
status: reference
summary: 同一个戒烟问题，LLM对青少年和成人答案不同，给青少年的处方药信息少32-67个百分点。
tags:
- paper
- ai
title: 'Same Question, Different Answers: Auditing Persona-Dependent Variation in
  Six LLMs on Smoking-Cessation Advice'
url: https://arxiv.org/abs/2610.42039v1
---

# Same Question, Different Answers: Auditing Persona-Dependent Variation in Six LLMs on Smoking-Cessation Advice

- **原标题**: Same Question, Different Answers: Auditing Persona-Dependent Variation in Six LLMs on Smoking-Cessation Advice
- **作者**: Artin Yousefi, Aizierjiang Aiersilan, Lorien C Abroms, David A Broniatowski
- **来源**: arXiv
- **发表日期**: 2026-10-30
- **原文**: [https://arxiv.org/abs/2610.42039v1](https://arxiv.org/abs/2610.42039v1)
- **AI 评分**: 8.4 / 10  (这篇论文直接落在用户的核心AI领域，审视日常医疗场景中的LLM行为，对AI工程和内容创作都非常相关。概念用通俗语言解释（人设、事实底线），而且结论可以迁移——提示词干预在不同模型上迁移效果不同，对构建AI工作流或做技术账号视频都是很好的可操作启发。)

## 一句话结论
同一个戒烟问题，LLM对青少年和成人答案不同，给青少年的处方药信息少32-67个百分点。

## 通俗解读
背景：数亿人向AI聊天机器人问健康建议，但不同人得到的建议是否一样？方法：研究者用6个主流LLM，对12种不同人设（年龄、自述专业度、吸烟史）问4个戒烟问题，共2880条回答。发现：模型会看人下菜碟——对青少年人设，提到FDA批准处方戒烟药的概率比成人低32-67个百分点；6个模型中有5个对自称医疗专家的人设给出更少事实。意义：AI健康建议存在人设偏差，且一个模型上有效的提示词不能直接套用到另一个模型。

## 关键方法
用12种人设（如青少年/成人、自称专家/无专业背景）组合提问，统计每个模型回答中关键医学事实的出现率，再测试一个'事实底线'系统提示词能否缩小差异。

## 对你的启发

- **程序员视角**: 做AI应用时，别假设同一个prompt在不同模型上效果一致；关键事实覆盖需要按用户属性（如年龄）做条件化底线，而不是一刀切。
- **投资视角**: AI医疗健康是巨大市场，但模型行为不一致和监管风险（如对未成年人建议）是落地障碍，投资时需关注可审计性和合规性。
- **内容视角**: 抖音钩子：'我问了6个AI同一个戒烟问题，结果它们对青少年和成人说的完全不一样！' 展示AI健康建议的隐藏偏差。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.42039v1)