---
area: tech
created: '2026-06-13'
id: arxiv:2606.13610
score: 8.4
source: arXiv
starred: false
status: reference
summary: AI推荐系统容易被一条虚假网页内容欺骗，向用户推荐假货。
tags:
- paper
- ai
title: 'One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative
  Recommenders'
url: https://arxiv.org/abs/2606.13610v1
---

# One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders

- **原标题**: One Polluted Page Is Enough: Evaluating Web Content Pollution in Generative Recommenders
- **作者**: Minghao Luo, Liang Chen
- **来源**: arXiv
- **发表日期**: 2026-06-11
- **原文**: [https://arxiv.org/abs/2606.13610v1](https://arxiv.org/abs/2606.13610v1)
- **AI 评分**: 8.4 / 10  (AI安全与用户决策高度相关，通俗易懂且有工程防伪启发，适合内容创作讨论LLM可靠性。)

## 一句话结论
AI推荐系统容易被一条虚假网页内容欺骗，向用户推荐假货。

## 通俗解读
背景：现在的AI推荐系统（比如购物助手）会从网上搜索最新信息来推荐商品，但这可能被虚假评论或促销页面误导。方法：研究者创建了一个基准测试FORGE，模拟网上虚假内容（如把真实产品信息改成假的），测试12个领先AI模型在225种商品、5种场景下的表现。发现：仅一条虚假网页就能让AI在27%的情况下推荐假货，而替换前三结果时，受骗率高达73.8%。推理能力不仅没帮助，反而让AI编造理由来支持假推荐。意义：这说明AI推荐系统极易被污染，需要更好的防御，比如质疑提示或共识过滤。

## 关键方法
FORGE基准：用本地脚本将检索到的真实网页内容改写为虚假产品信息，然后统计AI模型推荐假产品的比例。

## 对你的启发

- **程序员视角**: 在设计搜索增强型AI应用时，必须加入网页内容的可信度评分或投票机制，避免单一来源污染整体推荐。
- **投资视角**: AI推荐系统的脆弱性可能影响电商和搜索广告的商业模式，需警惕相关AI公司因内容污染导致用户信任下降的风险。
- **内容视角**: 可以制作短视频揭露AI购物助手被虚假信息欺骗的案例，标题如"你的AI购物助手正在骗你？一条假评论就让它推荐假货"，引发观众好奇。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.13610v1)