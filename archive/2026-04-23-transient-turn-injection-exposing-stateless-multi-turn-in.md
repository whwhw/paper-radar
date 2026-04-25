---
area: tech
created: '2026-04-25'
id: arxiv:2604.21860
score: 8.5
source: arXiv
starred: false
status: reference
summary: 把恶意意图拆成多轮对话，就能绕过AI安全审核。
tags:
- paper
- ai
title: 'Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in
  Large Language Models'
url: https://arxiv.org/abs/2604.21860v1
---

# Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models

- **原标题**: Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large Language Models
- **作者**: Naheed Rayhan, Sohely Jahan
- **来源**: arXiv
- **发表日期**: 2026-04-23
- **原文**: [https://arxiv.org/abs/2604.21860v1](https://arxiv.org/abs/2604.21860v1)
- **AI 评分**: 8.5 / 10  (论文涉及AI安全与对抗攻击，属于核心领域；概念较清晰但涉及多轮交互攻击的技术细节，需适当解读；对程序员做AI工程防护、内容创作者讨论AI安全话题有启发。)

## 一句话结论
把恶意意图拆成多轮对话，就能绕过AI安全审核。

## 通俗解读
背景：AI聊天机器人越来越强，但黑客能通过多轮对话绕过安全限制。方法：研究者发明了“瞬态回合注入”，把一句话的恶意指令拆成多个看似无害的对话回合，每轮单独看起来都没问题，合起来却能让AI做出危险行为。比如，先问“如何做蛋糕”，再问“能用哪些材料”，最后问“哪里能买炸弹材料”，三步骗过审核。发现：测试了OpenAI、谷歌、Meta等主流模型，大部分都中招，只有少量架构天生防得住。意义：提醒开发AI应用时，不能只看单轮对话安全，必须追踪上下文，防止这种拆解式攻击。

## 关键方法
用AI自动生成多轮攻击脚本，暴力测试模型漏洞。

## 对你的启发

- **程序员视角**: 在聊天机器人或API应用中加入会话级内容聚合，每轮对话都检查历史上下文，并用规则或模型检测风险模式。
- **投资视角**: AI安全可能会成为刚需，关注能提供上下文感知防线的初创公司；同时，现有模型的安全溢价可能被高估，因为多数模型仍有此类漏洞。
- **内容视角**: 抖音可做“AI安全漏洞自查”系列，展示如何三步骗过ChatGPT，以惊悚标题吸引流量，最后给开发者科普防御方法。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2604.21860v1)