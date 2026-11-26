---
area: tech
created: '2026-11-26'
id: arxiv:2611.34920
score: 7.8
source: arXiv
starred: false
status: reference
summary: 多用户语音助手在共享空间任务中表现差，开放模型尤其弱，大群体更难。
tags:
- paper
- ai
title: '$μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice
  Agents'
url: https://arxiv.org/abs/2611.34920v1
---

# $μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents

- **原标题**: $μ$-Bench: Benchmarking Multi-User Task Completion in Shared Interaction Voice Agents
- **作者**: Qihao Lin, Guanxu Chen, Shuhang Zheng, Xiaoya Lu, Jingyi Yang
- **来源**: arXiv
- **发表日期**: 2026-11-25
- **原文**: [https://arxiv.org/abs/2611.34920v1](https://arxiv.org/abs/2611.34920v1)
- **AI 评分**: 7.8 / 10  (这篇论文属于AI领域，研究多用户共享空间中的语音智能体，与用户的AI工程关注点高度相关。摘要技术性较强，但概念清晰，涉及多用户协作、权限和隐私等日常场景，可以做成抖音技术号上关于AI智能体能力边界的选题。)

## 一句话结论
多用户语音助手在共享空间任务中表现差，开放模型尤其弱，大群体更难。

## 通俗解读
背景：语音助手常需同时服务多人（如家庭、会议），但现有测试只考虑单用户或简单场景。方法：作者构建μ-Bench基准，模拟多个用户各有不同目标、知识和权限，在20个领域设计100个场景（共800案例），要求助手完成所有任务并保护隐私。发现：13个语音助手中，商业系统成功率最高约65%，开源模型低于20%；诊断显示开源模型在多轮对话中难以区分和跟踪不同用户。意义：这是首个闭环多用户语音助手测试平台，揭示了当前系统的重大缺陷。

## 关键方法
用模拟用户（各有独立目标、知识和权限）与语音助手实时交互，通过工具调用和对话完成联合任务；成功需所有用户目标达成、隐私不泄露、状态正确。

## 对你的启发

- **程序员视角**: 开发多用户对话系统时，需设计用户区分和权限控制机制；可用μ-Bench思路构建测试用例，确保系统在并发交互中不混淆用户上下文。
- **投资视角**: 语音AI在复杂场景的成熟度仍低，开源模型差距大，投资应关注能解决多用户协同和隐私问题的团队。
- **内容视角**: 抖音钩子：'你家智能音箱能同时听懂全家人的指令吗？测试结果惊了！' 展示多用户语音助手的翻车现场。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.34920v1)