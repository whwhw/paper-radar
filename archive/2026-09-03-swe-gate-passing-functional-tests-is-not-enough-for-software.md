---
area: tech
created: '2026-09-05'
id: arxiv:2609.04167
score: 8.1
source: arXiv
starred: false
status: reference
summary: AI编程工具通过测试不等于合格，代码评审意见常被忽略。
tags:
- paper
- ai
title: 'SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering
  Agents'
url: https://arxiv.org/abs/2609.04167v1
---

# SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents

- **原标题**: SWE-Gate: Passing Functional Tests Is Not Enough for Software Engineering Agents
- **作者**: Xin He, Yanlin Wang, Mingwei Liu, Jiachi Chen, Hongyu Zhang
- **来源**: arXiv
- **发表日期**: 2026-09-03
- **原文**: [https://arxiv.org/abs/2609.04167v1](https://arxiv.org/abs/2609.04167v1)
- **AI 评分**: 8.1 / 10  (该论文属于AI工程核心领域（软件工程智能体），且与程序员日常开发工具直接相关，启发潜力高；虽有技术细节但概念清晰，普通读者能理解主要观点。)

## 一句话结论
AI编程工具通过测试不等于合格，代码评审意见常被忽略。

## 通俗解读
背景：现在评价AI写代码好不好，主要看它能不能通过功能测试。但真实开发中，代码还得过代码评审这一关，评审人的意见（比如风格、边界条件）没被重视。方法：研究者做了个新测试集SWE-Gate，从真实项目的评审评论中提取要求，让AI在修bug的同时满足这些要求。发现：在644个通过功能测试的修复中，有221个没满足评审要求，说明只看功能测试会高估AI能力。意义：AI编程工具需要更全面的评价标准，不能只盯着测试通过。

## 关键方法
他们把代码评审意见变成了单独测试，有点像考试分开考基础题和附加题，附加题考的是代码规范和隐藏要求。

## 对你的启发

- **程序员视角**: 在做自动化代码审查或CI流程时，可以加入类似评审约束测试，让AI生成的代码更符合团队规范。
- **投资视角**: 这说明AI编程工具能力被高估，实际落地还有差距，投资时需关注其处理真实工程约束的能力。
- **内容视角**: 可以拍一条视频：用几个例子展示AI修好bug但被评审打回，聊AI离独立干活还有多远。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2609.04167v1)