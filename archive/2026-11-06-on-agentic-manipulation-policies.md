---
area: tech
created: '2026-11-09'
id: arxiv:2611.09892
score: 8.4
source: arXiv
starred: false
status: reference
summary: 通用AI模型直接控制机械臂，零样本成功率远超专用机器人策略。
tags:
- paper
- ai
title: On Agentic Manipulation Policies
url: https://arxiv.org/abs/2611.09892v1
---

# On Agentic Manipulation Policies

- **原标题**: On Agentic Manipulation Policies
- **作者**: Chen Chen, Omid Bagherieh, Naveen Nikamanth Appiah Balaji, Jesse T. Gonzalez, Negin Heravi
- **来源**: arXiv
- **发表日期**: 2026-11-06
- **原文**: [https://arxiv.org/abs/2611.09892v1](https://arxiv.org/abs/2611.09892v1)
- **AI 评分**: 8.4 / 10  (论文属于 AI 与机器人交叉领域，核心用通用 AI 模型直接控制机械臂，与用户关注的 AI 工程和自动化工作流高度匹配；结论清晰且反常识，适合做成科普内容，对搭建 Agent 系统也有直接启发。)

## 一句话结论
通用AI模型直接控制机械臂，零样本成功率远超专用机器人策略。

## 通俗解读
机器人操作通常依赖专门训练的专用策略（如视觉-语言-动作模型VLA或世界-动作模型WAM），需要大量演示数据且任务特定。本文提出智能体操作策略（AMP），让通用AI模型直接命令机械臂，根据任务进展动态调整动作。作者构建了AMP1参考框架，无需演示或任务训练，在RoboLab-120基准上零样本达到85.6%成功率，而VLA和WAM分别只有49.2%和42.9%。在真实世界108次试验中成功104次，失败率降低20倍和15倍。智能体还自创策略，如寻找隐藏物体、使用工具、校准相机。加入持久记忆后，失败率进一步降低4.6倍。表明AMP比专用策略更通用、更鲁棒。

## 关键方法
AMP1使用通用AI模型（如大语言模型）作为控制器，直接输出机械臂动作指令，无需预训练技能库；通过闭环反馈适应任务变化，并可选地加入记忆存储来积累经验。

## 对你的启发

- **程序员视角**: 在自动化工作流中，可以用通用LLM作为决策核心，替代硬编码的专用逻辑，通过记忆模块积累经验，提升鲁棒性和泛化能力。
- **投资视角**: AMP的成功暗示通用AI模型在机器人领域的潜力，可能加速AI与机器人融合，关注相关AI基础设施和机器人公司的长期价值。
- **内容视角**: 抖音钩子：『不用教机器人，AI自己学会抓东西！成功率85% vs 50%，通用模型碾压专用策略』，演示零样本操作和自创策略的趣味片段。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.09892v1)