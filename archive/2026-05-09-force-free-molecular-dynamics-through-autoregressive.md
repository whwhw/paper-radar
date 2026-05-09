---
area: tech
created: '2026-05-09'
id: rss:0b2cc534ef436e6c
score: 7.6
source: Nature Machine Intelligence
starred: false
status: reference
summary: 新AI模型跳过算力，直接预测原子轨迹，模拟速度提升30倍。
tags:
- paper
- tech
title: Force-free molecular dynamics through autoregressive equivariant networks
url: https://www.nature.com/articles/s42256-026-01227-7
---

# Force-free molecular dynamics through autoregressive equivariant networks

- **原标题**: Force-free molecular dynamics through autoregressive equivariant networks
- **作者**: Fausto Martelli
- **来源**: Nature Machine Intelligence
- **发表日期**: 2026-05-09
- **原文**: [https://www.nature.com/articles/s42256-026-01227-7](https://www.nature.com/articles/s42256-026-01227-7)
- **AI 评分**: 7.6 / 10  (论文涉及AI驱动的分子动力学模拟，属于科技/AI核心领域，但偏向物理化学，与用户主要关注点略有距离；摘要概念清晰，无复杂公式，通俗易懂；对程序员有启发，可借鉴其绕过力计算直接预测轨迹的思路用于其他物理模拟或工作流优化，内容创作者也可讲解该技术以吸引科技爱好者。)

## 一句话结论
新AI模型跳过算力，直接预测原子轨迹，模拟速度提升30倍。

## 通俗解读
传统分子模拟需要一步步计算原子间的作用力，非常慢。这篇论文提出的TrajCast模型，就像看天气预报一样，直接根据当前每个原子的位置和速度，预测它们下一步的位置，跳过了繁琐的力计算。模型用了等变神经网络，保证预测的运动方向是物理上合理的。实验结果发现，TrajCast能把模拟的时间步长拉长30倍，还能准确还原分子和材料的各种性质。这意味着未来用AI模拟蛋白质折叠、材料设计会快很多。

## 关键方法
Autoregressive equivariant network：每次预测下一步原子的位置时，输入上一步所有原子的位置和速度，网络输出一个概率分布，从中采样得到下一步位置。等变性保证预测结果在旋转平移下不变。

## 对你的启发

- **程序员视角**: 在模拟或物理引擎中，如果力计算是瓶颈，可以用这种直接预测轨迹的方法替代传统数值积分，比如游戏物理或机器人仿真。
- **投资视角**: 这项技术可能加速新药研发和材料发现，关注相关初创公司（如Schrödinger、Dassault Systèmes）和AI模拟赛道。
- **内容视角**: 标题：AI让分子模拟快30倍！为什么说这是科学计算的下一个GPT时刻？内容：对比传统方法，展示TrajCast如何预测水分子运动，类比自动驾驶预测轨迹。

## 原文 → 进一步阅读
- [原文链接](https://www.nature.com/articles/s42256-026-01227-7)