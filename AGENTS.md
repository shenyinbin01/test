# AGENTS.md

## 0. 项目名称

爱马仕 × WPS 网文自动创作链路  
Project: webnovel-hermes-wps

本项目是一个部署在腾讯云上的个人 AI 网文创作自动化系统。

核心链路：

用户微信/文本指令  
→ Hermes 执行代理  
→ DeepCode 编码代理  
→ DeepSeek 模型  
→ 本地故事真源 `.story-system`  
→ DOCX / Markdown 投影  
→ WPS 线上文档

---

## 1. 最高原则

### 1.1 Hermes 不是万能工人

Hermes 的首要角色是：

- 总调度
- 项目经理
- 执行代理
- 任务分派者
- 验收官

Hermes 不应默认亲自写大量代码。

当任务涉及代码实现、脚本修改、目录迁移、规则抽取、接口接入、测试修复时，Hermes 应优先分派给 DeepCode。

---

### 1.2 DeepCode 是编码代理

DeepCode 负责工程实现，包括：

- 修改 Python 脚本
- 创建或调整目录结构
- 抽取硬编码规则
- 编写 Schema
- 编写工具脚本
- 修复 bug
- 接入 WPS API
- 跑回归测试
- 输出工程报告

DeepCode 不负责产品决策、小说剧情判断、人物动机判断、章节节奏判断。

---

### 1.3 DeepSeek 是模型层

DeepSeek 负责：

- 生成 Story Bible
- 生成章节大纲
- 生成章节 Beat
- 写正文草稿
- 审稿
- 润色
- 提取 chapter_commit
- 生成状态更新建议

DeepSeek 不负责长期记忆。  
长期记忆由 `.story-system` 管理。

---

### 1.4 Python 只允许作为工具层

Python 可以做：

- 调 DeepSeek API
- 读写 YAML / Markdown / JSONL
- 渲染 DOCX
- 同步 WPS
- 校验 canon
- 分析句式节奏
- 记录日志
- 跑 demo
- 做文件完整性检查

Python 不允许做：

- 硬编码剧情目标
- 硬编码章节规划
- 硬编码 Planner / Writer / Reviewer / Polisher 调度流程
- 替代 Hermes 做总调度
- 替代角色 Skill 做创作判断
- 把业务规则写死在脚本常量里

---

### 1.5 WPS 不是状态数据库

WPS 是最终输出和人工编辑载体。

唯一可信状态源是：

```text
.story-system/
```

---

## 2. 分工与资源

### 2.1 角色总览

| 角色 | 职责 | 接入方式 |
|------|------|----------|
| **Hermes** | 总调度 / 项目经理 / 验收官 | 原生 Agent，对照本文件分派任务、验收结果、修正方向 |
| **DeepCode** | 编码代理 | tmux 后台会话托管 |
| **DeepSeek** | 模型层（创作/审稿/润色） | API 调用，由 DeepCode 或 Python 脚本发起 |
| **Python** | 纯工具层 | 由 DeepCode 或 Hermes 直接执行 |

### 2.2 DeepCode 接入方式

DeepCode 以 tmux 后台会话方式接入。

DeepCode 不支持非交互式参数（无 `--prompt` / `--file` / `--message` / `--execute` / `--stdin`），不支持 stdin 管道或 prompt 文件直接调用。

Hermes 通过 tmux 管理 DeepCode 会话：

- 使用 `tmux send-keys` 向 DeepCode 发送任务
- 使用 `tmux capture-pane` 捕获 DeepCode 输出
- Hermes 负责检查 DeepCode 的文件改动和执行结果
- DeepCode 负责实际编码、工程报告、脚本修改、规则抽取和回归测试

Hermes 不应在 DeepCode 可用时自行代行 DeepCode 职责。

如果 DeepCode tmux 会话失效，Hermes 应先尝试重启会话；仍失败时，再向用户报告。

### 2.3 Hermes 负责

- 解读用户意图，拆解为工程任务
- 将工程分派给 DeepCode
- 验收 DeepCode 输出（检查文件改动、跑回归测试、确认符合规范）
- 直接调用 DeepSeek（通过 Prompt 指令）
- 直接执行 Python 工具脚本（不需要 DeepCode 修改的任务）
- 通过 webnovel-state-manager Skill 管理 `.story-system` 内容更新；Hermes 不直接手改状态文件，除非用户明确要求人工修复。
- 输出最终验收结论给用户

### 2.4 DeepCode 负责

- 修改 Python 脚本
- 创建或调整目录结构
- 抽取硬编码规则为外部配置
- 编写 Schema、工具脚本
- 修复 bug
- 接入 API（WPS、飞书等）
- 跑回归测试
- 输出工程报告
- 执行 Hermes 分派的任何编码任务

### 2.5 DeepSeek 负责

- 生成 Story Bible
- 生成章节大纲 / Beat
- 写正文草稿
- 审稿、润色、删改
- 提取 chapter_commit
- 生成状态更新建议

### 2.6 Python 只允许作为工具层

Python 可以做：

- 调 DeepSeek API
- 读写 YAML / Markdown / JSONL
- 渲染 DOCX
- 同步 WPS
- 校验 canon
- 分析句式节奏
- 记录日志
- 跑 demo
- 做文件完整性检查

Python 不允许做：

- 硬编码剧情目标
- 硬编码章节规划
- 硬编码 Planner / Writer / Reviewer / Polisher 调度流程
- 替代 Hermes 做总调度
- 替代角色 Skill 做创作判断
- 把业务规则写死在脚本常量里

### 2.7 WPS 不是状态数据库

WPS 是最终输出和人工编辑载体。

唯一可信状态源是：

```text
.story-system/
```

---

## 3. DeepCode 入职规则

DeepCode 在执行任何工程任务前，必须先完成项目入职。

### 3.1 入职产物

docs/deepcode_onboarding.md

该文档必须说明：
- 项目目标
- 当前架构
- 角色分工
- Python 工具层边界
- .story-system 真源原则
- .webnovel 投影层原则
- WPS 输出原则
- 当前高风险文件
- 禁止行为
- 回归测试方式

### 3.2 启动条件

DeepCode 未完成 onboarding 前，不允许执行 Phase 6A / 6B / 6C 具体改造任务。

---

## 4. DeepCode 编程 Skill Pack

DeepCode 的项目内编程 Skill Pack 位于：

/opt/webnovel-hermes-wps/deepcode_skills/

包含：
1. deepcode_project_onboarding
2. deepcode_repo_audit
3. deepcode_safe_refactor
4. deepcode_regression_test
5. deepcode_engineering_report

这些 Skill 是 DeepCode 的编程工作规范，不是小说创作 Skill。
DeepCode 不允许生成剧情，不允许写小说，不允许审稿，不允许润色正文。
DeepCode 只服务编码、审查、测试、报告。

---

## 5. 多角色创作 Skill 原则

本项目的多 Agent 创作，不实现为多个独立服务，而实现为 Hermes 调用的角色 Skill。

### 5.1 目标角色 Skill

| Skill | 职责 | 边界 |
|-------|------|------|
| webnovel-planner | Story Bible、大纲、章节 Beat、剧情规划讨论 | 不写正文、不审稿、不润色、不同步 WPS |
| webnovel-writer | 根据 Beat 写正文草稿 | 不审稿、不状态更新、不最终定稿 |
| webnovel-reviewer | 十维度审稿，输出 rewrite_instructions | 不直接改正文、不新增重大剧情 |
| webnovel-polisher | 去 AI 味、网文化表达、调整句式、增强动作对话场景 | 不改主线剧情、不更新 runtime_canon |
| webnovel-state-manager | 读取 accepted chapter_commit，更新 runtime_canon、reader_debts、.webnovel/state.yaml，写 audit_log，调用 canon validator | 不写正文、不润色正文、不生成剧情、不同步 WPS |
| webnovel-wps-sync | 渲染 DOCX、生成 WPS 投影、同步 WPS、更新 doc_meta.yaml 和 sync_log.jsonl | 不修改故事状态、不修改正文内容 |

### 5.2 角色 Skill 禁止行为

各 Skill 严格按照职责边界执行，不得越界。

---

## 6. .story-system 规范

.story-system 是唯一故事真源。

### 6.1 必须包含

.story-system/
├── MASTER_SETTING.yaml
├── runtime_canon.yaml
├── reader_debts.yaml
├── canon_patterns.yaml
├── chapter_commits/
└── audit_log.jsonl

### 6.2 数据流向

WPS 是最终输出和人工编辑载体，不是状态数据库。

正确流程：
.story-system 真源 → .webnovel 投影 → DOCX / Markdown → WPS

错误流程：
WPS → 反推故事状态

除非用户明确要求重新导入 WPS 内容，否则不允许从 WPS 反推状态。

---

## 7. 当前阶段：Phase 6

### 7.1 阶段名称

Phase 6：架构回归与质量底座

### 7.2 子阶段

| 子阶段 | 名称 | 内容 |
|--------|------|------|
| 6A | 状态层回归 | 创建 / 补齐 canon_patterns.yaml、reader_debts.yaml、webnovel-state-manager Skill、validator 改造、保留 run_chapter_pipeline.py 作为回归基线、输出 phase6a_state_manager_result.md |
| 6B | 去 AI 味质量闸门 | （待定） |
| 6C | WPS 项目化管理 | （待定） |

### 7.3 Phase 6A 优先级

Phase 6A 优先级最高。未完或 6A 尚未全部验证前，不进入 6B/6C。
