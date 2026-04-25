---
area: tech
created: '2026-04-25'
id: arxiv:2604.21911
score: 7.7
source: arXiv
starred: false
status: reference
summary: AI看图时太信文字提示，导致幻觉，新方法用偏好训练减少错误。
tags:
- paper
- ai
title: 'When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs'
url: https://arxiv.org/abs/2604.21911v1
---

# When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs

- **原标题**: When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs
- **作者**: Pegah Khayatan, Jayneel Parekh, Arnaud Dapogny, Mustafa Shukor, Alasdair Newson
- **来源**: arXiv
- **发表日期**: 2026-04-23
- **原文**: [https://arxiv.org/abs/2604.21911v1](https://arxiv.org/abs/2604.21911v1)
- **AI 评分**: 7.7 / 10  (属于核心AI领域，语言模型的幻觉问题对程序员有工程启发；摘要清晰易懂但涉及DPO等技术细节；可启发内容创作（讲解AI幻觉）或投资判断（评估模型可靠性）。)

## 一句话结论
AI看图时太信文字提示，导致幻觉，新方法用偏好训练减少错误。

## 通俗解读
背景：现在的AI看图模型（LVLM）虽然很厉害，但经常“幻觉”——编造图片里没有的东西。以前大家以为是AI眼睛不行，或者语言模型太强。方法：研究者做了个测试集（HalluScope），发现幻觉主要是因为AI太依赖文字提示和背景知识，特别是用户指令里的信息。他们又提出新方法（HalluVL-DPO），像教小孩一样，给AI看正确和错误答案，让它学会优先看图片再回答。结果：优化后的AI幻觉大大减少，其他能力也没变差。意义：提示词会覆盖视觉，所以要多管齐下纠正AI。

## 关键方法
HalluVL-DPO：用偏好优化训练，给AI一对正确/错误答案，让它学会选择基于图片的回应。

## 对你的启发

- **程序员视角**: 在构建多模态AI应用时，可以加入类似DPO的偏好优化模块，优先校验视觉输入，减少提示词过拟。
- **投资视角**: 该发现暗示多模态算法的可靠性瓶颈在文本-视觉对齐，投资方向可关注偏好优化和反幻觉技术。
- **内容视角**: 抖音/小红书标题：《AI看照片也会骗人？教你用新方法让它闭嘴》。钩子：测测你的AI有没有被提示词洗脑。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2604.21911v1)