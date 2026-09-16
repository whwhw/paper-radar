---
area: tech
created: '2026-09-16'
id: arxiv:2609.17516
score: 7.8
source: arXiv
starred: false
status: reference
summary: 让AI先自问'我到底知不知道'，再决定答不答，错误率降三成。
tags:
- paper
- ai
title: When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control
url: https://arxiv.org/abs/2609.17516v1
---

# When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control

- **原标题**: When Should LLMs Abstain? Chain-of-Self-Questioning for Selective Risk Control
- **作者**: Ali Şenol
- **来源**: arXiv
- **发表日期**: 2026-09-15
- **原文**: [https://arxiv.org/abs/2609.17516v1](https://arxiv.org/abs/2609.17516v1)
- **AI 评分**: 7.8 / 10  (这篇论文提出了一种让LLM在不确定时主动'弃权'的提示框架，属于AI工程领域，可直接用于构建更可靠的生产系统，尤其适合程序员和内容创作者讲解。但摘要包含较多实验细节和术语，通俗度中等，需适当简化才能做成科普内容。)

## 一句话结论
让AI先自问'我到底知不知道'，再决定答不答，错误率降三成。

## 通俗解读
背景：大模型经常一本正经地胡说八道，明明没把握却硬答。方法：作者设计'自问链'，让模型答题前先自问几个问题，评估自己有没有足够依据，没把握就选择不答（弃权）。发现：在TruthfulQA测试集上，加上这个'自问'机制后，11个模型的错误承诺率平均从13.1%降到8.9%，而答对率反而从86.9%升到89.7%。意义：告诉AI'不会就别装会'，能让它在高风险场景下更可靠，宁可说'我不知道'也别乱答。

## 关键方法
就像考试前先问自己：这题我见过吗？有依据吗？如果答案是'没有'，就交白卷而不是瞎蒙。CoSQ让模型在回答前生成几个自检问题，用自我评估结果决定是否作答，并可通过阈值调节'答多少题'和'答多准'的平衡。

## 对你的启发

- **程序员视角**: 可以在AI Agent或RAG系统里加一层'自检弃权'逻辑：先让模型自评证据是否充分，不足就触发人工审核或拒答，能显著降低幻觉带来的线上事故。
- **投资视角**: 这强化了'AI可靠性'是落地关键赛道的判断——谁能解决幻觉和过度自信，谁就能拿下金融、医疗等高价值场景，相关工具链和评测标准值得关注。
- **内容视角**: 抖音钩子：'AI为什么总胡说八道？科学家让它学会说我不知道，错误率直接降三成'——用考试蒙题类比讲清'自问链'，结尾问观众敢不敢让AI拒答。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2609.17516v1)