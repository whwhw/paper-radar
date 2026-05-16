---
area: tech
created: '2026-05-16'
id: arxiv:2605.15164
score: 8.1
source: arXiv
starred: false
status: reference
summary: AI安全靠测行为不行，得看内部机理。
tags:
- paper
- ai
title: 'Position: Behavioural Assurance Cannot Verify the Safety Claims Governance
  Now Demands'
url: https://arxiv.org/abs/2605.15164v1
---

# Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands

- **原标题**: Position: Behavioural Assurance Cannot Verify the Safety Claims Governance Now Demands
- **作者**: Pratinav Seth, Vinay Kumar Sankarapu
- **来源**: arXiv
- **发表日期**: 2026-05-14
- **原文**: [https://arxiv.org/abs/2605.15164v1](https://arxiv.org/abs/2605.15164v1)
- **AI 评分**: 8.1 / 10  (核心领域AI相关，讨论了AI治理与安全性验证，对AI工程有启发；概念较抽象但无需数学公式，易理解；可转化为内容创作话题，对投资者理解AI风险也有价值。)

## 一句话结论
AI安全靠测行为不行，得看内部机理。

## 通俗解读
背景：政府要求AI公司保证模型安全，比如没有隐藏目标、不会失控、能力有限。方法：目前主要靠行为测试（输入输出检查）和红队攻击（模拟黑客）。发现：这些方法只能看到表面行为，看不到模型内部到底怎么想，比如有没有隐藏意图或长期规划能力。就像医生只看病人脸色就开药，不看体检报告和基因。意义：需要结合“解剖式”检测，比如用线性探针看内部状态、用激活修复找漏洞、比较训练前后变化，才能真正确保安全。

## 关键方法
机械证据类：线性探针（检测内部神经元是否代表危险概念）、激活修复（修改部分神经活动看模型反应变化）、训练前后对比（看是否学到危险能力）。

## 对你的启发

- **程序员视角**: 部署AI时别光测输入输出，可以加内部监控，比如用探针检查模型是否产生异常中间状态，类似代码审计。
- **投资视角**: 政策收紧下，专注行为测试的安全公司可能被高估，押注能提供内部可解释性技术的团队更靠谱，这会影响AI安全赛道估值。
- **内容视角**: 做一期短视频标题："AI公司说安全？看看你上当了没"，用医院体检比喻解释行为测试和内部检测的区别，展示论文核心观点。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.15164v1)