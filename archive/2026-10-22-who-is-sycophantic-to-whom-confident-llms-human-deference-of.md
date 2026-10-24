---
area: tech
created: '2026-10-24'
id: arxiv:2610.31579
score: 8.1
source: arXiv
starred: false
status: reference
summary: AI越自信，人越容易信错——信任校准彻底失灵。
tags:
- paper
- ai
title: Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse
  of Trust Calibration
url: https://arxiv.org/abs/2610.31579v1
---

# Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration

- **原标题**: Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration
- **作者**: Deepthika S, Pawni Yadav, B. Sankar
- **来源**: arXiv
- **发表日期**: 2026-10-22
- **原文**: [https://arxiv.org/abs/2610.31579v1](https://arxiv.org/abs/2610.31579v1)
- **AI 评分**: 8.1 / 10  (这是一篇AI领域核心论文，研究LLM的自信错误如何导致人类信任崩塌，与用户关注的AI工程和认知科学高度契合，且实验设计直观、结论生动，容易转化为抖音技术号内容；虽然涉及实验统计术语但核心机制易懂，值得作为AI可信度话题的素材。)

## 一句话结论
AI越自信，人越容易信错——信任校准彻底失灵。

## 通俗解读
研究问了一个反向问题：不是AI迎合人，而是人会不会迎合自信的AI？32人分别和5个同一模型的AI助教聊科学话题，暗中把每个助教的事实以0%、25%、50%、75%、100%的比例换成听起来合理的假话，且所有助教都表现得十足自信。结果：满分10分的测验，得分从7.4跌到2.9；被替换成假话的题目里，60%的人选了假答案（正常情况只有11%）。更糟的是，人对假答案的信心和真答案一样高（8.4/10），原本能靠'信心高低'分辨对错的能力消失了，事后信任评分却几乎不动。模型本身几乎不谄媚，被质疑也不让步。意义是：可信度是人和AI配对后的共同属性，评估谄媚要双向看。

## 关键方法
把'错误率'当成旋钮：同一模型生成5个助教，按0到100%的比例用貌似合理的假事实替换真事实，再让每位助教都用满格自信说话。之后用突击测验同时给出正确项、植入的假项和两个干扰项，并让用户给每个答案打信心分——这样就能分离出'用户信错'和'用户信对但有信心'两种状态。

## 对你的启发

- **程序员视角**: 做AI应用时，别让模型'永远自信'，要在UI层做逐条claim的可信度标注（来源、置信度、可验证链接），否则用户会把错误当事实吸收；内部评测也该加'人-AI配对'指标，而不只测模型单侧。
- **投资视角**: AI赛道里'模型能力'不是护城河，'可信度可读性'才是——能做出claim级溯源与校准的产品（如搜索、医疗、金融Agent）更有长期价值；对纯靠'语气自信'卖AI的团队要警惕，用户信任崩塌是系统性风险。
- **内容视角**: 抖音钩子：'AI越自信，你越容易被骗？一个实验让32个人集体信错'——用0%/50%/100%三档假话助教做对照演示，结尾抛'你每天问的AI，信心是校准过的还是装出来的？'

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.31579v1)