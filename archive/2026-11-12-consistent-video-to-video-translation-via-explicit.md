---
area: tech
created: '2026-11-14'
id: arxiv:2611.17298
score: 8.4
source: arXiv
starred: false
status: reference
summary: 视频翻译时，用输入视频的匹配区域找回历史输出，轻松保持长时一致性。
tags:
- paper
- ai
title: Consistent Video-to-Video Translation via Explicit Correspondences
url: https://arxiv.org/abs/2611.17298v1
---

# Consistent Video-to-Video Translation via Explicit Correspondences

- **原标题**: Consistent Video-to-Video Translation via Explicit Correspondences
- **作者**: Gaurav Parmar, Zhengqi Li, Richard Zhang, Jun-Yan Zhu, Srinivasa Narasimhan
- **来源**: arXiv
- **发表日期**: 2026-11-12
- **原文**: [https://arxiv.org/abs/2611.17298v1](https://arxiv.org/abs/2611.17298v1)
- **AI 评分**: 8.4 / 10  (这是 AI 视频生成领域的长时序一致性问题，属核心 AI 领域；核心思路（用输入视频的 patch 对应关系检索历史输出）可用'输入中匹配的地方输出也应匹配'的日常直觉理解，对做 AI 工具讲解的技术号是很好的选题，对工程上设计长上下文/缓存检索也有可迁移启发。)

## 一句话结论
视频翻译时，用输入视频的匹配区域找回历史输出，轻松保持长时一致性。

## 通俗解读
背景：视频到视频翻译要求实时且长时间一致，但现有方法只看固定窗口，历史一长就丢。方法：输入视频里相似区域，输出也该相似，所以先找输入中的匹配块，再用它们检索以前生成的输出块，通过注意力机制指导生成。发现：在多个视频模型上，长时一致性明显提升，生成质量和实时性不变。意义：为实时视频翻译提供简单有效的长时一致性方案。

## 关键方法
核心是“对应关系检索”：在输入视频中找相似块，然后从之前生成的输出中取回对应块，用注意力机制融合到当前生成中。

## 对你的启发

- **程序员视角**: 可借鉴到视频处理项目：利用输入相似性检索历史输出，提升长序列一致性；或实现一个轻量级对应检索模块。
- **投资视角**: 对AI视频生成赛道是利好，提升实时长视频生成质量，可能加速视频编辑、直播滤镜等应用落地。
- **内容视角**: 抖音钩子：“视频翻译不闪烁！揭秘如何让AI实时转换视频保持长时间一致” 演示前后对比。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.17298v1)