---
area: tech
created: '2026-06-07'
id: arxiv:2606.06462
score: 8.7
source: arXiv
starred: false
status: reference
summary: AI自动生成测试题，又快又好，还能持续更新，不再怕模型刷分。
tags:
- paper
- ai
title: Benchmark Everything Everywhere All at Once
url: https://arxiv.org/abs/2606.06462v1
---

# Benchmark Everything Everywhere All at Once

- **原标题**: Benchmark Everything Everywhere All at Once
- **作者**: Shiyun Xiong, Dongming Wu, Peiwen Sun, Yuang Ai, Bokang Yang
- **来源**: arXiv
- **发表日期**: 2026-06-04
- **原文**: [https://arxiv.org/abs/2606.06462v1](https://arxiv.org/abs/2606.06462v1)
- **AI 评分**: 8.7 / 10  (直接相关AI核心领域，自动化基准构建对程序员有工程启发，概念清晰易懂，易转化为技术号内容。)

## 一句话结论
AI自动生成测试题，又快又好，还能持续更新，不再怕模型刷分。

## 通俗解读
背景：现在测试AI模型（比如ChatGPT）用的考试题，都是人手工做的，费时费力，而且用久了模型能背答案，测不出真实水平。方法：这篇论文搞了个叫“Benchmark Agent”的自动出题系统，你给它一个主题（比如“数学推理”），它自己就能分解任务、出题、检查答案质量，全程不用人管。发现：系统出的15套题，覆盖文字、图片、专业知识，经人工和AI双重验证，质量跟人出的差不多。意义：以后可以随时生成新题，防止模型刷分，还能快速发现模型弱点。

## 关键方法
Agent系统：用户输入需求→自动拆解子任务→调用大模型生成题目→多轮质量筛选（去重、难度调整）→输出最终题库。核心是让AI自己当“出题老师”和“阅卷老师”。

## 对你的启发

- **程序员视角**: 可以集成到CI/CD流水线中，每次新模型发布时自动生成测试集，评估模型退化或改进；也能用来生成本地代码工程的单元测试，节省人工写测试用例的时间。
- **投资视角**: 利好AI数据服务公司，自动出题工具可能颠覆传统人工标注市场；长期看，持续更新的测评能更真实反映模型能力，辅助判断哪家技术真领先，避免被刷分PPT误导。
- **内容视角**: 抖音标题：《AI考AI！自动出题系统让ChatGPT自己给自己做卷子》——展示系统出题过程和结果对比，制造“AI内卷”概念，吸引技术好奇和焦虑流量。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.06462v1)