---
area: tech
created: '2026-08-02'
id: arxiv:2607.28545
score: 8.1
source: arXiv
starred: false
status: reference
summary: 最强AI在真实故障排查任务中准确率仅25%，离替代值班工程师还差得远。
tags:
- paper
- ai
title: 'ORCA-bench: How Ready Are Language Model Agents for Oncall?'
url: https://arxiv.org/abs/2607.28545v1
---

# ORCA-bench: How Ready Are Language Model Agents for Oncall?

- **原标题**: ORCA-bench: How Ready Are Language Model Agents for Oncall?
- **作者**: Albert Gong, Kyuseong Choi, Abhineet Agarwal, Jason Schechner, Ryan Huang
- **来源**: arXiv
- **发表日期**: 2026-07-30
- **原文**: [https://arxiv.org/abs/2607.28545v1](https://arxiv.org/abs/2607.28545v1)
- **AI 评分**: 8.1 / 10  (论文属于AI工程领域，直接关系到LLM智能体在真实生产环境中的可靠性，对程序员关注的AI工程实践有高度相关性；概念清晰，虽有技术细节但可懂，且对内容创作者有启发性和工程投资判断的启示。)

## 一句话结论
最强AI在真实故障排查任务中准确率仅25%，离替代值班工程师还差得远。

## 通俗解读
背景：大模型能写代码，但值班工程师要面对的是报警、日志、指标等混乱信息，找出故障根因。方法：研究者搭建了一个模拟真实微服务系统的测试平台，包含6天的监控数据、日志和代码，设计了1079个故障排查任务，让五个顶级AI智能体（如Claude）去解决。结果：在中等难度任务中，最好成绩只有25.3%的准确率，困难任务只有10%；最差的模型在40%的报告里会编造不合理的根因。意义：这说明AI在真实运维中远达不到可靠水平，要安全地交给AI处理生产事故，还需要大量工程投入。

## 关键方法
他们构建了一个逼真的模拟环境：用真实的微服务系统（带OpenTelemetry监控）、真实的监控工具（Prometheus、Jaeger等），并让资深运维专家人工审核了故障根因的标注。

## 对你的启发

- **程序员视角**: 在做AI运维工具时，不能只看模型能力，要设计可验证的模拟环境和评估指标，就像ORCA-bench一样，先在小范围测试，再逐步放开权限。
- **投资视角**: AI在运维领域的落地比想象中慢，短期不要高估AI替代运维人员的能力，但长期看，这个赛道值得关注，因为一旦成熟，价值巨大。
- **内容视角**: 可以做个视频标题：“我用AI当了一天程序员，结果它连bug都找不到？”用这个benchmark的案例，直观展示AI的局限性，引发讨论。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.28545v1)