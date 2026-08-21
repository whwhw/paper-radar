---
area: tech
created: '2026-08-21'
id: arxiv:2608.20271
score: 8.4
source: arXiv
starred: false
status: reference
summary: 用交易前5分钟数据，机器学习能提前揪出Solana上的假迷因币骗局。
tags:
- paper
- ai
title: 'Catching the Rug: Early Prediction of Fraudulent Memecoins on Solana via Machine
  Learning'
url: https://arxiv.org/abs/2608.20271v1
---

# Catching the Rug: Early Prediction of Fraudulent Memecoins on Solana via Machine Learning

- **原标题**: Catching the Rug: Early Prediction of Fraudulent Memecoins on Solana via Machine Learning
- **作者**: Jianghai Li, Pavel Kuznetsov, Yury Yanovich, Konstantin Nott-Whaley, Igor Vodolazov
- **来源**: arXiv
- **发表日期**: 2026-08-20
- **原文**: [https://arxiv.org/abs/2608.20271v1](https://arxiv.org/abs/2608.20271v1)
- **AI 评分**: 8.4 / 10  (论文聚焦于Solana上memecoin的rug pull检测，属于Web3和AI交叉领域，与用户核心关注高度相关；概念清晰，无需深度数学背景即可理解，且对投资者和内容创作者有实用启发。)

## 一句话结论
用交易前5分钟数据，机器学习能提前揪出Solana上的假迷因币骗局。

## 通俗解读
背景：Solana上有很多迷因币，其中很多是骗局（拉地毯），投资者损失惨重。方法：研究者收集了640万个代币的数据，用机器学习（特别是XGBoost）分析它们上市后前5分钟的交易数据，比如价格变动、交易量等。发现：大多数骗局币在1小时内就露出马脚，而仅用前5分钟数据就能高准确率预测。意义：这能帮投资者在早期避开骗局，也说明AI在DeFi安全中有用。

## 关键方法
用XGBoost模型，只看前5分钟交易数据（如价格波动、交易量、持有人数），训练分类器区分正常币和拉地毯币，并验证了跨平台泛化。

## 对你的启发

- **程序员视角**: 可借鉴其Feature Engineering思路，在交易监控或异常检测中，用极短时间窗口的特征做实时风险预警。
- **投资视角**: 对加密投资有直接参考：投资迷因币前，可自动分析前5分钟链上数据，避开高风险币种。
- **内容视角**: 内容钩子：'用AI预测加密骗局，5分钟识别拉地毯币'，适合技术科普，可演示实际检测过程。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.20271v1)