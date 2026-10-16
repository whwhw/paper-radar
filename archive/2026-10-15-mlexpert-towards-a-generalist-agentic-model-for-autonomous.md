---
area: tech
created: '2026-10-16'
id: arxiv:2610.22344
score: 7.8
source: arXiv
starred: false
status: reference
summary: 35B小模型学会自己做AI实验，拿牌率从38%飙到73%，逼近顶级大模型。
tags:
- paper
- ai
title: 'MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning
  Engineering'
url: https://arxiv.org/abs/2610.22344v1
---

# MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering

- **原标题**: MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering
- **作者**: Shangheng Du, Jinxin Shi, Shuaiyu Zhang, Yiming Wu, Junpeng Zhao
- **来源**: arXiv
- **发表日期**: 2026-10-15
- **原文**: [https://arxiv.org/abs/2610.22344v1](https://arxiv.org/abs/2610.22344v1)
- **AI 评分**: 7.8 / 10  (直接落在 AI 工程/自动化工作流核心领域，讲的是用 agentic 模型自主做机器学习工程，与用户 AI 工程和抖音技术号内容高度契合。但摘要术语密集（MoE、SFT、WIRL、异步收集等），非学术读者需要解读；核心思想可迁移到自动化工作流与 AI4AI 趋势脚本，启发潜力高。)

## 一句话结论
35B小模型学会自己做AI实验，拿牌率从38%飙到73%，逼近顶级大模型。

## 通俗解读
背景：现在大模型不仅能写代码，还想自己当科学家、自己改进AI。但让AI自主做机器学习实验很难，因为一次实验要跑很久，中间几十步操作谁对谁错说不清。方法：作者造了个'Kaggle工厂'批量生成可执行的实验任务，先让模型跟着成功案例学基本操作（SFT），再用'WIRL'把两次实验结果之间的多步操作打包，只看最终结果给统一打分。发现：35B的MLExpert在MLE-Bench Lite上拿牌率从37.9%升到72.7%，追平Kimi-K3这类更大的前沿模型，还能迁移到别的优化任务。意义：AI自己搞AI研发（AI4AI）这条路，小模型+好训练法就能走通，不一定非要堆参数。

## 关键方法
WIRL的核心思想：把'两次实验结果之间的所有操作'看成一个回合，只根据这个回合的最终得分给整段操作发一个奖励。就像打游戏只看通关没通关给经验值，而不是逐步点评每个按键，避免中间步骤奖励难分配的问题。

## 对你的启发

- **程序员视角**: 可以直接借鉴'窗口化RL'思路做Agent工作流：别对每一步工具调用单独打分，把一段连续操作打包、只看最终产出质量奖励，训练/评估自动化Agent时更稳、更省标注。
- **投资视角**: AI4AI和递归自我改进从概念走向工程化，意味着AI能力迭代可能加速；关注'小模型+专门训练法逼近前沿'的路线，可能压低算力军备竞赛的护城河逻辑，对英伟达叙事和开源模型生态都有影响。
- **内容视角**: 钩子：'一个35B的小模型，自己刷Kaggle刷到拿牌率翻倍，还追平了千亿大模型——AI开始自己训练AI了，普通人该慌还是该兴奋？' 拆解AI4AI概念，通俗讲清'自己改进自己'到底意味着什么。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.22344v1)