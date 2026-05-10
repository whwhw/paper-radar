---
area: tech
created: '2026-05-10'
id: arxiv:2605.06638
score: 7.8
source: arXiv
starred: false
status: reference
summary: 逻辑表达能力越强，RL训练LLM的推理深度越难，需更多算力，但迁移效果更好。
tags:
- paper
- ai
title: Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key
url: https://arxiv.org/abs/2605.06638v1
---

# Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key

- **原标题**: Can RL Teach Long-Horizon Reasoning to LLMs? Expressiveness Is Key
- **作者**: Tianle Wang, Zhaoyang Wang, Guangchen Lan, Xinpeng Wei, Sipeng Zhang
- **来源**: arXiv
- **发表日期**: 2026-05-07
- **原文**: [https://arxiv.org/abs/2605.06638v1](https://arxiv.org/abs/2605.06638v1)
- **AI 评分**: 7.8 / 10  (核心领域AI，方法论（RL+LLM推理）对技术内容创作有启发，但逻辑表达式的细节可能稍显抽象。)

## 一句话结论
逻辑表达能力越强，RL训练LLM的推理深度越难，需更多算力，但迁移效果更好。

## 通俗解读
背景：强化学习（RL）可训练大语言模型（LLM）进行复杂推理，但推理难度如何影响训练效率？作者发明了ScaleLogic框架，像搭积木一样控制逻辑复杂度（从简单“如果-那么”到含“且、或、非”的高阶逻辑）和推理步数（深度）。方法：让LLM在不同逻辑和深度下用RL学推理，记录训练所用算力。发现：训练算力随推理深度呈幂律增长（T∝D^γ），且逻辑越复杂，增长指数γ就越大（1.04→2.60）。意义：训练数据的内容比训练量更重要——复杂逻辑场景下的训练能更高效迁移到真实数学题中（性能提升最高10.66分）。

## 关键方法
ScaleLogic框架：通过合成逻辑推理任务独立控制推理深度和逻辑表达力，模拟从简单if-then到一阶逻辑的难度，用于系统地测量RL训练算力与难度的关系。

## 对你的启发

- **程序员视角**: 工程中若需LLM处理长链推理（如代码生成或漏洞修复），应考虑先用高表达力逻辑（如包含and/or/not）的任务进行预训练或课程学习，可能比单纯增加数据量更省算力。
- **投资视角**: 该论文显示AI模型能力与任务复杂度呈幂律关系，表明提升推理深度需要指数级算力。这对LLM推理优化公司（如算法改进）利好，但对依赖简单扩展规模的公司是风险信号。
- **内容视角**: 抖音可做“AI推理的天花板”系列：用动画展示简单if-then逻辑到复杂逻辑的推理链爆炸，解释为何数学题难倒AI，结尾抛出“如何让AI像人一样思考？”。钩子：“你的数学题AI解不了？因为逻辑太‘深’了！”

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.06638v1)