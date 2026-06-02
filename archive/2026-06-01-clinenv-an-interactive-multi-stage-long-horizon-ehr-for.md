---
area: tech
created: '2026-06-02'
id: arxiv:2606.02568
score: 8.1
source: arXiv
starred: false
status: reference
summary: 模拟真实医生看病过程的新测试显示，最佳AI模型也只拿到31分（满分100），诊断还行但治疗决策很差。
tags:
- paper
- ai
title: 'ClinEnv: An Interactive Multi-Stage Long Horizon EHR Environment for Agents'
url: https://arxiv.org/abs/2606.02568v1
---

# ClinEnv: An Interactive Multi-Stage Long Horizon EHR Environment for Agents

- **原标题**: ClinEnv: An Interactive Multi-Stage Long Horizon EHR Environment for Agents
- **作者**: Yuxing Lu, Yushuhong Lin, Wenqi Shi, J. Ben Tamo, Xukai Zhao
- **来源**: arXiv
- **发表日期**: 2026-06-01
- **原文**: [https://arxiv.org/abs/2606.02568v1](https://arxiv.org/abs/2606.02568v1)
- **AI 评分**: 8.1 / 10  (该论文属于AI领域，与用户核心领域高度相关；摘要概念清晰，但涉及医疗决策细节，需要一定背景理解；对AI工程中多智能体协作和长序列决策有启发，可转化为技术号内容。)

## 一句话结论
模拟真实医生看病过程的新测试显示，最佳AI模型也只拿到31分（满分100），诊断还行但治疗决策很差。

## 通俗解读
背景：现有医疗AI测试像选择题，但真实医生需要一步步收集信息、做不可逆决策，过程更重要。方法：研究团队开发了ClinEnv系统，把真实住院病历变成多阶段模拟，AI模型像医生一样依次查询四个专家（如检查、用药等）再做决定，根据诊断和流程双维度评分。发现：最强模型决策F1仅0.31，诊断恢复（0.51）远好于管理行动（0.17），而且后期阶段表现更差，还会重复查询。意义：ClinEnv暴露了单纯看结果会忽略的信息获取缺陷，为提升AI临床推理提供了新检验方法。

## 关键方法
多阶段纵向住院模拟：自动将病历拆解为有序决策阶段，每个阶段模型必须主动查询四个专业代理（检查、用药、操作、诊断）后做出决策，评分同时考量决策结果（本体匹配）和过程质量（如查询效率）。

## 对你的启发

- **程序员视角**: 可以借鉴这种多阶段交互式评测框架来测试AI工作流，比如自动拆解复杂任务为子步骤，每个步骤验证中间决策质量，避免只看最终结果。
- **投资视角**: 该测试暴露了当前医疗AI在治疗决策上的严重短板，提示投资应关注能否在真实临床流程中表现稳定，而非仅看诊断准确率。
- **内容视角**: 抖音可用“医生AI考试翻车现场”作标题，对比看病选择题满分的大模型在真实模拟中只拿31分，引发对AI可靠性的讨论。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.02568v1)