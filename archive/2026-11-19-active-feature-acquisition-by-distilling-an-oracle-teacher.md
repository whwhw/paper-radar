---
area: tech
created: '2026-11-22'
id: arxiv:2611.26598
score: 7.8
source: arXiv
starred: false
status: reference
summary: 让AI决定先买哪些数据，能省75%成本还保持90%准确率。
tags:
- paper
- ai
title: Active Feature Acquisition by Distilling an Oracle Teacher
url: https://arxiv.org/abs/2611.26598v1
---

# Active Feature Acquisition by Distilling an Oracle Teacher

- **原标题**: Active Feature Acquisition by Distilling an Oracle Teacher
- **作者**: Yang Meng, Zixin Ding, Robert L. Grossman, Yuxin Chen
- **来源**: arXiv
- **发表日期**: 2026-11-19
- **原文**: [https://arxiv.org/abs/2611.26598v1](https://arxiv.org/abs/2611.26598v1)
- **AI 评分**: 7.8 / 10  (AFA 属于 AI 工程中很实用的话题（用有限预算决定采集哪些特征），和用户关注的自动化工作流、工程决策直接相关；摘要概念清晰但有一定术语门槛，需要稍作通俗化，不过'老师-学生'式解释也能做出好脚本。用显式 oracle 教师替代隐式优化目标这一思路，也能迁移到 Web3 风控判断、内容选题的'先获取哪个信息'场景。)

## 一句话结论
让AI决定先买哪些数据，能省75%成本还保持90%准确率。

## 通俗解读
很多场景下获取全部数据很贵（比如医疗检查）。本文提出让AI学会挑最有用的数据先获取。训练时用“上帝视角”老师（知道所有答案）给每个数据打分，然后让学生AI模仿老师的打分。在医疗诊断和基准测试中，学生AI只用1/4成本就达到90%的准确率提升。意义：为资源受限的AI应用提供了高效数据采集策略。

## 关键方法
训练时有个“先知”老师知道所有隐藏特征和标签，能直接算出每个特征对降低预测错误的价值并排序。学生模型只看到已获取的特征，学习模仿老师的排序，从而在部署时也能做出类似决策。

## 对你的启发

- **程序员视角**: 在自动化工作流中，可以模仿这种“先知-学生”模式：先用全量数据训练一个昂贵但准确的模型作为老师，再蒸馏出轻量策略，用于在线决策（如日志采样、API调用优先级），节省资源。
- **投资视角**: 对AI赛道：这降低了AI应用的数据成本，利好边缘AI和个性化服务。对加密赛道：类似思路可用于链上数据采集优化（如只监听关键事件），但影响间接。长寿领域：医疗诊断成本降低可能加速AI辅助诊断普及。
- **内容视角**: 抖音钩子：“AI教你省钱：如何用1/4的检查费达到90%的诊断准确率？” 演示一个医疗AI如何智能选择检查项目，对比传统全查方案，突出成本效益。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.26598v1)