# Human Texture Engine Summary

## 执行结论

当前 Phase 8 能把钩子、规则、破局、代价、设定揭示写出来，但 5 章样本仍明显像“机制运行展示”。问题不在句子是否通顺，而在每章的场景、人物、情绪和关系大多服务于信息传递，缺少人物私心、生活阻力、关系余波和非工具性细节。

建议自研 Human Texture Engine，并把它作为现有 Planner / Writer / Reviewer / Polisher 之间的一层叙事质感合同，而不是一个后置“去 AI 味”工具。

## 当前 5 章诊断摘要

- 系统展示感：C3 矿洞、C4 复检、C5 古镜/元启大量把设定直接显示给读者，人物经常变成理解机制的屏幕。
- 人物功能件：胖少年、执事、测试官、甚至柳青砚常承担“证人、提示、质问、解释”功能，个人生活和自我目标不足。
- 情绪空心化：恐惧、愤怒、恨意常被命名并转化为积分/杂质/蓝光，缺少身体和行为上的迟滞后果。
- 场景生活质感不足：饭堂、寝舍、后山、矿洞都具备可写空间，但最终大多只作为信息触发器。
- 代价后果不够：烧掉情绪、手骨撞墙、信任破裂等都出现了，但没有在后续生活、关系和选择中持续造成麻烦。
- 潜力：C1 旧衣、C2 测试官“枯井”、C3 饭堂木屏风、C4 胖少年作证、C5 “我也没底”都能扩展成真正的人味节点。

完整分析见 `audit/current_5ch_failure_diagnosis.md`。

## 评价框架摘要

Human Texture 评价框架建议设置 10 个维度：人物可信度、私心/羞耻/犹豫、情绪真实度、关系摩擦、场景生活质感、非工具性细节、信息露出自然度、代价真实后果、语言光泽与余味、系统展示感。每项都落到 Planner / Writer / Reviewer / Polisher 中可审查的交付物。

完整框架见 `research/human_texture_evaluation_rubric.md`。

## 调研摘要

行业工具中，Sudowrite、Novelcrafter、NovelAI 值得借鉴“故事圣经 / Codex / Lorebook / Memory”的上下文组织；Fictionary、AutoCrit、ProWritingAid 值得借鉴编辑维度；GPTZero、Originality.ai、人类化工具只适合作为风险参考，不适合作为目标函数。

GitHub 项目中，`NovelGenerator` 的 StoryContextDB 与 anti-LLM prompt、`knowrite` 的多阶段 novel engine、`novel-bot` 的本地 memory/context 技能结构最值得借鉴。`pulpgen` 和 `novel-bot` 可做小规模可复现实验。不建议直接 fork 大型项目。

## 最小可行方案

第一阶段只做一个 Human Texture MVP：

1. 在 Planner 输出 `human_texture_packet`：人物私心、羞耻/回避、关系债、场景生活阻力、信息载体、代价余波。
2. 在 Writer 注入微动作、非工具细节、关系摩擦和后果延迟。
3. 在 Reviewer 使用 10 维 rubric 打分，低分项必须回到对应层修正。
4. Polisher 只处理语言光泽和余味，不负责补结构。
5. 用当前 5 章作为 baseline，做 A/B 人审和 rubric 评分验证。

## 下一步

建议第一阶段先建立 20-40 个中文网文“人味片段”样本库与 20 个负样本库，然后在不动全量 skill-pack 的前提下做一个实验性 wrapper：读取章节计划、生成 Human Texture Packet、让 Writer 只改一个章节片段，再用 Reviewer rubric 对比 baseline。
