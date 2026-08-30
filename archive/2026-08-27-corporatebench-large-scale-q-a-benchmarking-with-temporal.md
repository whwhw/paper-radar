---
area: tech
created: '2026-08-30'
id: arxiv:2608.27391
score: 8.1
source: arXiv
starred: false
status: reference
summary: 大模型在超长企业文档问答上，规模越大表现越差。
tags:
- paper
- ai
title: 'CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases'
url: https://arxiv.org/abs/2608.27391v1
---

# CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases

- **原标题**: CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases
- **作者**: Sil Hamilton, Albert Yu Sun, Oscar J. Romero, Carl-Leander Henneking, David Mimno
- **来源**: arXiv
- **发表日期**: 2026-08-27
- **原文**: [https://arxiv.org/abs/2608.27391v1](https://arxiv.org/abs/2608.27391v1)
- **AI 评分**: 8.1 / 10  (论文聚焦AI大模型在企业文档问答中的评测，完全属于核心关注领域，且大型基准对工程实践有直接参考价值。尽管涉及知识库查询等技术细节，但概念清晰，可类比为'给AI做考试卷'，对程序员和内容创作者均有启发。)

## 一句话结论
大模型在超长企业文档问答上，规模越大表现越差。

## 通俗解读
背景：企业想用AI处理海量内部文档，但公开数据少，测试集又太简单。方法：作者造了4个虚拟公司（12到1万人），每个有约23万份随时间更新的文档，像真实世界一样逻辑一致，还人工验证过。然后让5个AI模型在这些文档上做问答。发现：文档越多，AI答得越差，尤其到了上万员工的规模，错误明显增多。意义：这就像考AI做“企业版阅读理解”，提醒我们AI在真实复杂场景下还没那么可靠，也给了开发者和企业一个更真实的测试工具。

## 关键方法
构建合成企业知识库：先定义公司的人员、项目、会议等事件，按时间线生成邮件、报告、聊天记录，保证所有文档逻辑连环相扣，再人工抽检验证。

## 对你的启发

- **程序员视角**: 可以用类似思路做自动化测试：生成模拟业务数据流，检验你的AI Agent在长上下文下是否真的能跨文档推断，而不只是单点检索。
- **投资视角**: 这提醒投资AI应用时，要警惕“demo效果好，大规模失效”的坑。企业级AI落地可能比想象中更慢，也说明长文本推理是下一个技术瓶颈，相关公司值得关注。
- **内容视角**: 内容钩子：“AI读不了100万字？我实测了AI在超大企业文档上的翻车现场！”可以准备几个实际案例，对比小数据和大数据下AI回答质量，直观展示问题。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.27391v1)