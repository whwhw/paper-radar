---
area: tech
created: '2026-09-10'
id: arxiv:2609.10451
score: 8.1
source: arXiv
starred: false
status: reference
summary: 现有GUI智能体只会在单设备上表演，一跨设备就露馅。
tags:
- paper
- ai
title: 'JarvisGUI: Towards Cross-Device GUI Agents with Dynamic Task Composition'
url: https://arxiv.org/abs/2609.10451v1
---

# JarvisGUI: Towards Cross-Device GUI Agents with Dynamic Task Composition

- **原标题**: JarvisGUI: Towards Cross-Device GUI Agents with Dynamic Task Composition
- **作者**: Zixiang Chen, Yuheng Lu, Zihao Cheng, Zeming Liu, Jizeng Bai
- **来源**: arXiv
- **发表日期**: 2026-09-09
- **原文**: [https://arxiv.org/abs/2609.10451v1](https://arxiv.org/abs/2609.10451v1)
- **AI 评分**: 8.1 / 10  (论文聚焦跨设备GUI智能体（AI核心领域），涉及操作系统协作，与用户AI工程兴趣高度相关；摘要概念清晰，无深奥数学，但涉及技术细节可理解；对程序员设计自动化工作流和内容创作者制作AI工具评测视频有直接启发。)

## 一句话结论
现有GUI智能体只会在单设备上表演，一跨设备就露馅。

## 通俗解读
背景：现实里我们经常要在手机、电脑多个设备间来回倒腾数据，但现在的AI助手考试都只考单设备、固定套路的任务，成绩虚高。方法：作者造了个新考场JarvisGUI，把任务看成'输入→输出'的小积木，可以自动拼出跨安卓、Windows、Ubuntu的多设备流程。发现：最牛的开源GUI智能体在这些真活儿上频频翻车，搞不清状态该传到哪、也管不好长链条依赖。意义：说明AI自动操作电脑离真正实用还有明显短板，现有评测太乐观了。

## 关键方法
把每个GUI操作定义成'吃什么输入、吐什么输出'的积木块，再用一套简单规则自动把积木拼成跨设备的多步任务，这样就能批量生成复杂考题并自动打分。

## 对你的启发

- **程序员视角**: 做Agent工作流时，可以借鉴这种'输入输出契约+动态编排'思路，把跨服务、跨环境的步骤拆成有类型约束的模块，避免状态乱飞。
- **投资视角**: 这说明AI Agent真正落地到多设备自动化还有硬骨头，短期别高估'AI帮你操作一切'的叙事，相关标的的兑现节奏可能慢于预期。
- **内容视角**: 抖音钩子：'我让AI同时操作手机和电脑干活，结果它当场社死——跨设备智能体的真实水平测试'。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2609.10451v1)