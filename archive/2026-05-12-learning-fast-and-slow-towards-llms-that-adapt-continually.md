---
area: tech
created: '2026-05-13'
id: arxiv:2605.12484
score: 8.1
source: arXiv
starred: false
status: reference
summary: LLM学习不该只改参数，结合上下文优化效率高3倍，不忘旧知识。
tags:
- paper
- ai
title: 'Learning, Fast and Slow: Towards LLMs That Adapt Continually'
url: https://arxiv.org/abs/2605.12484v1
---

# Learning, Fast and Slow: Towards LLMs That Adapt Continually

- **原标题**: Learning, Fast and Slow: Towards LLMs That Adapt Continually
- **作者**: Rishabh Tiwari, Kusha Sareen, Lakshya A Agrawal, Joseph E. Gonzalez, Matei Zaharia
- **来源**: arXiv
- **发表日期**: 2026-05-12
- **原文**: [https://arxiv.org/abs/2605.12484v1](https://arxiv.org/abs/2605.12484v1)
- **AI 评分**: 8.1 / 10  (核心AI领域，解释了快慢框架和持续学习，通俗易懂，程序员可借鉴思路用于模型微调或Prompt工程。)

## 一句话结论
LLM学习不该只改参数，结合上下文优化效率高3倍，不忘旧知识。

## 通俗解读
大语言模型学习新任务时，常用方法更新模型参数，但这会让模型忘记以前学的能力。人类学习有快慢系统：快系统（如直觉）和慢系统（如深思）。这篇论文提出“快慢学习框架”：把模型参数当慢权重，把输入上下文当快权重。快权重通过文本反馈快速吸收任务信息，慢权重保持通用能力。实验表明，这种训练比纯参数更新高效3倍，学得更好，且遗忘少70%。

## 关键方法
Fast-Slow Training (FST)：模型参数为慢权重，优化的上下文（如提示词）为快权重，两者交替更新。

## 对你的启发

- **程序员视角**: 可以在多智能体系统中用此框架：每个智能体维护慢权重（通用能力）和快权重（当前任务上下文），动态切换任务时无需重训模型。
- **投资视角**: 持续学习能力降低模型迭代成本，利好AI公司如OpenAI、Anthropic，尤其是需要长期维护模型版本的企业。
- **内容视角**: 制作抖音视频标题《ChatGPT新训练法：效率提升3倍，再也不怕它忘事》，解释AI如何像人一样快慢结合，吸引程序员和科技爱好者。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.12484v1)