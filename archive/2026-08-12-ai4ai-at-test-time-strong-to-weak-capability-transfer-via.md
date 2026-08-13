---
area: tech
created: '2026-08-13'
id: arxiv:2608.12307
score: 8.0
source: arXiv
starred: false
status: reference
summary: 大模型不用改参数，靠推理时搭脚手架就能带飞小模型，任务准确率近乎翻倍。
tags:
- paper
- ai
title: 'AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses'
url: https://arxiv.org/abs/2608.12307v1
---

# AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses

- **原标题**: AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses
- **作者**: Cheng Qian, Wenting Zhao, Liangwei Yang, Heng Wang, Jielin Qiu
- **来源**: arXiv
- **发表日期**: 2026-08-12
- **原文**: [https://arxiv.org/abs/2608.12307v1](https://arxiv.org/abs/2608.12307v1)
- **AI 评分**: 8.0 / 10  (论文涉及AI能力迁移，与用户核心AI领域高度相关，且提出的'构建推理时脚手架'概念对程序员有直接启发，可能促成AI工具或工作流改进；摘要概念清晰，无需深厚数学基础，但需要一定AI知识背景。)

## 一句话结论
大模型不用改参数，靠推理时搭脚手架就能带飞小模型，任务准确率近乎翻倍。

## 通俗解读
背景：通常让大模型教小模型，需要重新训练（蒸馏），耗时耗力。方法：研究者提出测试时搭建“脚手架”：让大模型（Builder）设计一套推理流程，包括写代码、路由选择和答案格式检查，小模型（Target）只需按流程走，不更新参数。发现：在四个社交推理任务上，小模型平均准确率从0.49提升到0.91，且提升主要来自将不稳定的推理外包给确定性代码，而不是让小模型多思考。意义：无需重训练就能转移能力，为模型优化提供了新思路，尤其适合无法重训的场景。

## 关键方法
用大模型在验证集上迭代优化推理流程（脚手架），流程包含：将推理步骤转化为代码、任务分类、答案格式约束。

## 对你的启发

- **程序员视角**: 可以借鉴这种“脚手架”模式，用大模型自动生成代码或规则，辅助现有AI系统处理不稳定逻辑，提升可靠性。
- **投资视角**: 测试时增强技术可能降低对大规模重训练的依赖，利好推理优化和AI基础设施公司，并可能影响模型间的能力壁垒。
- **内容视角**: 标题可作“不训练也能提升AI？大模型搭个架，小模型变聪明”，用通俗比喻展示AI技术，吸引对AI开发好奇的观众。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.12307v1)