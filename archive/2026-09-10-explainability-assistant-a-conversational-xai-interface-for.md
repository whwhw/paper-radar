---
area: tech
created: '2026-09-13'
id: arxiv:2609.11860
score: 8.0
source: arXiv
starred: false
status: reference
summary: 用大模型聊天界面解释能耗预测模型，准确率94%，专家全票选它。
tags:
- paper
- ai
title: 'Explainability Assistant: A Conversational XAI Interface for Interpreting
  Energy Consumption Models'
url: https://arxiv.org/abs/2609.11860v1
---

# Explainability Assistant: A Conversational XAI Interface for Interpreting Energy Consumption Models

- **原标题**: Explainability Assistant: A Conversational XAI Interface for Interpreting Energy Consumption Models
- **作者**: Rodion Krjutškov, Eduard Barbu, Nikos Sakkas, Sofia Yfanti
- **来源**: arXiv
- **发表日期**: 2026-09-10
- **原文**: [https://arxiv.org/abs/2609.11860v1](https://arxiv.org/abs/2609.11860v1)
- **AI 评分**: 8.0 / 10  (该论文结合了AI可解释性和LLM函数调用，属于用户核心的AI领域，且涉及能源领域但可迁移到Web3投资解释等场景。摘要清晰，用对比和准确率数据说明，容易理解，对程序员的AI工程实践和内容创作（讲解XAI+LLM）都有启发。)

## 一句话结论
用大模型聊天界面解释能耗预测模型，准确率94%，专家全票选它。

## 通俗解读
背景：现在预测楼宇耗电用的是很复杂的AI模型，像黑箱一样，管理员看不懂它为什么给出某个预测。方法：以前有可解释AI面板，但要懂技术才会用；本文做了个聊天助手，借助大模型自己会"调用工具"的能力，用户用大白话提问，它就去调相应的解释功能。发现：意图识别准确率从76.8%升到94%，不用专门训练就能适配不同模型任务。意义：能源专家对比测试后觉得更好用，全员愿意在真实工作中使用。

## 关键方法
关键不在自己写语法规则，而是让大模型当"调度员"：用户问一句话，模型判断该调用哪个解释工具（如看哪个特征影响最大），再把结果翻译成人话。相当于把死板的菜单点餐，换成了会理解你的服务员。

## 对你的启发

- **程序员视角**: 做内部工具/可观测性面板时，别只堆图表，加一层LLM function-calling做自然语言入口，让非技术同事直接问"昨天这指标为什么掉"，复用现有API即可，无需重训模型。
- **投资视角**: 说明AI落地正从"模型能力"转向"人机接口"，能降低企业用AI的门槛；能源管理这类垂直场景的AI解释性需求会催生工具层机会，可关注能源SaaS+AI交互方向。
- **内容视角**: 钩子：《把黑箱AI变成会聊天的同事——我用大模型给公司监控面板加了个嘴》。演示对比传统仪表盘vs一句大白话提问，突出"不懂技术也能问AI为什么"。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2609.11860v1)