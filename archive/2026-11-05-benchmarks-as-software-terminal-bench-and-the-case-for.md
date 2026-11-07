---
area: tech
created: '2026-11-07'
id: arxiv:2611.08417
score: 8.1
source: arXiv
starred: false
status: reference
summary: 基准测试像软件一样会过时，三成题目有缺陷，修好后AI得分能涨10个百分点。
tags:
- paper
- ai
title: 'Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks'
url: https://arxiv.org/abs/2611.08417v1
---

# Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks

- **原标题**: Benchmarks as Software: Terminal-Bench and the Case for Continuous Benchmarks
- **作者**: E. Kelly Buchanan, Crystal Zhou, Scott W. Linderman, Christopher Ré
- **来源**: arXiv
- **发表日期**: 2026-11-05
- **原文**: [https://arxiv.org/abs/2611.08417v1](https://arxiv.org/abs/2611.08417v1)
- **AI 评分**: 8.1 / 10  (这篇论文属于 AI 工程中的代码智能体评测主题，与用户核心关注的 AI 领域高度契合。文中提出'benchmark maintenance debt'概念，并用时间预算影响评测结果作为例子，对程序员的工程实践和内容创作者做 AI 工具讲解都有直接启发；概念清晰、少有复杂数学公式，非学术读者基本能够理解。)

## 一句话结论
基准测试像软件一样会过时，三成题目有缺陷，修好后AI得分能涨10个百分点。

## 通俗解读
背景：AI编程能力越来越强，但用来衡量它们的基准测试可能因题目过时或验证器错误而失真。方法：作者提出“持续验证”流程，结合社区报告、任务文件、AI运行记录和自动检查，对Terminal-Bench 2.0进行审计。发现约30%的测试题有问题，修复后发布2.1版，AI正确率提升超10个百分点，排行榜最多变动三名；此外，固定时间限制会严重影响成绩，放宽后能缩小不同测试环境间的差距。意义：基准测试需要像软件一样持续维护，否则分数不能真实反映AI能力。

## 关键方法
把基准测试当作软件来维护：收集社区反馈和AI运行日志，自动检查答案正误，人工审核后修复题目。同时需校验资源（如时间限制）是否公平。

## 对你的启发

- **程序员视角**: 在工程中，对AI代理的评测要定期审计题目和运行环境，尤其时间限制对性能影响大，需固定资源并持续修正测试用例。
- **投资视角**: AI模型排名可能受基准缺陷影响，投资时别只看分数，要关注基准是否经过持续验证和资源公平性，避免高估或低估模型能力。
- **内容视角**: 抖音钩子：『AI排行榜可能骗了你？30%的测试题是错的！』用动画展示修复前后排名变化，引发对AI评测可靠性的讨论。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.08417v1)