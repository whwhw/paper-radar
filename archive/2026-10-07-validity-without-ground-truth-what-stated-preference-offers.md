---
area: tech
created: '2026-10-08'
id: arxiv:2610.10506
score: 8.4
source: arXiv
starred: false
status: reference
summary: 有些问题没有标准答案，用经济学‘望闻问切’也能分辨语言模型好坏。
tags:
- paper
- ai
title: 'Validity Without Ground Truth: What Stated-Preference Economics Offers the
  Evaluation of Language Models'
url: https://arxiv.org/abs/2610.10506v1
---

# Validity Without Ground Truth: What Stated-Preference Economics Offers the Evaluation of Language Models

- **原标题**: Validity Without Ground Truth: What Stated-Preference Economics Offers the Evaluation of Language Models
- **作者**: Daniel Robert Kling Alexander, Catherine Louise Kling
- **来源**: arXiv
- **发表日期**: 2026-10-07
- **原文**: [https://arxiv.org/abs/2610.10506v1](https://arxiv.org/abs/2610.10506v1)
- **AI 评分**: 8.4 / 10  (将计量经济学中的陈述偏好效度框架迁移到LLM评估，强烈关联AI与复杂系统领域；概念清晰、无复杂公式，有易懂类比；对程序员构建AI评估管线、内容创作者做AI评测脚本都有直接启发。)

## 一句话结论
有些问题没有标准答案，用经济学‘望闻问切’也能分辨语言模型好坏。

## 通俗解读
背景：很多问题（如‘该选哪个政策’）没有唯一正确答案，传统打分法失效。方法：借用在经济学中用了50年的‘陈述偏好’评估框架，用内容效度、结构效度等指标来检查模型回答是否自洽。发现：用一份水质价值调查问卷测试六个模型，两个旧模型连‘收入越高愿付越多’这种常识都通不过，两个新模型则通过所有理论检验，但在收敛效度上出现分歧。意义：通过检验只说明回答自洽，不等于正确，但给无标准答案的评估提供了新思路。

## 关键方法
不看答案对错，看回答是否符合经济理论预测：比如需求曲线向下倾斜、支付意愿随商品范围或收入变化。模型若违背这些基本常识，就不靠谱。

## 对你的启发

- **程序员视角**: 可借鉴这套‘无 ground truth 评估’思路，为聊天机器人或推荐系统设计逻辑一致性测试，比如让模型在价格变化时给出合理反应，自动检测自相矛盾。
- **投资视角**: 对AI赛道：评估标准正从‘答对’转向‘答得自洽’，这会影响对模型商业化成熟度的判断，尤其涉及决策辅助的场景。
- **内容视角**: 抖音钩子：‘没有标准答案的题，AI怎么打分？经济学家想出绝招，结果两个旧模型当场翻车！’

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.10506v1)