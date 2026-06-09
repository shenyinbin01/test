# C Engine Reframe v0

当前阶段不是继续证明 Longform 车架，而是冻结 B 为 chassis，并把 C 重建为 authorial cognition、character mind、reader decompression engine，让文本从 engineering sample 走向 readable fiction。

## 背景

run_002_hermes_abc 已经给出三组对照：A_baseline、B_longform_structure、C_longform_engine。A 证明了无车架写作会依赖模型隐式判断；B 证明 chapter cards、state deltas、ledger previews 和 reviewer gates 足以维持三章连续性；C 证明额外 engine 模块能带来更强的可审计性和主角选择轨迹，但也暴露出技术痕迹过重的问题。

本目录吸收 run_002 的真实产物和后续架构判断，不把 `C_best` 当作最终结论。C 在工程评分上更完整，但“工程完整”不等于“读者愿意读”。因此本阶段把 B 冻结为 Longform Chassis，把 C 从 scene_agency_packet/agency_choice 的显式字段系统，重建为私有后端的作者认知与角色压力 harness。

## Run 002 判断

- A retired：A 缺少显式长期结构，后续不再作为可选架构，只保留历史基线价值。
- B frozen：B 负责 continuity、state_delta、ledger preview、reader_question、consequence ledger、drift detection 和 renderer hard boundary。
- C rebuild：当前 C 只说明“方向有信号”，不是最终可接受引擎。它必须降低工程可见度，补足角色私心、场景热度、读者解压和叙述姿态。
- No 5-10 chapters yet：在 C 仍可能把字段泄进正文前，继续拉长窗口只会放大同一问题。
- Run 003：不再做等权 A/B/C，而做 C0/C1/C2/C3 变体实验，验证 C 如何从工程合规转向小说可读性。

## 导航

- `decision_record.md`：本阶段决策记录，等待项目负责人接受。
- `run002_reinterpretation.md`：重新解释 run_002，不把 C_best 当最终。
- `b_chassis_freeze/`：B 车架冻结契约和边界。
- `c_engine_rebuild/`：C 引擎重建架构、私有 packet schema、renderer boundary v2。
- `exemplar_distillation/`：技法样本政策，明确不是作者模仿。
- `run003_c_variants/`：run_003 C 变体实验包。
- `migration_plan/`：模块迁移矩阵、风险和下一步。

## 当前状态

本包是设计产物，不生成新正文，不执行 run_003，不修改 run_002 产物，不创建正式 ledger，不接受任何 state_delta。
