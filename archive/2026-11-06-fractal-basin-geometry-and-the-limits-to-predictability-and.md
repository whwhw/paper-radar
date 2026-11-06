---
area: tech
created: '2026-11-06'
id: rss:9c3076d776c6ff5d
score: 7.8
source: Nature Machine Intelligence
starred: false
status: reference
summary: 深度学习训练结果难复现，根源是训练起点像分形一样无限纠缠。
tags:
- paper
- tech
title: Fractal basin geometry and the limits to predictability and reproducibility
  in deep learning
url: https://www.nature.com/articles/s42256-026-01336-3
---

# Fractal basin geometry and the limits to predictability and reproducibility in deep learning

- **原标题**: Fractal basin geometry and the limits to predictability and reproducibility in deep learning
- **作者**: Pulin Gong
- **来源**: Nature Machine Intelligence
- **发表日期**: 2026-11-06
- **原文**: [https://www.nature.com/articles/s42256-026-01336-3](https://www.nature.com/articles/s42256-026-01336-3)
- **AI 评分**: 7.8 / 10  (这是发表在 Nature Machine Intelligence 上、关于深度学习可预测性与可复现性的核心 AI 方向论文，对用户的 AI 工程关注非常契合；分形盆地几何这一概念带有很强的可视化与日常类比空间（迷宫、海岸线），但涉及动力系统，对普通读者仍有一定门槛；它解释了 AI 训练结果为何难以复现，能直接启发用户的工作流自动化、模型调试，也能做成抖音上'为什么 AI 结果总不一样'的爆款选题。)

## 一句话结论
深度学习训练结果难复现，根源是训练起点像分形一样无限纠缠。

## 通俗解读
背景：同样代码同样数据跑两次，却常得不同模型，大家以为是随机种子问题。方法：作者把训练过程看成小球滚下山，看起点落在哪片谷底会滚出不同结果，发现这些谷底边界是分形的，就像海岸线放大后永远还有锯齿。发现：起点只要差一点点，甚至理论上无限小的差距，都可能滚向完全不同的结果，提高计算精度几乎没用。意义：复现失败不是工程粗心，而是系统本身的性质，需要换思路衡量可复现性。

## 关键方法
把"损失地形"想成山谷地图，画出每次训练终点属于哪个谷底的"分水岭"，再不断放大观察分界线的形状，看它是否越放大越细碎。

## 对你的启发

- **程序员视角**: 工程上，别把"同 seed 能复现"当作必然，训练管线要记录完整的初始化和数据顺序，同时用多次运行的分布和集成来评估模型，而不是只看单次结果。
- **投资视角**: 对 AI 赛道是个提醒：模型能力有"先天混沌"上限，可复现性和可控性是长期护城河，值得关注做评测、审计、确定性训练工具的公司。
- **内容视角**: 抖音钩子："同样的代码跑两遍，模型却不一样？科学家发现，答案藏在分形里：你的训练起点，早就决定了结局。"用海岸线放大动画做可视化。

## 原文 → 进一步阅读
- [原文链接](https://www.nature.com/articles/s42256-026-01336-3)