---
area: tech
created: '2026-11-18'
id: arxiv:2611.23202
score: 8.4
source: arXiv
starred: false
status: reference
summary: 给AI代理装『跨组织身份证』，攻击拦截率从43%升至84%，每请求仅多174微秒。
tags:
- paper
- ai
title: 'Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation,
  and Accountability Architecture for Cross-Organization Autonomous AI Agents'
url: https://arxiv.org/abs/2611.23202v1
---

# Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents

- **原标题**: Agent Trust Infrastructure (ATI): A Federated Identity, Trust, Attestation, and Accountability Architecture for Cross-Organization Autonomous AI Agents
- **作者**: Viet K. Nguyen, Mohammad I. Husain
- **来源**: arXiv
- **发表日期**: 2026-11-17
- **原文**: [https://arxiv.org/abs/2611.23202v1](https://arxiv.org/abs/2611.23202v1)
- **AI 评分**: 8.4 / 10  (论文属于AI工程（agent安全/身份认证）核心领域，且与Web3的信任与去中心化身份（PKI联邦信任、无共同根）高度呼应。概念如PKI、Zero Trust、远程认证对程序员可理解，攻击遏制率43%→84%的数字很有说服力，可迁移到AI agent落地安全与内容选题。)

## 一句话结论
给AI代理装『跨组织身份证』，攻击拦截率从43%升至84%，每请求仅多174微秒。

## 通俗解读
不同公司的AI代理协作时，怎么确认对方身份、是否被篡改？现有框架没有统一方案。作者提出ATI：不依赖单一根证书，而是像国家间互认护照一样，让各组织用自己的证书机构互信；执行前检查代理证书、模型、工具和提示词是否经过批准，并通过三重策略校验权限。在8个组织、6种框架的模拟中，启用全部机制后攻击拦截率从43%升至84%，额外开销仅174微秒。这意味着AI代理大规模跨组织协作有了可落地的安全底座。

## 关键方法
类似『护照+签证』体系：每个组织自建发证机构(AgentCA)，互相承认对方签发的代理证书；代理执行任务前需出示证书、证明自己的模型/工具/提示词未篡改，并出示授权策略；请求用IETF的WIMSE令牌和实体证明令牌标准化，方便跨框架集成。

## 对你的启发

- **程序员视角**: 开发多智能体系统时，可以借鉴ATI的『外部安全层』思路——把身份验证和授权做成独立中间件，不侵入业务代码；用短期令牌+三方互认CA替代单点信任根，降低被攻破风险。
- **投资视角**: AI代理安全基础设施是AI工程化的关键卡位，PKI和零信任理念向代理层延伸可能催生新的安全赛道；Web3的DID/可验证凭证方案与ATI思路相通，长期利好去中心化身份方向。
- **内容视角**: 抖音钩子：『两个AI代理互不认识，怎么确认对方没被黑？科学家给了它们一套跨国护照系统，攻击拦截率翻倍！』用谍战片风格讲AI代理身份安全。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.23202v1)