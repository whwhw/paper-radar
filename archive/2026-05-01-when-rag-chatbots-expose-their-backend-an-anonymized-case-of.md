---
area: tech
created: '2026-05-04'
id: arxiv:2605.00796
score: 8.1
source: arXiv
starred: false
status: reference
summary: 病人用AI聊天机器人竟能轻松泄露患者对话和系统配置，开发者要注意了。
tags:
- paper
- ai
title: 'When RAG Chatbots Expose Their Backend: An Anonymized Case Study of Privacy
  and Security Risks in Patient-Facing Medical AI'
url: https://arxiv.org/abs/2605.00796v1
---

# When RAG Chatbots Expose Their Backend: An Anonymized Case Study of Privacy and Security Risks in Patient-Facing Medical AI

- **原标题**: When RAG Chatbots Expose Their Backend: An Anonymized Case Study of Privacy and Security Risks in Patient-Facing Medical AI
- **作者**: Alfredo Madrid-García, Miguel Rujas
- **来源**: arXiv
- **发表日期**: 2026-05-01
- **原文**: [https://arxiv.org/abs/2605.00796v1](https://arxiv.org/abs/2605.00796v1)
- **AI 评分**: 8.1 / 10  (直接相关AI安全和隐私工程，对程序员有工程启发（如客户端通信安全），通俗度高但涉及少量技术细节。)

## 一句话结论
病人用AI聊天机器人竟能轻松泄露患者对话和系统配置，开发者要注意了。

## 通俗解读
背景：医院用RAG技术做医疗问答机器人，号称安全。方法：研究人员用AI帮忙找漏洞，再用浏览器开发者工具手动验证。发现：打开浏览器工具就能看到系统提示词、知识库内容，甚至最近1000条患者对话，都不用登录。意义：这类AI系统存在严重隐私风险，普通浏览器就能扒光数据，上线前必须做独立安全审查。

## 关键方法
两阶段测试：先用Claude AI生成攻击假设，再手动用Chrome开发者工具检查网络请求和存储数据。

## 对你的启发

- **程序员视角**: 如果你在开发RAG聊天机器人，务必把敏感配置和对话记录全放服务器端，不要通过前端网络暴露任何内部数据。
- **投资视角**: 医疗AI安全风险高，投资前要核查项目的隐私防护能力，这类漏洞一旦曝光会引发信任危机和法律风险。
- **内容视角**: 抖音标题：《你的AI病历人人能看？揭秘医疗聊天机器人泄露隐私》。用黑客视角演示浏览器点几下就能看到患者对话，制造反差感。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2605.00796v1)