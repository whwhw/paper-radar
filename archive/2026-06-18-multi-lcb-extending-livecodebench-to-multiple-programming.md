---
area: tech
created: '2026-06-20'
id: arxiv:2606.20517
score: 8.4
source: arXiv
starred: false
status: reference
summary: 大模型写Python代码很溜，但换成其他语言就拉胯了。
tags:
- paper
- ai
title: 'Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages'
url: https://arxiv.org/abs/2606.20517v1
---

# Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages

- **原标题**: Multi-LCB: Extending LiveCodeBench to Multiple Programming Languages
- **作者**: Maria Ivanova, Pavel Zadorozhny, Rodion Levichev, Ivan Petrov, Adamenko Pavel
- **来源**: arXiv
- **发表日期**: 2026-06-18
- **原文**: [https://arxiv.org/abs/2606.20517v1](https://arxiv.org/abs/2606.20517v1)
- **AI 评分**: 8.4 / 10  (核心AI领域，涉及代码生成评估，对程序员（尤其是全栈和多语言开发者）有直接相关性；摘要清晰，没有复杂公式，容易理解；可以启发关于模型在多语言环境下表现的思考，对技术内容创作有潜力。)

## 一句话结论
大模型写Python代码很溜，但换成其他语言就拉胯了。

## 通俗解读
背景：LiveCodeBench是测试大模型写代码能力的常用基准，但只测Python。方法：我们做了Multi-LCB，把Python题目翻译成12种语言（如Java、C++），保持评测标准一致。发现：测试24个模型后发现，模型在Python上表现很好，但切换到其他语言时准确率大幅下降，存在“Python过拟合”和语言特定污染问题。意义：大模型的多语言编码能力被高估，实际工程中需要更全面的评测。

## 关键方法
将Python代码题翻译成12种语言，用相同测试用例和评分标准进行跨语言评估。

## 对你的启发

- **程序员视角**: 如果你做多语言项目，别假设同一个LLM能同样好地处理所有语言代码，可能需要为不同语言微调或选择不同模型。
- **投资视角**: 这暴露了当前代码LLM的短板——多数模型实际只擅长Python，这对依赖多语言代码生成的AI产品是个风险，投资时应关注模型真正的通用性。
- **内容视角**: 可以做个对比视频：让GPT-4和Claude写同一道题的不同语言版本，展示错误率差异，标题用“你的AI助手其实只会一种语言？”吸引眼球。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.20517v1)