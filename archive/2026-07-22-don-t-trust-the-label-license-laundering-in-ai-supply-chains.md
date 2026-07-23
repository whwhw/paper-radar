---
area: tech
created: '2026-07-23'
id: arxiv:2607.20300
score: 8.1
source: arXiv
starred: false
status: reference
summary: AI供应链里超六成链条有许可证被洗掉或偷换，宽松变严格去生存率极低。
tags:
- paper
- ai
title: 'Don''t Trust the Label: License Laundering in AI Supply Chains'
url: https://arxiv.org/abs/2607.20300v1
---

# Don't Trust the Label: License Laundering in AI Supply Chains

- **原标题**: Don't Trust the Label: License Laundering in AI Supply Chains
- **作者**: James Jewitt, Hao Li, Gopi Krishnan Rajbahadur, Bram Adams, Ahmed E. Hassan
- **来源**: arXiv
- **发表日期**: 2026-07-22
- **原文**: [https://arxiv.org/abs/2607.20300v1](https://arxiv.org/abs/2607.20300v1)
- **AI 评分**: 8.1 / 10  (直接涉及AI工程中的供应链合规问题，对程序员有实用价值，但需要解释概念；可启发内容创作或法律风险意识。)

## 一句话结论
AI供应链里超六成链条有许可证被洗掉或偷换，宽松变严格去生存率极低。

## 通俗解读
AI模型从数据集到应用要经过多平台（比如Hugging Face、GitHub）。每个包都有使用许可（比如开源协议），按理说下游应该遵守上游的许可。但科学家追踪了23万条链条，发现62.3%的链条中至少有一个包没有明确许可，而下游却给它贴上了新标签。更严重的是，严格限制的许可（如GPL）几乎全被洗成宽松许可（如MIT），只有不到7%存活，而宽松许可的存活率高达95.1%。这意味着很多AI应用实际在违规使用数据，但没人发现。

## 关键方法
他们从Hugging Face和GitHub爬取数据集、模型和应用信息，构建链条，然后比较每个环节的许可证类型是否一致。

## 对你的启发

- **程序员视角**: 做AI工具时，可以加一个许可证检测模块，自动检查依赖链上的许可证是否一致，避免侵权。
- **投资视角**: 投资AI公司时要检查其数据来源的许可证，许可证不透明可能带来法律风险，影响估值。
- **内容视角**: 可以做一条抖音视频，标题“你的AI模型可能侵权了！”，解析许可证洗白现象，教大家自查工具链。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2607.20300v1)