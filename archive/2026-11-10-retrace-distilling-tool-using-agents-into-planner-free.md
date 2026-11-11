---
area: tech
created: '2026-11-11'
id: arxiv:2611.14492
score: 8.8
source: arXiv
starred: false
status: reference
summary: 让 AI 代理把自己的判断整理成流程图，之后每次都执行固定流程，不再调用大模型；成本降两成多，速度快上百倍。
tags:
- paper
- ai
title: 'ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows'
url: https://arxiv.org/abs/2611.14492v1
---

# ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows

- **原标题**: ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows
- **作者**: Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta
- **来源**: arXiv
- **发表日期**: 2026-11-10
- **原文**: [https://arxiv.org/abs/2611.14492v1](https://arxiv.org/abs/2611.14492v1)
- **AI 评分**: 8.8 / 10  (这篇论文直接切中AI Agent工程化落地的核心痛点（用代码替代LLM做流程决策来降本提速），对做自动化工作流的程序员有极强可迁移性；方法思路清晰（从跑通的日志里抽取规则），无需深奥数学即可理解，还能做成抖音'为什么你的Agent太贵太慢'的爆款选题。)

## 一句话结论
让 AI 代理把自己的判断整理成流程图，之后每次都执行固定流程，不再调用大模型；成本降两成多，速度快上百倍。

## 通俗解读
企业里很多重复业务，比如报销审批、客服工单，都有固定流程（SOP）。现在用大模型代理逐行执行：每走一步问一次大模型，就能跑，但每次都要等十几秒、花不少钱。这篇论文发现，代理每次调用工具时写的“理由说明”里藏着判断条件，比如“因为金额>500 才转人工”。ReTrace 把这些理由中的条件抠出来，跨多次运行合并成一份规则文档，再自动生成可执行的工作流；之后由代码逐步判断，只有最后生成工作流这一步依赖平台。结果：生产环境 79 个流程完成率 93.8%，代理执行则是 96.8%；但每个任务成本低 24%，基准测试速度快 130 倍。

## 关键方法
核心是从“推理日志”反推决策条件：代理每次调用工具时都会写明自己为什么这么做，ReTrace 把这些理由转成 if-else 规则，多次运行后去重合并成精简规则集，再编译成代码工作流；出错时用带标签的失败案例自动修补规则。

## 对你的启发

- **程序员视角**: 很适合把 LLM 的决策过程固化：先让 Agent 跑几次并留下日志，再把日志里的“为什么”提炼成规则和代码；正式执行时走 if-else，不调用大模型，等规则出错再触发修补，这就是 AI 工作流的“教一次、跑一万次”模式。
- **投资视角**: 这指向 AI 应用层的成本结构：模型调用不只是被更便宜的推理替代，还可以被“从大模型蒸馏出来的代码”替代；能沉淀 SOP、规则资产的公司，护城河会比只买 API 的更深。
- **内容视角**: 抖音可以拍一条视频《我把 AI 员工的话记录成规则，它以后就不思考了，速度提升 130 倍》。钩子：AI 干活时总自言自语，这些碎碎念里藏着一整套自动化的密码。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2611.14492v1)