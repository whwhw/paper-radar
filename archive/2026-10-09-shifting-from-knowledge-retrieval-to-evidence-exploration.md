---
area: tech
created: '2026-10-09'
id: rss:d4d992015c972e7b
score: 8.0
source: Nature Machine Intelligence
starred: false
status: reference
summary: 科研AI进入新阶段：不再只是查资料，而是会主动找证据、拼出结论。
tags:
- paper
- tech
title: Shifting from knowledge retrieval to evidence exploration and synthesis
url: https://www.nature.com/articles/s42256-026-01313-w
---

# Shifting from knowledge retrieval to evidence exploration and synthesis

- **原标题**: Shifting from knowledge retrieval to evidence exploration and synthesis
- **作者**: Krishna C. Bulusu
- **来源**: Nature Machine Intelligence
- **发表日期**: 2026-10-09
- **原文**: [https://www.nature.com/articles/s42256-026-01313-w](https://www.nature.com/articles/s42256-026-01313-w)
- **AI 评分**: 8.0 / 10  (论文讨论AI深度研究代理从知识检索转向证据探索与综合，直接属于AI核心领域；概念通俗易懂，没有复杂公式，普通人也能理解证据整合的思路；对程序员做自动化工作流、内容创作者讲解AI工具有很好的迁移启发，也能帮助理解AI趋势判断。)

## 一句话结论
科研AI进入新阶段：不再只是查资料，而是会主动找证据、拼出结论。

## 通俗解读
现在生物医学研究不缺数据，缺的是把零散证据拼成结论的能力。以前的AI主要做'检索'：你问问题，它给你一堆相关论文。DeepEvidence换了个思路——它像一个侦探，先找到每一条证据，再把证据之间的关系（支持、矛盾、强弱）显式画出来，最后综合成判断。相当于从'图书馆管理员'升级成'研究员助手'。意义在于：这可能是AI从'信息工具'走向'科学发现伙伴'的关键一步，也让研究者能更快看清一个结论到底靠不靠谱。

## 关键方法
把'证据'当成一等公民：不是只存文本片段，而是为每条证据建立结构化表示（来源、结论、方向、强度），再在这些表示上做推理和综合。类比：以前是把书扔给你，现在是帮你做出一张带箭头和权重的论证地图。

## 对你的启发

- **程序员视角**: 做RAG或Agent时，别只做向量检索+拼prompt。可以引入'explicit evidence graph'：每条引用附上元数据（支持/反对、置信度、来源），让Agent在图上推理，输出可追溯、可审计的结论链。
- **投资视角**: AI4Science是长周期大方向，'证据综合型Agent'可能成为药研、临床决策的基础设施。关注能把科研工作流自动化的团队，而不是只做聊天界面的。
- **内容视角**: 抖音钩子：'AI终于不瞎编了？它现在会像侦探一样找证据、画关系图，告诉你一个结论到底站不站得住脚。'演示一个争议问题，让AI列出支持和反对的证据。

## 原文 → 进一步阅读
- [原文链接](https://www.nature.com/articles/s42256-026-01313-w)