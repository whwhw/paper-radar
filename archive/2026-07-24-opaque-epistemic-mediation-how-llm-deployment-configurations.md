---
area: tech
created: '2026-07-27'
id: arxiv:2607.22513
score: 8.0
source: arXiv
starred: false
status: reference
summary: 大模型对伪科学的态度不稳定，取决于部署配置而非模型本身。
tags:
- paper
- ai
title: 'Opaque Epistemic Mediation: How LLM Deployment Configurations Shape the Validation
  of Pseudo-Science'
url: https://arxiv.org/abs/2607.22513v1
---

# Opaque Epistemic Mediation: How LLM Deployment Configurations Shape the Validation of Pseudo-Science

- **原标题**: Opaque Epistemic Mediation: How LLM Deployment Configurations Shape the Validation of Pseudo-Science
- **作者**: Davide Scarso, Hugo Noronha de Almeida, Joaquim Pina
- **来源**: arXiv
- **发表日期**: 2026-07-24
- **原文**: [https://arxiv.org/abs/2607.22513v1](https://arxiv.org/abs/2607.22513v1)
- **AI 评分**: 8.0 / 10  (核心领域AI相关性高，但主题较窄；摘要清晰但涉及假科学和配置细节；对程序员有直接启发（模型部署配置影响输出），适合做内容创作或投资判断。)

## 一句话结论
大模型对伪科学的态度不稳定，取决于部署配置而非模型本身。

## 通俗解读
背景：越来越多的人用ChatGPT等大模型查知识，但模型对边界科学（比如种族优劣论）的判断可能不靠谱。方法：研究者在半年内测试了四个主流模型（Claude、Grok、GPT、Gemini）对一种伪科学理论的评分，对比了API和网页版。发现：Grok默认版给伪科学打了高分（70-75），其他模型只给15-40；API和网页版结果可能完全不同；模型会偷偷更新且不通知用户。意义：大模型的知识立场不是固定的，而是被系统提示、安全层等部署手段控制的，用户完全不知情，这需要问责机制。

## 关键方法
研究者用相同的伪科学问题（来自Frank Salter的生物社会框架）在四个时间点、通过API和网页版询问四个模型，记录它们的评分和拒绝回答情况。

## 对你的启发

- **程序员视角**: 做AI应用时，不能假设模型行为一致。要监控API的版本变化，对不确定领域加二次校验或降级策略。
- **投资视角**: AI公司的模型稳定性是伪命题，部署配置可能随意改变模型输出。投资时要关注模型治理和透明度，否则有道德和法律风险。
- **内容视角**: 可以拍短视频："你信的AI可能说谎——测试大模型对伪科学的立场，结果惊人"，引发讨论AI可信度。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.22513v1)