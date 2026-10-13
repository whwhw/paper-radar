---
area: tech
created: '2026-10-13'
id: arxiv:2610.13806
score: 7.8
source: arXiv
starred: false
status: reference
summary: 用扰动+分组消融能安全删掉推荐系统30%+没用的特征，省成本不降效果。
tags:
- paper
- ai
title: 'FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial
  Recommender Systems'
url: https://arxiv.org/abs/2610.13806v1
---

# FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial Recommender Systems

- **原标题**: FORTE: A Production Framework for Feature Evaluation and Deprecation in Industrial Recommender Systems
- **作者**: Vishnu Arun, Adam Obeng, Tianyou Wang, Zilin Ren, Mukuntha Narayanan Sundararaman
- **来源**: arXiv
- **发表日期**: 2026-10-09
- **原文**: [https://arxiv.org/abs/2610.13806v1](https://arxiv.org/abs/2610.13806v1)
- **AI 评分**: 7.8 / 10  (这篇论文属于 AI 工程领域，直接涉及生产环境推荐系统的特征管理，与用户作为程序员和 AI 工程关注者高度相关。摘要用词偏工程化但易理解，有具体数字和数据，且提供了可迁移的工程方法论，对优化工程实践和内容创作都有启发。)

## 一句话结论
用扰动+分组消融能安全删掉推荐系统30%+没用的特征，省成本不降效果。

## 通俗解读
推荐系统里加特征容易（有效果就行），删特征却很难——怕影响效果、怕和其他特征纠缠、怕上线出问题。FORTE 是一个通用框架，通过高效扰动和分组消融，每天评估哪些特征可以安全删除，还追踪所有使用该特征的下游模型，确保彻底移除。在两个大型推荐系统上验证：搜索相关性模型删了48个特征（占43.3%），排序模型删了8个，参数减少29.9%，吞吐提升近20%，年省数十万美元训练成本，线上A/B测试均无效果回退。

## 关键方法
对每个特征做扰动，观察对指标的影响；把低重要性特征组合成候选集合，用分组消融（一次删一组）来捕捉特征间的交互；再用血缘追踪找出所有用该特征的模型，保证协同删除。

## 对你的启发

- **程序员视角**: 可以借鉴到ML工程中：用扰动和分组消融定期清理无用特征，结合血缘追踪做特征依赖管理，能显著降低模型维护成本和提升推理速度。
- **投资视角**: 说明AI模型降本增效有实际落地空间，尤其推荐系统领域；关注能优化模型效率的工具链或平台，可能是投资机会。
- **内容视角**: 抖音视频钩子：『推荐系统删掉一半特征，效果不变还省几十万？程序员教你如何安全给模型瘦身』。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.13806v1)