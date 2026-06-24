---
area: tech
created: '2026-06-24'
id: arxiv:2606.24855
score: 8.1
source: arXiv
starred: false
status: reference
summary: 公开了一套全流程数据配方，用10万条数据训练出的智能体模型比目前最强的开源模型还强4%。
tags:
- paper
- ai
title: 'OpenThoughts-Agent: Data Recipes for Agentic Models'
url: https://arxiv.org/abs/2606.24855v1
---

# OpenThoughts-Agent: Data Recipes for Agentic Models

- **原标题**: OpenThoughts-Agent: Data Recipes for Agentic Models
- **作者**: Negin Raoof, Richard Zhuang, Marianna Nezhurina, Etash Guha, Atula Tejaswi
- **来源**: arXiv
- **发表日期**: 2026-06-23
- **原文**: [https://arxiv.org/abs/2606.24855v1](https://arxiv.org/abs/2606.24855v1)
- **AI 评分**: 8.1 / 10  (核心领域AI：高度相关，Agent模型是AI工程热点；概念清晰但含消融实验细节，通俗性中等；可启发程序员设计自动化工作流，内容创作者可做AI工具讲解脚本。)

## 一句话结论
公开了一套全流程数据配方，用10万条数据训练出的智能体模型比目前最强的开源模型还强4%。

## 通俗解读
背景：训练AI智能体（能自己操作电脑、写代码的那种）需要大量高质量数据，但大家不太清楚具体怎么配数据。方法：作者开源了完整的数据处理流水线，并通过100多次对比实验，仔细研究了每个环节的影响，比如任务来源和多样性。发现：用这个流水线生成的10万条训练数据微调Qwen3-32B模型，在7个智能体测试中平均得分44.8%，比之前最好的开源模型高4个百分点。意义：这套公开的数据“配方”让更多人能复现和改进，加速智能体AI的发展。

## 关键方法
通过100多次消融实验，系统性地研究了数据流水线各环节（如任务来源、多样性）对模型性能的影响，并最终确定了最佳数据配比。

## 对你的启发

- **程序员视角**: 可以借鉴他们的数据流水线思路，为自己的AI项目构建高质量训练数据，比如通过自动生成和过滤步骤收集任务数据。
- **投资视角**: 这表明开源模型正在快速追赶，智能体赛道竞争加剧，关注能提供高效数据工具或模型的初创公司。
- **内容视角**: 做一个“AI智能体数据炼丹”主题视频，展示如何用开源流水线训练自己的智能体，吸引程序员和AI爱好者。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2606.24855v1)