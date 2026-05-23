# DeepCode 项目入职文档

> 生成日期: 2026-05-23
> 项目: webnovel-hermes-wps (爱马仕 × WPS 网文自动创作链路)

---

## 1. 项目目标

本项目是一个部署在腾讯云上的个人 AI 网文创作自动化系统。核心链路为：

```
用户微信/文本指令
→ Hermes 执行代理（总调度）
→ DeepCode 编码代理（工程实现）
→ DeepSeek 模型（创作/审稿/润色）
→ 本地故事真源 `.story-system/`
→ `.webnovel/` 投影层
→ DOCX / Markdown 渲染
→ WPS 线上文档
```

当前处于 **Phase 6（架构回归与质量底座）**，具体到 Phase 6A（状态层回归），已完成：
- `canon_patterns.yaml` 外置到 `.story-system/`
- `reader_debts.yaml` 补齐到 `.story-system/`
- `webnovel-state-manager` Skill 创建
- 两个 validator 改造为优先读取 `.story-system/canon_patterns.yaml`
- `run_chapter_pipeline.py` 作为回归基线保留

---

## 2. 当前架构

### 2.1 目录结构

```
/opt/webnovel-hermes-wps/          # 代码根目录 (WEBNOVEL_CODE_ROOT)
├── AGENTS.md                      # 角色分工与最高原则
├── README.md                      # README（当前为空占位）
├── .env.example                   # 环境变量模板
├── scripts/                       # Python 工具层（11 个脚本）
│   ├── call_deepseek.py           # 统一 DeepSeek API 调用封装（mock/real）
│   ├── run_chapter_pipeline.py    # 三章连续生产 pipeline（含 phase4b/4c）
│   ├── validate_phase4.py         # 阶段四三章验证（含 phase4b/4c 验证）
│   ├── validate_canon_consistency.py  # Canon 一致性检查
│   ├── validate_project.py        # 项目结构完整性检查
│   ├── validate_wps_sync.py       # WPS 同步结果验证
│   ├── build_wps_projection.py    # 生成 WPS 投影（MD + DOCX + manifest）
│   ├── render_docx.py             # DOCX 渲染（降级方案为 Markdown）
│   ├── sync_wps.py                # 同步 DOCX 到 WPS/kdocs（含 dry-run）
│   ├── run_demo.py                # Demo 运行
│   └── env_check.py               # 环境检查
├── schemas/                       # YAML Schema（6 个）
│   ├── master_setting.schema.yaml
│   ├── runtime_canon.schema.yaml
│   ├── chapter_outline.schema.yaml
│   ├── chapter_beat.schema.yaml
│   ├── review_report.schema.yaml
│   └── chapter_commit.schema.yaml
├── templates/                     # Prompt 模板
│   ├── prompts/                   # 8 个创作提示词模板
│   ├── deai_rules/                # 5 个去 AI 味规则
│   └── wps/                       # WPS 模板
├── deepcode_skills/               # DeepCode 编程 Skill Pack（5 个）
│   ├── deepcode_project_onboarding/
│   ├── deepcode_repo_audit/
│   ├── deepcode_safe_refactor/
│   ├── deepcode_regression_test/
│   └── deepcode_engineering_report/
├── docs/                          # 阶段报告
│   ├── phase4b_result.md
│   ├── phase4c_result.md
│   ├── phase5_fix_result.md
│   ├── phase5_result.md
│   └── phase6a_state_manager_result.md
├── skills/                        # 创作角色 Skill（当前为空）
├── examples/                      # 示例（当前为空）
├── pipelines/                     # Pipeline 定义（当前为空）
└── full_review/                   # 复审包
```

### 2.2 数据目录

```
/data/webnovel-lab/                # 数据根目录 (WEBNOVEL_DATA_ROOT)
├── workspace/novels/price_tag_life/   # 小说工作区
│   ├── .story-system/             # 故事真源
│   │   ├── MASTER_SETTING.yaml
│   │   ├── runtime_canon.yaml
│   │   ├── canon_patterns.yaml
│   │   ├── reader_debts.yaml
│   │   └── chapter_commits/
│   ├── chapters/                  # 章节文件（由 pipeline 使用）
│   └── manuscript/                # 手稿（由 render_docx.py 使用）
├── demo_output/                   # Demo 输出
│   ├── phase4_run/                # 阶段四A输出
│   ├── phase4b_real_run/          # 阶段四B输出（Chapter 1 real）
│   ├── phase4c_real_run/          # 阶段四C输出（Chapter 2-3 real）
│   ├── phase5_wps_projection/     # WPS 投影文件
│   └── phase5_wps_state/          # WPS 同步状态
└── exports/                       # 导出目录
```

### 2.3 数据流向

```
.story-system 真源
    ↓ 读取
Hermes Agent / Python 工具层
    ↓ 处理
.webnovel/ 投影层（扁平 state.yaml + chapter context）
    ↓ 渲染
DOCX / Markdown
    ↓ 同步
WPS 线上文档

不允许：WPS → 反推故事状态（除非用户明确要求）
```

---

## 3. 角色分工

| 角色 | 职责 | 接入方式 |
|------|------|----------|
| **Hermes** | 总调度 / 项目经理 / 验收官 | 原生 Agent，分派任务、验收结果、修正方向 |
| **DeepCode** | 编码代理 | tmux 后台会话托管 |
| **DeepSeek** | 模型层（创作/审稿/润色） | API 调用，由 DeepCode 或 Python 脚本发起 |
| **Python** | 纯工具层 | 由 DeepCode 或 Hermes 直接执行 |

### 3.1 Hermes 负责
- 解读用户意图，拆解为工程任务
- 将工程分派给 DeepCode
- 验收 DeepCode 输出（检查文件改动、跑回归测试、确认符合规范）
- 直接调用 DeepSeek（通过 Prompt 指令）
- 直接执行 Python 工具脚本（不需要 DeepCode 修改的任务）
- 管理 `.story-system` 内容更新（状态层）
- 输出最终验收结论给用户

### 3.2 DeepCode 负责
- 修改 Python 脚本
- 创建或调整目录结构
- 抽取硬编码规则为外部配置
- 编写 Schema、工具脚本
- 修复 bug
- 接入 API（WPS、飞书等）
- 跑回归测试
- 输出工程报告
- 执行 Hermes 分派的任何编码任务

### 3.3 DeepSeek 负责
- 生成 Story Bible
- 生成章节大纲 / Beat
- 写正文草稿
- 审稿、润色、删改
- 提取 chapter_commit
- 生成状态更新建议

### 3.4 六个角色 Skill

| Skill | 职责 | 边界 |
|-------|------|------|
| webnovel-planner | Story Bible、大纲、章节 Beat、剧情规划讨论 | 不写正文、不审稿、不润色、不同步 WPS |
| webnovel-writer | 根据 Beat 写正文草稿 | 不审稿、不状态更新、不最终定稿 |
| webnovel-reviewer | 十维度审稿，输出 rewrite_instructions | 不直接改正文、不新增重大剧情 |
| webnovel-polisher | 去 AI 味、网文化表达、调整句式、增强动作对话场景 | 不改主线剧情、不更新 runtime_canon |
| webnovel-state-manager | 读取 chapter_commit，更新 runtime_canon / reader_debts / .webnovel/state.yaml，写 audit_log，调用 canon validator | 不写正文、不润色正文、不生成剧情、不同步 WPS |
| webnovel-wps-sync | 渲染 DOCX、生成 WPS 投影、同步 WPS、更新 doc_meta.yaml 和 sync_log.jsonl | 不修改故事状态、不修改正文内容 |

---

## 4. Python 工具层边界

### 4.1 Python 可以做的
- 调 DeepSeek API
- 读写 YAML / Markdown / JSONL
- 渲染 DOCX
- 同步 WPS
- 校验 canon
- 分析句式节奏
- 记录日志
- 跑 demo
- 做文件完整性检查

### 4.2 Python 禁止做的
- 硬编码剧情目标
- 硬编码章节规划
- 硬编码 Planner / Writer / Reviewer / Polisher 调度流程
- 替代 Hermes 做总调度
- 替代角色 Skill 做创作判断
- 把业务规则写死在脚本常量里

### 4.3 主要脚本职责速查

| 脚本 | 模式 | 关键输入 | 关键输出 | 风险 |
|------|------|----------|----------|------|
| `call_deepseek.py` | mock / real | system prompt, user input | generated text, JSONL log | API Key 泄露, canon 注入规则冲突 |
| `run_chapter_pipeline.py` | mock / real (phase4b/4c) | chapter goal, outline | final.md, commit.yaml, runtime_canon | 调度逻辑与 Hermes 角色冲突 |
| `validate_phase4.py` | mock / real | workspace, chapters | phase4_validation.json | 硬编码 fallback 与 canon_patterns.yaml 不一致 |
| `validate_canon_consistency.py` | mock / real | canon file, output dir | canon_consistency_report.json | 硬编码 fallback 与 canon_patterns.yaml 不一致 |
| `validate_project.py` | (无模式) | code root | JSON report | 无 |
| `build_wps_projection.py` | (无模式) | project name | MD, DOCX, manifest | 无 |
| `render_docx.py` | (无模式) | project dir | DOCX / MD | python-docx 不可用时降级 |
| `sync_wps.py` | dry-run / real | DOCX path | doc_meta.yaml, sync_log | kdocs-cli 不可用, 超时, stdout 非 JSON |
| `validate_wps_sync.py` | (无模式) | meta, log | 验证报告 | 无 |
| `run_demo.py` | (无模式) | project | demo output | 无 |
| `env_check.py` | (无模式) | code/data root | 检查报告 | 无 |

---

## 5. `.story-system` 真源原则

### 5.1 核心原则
`.story-system/` 是**唯一可信故事状态源**。WPS 是最终输出和人工编辑载体，不是状态数据库。

### 5.2 目录结构

```
.story-system/
├── MASTER_SETTING.yaml        # 不变的项目元设定
├── runtime_canon.yaml         # 已发生正典（动态更新）
├── canon_patterns.yaml        # 禁止词/锚点规则
├── reader_debts.yaml          # 读者债务追踪
├── chapter_commits/           # 已确认的章节 commit
│   ├── chapter_001_commit.yaml
│   └── ...
└── audit_log.jsonl            # 审计日志
```

### 5.3 正确流程
```
.story-system 真源 → .webnovel 投影 → DOCX / Markdown → WPS
```

### 5.4 错误流程
```
WPS → 反推故事状态（禁止，除非用户明确要求重新导入）
```

### 5.5 当前文件状态

| 文件 | 存在 | 说明 |
|------|------|------|
| `MASTER_SETTING.yaml` | ✅ | 包含项目元设定、角色、世界观、大纲 |
| `runtime_canon.yaml` | ✅ | 当前 1 章事件，含 timeline、character_states、active_threads |
| `canon_patterns.yaml` | ✅ | 25 条禁止词 + 3 条豁免模式 + 10 条锚点 + 3 条否定前缀 |
| `reader_debts.yaml` | ✅ | 14 条债务（ch1: 8条, ch2: 6条） |
| `chapter_commits/` | ✅ | 目录存在 |
| `audit_log.jsonl` | ❌ | 尚未创建 |

---

## 6. `.webnovel` 投影层说明

### 6.1 用途
`.webnovel/` 是 Python 工具层可读取的扁平化投影，非独立状态源。

### 6.2 目录结构（目标）

```
.webnovel/
├── state.yaml                 # 当前状态快照
├── context/
│   └── chapter_NNN_context.md # 写某章时的上下文
└── projection/
    └── ...
```

### 6.3 当前状态
`.webnovel/` 目录在 `.story-system/` 同级路径中尚未实际创建。当前 WPS 投影输出到 `/data/webnovel-lab/demo_output/phase5_wps_projection/`。

这是 Phase 6 待解决的问题之一（state.yaml 未作为独立产物导出）。

---

## 7. WPS 输出链路说明

### 7.1 链路流程

```
Phase 4 real 产出 final.md
    ↓ build_wps_projection.py
单章 MD + 合集 MD + DOCX + projection_manifest.json
    ↓ render_docx.py (可单独调用)
DOCX / Markdown
    ↓ sync_wps.py (dry-run / real)
kdocs-cli upload-file
    ↓
WPS 线上文档
    ↓ validate_wps_sync.py
验证同步结果
```

### 7.2 关键文件

| 文件 | 路径 | 说明 |
|------|------|------|
| 单章 MD | `demo_output/phase5_wps_projection/{project}_ch{NNN}.md` | 单章正文 |
| 合集 MD | `demo_output/phase5_wps_projection/{project}_volume_001.md` | 三章合集 |
| DOCX | `demo_output/phase5_wps_projection/{project}_volume_001.docx` | 可同步到 WPS |
| manifest | `demo_output/phase5_wps_projection/projection_manifest.json` | 投影清单 |
| doc_meta | `demo_output/phase5_wps_state/doc_meta.yaml` | 同步元数据 |
| sync_log | `demo_output/phase5_wps_state/sync_log.jsonl` | 同步日志 |

### 7.3 当前风险
- `kdocs-cli` 依赖：WPS 同步依赖 `kdocs-cli` 命令，`env_check.py` 中已检测到其不可用状态
- 超时处理：sync_wps.py 对 kdocs-cli 超时做了状态文件保障
- stdout 非 JSON：已做防御性处理，写入 `status=unknown`

---

## 8. 当前高风险文件

### 8.1 高风险（修改需谨慎）

| 文件 | 风险原因 |
|------|----------|
| `scripts/validate_phase4.py` | 涉及 canon 规则读取逻辑，内置 25 条 unicode-escape 编码的 fallback；STORY_SYSTEM_PATTERNS 路径指向 `workspace/novels/` 但旧路径可能是 `workspace/` |
| `scripts/validate_canon_consistency.py` | 涉及 canon 规则读取逻辑，内置 15 条明文中文 fallback + 3 wide + 10 anchors；与 validate_phase4.py 的 fallback 规则集不一致（Phase 6A 已知风险） |
| `scripts/run_chapter_pipeline.py` | 承担了调度职责（6 个节点编排），与 AGENTS.md 中"Python 不允许替代 Hermes 做总调度"的原则有冲突；包含硬编码剧情目标和 must_include |
| `scripts/call_deepseek.py` | 核心 API 调用封装，涉及 canon 注入逻辑、API Key 安全、重试策略 |

### 8.2 中风险

| 文件 | 风险原因 |
|------|----------|
| `scripts/sync_wps.py` | 依赖 kdocs-cli 外部命令，超时/非 JSON 输出已做防御但仍需关注 |
| `scripts/build_wps_projection.py` | 对 final.md 做 canon_check 段落过滤，可能引入内容丢失 |
| `AGENTS.md` | 项目最高原则文档，修改需慎重 |

### 8.3 低风险（可安全修改）

| 文件 | 说明 |
|------|------|
| `scripts/env_check.py` | 纯检查脚本 |
| `scripts/validate_project.py` | 结构检查脚本 |
| `scripts/render_docx.py` | 渲染脚本，有降级方案 |
| `scripts/run_demo.py` | Demo 脚本 |
| `scripts/validate_wps_sync.py` | 验证脚本 |
| `docs/*.md` | 文档报告 |

---

## 9. 当前禁止行为

### 9.1 DeepCode 禁止行为（来自 deepcode_project_onboarding Skill）
1. 不允许修改 Python 代码（仅本入职任务期间）
2. 不允许修改 pipeline
3. 不允许修改 `.story-system/`
4. 不允许修改 WPS 同步逻辑
5. 不允许生成小说内容
6. 不允许创建新架构
7. 不允许删除任何文件

### 9.2 Python 工具层禁止行为（来自 AGENTS.md）
1. 硬编码剧情目标
2. 硬编码章节规划
3. 硬编码 Planner / Writer / Reviewer / Polisher 调度流程
4. 替代 Hermes 做总调度
5. 替代角色 Skill 做创作判断
6. 把业务规则写死在脚本常量里

### 9.3 各角色 Skill 禁止行为
- 各 Skill 严格按照职责边界执行，不得越界
- DeepCode 不允许生成剧情、写小说、审稿、润色正文
- DeepCode 只服务编码、审查、测试、报告

### 9.4 WPS 禁止行为
- WPS 不是状态数据库
- 不允许从 WPS 反推故事状态（除非用户明确要求重新导入）

---

## 10. DeepCode 后续接活规则

### 10.1 入职条件
DeepCode 在执行任何工程任务前，必须先完成项目入职（即本文档必须存在）。

### 10.2 接活流程
1. Hermes 拆解用户意图为工程任务
2. Hermes 通过 tmux send-keys 向 DeepCode 发送任务
3. DeepCode 执行编码、审查、测试、报告
4. Hermes 通过 tmux capture-pane 捕获 DeepCode 输出
5. Hermes 检查文件改动和执行结果
6. Hermes 验收通过后输出最终结论

### 10.3 最佳实践
- 修改前先读取文件，理解上下文（特别是 validate_phase4.py 和 validate_canon_consistency.py 的关系）
- 修改后跑回归测试（见第 11 节）
- 不盲目删除硬编码 fallback — 它们是有意保留的降级策略
- 向 `.story-system/canon_patterns.yaml` 添加规则时，需同时更新两个 validator 的 fallback 保持一致

### 10.4 当前 Phase 6A 已知问题
- 两个 validator 的 fallback 规则不一致（25 条 vs 15 条）
- `style_constraints` / `continuity_constraints` / `ai_flavor_constraints` 尚未从 Python 硬编码中提取到 canon_patterns.yaml
- `.webnovel/` 投影层尚未实际创建
- `audit_log.jsonl` 尚未创建

---

## 11. 建议的回归测试方式

### 11.1 最小回归命令集

```bash
# 1. 环境检查
python scripts/env_check.py

# 2. 项目结构检查
python scripts/validate_project.py

# 3. Canon 一致性检查（从 .story-system 加载规则）
python scripts/validate_canon_consistency.py --mode real

# 4. 阶段四验证（从 .story-system 加载规则）
python scripts/validate_phase4.py --project price_tag_life --chapters 1,2,3 --mode real
python scripts/validate_phase4.py --project price_tag_life --phase4b
python scripts/validate_phase4.py --project price_tag_life --phase4c

# 5. Mock pipeline 回归（验证 pipeline 本身不被破坏）
python scripts/run_chapter_pipeline.py --project price_tag_life --chapters 1,2,3 --mode mock

# 6. WPS 投影生成
python scripts/build_wps_projection.py --project price_tag_life
```

### 11.2 Phase 6A 专项验证

```bash
# 验证 canon_patterns.yaml 被正确加载（两个 validator 均不应使用 fallback）
python scripts/validate_canon_consistency.py --mode real 2>&1 | grep "从 .story-system 加载规则"
python scripts/validate_phase4.py --project price_tag_life --chapters 1,2,3 --mode real 2>&1 | grep "从 .story-system 加载禁止词"
```

### 11.3 触发条件
- 每次修改 `scripts/` 下的 Python 文件后
- 每次修改 `.story-system/canon_patterns.yaml` 后
- 每次修改 AGENTS.md 后
- 进入新的 Phase 子阶段前
- Hermes 验收前

---

*文档结束 — DeepCode 项目入职完成*
