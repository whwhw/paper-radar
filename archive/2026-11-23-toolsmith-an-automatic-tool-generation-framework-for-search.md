---
area: tech
created: '2026-11-24'
id: arxiv:2611.31198
score: 8.4
source: arXiv
starred: false
status: reference
summary: 让AI搜索代理自己造工具，比人工预设的工具库更灵活、更强大。
tags:
- paper
- ai
title: 'ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents'
url: https://arxiv.org/abs/2611.31198v1
---

# ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents

- **原标题**: ToolSmith: An Automatic Tool-Generation Framework for Multimodal Search Agents
- **作者**: Rui Sun, Junhua Huang, Luca Zancato, Md Mofijul Islam, Kai-Wei Chang
- **来源**: arXiv
- **发表日期**: 2026-11-23
- **原文**: [https://arxiv.org/abs/2611.31198v1](https://arxiv.org/abs/2611.31198v1)
- **AI 评分**: 8.4 / 10  (这篇论文直接落在 AI 工程领域，讲的是多模态搜索智能体的自动工具生成，和用户关注的 AI 工程、自动化工作流高度相关。概念清晰、有'像人类临时造工具'的日常类比，可以迁移到智能体工程和内容创作选题。)

## 一句话结论
让AI搜索代理自己造工具，比人工预设的工具库更灵活、更强大。

## 通俗解读
多模态搜索代理原本靠一套人工编写的工具库来回答问题，但遇到新情况就束手无策。ToolSmith受人类“缺工具就自己造”的启发，让AI在基础工具上自动生成并复用新模块。在多个测试中，它持续超越原工具库，且模型越大提升越明显，说明这种方法能随模型规模扩展。意义在于：AI代理能自我进化工具，不再依赖人工维护。

## 关键方法
把工具库看作积木：基础工具是标准件，AI遇到新任务时，用现有积木拼出新工具（自动生成代码），并保存下来供以后复用。就像程序员写函数库，越用越丰富。

## 对你的启发

- **程序员视角**: 可以在自动化工作流中引入“工具生成”机制：当现有API不够用时，让AI动态生成小函数并缓存复用，提升系统适应性。
- **投资视角**: 这强化了AI代理自主进化的趋势，利好AI基础设施和自动化赛道；长期看，能降低人工维护成本的公司更具壁垒。
- **内容视角**: 抖音钩子：“AI自己造工具？程序员要失业了吗？——解读ToolSmith让代理自我升级的魔法。”

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.31198v1)