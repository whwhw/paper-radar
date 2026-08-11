---
area: tech
created: '2026-08-11'
id: arxiv:2608.08570
score: 8.4
source: arXiv
starred: false
status: reference
summary: 把模型答错的题变成新教材，能让AI编程能力再涨6.6个百分点。
tags:
- paper
- ai
title: 'FailForge: Distilling Procedural Competence from Persistent Failures into
  Code Agents'
url: https://arxiv.org/abs/2608.08570v1
---

# FailForge: Distilling Procedural Competence from Persistent Failures into Code Agents

- **原标题**: FailForge: Distilling Procedural Competence from Persistent Failures into Code Agents
- **作者**: Dongyi Lv, Fushun E, Aichen Cai, Liang Huang, Ya Zhang
- **来源**: arXiv
- **发表日期**: 2026-08-09
- **原文**: [https://arxiv.org/abs/2608.08570v1](https://arxiv.org/abs/2608.08570v1)
- **AI 评分**: 8.4 / 10  (论文聚焦AI代码智能体训练，属于用户核心领域AI/科技，且对全栈程序员有直接可迁移启发（如将失败反馈转化为技能提升）。概念清晰，虽涉及机器学习术语但易于理解，且能启发内容创作（如AI工具讲解）。)

## 一句话结论
把模型答错的题变成新教材，能让AI编程能力再涨6.6个百分点。

## 通俗解读
训练AI写代码时，常用“淘汰错题”方法：只保留答对的题，扔掉错题。但错题往往是最难、最有价值的。FailForge让AI自己分析错题，总结成“答题技巧”，再用技巧引导它重做一遍。如果重做成功，就把这道题连同技巧一起加入训练数据。训练时去掉技巧，让AI内化这些能力。结果，AI能答对26%原本会错的题，编程水平（SWE-bench指标）提升6.6%，尤其是难题提升明显。

## 关键方法
对每次失败，用大模型诊断错误，生成简短技能说明，并注入上下文重试；成功则把技能一并加入训练数据，但训练时隐藏技能。

## 对你的启发

- **程序员视角**: 可以借鉴到工程中：用LLM自动分析测试失败日志，生成修复建议，再让AI二次提交，提高自动化修复率。
- **投资视角**: 验证了“失败数据”的价值，AI训练数据利用效率提升是关键方向，利好数据服务或合成数据公司。
- **内容视角**: 标题：AI模型的“错题本”居然能逆袭？3分钟看懂如何让AI越挫越勇！

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.08570v1)