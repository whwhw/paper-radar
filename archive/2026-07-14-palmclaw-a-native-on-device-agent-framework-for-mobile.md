---
area: tech
created: '2026-07-15'
id: arxiv:2607.13027
score: 8.4
source: arXiv
starred: false
status: reference
summary: PalmClaw让AI直接在手机上操作App，任务成功率提升11.5%，时间缩短94.9%
tags:
- paper
- ai
title: 'PalmClaw: A Native On-Device Agent Framework for Mobile Phones'
url: https://arxiv.org/abs/2607.13027v1
---

# PalmClaw: A Native On-Device Agent Framework for Mobile Phones

- **原标题**: PalmClaw: A Native On-Device Agent Framework for Mobile Phones
- **作者**: Hongru Cai, Yongqi Li, Ran Wei, Wenjie Li
- **来源**: arXiv
- **发表日期**: 2026-07-14
- **原文**: [https://arxiv.org/abs/2607.13027v1](https://arxiv.org/abs/2607.13027v1)
- **AI 评分**: 8.4 / 10  (AI agent框架直接相关，适合程序员理解；摘要较清晰但需一定背景知识；对构建自动化工作流和内容创作有启发。)

## 一句话结论
PalmClaw让AI直接在手机上操作App，任务成功率提升11.5%，时间缩短94.9%

## 通俗解读
背景：AI助手通常只在电脑上运行，无法直接控制手机App。方法：研究人员设计了一个叫PalmClaw的框架，它像手机的'遥控器'，将打电话、发短信、调音量等手机功能变成一个个小工具，AI可以像搭积木一样使用它们。发现：在测试中，PalmClaw完成任务的成功率比现有方案高11.5%，而且速度快了94.9%，因为它不用模拟点击屏幕，而是直接调用底层功能。意义：未来的AI助手可以更高效地帮你操作手机，比如自动订外卖、查消息，且每一步都透明可控。

## 关键方法
把手机硬件和App能力封装成'工具'（如发送短信、获取位置），每个工具有明确的输入输出和权限边界，AI通过调用这些工具而非模拟点击来执行任务。

## 对你的启发

- **程序员视角**: 可以借鉴PalmClaw的工具化设计，为自己的项目封装底层接口为可组合功能模块，让AI或自动化脚本通过API而非GUI操作，提高稳定性和效率。
- **投资视角**: PalmClaw展示了移动AI原生运行的趋势，利好手机厂商和AI中间件公司。若开源生态成熟，可能催生新的移动端AI应用市场，值得关注相关赛道。
- **内容视角**: 做一期'AI直接操控手机，告别模拟点击'的抖音视频，演示PalmClaw自动发微信、查天气，对比传统方式的速度差异，标题用'手机AI可以自己动手了？'作为钩子。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.13027v1)