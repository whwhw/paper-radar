---
area: tech
created: '2026-08-12'
id: arxiv:2608.11095
score: 8.8
source: arXiv
starred: false
status: reference
summary: AI编码提示词无限膨胀，加注释能解决99%冗余。
tags:
- paper
- ai
title: Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding
url: https://arxiv.org/abs/2608.11095v1
---

# Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding

- **原标题**: Why Does CLAUDE.md Keep Growing? Catastrophic Remembering in Agentic Coding
- **作者**: Kushal Chakrabarti
- **来源**: arXiv
- **发表日期**: 2026-08-11
- **原文**: [https://arxiv.org/abs/2608.11095v1](https://arxiv.org/abs/2608.11095v1)
- **AI 评分**: 8.8 / 10  (AI工程核心领域，关于智能体编码中提示词文件膨胀的实证研究，对程序员有直接启发；概念清晰但包含统计术语，需通俗解读；工程实践和内容创作素材潜力大。)

## 一句话结论
AI编码提示词无限膨胀，加注释能解决99%冗余。

## 通俗解读
背景：程序员用AI写代码时，会维护一个说明文件（如CLAUDE.md），但文件越来越长，删不掉。方法：研究者分析1867个仓库中的247694条指令，发现提示词每提交一次就增加4.9条，且越老的指令越难删。进一步，他们提出“提示词注释”（类似代码注释）来编码推理过程。发现：加上注释后，冗余指令减少99.3%，真实任务表现提升23.1%。意义：给AI的指令文件加注释，能防止“灾难性记忆”，让AI更稳定。

## 关键方法
提示词注释：在指令后添加解释为什么需要这条指令，像代码注释一样，防止指令被误删或过度累积。

## 对你的启发

- **程序员视角**: 可以在项目实践中，给CLAUDE.md或AI提示词添加注释，明确每条指令的意图，定期清理冗余，提升AI生成代码的质量。
- **投资视角**: 该研究揭示AI开发流程中的痛点，提示AI工具链（如提示词管理、记忆优化）有市场机会，可能影响AI工程化赛道的投资判断。
- **内容视角**: 抖音视频钩子：“AI提示词也会‘内存泄漏’？三招搞定无限膨胀” 展示如何用注释优化AI提示词，吸引程序员和AI爱好者。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.11095v1)