---
area: tech
created: '2026-10-22'
id: arxiv:2610.30113
score: 8.4
source: arXiv
starred: false
status: reference
summary: 九个顶尖大模型做量化投研，最牛的 GPT-6 也没跑赢 2024 年的等权指数。
tags:
- paper
- ai
title: 'Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research'
url: https://arxiv.org/abs/2610.30113v1
---

# Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research

- **原标题**: Quant-Arena: Benchmarking LLM Agents for Quantitative Trading Research
- **作者**: Houde Qian, Zheng Jiang, Wenyi Li, Chenxi Xu, Xinjie Lin
- **来源**: arXiv
- **发表日期**: 2026-10-21
- **原文**: [https://arxiv.org/abs/2610.30113v1](https://arxiv.org/abs/2610.30113v1)
- **AI 评分**: 8.4 / 10  (直接命中用户AI工程与量化投资交叉领域，且对Web3投资者有策略验证的可迁移启发。摘要不含复杂公式，概念清晰（研究循环、冻结策略、市场冲击），仅模拟订单簿略偏工程。GPT-6仍跑不赢等权市场的结论可做成抖音爆款选题，启发价值很高。)

## 一句话结论
九个顶尖大模型做量化投研，最牛的 GPT-6 也没跑赢 2024 年的等权指数。

## 通俗解读
背景：以前考大模型，要么只考写公式、写代码，要么只考单笔买卖，没人测过它能不能走完整个量化研究闭环。方法：Quant-Arena 用真实 A 股数据搭了个“考试场”——模型自己造特征、写选股代码，只在 2022-2023 年看成绩，定稿后一次性放到封闭的 2024 年“盲测”，还要扣交易成本和模拟盘口的冲击成本。发现：九个前沿模型里 GPT-6 Astra 分数最高，但放到 2024 年，没有一个能打赢“所有股票等权买入”这种笨办法。意义：大模型能写出像样的策略流程，但暂不具备真正跑赢市场的投研能力，别急着让它替你炒股。

## 关键方法
像“先给练习卷、再考密封卷”：研究期这两年数据随便调参，2024 年数据完全封存只跑一次，防止过拟合；评分主要看扣费后的真实超额收益，再看信号质量和特征多样性，避免靠堆特征刷分。

## 对你的启发

- **程序员视角**: 做 AI Agent 评估可以抄这个思路：训练和测试数据物理隔离，指标用“扣完成本后的净值提升”，而不是任务完成率之类的中间指标，防止 Agent 表演式刷分。
- **投资视角**: 对“AI 自动炒股”叙事要打折：顶级模型连等权基准都跑不赢，说明 LLM 目前更适合做投研辅助和因子挖掘助手，而不是替代策略大脑，别为纯 AI 量化概念付溢价。
- **内容视角**: 抖音钩子：“我把 GPT-6 扔进 A 股实战，结果输给了最笨的买法”——用真实盲测榜单讲 AI 的能力边界，比吹 AI 炒股更有反差和可信度。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.30113v1)