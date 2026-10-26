---
area: tech
created: '2026-10-26'
id: arxiv:2610.32891
score: 8.4
source: arXiv
starred: false
status: reference
summary: AI 自我优化代码：跑得更快，但更耗电，总账常亏。
tags:
- paper
- ai
title: Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based
  Code Optimizations
url: https://arxiv.org/abs/2610.32891v1
---

# Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based Code Optimizations

- **原标题**: Green Code or Costly Code? Evaluating the Energy Costs of Iterative LLM-Based Code Optimizations
- **作者**: Sadra Emami, Benjamin Weigell, Mohammad Reza Mousavi, Gunel Jahangirova, Hugo Araujo
- **来源**: arXiv
- **发表日期**: 2026-10-23
- **原文**: [https://arxiv.org/abs/2610.32891v1](https://arxiv.org/abs/2610.32891v1)
- **AI 评分**: 8.4 / 10  (论文属于AI工程与绿色计算交叉领域，直接回应用户对AI工作流和能效的关注；概念清晰，有执行次数、查询数等日常类比，但含部分测量术语；结论（LLM优化代码反而更耗能、MoE架构更省电、限制输出token最能省）对程序员写AI工具脚本和内容创作者做反直觉选题都很有启发。)

## 一句话结论
AI 自我优化代码：跑得更快，但更耗电，总账常亏。

## 通俗解读
背景：大家默认 LLM 优化代码、跑得更快就等于更省电。方法：作者拿 1000 道编程题，让 11 个开源模型多轮自我改进，同时用硬件级仪器量整机耗电。发现：生成阶段耗电 0.79 到 8.68 兆焦，约等于几百到几千次 GPT-4 查询；44 种配置里 42 种产出的代码每道题比人类参考更耗电，高出 4% 到 886%。意义：快和省电不是一回事，省下的电要跑几百万次才回本；选专家混合架构比调解码参数更省电。

## 关键方法
不只是测代码跑多久，而是全程用硬件电表量整机耗电，把生成和运行分开算；再用“回本点”衡量：优化过程多花的电，要执行多少次才赚回来，这个思路可直接用来评估任何自动化流水线的真实成本。

## 对你的启发

- **程序员视角**: 别把“快了”当“省了”。上线 AI 代码优化前先测总能耗与回本次数；优先选 MoE 模型、限制最大输出长度（最多省 69% 电），对调用频率低的脚本，裸写往往更划算。
- **投资视角**: AI 的隐藏成本在推理电费，不只是芯片。MoE 架构、输出长度控制是更关键的能效变量，利好高效推理路线与节能基础设施；对“AI 自动化=降本”的说法保持怀疑。
- **内容视角**: 钩子：“让 AI 帮你优化代码，电费可能涨 8 倍——你省的是时间，亏的是钱包。”拍成实测视频：同一段代码人工版与 AI 版比速度、比耗电，揭穿“快就是省”的直觉陷阱。

## 原文 → 进一步阅读
- [原文链接](https://arxiv.org/abs/2610.32891v1)