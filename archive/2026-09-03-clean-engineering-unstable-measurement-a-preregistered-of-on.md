---
area: tech
created: '2026-09-05'
id: arxiv:2609.04198
score: 8.1
source: arXiv
starred: false
status: reference
summary: 同一个AI模型名字，今天测和明天测结果可能不一样，不可靠！
tags:
- paper
- ai
title: 'Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure
  of Black-Box LLM Observers on Shared Endpoints'
url: https://arxiv.org/abs/2609.04198v1
---

# Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints

- **原标题**: Clean Engineering, Unstable Measurement: A Preregistered Reliability Failure of Black-Box LLM Observers on Shared Endpoints
- **作者**: Haoyaun Zhu, Jie Zhang
- **来源**: arXiv
- **发表日期**: 2026-09-03
- **原文**: [https://arxiv.org/abs/2609.04198v1](https://arxiv.org/abs/2609.04198v1)
- **AI 评分**: 8.1 / 10  (直接命中AI可靠性/科技核心领域，对依赖LLM做自动化评估的程序员和创作者极具警示价值；虽然涉及统计细节，但核心概念容易类比为'卷尺会变'，且能启发制作关于AI测评陷阱的内容。)

## 一句话结论
同一个AI模型名字，今天测和明天测结果可能不一样，不可靠！

## 通俗解读
背景：现在很多人用AI当裁判，比如让AI给文章打分，或者决定哪个AI回答更好。方法：研究者用同一个AI模型，发送完全一样的请求，在不同时间测试，检查结果是否一致。结果：发现重复测试的结果一致性很差，远低于标准要求。甚至同一天内，相同请求的排序一致性只有0.4（要求0.9），第二天完全相同的请求一致性也只有0.78（要求0.99）。原因：模型输出的随机性、标签映射偏差等。意义：说明AI裁判并不稳定，用AI评估结果需要谨慎，可能导致错误结论。

## 对你的启发

- **程序员视角**: 在工程中，如果依赖外部API（如OpenAI）做自动化测试或数据标注，别把输出当恒定结果。可以增加多次采样、一致性检查，或者改用自托管模型，但也要注意负载。
- **投资视角**: AI测评结果波动大，意味着依赖AI模型评估能力的产品（如自动评测工具）可能有问题。投资时关注那些能提供稳定测评解决方案的公司，或对AI不确定性有过滤机制的产品。
- **内容视角**: 抖音可以发视频：“你被AI骗了吗？同一个AI，同一句话，结果竟然不一样！”演示实际测试过程，引发对AI可靠性的讨论，吸引技术爱好者。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2609.04198v1)