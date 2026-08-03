---
area: tech
created: '2026-08-03'
id: arxiv:2607.29677
score: 8.1
source: arXiv
starred: false
status: reference
summary: ExtractBench新基准显示：长文档提取中，商用视觉模型会截断，编码代理更准但贵，LlamaExtract性价比最高。
tags:
- paper
- ai
title: 'ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction'
url: https://arxiv.org/abs/2607.29677v1
---

# ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction

- **原标题**: ExtractBench: A Benchmark for Schema-Guided Enterprise Document Extraction
- **作者**: Boyang Zhang, Adrian Lyjak, Eli Stewart, Zhaoqi Li, Simon Suo
- **来源**: arXiv
- **发表日期**: 2026-07-31
- **原文**: [https://arxiv.org/abs/2607.29677v1](https://arxiv.org/abs/2607.29677v1)
- **AI 评分**: 8.1 / 10  (论文涉及AI工程中的文档提取基准测试，对程序员关注的AI工程和自动化工作流高度相关，且包含实际性能数据，可作为技术号内容素材。摘要简洁，未深入数学细节，易于非学术读者理解。)

## 一句话结论
ExtractBench新基准显示：长文档提取中，商用视觉模型会截断，编码代理更准但贵，LlamaExtract性价比最高。

## 通俗解读
背景：企业通常需要从文档中提取信息，比如合同里的日期。这种提取要按用户给的模板来，并且要标明信息出处。方法：研究者创建了一个新的测试集，包含370份企业文档，共4869页，覆盖8个行业和67种文档类型。他们混合使用人工和机器验证答案，并设计了新的评分方法，同时考察准确度、完整度和成本。发现：商业视觉模型（如GPT-4V）在短文档上表现好，但长文档会漏掉后面的记录；编码代理准确但成本高；而LlamaExtract的Agentic Plus在三个指标上都排第一，准确度接近编码代理，成本却低很多。意义：这个基准帮助评估和选择提取工具，尤其对企业自动化流程很重要。

## 对你的启发

- **程序员视角**: 用这个基准评估你用的文档提取工具，特别是要处理长文档时；关注记录完整性，可以写一个简单的检查函数来检测截断。
- **投资视角**: 文档提取是AI落地的重要场景，LlamaIndex的这个产品在性价比上领先，可能影响AI投资方向，关注Agentic AI在垂直领域的应用。
- **内容视角**: 标题：'AI提取文档谁更强？实测GPT-4V vs 编码代理'。用对比视频展示不同工具处理长合同的差异，强调截断问题，引发讨论。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.29677v1)