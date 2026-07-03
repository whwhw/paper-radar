---
area: tech
created: '2026-07-03'
id: arxiv:2607.02512
score: 8.1
source: arXiv
starred: false
status: reference
summary: 用 AI 编译器把自然语言需求转成小型程序，比直接调大模型更省钱、更快、还能本地跑。
tags:
- paper
- ai
title: 'Program-as-Weights: A Programming Paradigm for Fuzzy Functions'
url: https://arxiv.org/abs/2607.02512v1
---

# Program-as-Weights: A Programming Paradigm for Fuzzy Functions

- **原标题**: Program-as-Weights: A Programming Paradigm for Fuzzy Functions
- **作者**: Wentao Zhang, Liliana Hotsko, Woojeong Kim, Pengyu Nie, Stuart Shieber
- **来源**: arXiv
- **发表日期**: 2026-07-02
- **原文**: [https://arxiv.org/abs/2607.02512v1](https://arxiv.org/abs/2607.02512v1)
- **AI 评分**: 8.1 / 10  (属于AI核心领域（把LLM能力变成本地可执行程序），概念清晰但涉及编译器/适配器等术语需要简单类比；对程序员做AI工具自动化工作流有直观启发，内容也适合做技术号脚本。)

## 一句话结论
用 AI 编译器把自然语言需求转成小型程序，比直接调大模型更省钱、更快、还能本地跑。

## 通俗解读
平时写代码，有些任务很难用规则写清楚，比如识别重要日志、修复坏掉的 JSON 或者按意图排序搜索结果。现在大家常用大语言模型 API 来做，但每次都调用很贵又慢，还不能离线。这篇论文提出“模糊函数编程”：先把自然语言需求交给一个编译器（4B 参数），根据需求生成一个小程序（权重），然后让一个很小的解释器（0.6B 参数）执行它。就像一个翻译官把需求变成一张简单的“乐谱”，然后一个小乐队就能演奏，效果和直接请 32 个大乐队一样好，但内存只用了 1/50，每秒还能处理 30 个任务。

## 关键方法
先训练一个编译器（4B 参数），在 1000 万样本的数据集上学习如何把自然语言需求转成参数高效的适配器，然后冻结一个轻量解释器（0.6B 参数）执行这些适配器。

## 对你的启发

- **程序员视角**: 可以不依赖大模型 API，本地实现模糊逻辑功能，比如写个插件自动分类用户反馈或修复数据，成本极低。
- **投资视角**: AI 从“每次调用付钱”转向“一次编译多次使用”的模式，可能颠覆 API 计费逻辑，关注边缘 AI 和本地模型公司的机会。
- **内容视角**: 可以做个视频标题：“为什么你不需要再买 API 额度了？AI 编程新范式，省钱又高效”，用代码对比展示直接调大模型 vs 本地小程序的成本差异。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.02512v1)