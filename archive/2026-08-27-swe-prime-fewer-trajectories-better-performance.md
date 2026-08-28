---
area: tech
created: '2026-08-28'
id: arxiv:2608.27449
score: 8.1
source: arXiv
starred: false
status: reference
summary: 少即是多：精选10%高质量轨迹训练，AI修Bug能力提升24%。
tags:
- paper
- ai
title: 'SWE-Prime: Fewer Trajectories, Better Performance'
url: https://arxiv.org/abs/2608.27449v1
---

# SWE-Prime: Fewer Trajectories, Better Performance

- **原标题**: SWE-Prime: Fewer Trajectories, Better Performance
- **作者**: Dewu Zheng, Ruizhe Ye, Yanlin Wang, Yang Ye, Hongyu Zhang
- **来源**: arXiv
- **发表日期**: 2026-08-27
- **原文**: [https://arxiv.org/abs/2608.27449v1](https://arxiv.org/abs/2608.27449v1)
- **AI 评分**: 8.1 / 10  (论文聚焦AI工程领域（代码智能体），与用户核心关注点高度相关，且思路可迁移到数据筛选和自动化流程设计；概念虽涉及机器学习细节，但类比数据筛选可以理解；启发潜力较高，可应用于技术内容创作和AI工具实践。)

## 一句话结论
少即是多：精选10%高质量轨迹训练，AI修Bug能力提升24%。

## 通俗解读
背景：以前训练AI修Bug，是把所有成功案例都喂给AI，但成功案例里也有废话和危险操作。方法：本文提出SWE-Prime，先把轨迹按质量筛选，再把轨迹切成小段，只挑有用片段参与训练。发现：只选10%优质轨迹训练，效果比用全部成功案例还好，在测试集上提升最高24.2%。意义：说明AI训练需要数据质量而非数量，扔垃圾数据会拖后腿。

## 关键方法
两步筛选：先按过程质量、结果质量、代表性筛选轨迹；再把轨迹按语义分段，评估每段对解决方案的贡献、可学性和风险，仅选优质段参与损失计算。

## 对你的启发

- **程序员视角**: 在微调模型时，可以借鉴这个思路，先清洗训练数据，剔除冗余和错误步骤，用小而精的数据集训练，既省算力又提升效果。
- **投资视角**: AI训练效率的提升意味着工具型AI（如代码助手）的迭代更快，关注那些有高效数据处理能力的AI公司，它们可能在成本上占优。
- **内容视角**: 钩子：'AI学修Bug，学太多反而傻？' 做个视频对比全量训练和精选训练的效果，用数据说话，解释数据质量比数量更重要。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.27449v1)