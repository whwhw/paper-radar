---
area: tech
created: '2026-11-23'
id: arxiv:2611.27962
score: 8.7
source: arXiv
starred: false
status: reference
summary: 训练时让模型自己拿剪刀删掉没用的层，剪出来的小模型又小又强。
tags:
- paper
- ai
title: 'Model Carving: Training Transformers That Optimize Their Own Topology'
url: https://arxiv.org/abs/2611.27962v1
---

# Model Carving: Training Transformers That Optimize Their Own Topology

- **原标题**: Model Carving: Training Transformers That Optimize Their Own Topology
- **作者**: Kaden Zheng, Pratyusha Sharma
- **来源**: arXiv
- **发表日期**: 2026-11-20
- **原文**: [https://arxiv.org/abs/2611.27962v1](https://arxiv.org/abs/2611.27962v1)
- **AI 评分**: 8.7 / 10  (这篇论文关于Transformer架构自优化，直接命中AI工程与自动化工作流主题，且想法清晰有日常类比（'雕刻'出更小网络）。它既能启发程序员缩减模型/加速推理，也能做成抖音'训练时自动剪枝'的爆款选题，对关注效率与成本的投资判断也有参考价值。)

## 一句话结论
训练时让模型自己拿剪刀删掉没用的层，剪出来的小模型又小又强。

## 通俗解读
传统做法是先把网络结构定死再训练，就像先盖好整栋楼再往里塞家具。作者给每个子层装了一个可学习的开关（标量门），训练时让损失函数自己把没用的层关掉，模型边学边"雕刻"出自己的形状。结果：同样的算力，雕出来的模型比用 1.7 倍算力训练的完整模型效果还好，也胜过事后压缩的大模型；推理时少跑 34% 的计算，解码快 1.6 倍且质量不掉。意义是结构不该提前拍板，应该和权重一样被学出来。

## 关键方法
给每个注意力/MLP 子层乘一个可训练的门系数，训练中门接近 0 的层直接移除；注意力顺序也可变，于是从均匀大模型里"雕"出一个更小、非均匀的异构网络。

## 对你的启发

- **程序员视角**: 可以借鉴到自动化工作流和 Agent 编排：给每个节点/工具/skill 挂一个可训练权重，用任务损失自动淘汰无用步骤，跑出更短更快的流水线，而不是手工设计固定拓扑。
- **投资视角**: 强化"推理成本下降"这条主线：小模型靠训练期裁剪而非事后压缩，意味着边缘 AI 和端侧部署会更快落地，利好端侧芯片和低成本推理服务，对"堆算力"叙事的溢价是边际利空。
- **内容视角**: 抖音钩子："大模型里藏着一个更小更快的自己，训练时就能把它雕刻出来"——用橡皮泥或 3D 打印的比喻讲"结构不该提前定"，结尾反问：你公司的人是不是也该这样裁？

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.27962v1)