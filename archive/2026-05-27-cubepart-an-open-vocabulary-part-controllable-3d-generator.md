---
area: tech
created: '2026-05-28'
id: arxiv:2605.28763
score: 8.7
source: arXiv
starred: false
status: reference
summary: AI 可根据文字描述和零件清单，自动生成可组装的 3D 模型部件。
tags:
- paper
- ai
title: 'CubePart: An Open-Vocabulary Part-Controllable 3D Generator'
url: https://arxiv.org/abs/2605.28763v1
---

# CubePart: An Open-Vocabulary Part-Controllable 3D Generator

- **原标题**: CubePart: An Open-Vocabulary Part-Controllable 3D Generator
- **作者**: Yiheng Zhu, Kangle Deng, Jean-Philippe Fauconnier, Inaki Navarro, Daiqing Li
- **来源**: arXiv
- **发表日期**: 2026-05-27
- **原文**: [https://arxiv.org/abs/2605.28763v1](https://arxiv.org/abs/2605.28763v1)
- **AI 评分**: 8.7 / 10  (直接命中用户核心兴趣（AI+科技），且与AI工程、自动化工作流强相关。方法直观，概念清晰，易于理解。能启发程序员的3D资产自动化生成思路，也可以作为技术号内容素材。)

## 一句话结论
AI 可根据文字描述和零件清单，自动生成可组装的 3D 模型部件。

## 通俗解读
背景：游戏和模拟中的 3D 物品通常需要拆分为独立零件（如手臂、轮子），但现有 AI 生模型只能生成一整个模型或随机拆分。方法：研究者创建了一个包含大量零件标注的 3D 数据集，并设计了一个两阶段模型，先生成整体形状，再按用户指定的零件列表逐个生成对应的网格。发现：生成的零件可直接用于游戏引擎，无需手动后处理。意义：让 3D 建模像搭积木一样灵活，设计师只需描述需求即可获得可交互的资产。

## 关键方法
两阶段生成：先根据文本生成整体形状隐式表示，再根据零件列表和整体信息解码出每个零件的网格，保证零件拼合后形成完整物体。

## 对你的启发

- **程序员视角**: 可以将此思路用于游戏资产流水线：用户输入文字和零件列表，自动生成可装配的模型，节省手动拆分时间。
- **投资视角**: 表明 AI 生成 3D 资产正从“生成一个模型”进化到“生成可交互的零件级模型”，利好数字孪生、游戏引擎和元宇宙平台。
- **内容视角**: 标题：AI 搭积木？一句话+零件清单，3D 模型自动拆解好！展示如何用 AI 生成游戏角色的可动零件。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.28763v1)