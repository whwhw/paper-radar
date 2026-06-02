---
area: tech
created: '2026-06-02'
id: arxiv:2606.02569
score: 8.5
source: arXiv
starred: false
status: reference
summary: AdaCodec 用最少视频帧数据达到更好 AI 理解效果，速度提升 5 倍。
tags:
- paper
- ai
title: 'AdaCodec: A Predictive Visual Code for Video MLLMs'
url: https://arxiv.org/abs/2606.02569v1
---

# AdaCodec: A Predictive Visual Code for Video MLLMs

- **原标题**: AdaCodec: A Predictive Visual Code for Video MLLMs
- **作者**: Haowen Hou, Zhen Huang, Zheming Liang, Qingyi Si, Chenglin Li
- **来源**: arXiv
- **发表日期**: 2026-06-01
- **原文**: [https://arxiv.org/abs/2606.02569v1](https://arxiv.org/abs/2606.02569v1)
- **AI 评分**: 8.5 / 10  (直接相关AI/科技领域，解释清晰有类比（预测编码），对视频处理工程有启发，但涉及技术细节较多。)

## 一句话结论
AdaCodec 用最少视频帧数据达到更好 AI 理解效果，速度提升 5 倍。

## 通俗解读
视频每帧之间通常变化很小，比如一个人从左边走到右边，背景几乎不变。现在的 AI 看视频时，却把每一帧都当成全新图片处理，导致大量重复计算，就像每次翻书都把整页重读一遍。AdaCodec 学聪明了：它只完整处理第一帧，后续帧只记录变化（比如“手向右移了 2 厘米”），只有场景完全改变时才发新参考帧。测试显示，用 1/7 的数据量（3.2 万 tokens vs 22.4 万），AI 理解长视频的表现反而更好，并且首次响应时间从 9.26 秒降到 1.62 秒。

## 关键方法
参考帧+预测编码：只传完整帧当“场景变化大”时，否则只传运动向量和残差作为紧凑 P-token。

## 对你的启发

- **程序员视角**: 做视频 AI 产品时，可以用类似增量编码减少 API 调用成本，例如监控视频只上报变化区域。
- **投资视角**: 这项技术可能降低视频 AI 推理成本，利好视频 SaaS 和边缘 AI 设备，建议关注相关创业公司。
- **内容视角**: 标题：“AI 看视频终于不傻了！只用 1/7 流量，看懂全片”。钩子：“你做的视频 AI 剪辑工具，可能成本能降 5 倍。”

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.02569v1)