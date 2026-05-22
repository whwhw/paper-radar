---
area: tech
created: '2026-05-22'
id: arxiv:2605.22775
score: 8.1
source: arXiv
starred: false
status: reference
summary: 新模型MambaGaze用实时眼动数据准确评估认知负荷，精准又省电。
tags:
- paper
- ai
title: 'MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive
  Load Assessment from Eye-Gaze Tracking Data'
url: https://arxiv.org/abs/2605.22775v1
---

# MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data

- **原标题**: MambaGaze: Bidirectional Mamba with Explicit Missing Data Modeling for Cognitive Load Assessment from Eye-Gaze Tracking Data
- **作者**: Amir Mousavi, Mohammad Sadegh Sirjani, Erfan Nourbakhsh, Mimi Xie, Rocky Slavin
- **来源**: arXiv
- **发表日期**: 2026-05-21
- **原文**: [https://arxiv.org/abs/2605.22775v1](https://arxiv.org/abs/2605.22775v1)
- **AI 评分**: 8.1 / 10  (论文涉及AI（眼动追踪+认知负荷评估）和科技（实时边缘部署），高相关性；概念较清晰，但Mamba-2等技术细节可能需背景知识；对程序员有启发：缺失数据处理技巧可迁移，边缘部署方案实用，也适合制作AI工具科普内容。)

## 一句话结论
新模型MambaGaze用实时眼动数据准确评估认知负荷，精准又省电。

## 通俗解读
背景：通过眼动追踪实时判断人的认知负荷（比如驾驶员是否疲劳），能提升人机交互安全。但数据常因眨眼或丢失不完整，且时间序列长。方法：MambaGaze提出XMD编码，把缺失信息和时间间隔显式加入模型；用双向Mamba-2结构高效处理长序列。发现：在CLARE和CL-Drive数据集上准确率76.8%和73.1%，比CNN等高出4-12个百分点。意义：边缘设备上43-68帧/秒、功耗低于7.5瓦，可用于可穿戴设备实时监测。

## 关键方法
XMD编码：给原始眼动特征加上观测掩码（表示是否缺失）和时间差，让模型明确知道数据不确定性。双向Mamba-2：类似Transformer但计算量线性增长，能同时看前后眼动规律。

## 对你的启发

- **程序员视角**: 可以借鉴XMD编码，在时间序列项目中处理缺失数据：不删不补，而是添加缺失掩码和时间差作为特征，让模型自己学习处理。
- **投资视角**: 眼动认知负荷监测是自动驾驶和智能座舱的关键技术，MambaGaze的低功耗高准确率可能加速商用落地，利好AI边缘计算和车载传感器公司。
- **内容视角**: 钩子：“你的眼睛出卖了你！AI看眼动就知你累不累。” 做短视频拆解：眨眼时模型如何应对缺失数据，类比“AI眼动侦探”，科普认知负荷监测如何让汽车更安全。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.22775v1)