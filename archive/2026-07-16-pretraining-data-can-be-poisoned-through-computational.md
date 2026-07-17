---
area: tech
created: '2026-07-17'
id: arxiv:2607.15267
score: 8.1
source: arXiv
starred: false
status: reference
summary: 用评论区发帖就能污染AI训练数据，让模型学坏还很难查出来。
tags:
- paper
- ai
title: Pretraining Data Can Be Poisoned through Computational Propaganda
url: https://arxiv.org/abs/2607.15267v1
---

# Pretraining Data Can Be Poisoned through Computational Propaganda

- **原标题**: Pretraining Data Can Be Poisoned through Computational Propaganda
- **作者**: Victoria Graf, Hannaneh Hajishirzi, Noah A. Smith, David Kohlbrenner, Kyle Lo
- **来源**: arXiv
- **发表日期**: 2026-07-16
- **原文**: [https://arxiv.org/abs/2607.15267v1](https://arxiv.org/abs/2607.15267v1)
- **AI 评分**: 8.1 / 10  (AI核心领域，讨论大模型预训练数据投毒风险，对程序员理解AI安全有启发；概念清晰但需一定技术背景，可制作成科普视频脚本。)

## 一句话结论
用评论区发帖就能污染AI训练数据，让模型学坏还很难查出来。

## 通俗解读
背景：训练大语言模型需要从网上抓海量数据，但坏人可能故意发些帖子污染这些数据。方法：作者发现，通过公开讨论区（比如论坛、评论区）发恶意帖子，就能把有害信息混进训练数据里。他们还发明了一种叫HalfLife的分析方法，可以估算这些帖子被爬虫抓取的概率。发现：这种攻击很可行，因为爬虫会抓取这些帖子进数据集，而现有清理手段很难完全过滤。意义：提醒大家，网上的公开讨论也能成为攻击AI的途径，数据安全得重视起来。

## 关键方法
HalfLife：一种新的分析工具，能估算恶意网页内容被爬虫抓取并保留在训练数据中的概率，类似半边衰期的概念。

## 对你的启发

- **程序员视角**: 做AI工程时，要警惕数据来源的开放性，尤其是爬虫抓取的公开内容。可以在数据清洗环节加入异常检测，比如检测重复或反常的文本模式，或者对来源进行信任评分。
- **投资视角**: AI模型的数据安全是个潜在风险点。如果这种攻击普及，依赖公开数据训练的模型会贬值，利好有私有高质量数据或强数据清洗能力的公司。加密领域同理，需关注链上数据治理的安全性。
- **内容视角**: 抖音可以做一期视频，标题如'AI毒奶粉：评论区发条帖子就能污染大模型'，用案例演示攻击原理，再聊聊如何防范。钩子：你发的评论可能正在喂给AI，小心被利用。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.15267v1)