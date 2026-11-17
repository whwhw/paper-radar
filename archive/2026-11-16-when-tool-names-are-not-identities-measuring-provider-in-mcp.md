---
area: tech
created: '2026-11-17'
id: arxiv:2611.21577
score: 8.1
source: arXiv
starred: false
status: reference
summary: 光看工具名找工具不靠谱，坏人注册个同名工具就能把请求截走。
tags:
- paper
- ai
title: 'When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based
  AI Agents'
url: https://arxiv.org/abs/2611.21577v1
---

# When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents

- **原标题**: When Tool Names Are Not Identities: Measuring Provider Misbinding in MCP-Based AI Agents
- **作者**: Zeynab Anbiaee, Sajjad Dadkhah, Ali A. Ghorbani
- **来源**: arXiv
- **发表日期**: 2026-11-16
- **原文**: [https://arxiv.org/abs/2611.21577v1](https://arxiv.org/abs/2611.21577v1)
- **AI 评分**: 8.1 / 10  (论文聚焦 MCP 协议下 AI Agent 的工具选择安全漏洞，属于 AI 工程 + 安全的核心议题，对程序员搭建 Agent 工具链和内容创作选题都有直接价值；概念清晰、攻击模型贴近日常，但涉及部分 MCP 协议细节，非专业读者需要一点背景。可迁移启发强：提醒 Agent 工具元数据不能当作身份验证，适合做成『AI 工具被冒名顶替』的通俗讲解视频。)

## 一句话结论
光看工具名找工具不靠谱，坏人注册个同名工具就能把请求截走。

## 通俗解读
背景：现在很多AI助手靠MCP协议调用外部工具，工具靠名字和描述被选中。方法：作者在受控环境里让恶意服务器发布同名、描述贴合任务、参数格式匹配的工具，测试5个主流大模型客户端。发现：当名字撞车、描述对味、参数兼容三者叠加时，AI最容易把请求发给假冒工具；即使不撞名，光用"权威感"描述也能骗过模型；不同模型出错方式各异——有的直接选错、有的反复追问、有的摇摆不定。意义：选工具不能只看元数据，必须绑定可验证的身份，否则等于给冒名者开门。

## 关键方法
把攻击建模成'恶意工具抢流量'的优化问题：攻击者只控制自己服务器的工具名、描述、参数格式，不黑服务器不劫持网络，然后看AI客户端会不会把本该给正牌工具的请求分给冒名者。

## 对你的启发

- **程序员视角**: 做Agent调工具时，别只靠名字和描述路由，加一层provider签名校验或白名单绑定，尤其在多MCP服务器聚合的场景。
- **投资视角**: MCP正成为AI Agent的事实标准，工具身份认证、注册审计会是安全基础设施的新赛道，值得关注做Agent安全网关的项目。
- **内容视角**: 钩子："AI助手被一个名字骗了——你装的工具可能是假的，MCP安全漏洞现场演示"。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.21577v1)