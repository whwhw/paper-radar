---
area: tech
created: '2026-06-30'
id: arxiv:2606.30587
score: 8.1
source: arXiv
starred: false
status: reference
summary: 大模型查代码漏洞时，跟人一样容易被上下文带偏，黑客可借此绕过检测。
tags:
- paper
- ai
title: 'Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based
  Code Vulnerability Detection'
url: https://arxiv.org/abs/2606.30587v1
---

# Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection

- **原标题**: Words Speak Louder Than Code: Investigating Cognitive Heuristics in LLM-Based Code Vulnerability Detection
- **作者**: Asif Shahriar, Hongyu Cai, Hadjer Benkraouda, Gang Wang, Z. Berkay Celik
- **来源**: arXiv
- **发表日期**: 2026-06-29
- **原文**: [https://arxiv.org/abs/2606.30587v1](https://arxiv.org/abs/2606.30587v1)
- **AI 评分**: 8.1 / 10  (本文探讨LLM在漏洞检测中受认知启发影响，属于AI核心领域，对程序员理解AI局限性和内容创作都有启发；概念清晰，没有复杂公式，容易理解；可启发程序员如何优化AI工作流，或为技术自媒体提供”AI幻觉新形式”的选题。)

## 一句话结论
大模型查代码漏洞时，跟人一样容易被上下文带偏，黑客可借此绕过检测。

## 通俗解读
背景：程序员用大模型（LLM）自动找代码漏洞，但研究发现它像人一样有认知偏见。方法：论文设计一个实验，代码不变，只改周围文字（比如作者名、任务描述、之前的结果），看模型判断是否变化。发现：所有测试的大模型都受影响，平均33%的判决被任务描述带偏；越需要理解语义的漏洞越容易被忽悠。意义：黑客可以利用这种偏见，通过构造上下文让模型漏报漏洞，比如把之前检测出的97%漏洞隐藏掉。

## 关键方法
控制变量实验：保持代码不变，仅改变提示中的作者名（光环效应）、任务目标（框架效应）或前人分析结果（锚定效应），观察模型判决变化。

## 对你的启发

- **程序员视角**: 写代码检测工具时，不能只依赖单个大模型判断，要结合静态分析或多次不同上下文提示取多数票，避免被偏见误导。
- **投资视角**: AI安全公司若只靠大模型做漏洞检测，产品有被攻击的风险；可关注融合多种检测方式的企业，或投资对抗性防御技术。
- **内容视角**: 抖音可以拍“大模型查Bug居然会被骗？”，做个实验演示：给AI同一段代码，换个说法它就判安全，吸引程序员围观讨论。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.30587v1)