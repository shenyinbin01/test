# Subproject Breakdown

## A. Human Texture v0 收口

| Field | Content |
| --- | --- |
| problem_statement | 人物、信息和关系容易像任务说明，不像人在压力下互相影响。 |
| goal | 固化 Human Texture v0 的最小字段、职责边界和验证结论。 |
| non_goal | 不把 Human Texture 当作最终人味方案，不解决叙述者位置、角色主权和读者代入。 |
| input | `production/human_texture/`、`skill_pack_design/`、`skill_pack_design_test/`。 |
| output | Human Texture v0 closure report and approved patch base decision. |
| owner_role | DeepCode for patching and tests; Hermes / project owner for acceptance. |
| validation_method | Field-level dry run, real-chain rerun if required, Reviewer rubric comparison. |
| success_criteria | 6-field packet can improve human credibility without template padding. |
| failure_signals | 角色变成情绪标签，细节堆砌，Polisher 被迫救结构。 |
| dependency | Current production skill-pack base. |
| next_step | Decide whether Human Texture v0 has formally entered the base branch. |

## B. Work Voice v0 收口

| Field | Content |
| --- | --- |
| problem_statement | 正文缺少稳定讲述者位置，导致段落像功能拼接，作者站位摇晃。 |
| goal | 建立可注入 Planner / Writer / Reviewer / Polisher 的 Work Voice v0 contract。 |
| non_goal | 不做作者模仿，不写 Author Fingerprint，不读取 raw corpus。 |
| input | `production/work_voice/research/`、`mvp/`、`skill_pack_injection_design/`。 |
| output | Skill diff proposal, synthetic dry run report, Work Voice v0 closure report. |
| owner_role | DeepCode for diff and tests; Hermes / project owner for creative boundary acceptance. |
| validation_method | Synthetic dry run, small A/B/C only after approval, Reviewer gate audit. |
| success_criteria | Narrator stance is visible but not preachy; Writer gets compact guidance; Reviewer can catch missing stance. |
| failure_signals | 变成作者腔模仿、老练说教、runtime packet 过长、Polisher 越权。 |
| dependency | Human Texture v0 fields in base or an approved bridge patch. |
| next_step | Resolve patch blocker and review the four target skill diffs. |

## C. Character Agency MVP

| Field | Content |
| --- | --- |
| problem_statement | 角色常被剧情推着走，行动像作者安排而不是角色选择。 |
| goal | 定义角色在场景中的目标、误判、资源、关系压力和可选策略。 |
| non_goal | 不要求主角永远主动出击，不替代剧情规划。 |
| input | Human Texture fields, Work Voice narrator boundary, sample scene beat. |
| output | Character Agency card, Writer conditioning block, Reviewer agency gate. |
| owner_role | Hermes / project owner for literary judgment; DeepCode for schema and tests if patching. |
| validation_method | Compare direct beat drafting against agency-conditioned drafting. |
| success_criteria | 行动能从角色自身压力推出，而不是从作者命令推出。 |
| failure_signals | 主角机械积极、配角只为主角服务、冲突被提前解释干净。 |
| dependency | Work Voice patch review should not be interrupted. |
| next_step | Draft a document-only MVP after Work Voice v0 closure reaches reviewable state. |

## D. Live Leakage MVP

| Field | Content |
| --- | --- |
| problem_statement | 正文缺少低显著、非功能化的活人痕迹，读感容易干净但空。 |
| goal | 设计轻量活人漏痕规则，让人物在行动缝隙里显出生活惯性和压力残留。 |
| non_goal | 不多加细节，不堆小动作，不用细节替代因果。 |
| input | Character Agency baseline, scene pressure, relationship context. |
| output | Live Leakage micro-pattern guide and Reviewer overuse gate. |
| owner_role | Hermes / project owner for taste boundary; DeepCode for schema only if needed. |
| validation_method | Small sample comparison focused on naturalness and density. |
| success_criteria | 细节轻、不抢戏、能暗示人物状态。 |
| failure_signals | 细节显眼、动作堆砌、每段都在表演人味。 |
| dependency | Character Agency MVP baseline. |
| next_step | Wait until agency judgment can distinguish purposeful action from decorative leakage. |

## E. Reader Immersion MVP

| Field | Content |
| --- | --- |
| problem_statement | 读者代入感容易被作者解释、结论提前和情绪指挥破坏。 |
| goal | 定义读者补全空间、解压路径和信息释放节奏。 |
| non_goal | 不解释读者应该怎么想，不把爽点写成说明书。 |
| input | Work Voice boundary, Character Agency action chain, Live Leakage density control. |
| output | Reader Immersion checklist and Reviewer gate. |
| owner_role | Hermes / project owner for reader experience judgment. |
| validation_method | Blind comparison of reader pull, curiosity, relief and pressure release. |
| success_criteria | 读者能自己补半截，情绪被场景带动而不是被作者命令。 |
| failure_signals | 频繁解释意义、替读者下结论、爽点变成口号。 |
| dependency | Work Voice plus Character Agency. |
| next_step | Design after Character Agency MVP shows stable positive signal. |

## F. Agentic Narrative Engine Research

| Field | Content |
| --- | --- |
| problem_statement | 传统链路仍然以章节规划驱动，角色主动性主要靠 prompt 约束补救。 |
| goal | 研究以 IP universe、world state、character agents 和 scene simulation 为核心的新范式。 |
| non_goal | 不替换当前 production pipeline，不做自由聊天型多 agent。 |
| input | Existing story-system principles, Character Agency learnings, Work Voice renderer boundary. |
| output | Research report, architecture sketch, risk register, minimal schema draft. |
| owner_role | Hermes for orchestration and research framing; DeepCode for prototypes only after approval. |
| validation_method | Design review and toy simulation, not production chapter validation. |
| success_criteria | 能说明 agent、orchestrator、renderer 和 reviewer 的边界。 |
| failure_signals | 范式过大、无法验收、角色自由跑飞、类型承诺丢失。 |
| dependency | Can run in parallel as isolated research. |
| next_step | Produce Agentic research brief after current Work Voice closure is not blocked. |

## G. Agentic Narrative 1-scene MVP

| Field | Content |
| --- | --- |
| problem_statement | Agentic 范式需要一个小到可验收的实验，而不是直接重建全链路。 |
| goal | 用一个固定 scene brief 测试 agent simulation plus renderer 是否增强角色主权感。 |
| non_goal | 不生成正式章节，不接入 WPS，不替换 Writer。 |
| input | Minimal agent cards, bounded scene brief, conflict resolver rules, renderer prompt. |
| output | Event log, rendered scene sample, comparison report, failure notes. |
| owner_role | Hermes / project owner for scene design; DeepCode for prototype scripts if approved. |
| validation_method | Same scene brief: direct Writer versus agent simulation then renderer. |
| success_criteria | 角色行动更有自身目标、误判和压力，且类型节奏未丢失。 |
| failure_signals | 多 agent 自由聊天、事件不可控、renderer 发明行动、Reviewer 无法判断。 |
| dependency | Preferably after Character Agency MVP. |
| next_step | Define minimal agent card schema before prototype. |
