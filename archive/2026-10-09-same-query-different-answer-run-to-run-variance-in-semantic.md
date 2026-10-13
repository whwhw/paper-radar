---
area: tech
created: '2026-10-13'
id: arxiv:2610.13823
score: 7.8
source: arXiv
starred: false
status: reference
summary: 同一个问题问AI，每次答案都可能不一样，基准测试跑一次根本不够。
tags:
- paper
- ai
title: 'Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing'
url: https://arxiv.org/abs/2610.13823v1
---

# Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing

- **原标题**: Same Query, Different Answer: Run-to-Run Variance in Semantic Query Processing
- **作者**: Oktie Hassanzadeh, Dharmashankar Subramanian
- **来源**: arXiv
- **发表日期**: 2026-10-09
- **原文**: [https://arxiv.org/abs/2610.13823v1](https://arxiv.org/abs/2610.13823v1)
- **AI 评分**: 7.8 / 10  (该论文属于AI工程中的LLM语义查询系统，与程序员关注的AI工程和自动化工作流高度相关；但摘要涉及benchmark术语和统计细节，对非学术读者有一定门槛；其发现的LLM输出变异性、计划放大效应和投票局限，对构建可靠AI系统、设计容错工作流以及内容创作（如讲解LLM不确定性）都有直接启发。)

## 一句话结论
同一个问题问AI，每次答案都可能不一样，基准测试跑一次根本不够。

## 通俗解读
背景：现在很多AI查询引擎靠大模型逐行判断，但评测只跑一次就下结论。方法：作者把三个主流测试集重新跑五遍，记录120万次调用，看结果变多少。发现：即使温度设0，也有0.07%到10.2%的行结果会变，个别任务高达24%；经过多步计划放大后，最终答案变化率可达三分之二。意义：一次评测不靠谱，会误判系统优劣，需要多次运行才能稳定评估。

## 关键方法
把大模型当成一个'有点随机的裁判'，重复问同一个问题多次，然后看哪些答案会变。就像让同一个老师反复批改同一份卷子，比较每次打分的差异，而不是只批一次就下结论。

## 对你的启发

- **程序员视角**: 在工程里，凡是让LLM做判断的环节（如数据清洗、分类），不能只跑一次就上线，要重复跑几次看结果是否稳定，对不稳定的行加人工审核或投票兜底。
- **投资视角**: 提醒我们：当前AI应用层的可靠性被高估，评测基准有水分。投资AI工具类公司时，要关注它们是否处理了这种随机性，这可能是产品护城河或风险点。
- **内容视角**: 抖音视频钩子：'同一个问题问AI，它每次答案都不一样？我测了120万次，结果吓人'。展示一次提问多次回答的差异对比，讲清楚为什么AI不能当唯一裁判。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.13823v1)