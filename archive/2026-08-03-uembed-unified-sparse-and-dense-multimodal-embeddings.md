---
area: tech
created: '2026-08-04'
id: arxiv:2608.02583
score: 7.8
source: arXiv
starred: false
status: reference
summary: 一个模型同时输出稀疏和稠密向量，支持图文搜索，性能强且效率高。
tags:
- paper
- ai
title: 'UEmbed: Unified Sparse and Dense Multimodal Embeddings'
url: https://arxiv.org/abs/2608.02583v1
---

# UEmbed: Unified Sparse and Dense Multimodal Embeddings

- **原标题**: UEmbed: Unified Sparse and Dense Multimodal Embeddings
- **作者**: Tingyu Song, Mingxin Li, Yanzhao Zhang, Dingkun Long, Pengjun Xie
- **来源**: arXiv
- **发表日期**: 2026-08-03
- **原文**: [https://arxiv.org/abs/2608.02583v1](https://arxiv.org/abs/2608.02583v1)
- **AI 评分**: 7.8 / 10  (论文属于AI核心领域，与用户关注高度相关；方法虽有工程细节但概念清晰，可理解；对程序员有启发，可借鉴统一稀疏和稠密嵌入的思路，且可用于RAG等技术。)

## 一句话结论
一个模型同时输出稀疏和稠密向量，支持图文搜索，性能强且效率高。

## 通俗解读
背景：搜索引擎和AI问答系统需要快速找到相关信息，传统方法要么用稀疏向量（像查字典）要么用稠密向量（像理解含义），且只能处理文本。方法：UEmbed是一个只解码器的大模型，输入文本或图片，通过添加特殊标记和划分词汇表，一次性输出两种向量。发现：在多个基准上，UEmbed性能超过同类模型，且推理速度快。意义：让搜索更智能、更通用，能同时理解文字和图像，为AI应用提供新思路。

## 关键方法
在输入末尾添加N个可学习特殊token，将词表分为N个不重叠子集，每个token负责预测其子集上的稀疏权重，拼接成完整稀疏向量；稠密向量则通过注意力池化得到。

## 对你的启发

- **程序员视角**: 可以借鉴其一次前向传播同时输出两种表示的设计，用于构建多模态RAG系统，减少部署成本和推理延迟。
- **投资视角**: 这表明多模态AI模型正走向统一和高效，可能利好提供基础模型API的公司，但需关注其开源许可和实际效果。
- **内容视角**: 抖音视频选题：'AI搜索新突破：一个模型看懂图片和文字'，演示用UEmbed进行图文混合搜索，如'找一张猫的图片，内容要有桌子'。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.02583v1)