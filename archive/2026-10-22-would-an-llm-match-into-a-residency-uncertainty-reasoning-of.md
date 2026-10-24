---
area: tech
created: '2026-10-24'
id: arxiv:2610.31586
score: 8.4
source: arXiv
starred: false
status: reference
summary: 开源医疗大模型考试能过线，但不知道自己何时会错，医学微调反而降低了准确性。
tags:
- paper
- ai
title: Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of
  Open Language Models on the Spanish MIR Examination
url: https://arxiv.org/abs/2610.31586v1
---

# Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination

- **原标题**: Would an LLM Match into a Residency? Uncertainty, Reasoning and Image Use of Open Language Models on the Spanish MIR Examination
- **作者**: Miguel Fernandez-de-Retana, Unai Zulaika, Ruben Sanchez-Corcuera, Aritz Bilbao-Jayo, Aitor Almeida
- **来源**: arXiv
- **发表日期**: 2026-10-22
- **原文**: [https://arxiv.org/abs/2610.31586v1](https://arxiv.org/abs/2610.31586v1)
- **AI 评分**: 8.4 / 10  (直接落在 AI 核心领域，且涉及医疗健康场景与开源模型部署，对关注 AI 工程和自动化工作流的程序员很有参考价值。研究揭示的‘弃答不划算’‘图像形同虚设’‘置信度不可靠’等结论通俗且有冲击力，既能指导工程实践（别盲信模型自信度、多模态未必真用图），也能做成抖音技术号爆款选题。)

## 一句话结论
开源医疗大模型考试能过线，但不知道自己何时会错，医学微调反而降低了准确性。

## 通俗解读
背景：人们常用医学考试分数证明AI能当医生，但真正部署前还需知道模型是否清楚自己可能出错。方法：用西班牙MIR住院医师考试1552道题测试四个开源模型（8-27B参数），按考试规则评分，并检查弃答、置信度、推理质量和图像使用。发现：三个大模型都能通过考试（排名前600-3000），但弃答从不划算，因为最不确定的答案正确率也超过25%的盈亏线；医学微调减少了过度自信却降低了准确率，且置信度无法区分对错；13-38%的正确答案基于临床不合理的理由，置信度也反映不出；移除或替换图像不影响准确率。意义：模型高分不等于可靠的临床推理和自我认知，部署前需多维度评估。

## 关键方法
用真实考试规则评分，并设计弃答机制、置信度校准、错误理由标注和图像消融实验，从多个角度评估模型可靠性。

## 对你的启发

- **程序员视角**: 在AI应用中，不能只看准确率，要加入不确定性估计和弃答机制，并做消融实验确认模型真的用了输入特征（如图像），避免虚假相关性。
- **投资视角**: 医疗AI落地不能只看基准分数，需关注模型校准和推理可靠性；开源模型在专业领域仍有差距，投资应重视评估工具和可解释性。
- **内容视角**: 抖音钩子：‘AI考过了医生执照，但它敢说自己不会吗？’ 用考试弃答和图像消融的实验，揭示高分背后的盲点。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.31586v1)