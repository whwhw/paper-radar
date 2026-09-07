---
area: tech
created: '2026-09-07'
id: arxiv:2609.05395
score: 8.2
source: arXiv
starred: false
status: reference
summary: 用自动验证的调用链生成训练数据，让小模型追上大模型。
tags:
- paper
- ai
title: 'Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis
  Recipe'
url: https://arxiv.org/abs/2609.05395v1
---

# Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe

- **原标题**: Multi-Step Tool-Calling over Korean Open Public APIs: A Benchmark and a Data-Synthesis Recipe
- **作者**: Dain Kim, Eungi Cho, Kyumin Kim, Shinyeong Noh, Kyuseong Lim
- **来源**: arXiv
- **发表日期**: 2026-09-04
- **原文**: [https://arxiv.org/abs/2609.05395v1](https://arxiv.org/abs/2609.05395v1)
- **AI 评分**: 8.2 / 10  (论文属于AI领域，且涉及工具调用和自动化工作流，与用户核心关注高度相关；概念虽涉及工程细节但整体结构清晰，对程序员的AI工程实践有直接启发。)

## 一句话结论
用自动验证的调用链生成训练数据，让小模型追上大模型。

## 通俗解读
韩国政府规定，公共机构必须用开源且本地部署的AI，这些AI要能接连调用多个政府网站接口来完成实际任务。但开源模型在这种多步操作中表现不佳，且缺乏评估标准。研究者创建了包含145个真实任务的基准测试KOPA-Bench，并提出一种叫EDGE的数据合成方法：它先画出接口调用关系图，然后真的去调用接口，只保留那些成功的连接，再沿着这些可靠路径生成训练数据。用强化学习（GRPO）微调一个9B模型，效果几乎赶上同系列的27B大模型，在KOPA-Bench和BFCL上都大幅提升。

## 关键方法
EDGE（执行验证动态图）：先用人工样例构建接口依赖图，然后真实调用接口，只保留能成功的边，再随机游走生成多步调用路径，最后用这些路径训练模型。

## 对你的启发

- **程序员视角**: 这个方法可以借鉴到微调代码生成模型上：生成训练数据时，不用只看静态代码，而是实际运行，只保留能通过测试的代码，这样能极大减少幻觉。
- **投资视角**: 开源AI正在转向特定领域（如公共数据API调用）的合规部署，这可能催生对私有化部署和本地数据合规服务的需求，值得关注相关基础设施公司。
- **内容视角**: 标题可以叫“让AI少说多做：一个让9B模型超越27B的秘诀”，适合讲数据质量比数据量重要，配合视频展示如何用真实API验证来清洗数据。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2609.05395v1)