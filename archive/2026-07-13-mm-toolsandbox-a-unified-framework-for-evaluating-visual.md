---
area: tech
created: '2026-07-14'
id: arxiv:2607.11818
score: 9.4
source: arXiv
starred: false
status: reference
summary: AI看图片调用工具成功率不到50%，看懂图比会规划还难。
tags:
- paper
- ai
title: 'MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents'
url: https://arxiv.org/abs/2607.11818v1
---

# MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents

- **原标题**: MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents
- **作者**: Kaixin Ma, Di Feng, Alexander Metz, Jiarui Lu, Eshan Verma
- **来源**: arXiv
- **发表日期**: 2026-07-13
- **原文**: [https://arxiv.org/abs/2607.11818v1](https://arxiv.org/abs/2607.11818v1)
- **AI 评分**: 9.4 / 10  (核心领域AI+科技，高度相关。摘要清晰，无复杂公式，易于理解。对程序员AI工程（工具调用评估）和内容创作（失败分析做视频选题）都有直接启发。)

## 一句话结论
AI看图片调用工具成功率不到50%，看懂图比会规划还难。

## 通俗解读
背景：AI助手要学会“看图片调用工具”，比如从一张外卖截图里找到订单号再取消订单。但现有评测大多只测单张图、单次任务，太简单。方法：研究者做了一个叫MM-ToolSandBox的测试平台，包含500多个工具和16个场景，支持多图多轮对话，还会中途修改目标或报错，模拟真实对话。他们自动生成了258个标准场景和50个UI交互场景，并用人类验证。发现：测试了12个模型（从40亿参数到顶级闭源模型），结果最好的成功率也不到50%。失败分析显示，53%的错误是因为模型没能从图片中正确提取信息（比如看错数字），而任务规划反而做对了。小模型主要是“不知道干什么”，大模型则是“看不到细节”，问题根源不同。意义：当前模型视觉精度是瓶颈，未来需要针对不同大小模型用不同方法改进。

## 关键方法
自动化场景生成：用信息流图规划任务步骤，再筛选高质量场景，类似程序员用流程图写测试用例。

## 对你的启发

- **程序员视角**: 在构建多模态Agent时，可借鉴其信息流图规划思想，先画出数据依赖关系再生成测试场景，提高测试覆盖率。
- **投资视角**: AI视觉调用工具能力尚未成熟，短期可关注提升视觉精度的技术（如高分辨率视觉编码），投资标的偏向底层感知层。
- **内容视角**: 抖音标题：《AI看截图总翻车？苹果最新研究揭示致命弱点》，用外卖取消订单等生活例子演示AI读图失败，引发观众共鸣。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.11818v1)