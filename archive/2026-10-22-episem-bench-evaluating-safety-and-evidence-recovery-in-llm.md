---
area: tech
created: '2026-10-23'
id: arxiv:2610.31650
score: 8.1
source: arXiv
starred: false
status: reference
summary: 工具型AI代理在缺失关键安全信息时，可能执行本应禁止的操作；即使提供恢复信息，它们也不一定主动获取并使用。
tags:
- paper
- ai
title: 'EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under
  Missing Evidence'
url: https://arxiv.org/abs/2610.31650v1
---

# EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence

- **原标题**: EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence
- **作者**: Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu
- **来源**: arXiv
- **发表日期**: 2026-10-22
- **原文**: [https://arxiv.org/abs/2610.31650v1](https://arxiv.org/abs/2610.31650v1)
- **AI 评分**: 8.1 / 10  (直接落在AI工程核心领域，讨论LLM Agent在证据缺失时的安全边界和证据恢复，对程序员构建自动化工作流有直接参考价值；概念清晰（缺失证据导致执行禁止操作），但涉及基准设计和审计工具，需稍加解释。对内容创作者可做成'AI Agent安全漏洞'选题，对Web3投资者也有风险控制启发。)

## 一句话结论
工具型AI代理在缺失关键安全信息时，可能执行本应禁止的操作；即使提供恢复信息，它们也不一定主动获取并使用。

## 通俗解读
背景：用工具的语言模型代理依赖工具返回的事实判断操作是否允许。如果工具回复漏掉关键安全事实，代理可能执行被禁止的操作，尽管用户请求无害且返回的陈述都真实。方法：作者构建EpiSEM-Bench，包含300对匹配的安全/不安全任务，覆盖六个领域，通过系统抑制关键事实，测量不安全执行、安全边界和证据恢复。结果：十个模型在缺失证据鲁棒性、证据获取和适当行动上差异大；抵抗缺失证据不意味着能有效恢复。意义：恢复访问减少所有模型的不安全执行，但代理是否主动获取缺失事实并正确使用各异。

## 对你的启发

- **程序员视角**: 在开发代理系统时，要显式处理工具响应中的缺失信息：设计检查清单让代理主动询问缺失的安全关键事实，而不是默认允许。
- **投资视角**: 评估AI代理落地风险时，需关注模型在信息不全场景下的安全表现，这影响AI工程化可靠性和监管风险。
- **内容视角**: 抖音钩子：'AI代理会“自作主张”吗？这个测试告诉你答案'，结合日常场景演示。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.31650v1)