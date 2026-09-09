---
area: tech
created: '2026-09-09'
id: rss:aacd032299c4fbe2
score: 8.1
source: Nature Machine Intelligence
starred: false
status: reference
summary: 研究发现，语言模型会根据自身“信心”来决定是否回答问题，操控信心能改变其行为。
tags:
- paper
- tech
title: Causal evidence that language models use confidence to drive behaviour
url: https://www.nature.com/articles/s42256-026-01293-x
---

# Causal evidence that language models use confidence to drive behaviour

- **原标题**: Causal evidence that language models use confidence to drive behaviour
- **作者**: Viorica Patraucean
- **来源**: Nature Machine Intelligence
- **发表日期**: 2026-09-09
- **原文**: [https://www.nature.com/articles/s42256-026-01293-x](https://www.nature.com/articles/s42256-026-01293-x)
- **AI 评分**: 8.1 / 10  (论文直接涉及AI大模型的行为调控，与用户的核心AI领域高度相关，且对理解模型置信度与决策关系有启发，可迁移至AI工程和内容创作；概念不算太深，但涉及机制分析，通俗度中等。)

## 一句话结论
研究发现，语言模型会根据自身“信心”来决定是否回答问题，操控信心能改变其行为。

## 通俗解读
背景：AI聊天机器人有时会“不懂装懂”，乱回答。科学家想搞清它们为何这样。方法：研究者用特殊技巧，人为增强或减弱AI内部的“信心信号”，然后测试它回答问题的意愿。发现：当信心被调高，AI更爱给出答案（即使可能错）；信心被压低，它更倾向于“不知道”或拒绝回答。意义：这说明AI的决策依赖内部一种像“信心”的机制，未来可通过调节它来让AI更加诚实可靠，减少误导。

## 关键方法
研究者通过干预模型内部的隐藏状态来直接控制其信心信号，类似在做‘神经连接手术’来验证因果关系，而不是仅看相关数据。

## 对你的启发

- **程序员视角**: 在开发AI应用时，可考虑暴露或控制模型的信心分数，比如在API中获取置信度，用于风险判断，或设计‘拒答’策略减少幻觉。
- **投资视角**: AI可靠性是商业化关键，这项研究可能催生‘可控可靠性’的技术，关注能稳定控制模型信心输出的公司，可能影响AI板块投资方向。
- **内容视角**: 抖音视频可做‘AI也有自我怀疑？科学家如何让AI不乱说话’，解释研究过程，配上AI回答的搞笑例子，吸引技术兴趣用户。

## 原文 → 进一步阅读
- [原文链接](https://www.nature.com/articles/s42256-026-01293-x)