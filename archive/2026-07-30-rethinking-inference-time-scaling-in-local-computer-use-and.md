---
area: tech
created: '2026-08-01'
id: arxiv:2607.28573
score: 8.1
source: arXiv
starred: false
status: reference
summary: 本地AI操作电脑时，加算力往往白费，关键要会挑重点花。
tags:
- paper
- ai
title: 'Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes
  and Compute Tradeoffs'
url: https://arxiv.org/abs/2607.28573v1
---

# Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs

- **原标题**: Rethinking Inference-Time Scaling in Local Computer-Use Agents: Failure Modes and Compute Tradeoffs
- **作者**: Woongkyu Lee, Jungwook Choi
- **来源**: arXiv
- **发表日期**: 2026-07-30
- **原文**: [https://arxiv.org/abs/2607.28573v1](https://arxiv.org/abs/2607.28573v1)
- **AI 评分**: 8.1 / 10  (论文聚焦AI智能体的推理时扩展，属于AI核心领域，与用户技术背景高度相关；概念虽涉及ML术语但整体可理解，且有实用启发。)

## 一句话结论
本地AI操作电脑时，加算力往往白费，关键要会挑重点花。

## 通俗解读
背景：想让AI自己操作电脑，但本地小模型受硬件限制，能力有限。方法：研究人员测试了多种本地模型，看增加思考时间或步骤是否有用。发现：多算往往效果不大，甚至改变错误类型；给历史信息能提升稳定性，但有上限；拆解任务反而增加负担。意义：未来应选择性分配算力，并设计更智能的控制机制，而非盲目堆算力。

## 关键方法
在OSWorld基准上，对多种本地模型进行系统性测试，从上下文、时间、结构、并行四个维度增加计算量，观察性能变化。

## 对你的启发

- **程序员视角**: 做AI自动化时，别盲目加推理步骤，可结合错误检测动态停止或调整算力，提高效率。
- **投资视角**: 投资AI时，注意本地模型推理效率与算力瓶颈，关注优化算力分配的技术公司。
- **内容视角**: 短视频可做“AI操作电脑的翻车现场”，展示堆算力的无用，吸引程序员和科技爱好者。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.28573v1)