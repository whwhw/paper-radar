---
area: tech
created: '2026-08-07'
id: arxiv:2608.06377
score: 7.8
source: arXiv
starred: false
status: reference
summary: 语言模型应学会选择性信任上下文，而非一味抵抗或全然忽略。
tags:
- paper
- ai
title: Learning When to Trust via Selective Context Preference Optimization
url: https://arxiv.org/abs/2608.06377v1
---

# Learning When to Trust via Selective Context Preference Optimization

- **原标题**: Learning When to Trust via Selective Context Preference Optimization
- **作者**: Xian Sun, Wei Chow, Yingshuo Wang, Junhao Liu, Wei Gao
- **来源**: arXiv
- **发表日期**: 2026-08-06
- **原文**: [https://arxiv.org/abs/2608.06377v1](https://arxiv.org/abs/2608.06377v1)
- **AI 评分**: 7.8 / 10  (论文涉及AI模型的可信度与选择性信任，属于核心AI领域，且对程序员调优模型有参考价值；但内容偏学术，数学公式和实验细节可能较难懂。)

## 一句话结论
语言模型应学会选择性信任上下文，而非一味抵抗或全然忽略。

## 通俗解读
背景：大语言模型回答问题时常依赖额外信息，但一条误导信息就能把对的答案带偏。现有办法是训练模型抵抗误导，但若模型完全忽略所有上下文，虽显稳实则无用。方法：作者提出SC2W指标衡量误导信息把正确回答变错的频率，并构建了MIST基准，包含四种对照条件（干净、误导、正确、无关）。发现：这种易感性普遍存在。于是提出SCOPE方法，基于DPO算法在四类样本上平衡优化，大幅减少误导翻转率，同时保持对正确或无关上下文的利用。意义：模型应被评估其选择性信任能力，而非单纯抵抗。

## 关键方法
SCOPE：从干净-正确和误导-错误的配对样本中挖掘失败案例，用DPO目标在四类条件平衡的偏好对上优化，而非仅针对误导样本。

## 对你的启发

- **程序员视角**: 在构建AI应用时，可借鉴选择性信任思路，为模型设计上下文可信度评估模块，对输入信号进行加权或过滤，避免被误导信息带偏。
- **投资视角**: 该研究推动模型更可靠地利用信息，可能提升AI在金融、医疗等领域的落地价值，关注相关NLP方向的公司。
- **内容视角**: 趣谈：如何让AI在信息洪流中不迷失？用MIST基准测试你的模型，展示现实场景中的“被带偏”案例，引发对AI可靠性的关注。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2608.06377v1)