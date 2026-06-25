---
area: tech
created: '2026-06-25'
id: arxiv:2606.26028
score: 8.1
source: arXiv
starred: false
status: reference
summary: ERC-8004名义上要做AI代理的信任层，但实际上大部分注册是空壳，声誉可被低成本操纵。
tags:
- paper
- ai
title: Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized
  AI Agent Ecosystem
url: https://arxiv.org/abs/2606.26028v1
---

# Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem

- **原标题**: Can Trustless Agents Be Trusted? An Empirical Study of the ERC-8004 Decentralized AI Agent Ecosystem
- **作者**: Xihan Xiong, Zelin Li, Wei Wei, Qin Wang, William Knottenbelt
- **来源**: arXiv
- **发表日期**: 2026-06-24
- **原文**: [https://arxiv.org/abs/2606.26028v1](https://arxiv.org/abs/2606.26028v1)
- **AI 评分**: 8.1 / 10  (论文聚焦去中心化AI代理信任层，紧密关联AI与区块链交叉领域，对Web3投资者理解链上声誉机制有直接启发；摘要虽含技术细节，但核心问题（信任、Sybil攻击）易于理解，可提炼为内容创作者讨论AI+加密的素材。)

## 一句话结论
ERC-8004名义上要做AI代理的信任层，但实际上大部分注册是空壳，声誉可被低成本操纵。

## 通俗解读
背景：AI代理越来越多，但它们之间如何互信是个大问题。ERC-8004协议试图通过三个链上注册表（身份、声誉、验证）建立信任层，但没人验证它是否有效。方法：研究者抓取了以太坊、BSC和Base三条链上的数据，包括身份、声誉和支付记录。发现：大部分身份注册只是占位符，只有3%-15%有真实服务；声誉值不统一，反馈记录很少基于真实交易，而且只要一点点成本就能刷分。超过半数的评价者存在联合造假行为，去掉这些假反馈，很多代理就没有效评价了。意义：这个协议目前不能作为信任信号，需要大改。

## 关键方法
爬取链上事件和链下文件，分析身份注册的真实性、声誉的可比性以及Sybil行为检测。

## 对你的启发

- **程序员视角**: 在构建AI代理系统时，不能依赖链上声誉作为唯一信任源，需要结合离线验证或挑战机制来防止刷分。
- **投资视角**: 如果ERC-8004无法解决信任问题，那么基于它的AI代理经济可能基础不稳，投资需谨慎；但改进后的版本可能有价值。
- **内容视角**: 抖音讲：'AI代理的信任危机——你以为的链上声誉，其实是机器人互刷的假数据'，配合案例展示数据操纵的容易程度。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.26028v1)