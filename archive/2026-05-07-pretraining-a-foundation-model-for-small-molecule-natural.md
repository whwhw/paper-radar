---
area: tech
created: '2026-05-07'
id: rss:d82118b8651aa7b5
score: 7.1
source: Nature Machine Intelligence
starred: false
status: reference
summary: 用AI预训练模型预测天然小分子药物，分类更准，挖新药更快。
tags:
- paper
- tech
title: Pretraining a foundation model for small-molecule natural products
url: https://www.nature.com/articles/s42256-026-01226-8
---

# Pretraining a foundation model for small-molecule natural products

- **原标题**: Pretraining a foundation model for small-molecule natural products
- **作者**: Zhenmin Liu
- **来源**: Nature Machine Intelligence
- **发表日期**: 2026-05-07
- **原文**: [https://www.nature.com/articles/s42256-026-01226-8](https://www.nature.com/articles/s42256-026-01226-8)
- **AI 评分**: 7.1 / 10  (AI和健康领域相关，但专业化程度高，可启发AI驱动的药物发现内容创作。)

## 一句话结论
用AI预训练模型预测天然小分子药物，分类更准，挖新药更快。

## 通俗解读
背景：天然产物（如植物里的化合物）是药物的重要来源，但传统方法找新药又慢又难，像大海捞针。方法：研究者用AI预训练技术，让模型先学海量已知天然产物的结构骨架（类似学字母组成单词），再用掩码目标（随机遮住部分结构让模型猜）和对比学习（区分相似/不同分子）来精调。发现：模型在分类天然产物类别、挖掘合成基因、虚拟筛选候选药物上，都比现有工具准确20%以上。意义：这套模型可以帮科学家快速从自然中筛选抗癌、抗生素等药物，缩短研发周期。

## 关键方法
骨架感知预训练：把分子结构拆成骨架片段，用掩码预测和对比学习让模型理解化学空间。

## 对你的启发

- **程序员视角**: 类似技术可用于化学结构数据库的智能补全或分子结构生成API，比如在药物研发平台中集成这个模型做候选分子推荐。
- **投资视角**: AI+药物发现赛道持续升温，这种基础模型可能催化天然产物新药研发效率，利好相关AI药企和生物科技公司。
- **内容视角**: 抖音标题：《AI学化学？它居然能预测天然药物分子！》。钩子：展示模型如何从植物谜题里找出抗癌密码，类比AI拆解分子乐高。

## 原文 → 进一步阅读
- [原文链接](https://www.nature.com/articles/s42256-026-01226-8)