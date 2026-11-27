---
area: tech
created: '2026-11-27'
id: arxiv:2611.34875
score: 7.8
source: arXiv
starred: false
status: reference
summary: AI 编程助手多改的代码主要是测试和文档，真正的代码其实和人类开发者一样必要。
tags:
- paper
- ai
title: How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded
  Edits in Repository-Level Agent Patches
url: https://arxiv.org/abs/2611.34875v1
---

# How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches

- **原标题**: How Much Do Coding Agents Over-Edit, and Why? An Empirical Study of Unneeded Edits in Repository-Level Agent Patches
- **作者**: Aakash Goel, Benjamin Steenhoek, Yu Hu
- **来源**: arXiv
- **发表日期**: 2026-11-25
- **原文**: [https://arxiv.org/abs/2611.34875v1](https://arxiv.org/abs/2611.34875v1)
- **AI 评分**: 7.8 / 10  (直接命中AI工程与自动化工作流核心议题，对用AI编码代理的程序员有极强实操价值；但DRA方法、精确率/召回率等指标偏工程学术，需要一定背景才能读懂。)

## 一句话结论
AI 编程助手多改的代码主要是测试和文档，真正的代码其实和人类开发者一样必要。

## 通俗解读
背景：AI 编程助手生成的补丁（代码修改）通常比人类开发者的大，大家以为它在“过度编辑”。方法：作者提出 DRA 方法，回放 AI 的修改过程，逐块撤销并重新运行测试，判断每块修改是否必要。发现：在 SWE-bench 上，AI 多改的 61% 是测试、13% 是文档，代码必要性平均甚至略高于人类；只有 11% 的代码修改是不必要的，其中 89% 会改变行为。意义：AI 编程助手没有想象中那么“浪费”，但仍有少量不必要的代码修改，建议评测时报告代码必要性，并通过训练和工具层面修剪。

## 关键方法
DRA 方法：回放 AI 修改轨迹，把最终补丁拆成小块，逐一撤销并重新运行测试，判断每块是否必要。类似把一篇文章的每个段落删掉，看文章是否还通顺。

## 对你的启发

- **程序员视角**: 在 CI 流程中加入类似 DRA 的自动修剪步骤，用测试验证每块修改的必要性，可减少 11% 的无用代码，但要注意精度只有 46%，可能误删有用代码。
- **投资视角**: AI 编程工具的效率被低估了，实际代码质量不差，这对 AI 编程赛道是利好；但评测基准需要改进，否则会误导投资判断。
- **内容视角**: 抖音钩子：“AI 写代码比你还啰嗦？实测发现多写的都是测试和文档，代码本身很精简！”

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.34875v1)