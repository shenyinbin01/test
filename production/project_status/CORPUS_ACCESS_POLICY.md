# CORPUS ACCESS POLICY — webnovel-hermes-wps

> **生效日期**: 2026-06-03
> **维护方**: Hermes Agent / 项目负责人
> **适用范围**: 所有接入本仓库的 AI 代理（Codex、DeepCode、ChatGPT 等）

---

## 1. 核心原则

### 1.1 Raw Corpus 不默认上传

`production/phase8/corpus/` 下的原始语料（full chapters、chapter_cards、全文压缩产物等）**不作为 GitHub 默认输入**。

原因：
- 包含他人版权作品的完整原文
- 即使本地来源合法，公开推送存在版权、权限和语料泄露风险
- Codex/DeepCode 等外部代理的调研任务通常不需要全量原文

### 1.2 按需最小化原则

外部代理只需获取完成任务所需的**最小必要数据**。

---

## 2. Human Texture 第一阶段数据策略

### 2.1 当前可用输入

Codex 第一任务（Human Texture Engine 调研与立项）所需数据已全部在 main 分支就位：

| 数据 | 路径 | 用途 |
|------|------|------|
| 项目规则 | `AGENTS.md` | 角色定义、协作规则、安全约束 |
| 创作角色 Skill | `skill-pack/creation_skills/` | 理解当前创作体系 |
| 已批准技法 | `production/phase8/craft_assets/approved_patterns/` | 理解已有注入内容 |
| 正向验证 | `production/phase8/forward_validation/` | 理解验证框架 |
| 失败样本 | `production/phase8/skill_injection_minimal/validation_5ch/drafts/` | 人味失败诊断素材 |
| 交接报告 | `production/project_status/CODEX_HANDOFF_STATUS.md` | 当前状态全貌 |

### 2.2 第一阶段不得要求的数据

- ❌ 全量章节原文（raw_text / full chapters）
- ❌ 全量 chapter_cards
- ❌ 任何未推送的本地 corpus 数据
- ❌ 《大乘期》及其他待拆解书籍的完整原文

### 2.3 当前可用失败样本

仅限 `validation_5ch/drafts/` 下的 5 章草稿。这 5 章标注为「机制注入可见，但人味失败」样本，足够支撑 Human Texture 第一阶段诊断。

---

## 3. 后续数据升级流程

如需更多样本数据，必须走以下流程：

### 3.1 允许的数据形式

- ✅ Curated excerpts（精选节选）
- ✅ Sanitized samples（脱敏/去标识样本）
- ✅ Owner-approved package（项目负责人批准的独立数据包）

### 3.2 禁止的数据形式

- ❌ 直接请求推送上传统 corpus
- ❌ 代理自行从本地文件系统读取未推送的 corpus
- ❌ 将 raw corpus 作为 model context 上传到外部 API

### 3.3 升级流程

```
代理提出数据需求
  → Hermes 评估（是否合理、是否最小必要）
    → 项目负责人审批
      → Hermes 准备 curated/sanitized/approved package
        → 推送至 GitHub
          → 代理接入使用
```

---

## 4. 代理合规要求

所有接入本仓库的 AI 代理必须遵守：

1. 不得主动要求上传 raw corpus
2. 不得以「资料不足」为由拒绝基于现有公开数据开展调研
3. 如需额外数据，先说明用途和最低必要范围，经审批后获取
4. 不得将本仓库数据上传至非项目授权的第三方服务
5. 本地已存在但未推送的 corpus 目录不得作为输入来源

---

## 5. 当前 corpus/dachengqi 状态

| 属性 | 值 |
|------|-----|
| 路径 | `production/phase8/corpus/dachengqi/` |
| 本地存在 | ✅ |
| GitHub main | ❌（有意不推送） |
| 原因 | 包含《大乘期》全量章节原文和 chapter_cards |
| 何时推送 | 项目负责人明确批准安全数据包后 |

---

## 6. 补充说明

- 此策略不限制 `production/phase8/reverse_assets/`、`craft_assets/`、`forward_validation/` 等已推送中间产物的正常使用
- 此策略不限制 `toy_book` 等非版权敏感测试数据的正常使用
- 此策略可在项目负责人批准后修订
