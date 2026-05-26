# Phase 6A Fix 收口报告

> 日期：2026-05-26
> 执行：Hermes Agent（无 DeepCode 介入）
> 项目：webnovel-hermes-wps

---

## 1. 本轮目标

收口 Phase 6A 遗留问题，不进入 6B，不大拆 pipeline。

四个任务：

| # | 任务 | 状态 |
|---|------|------|
| 1 | 统一 fallback 规则源 | ✅ 完成 |
| 2 | 固化 .webnovel 投影层 | ✅ 完成 |
| 3 | 修正 AGENTS.md 歧义 | ✅ 完成 |
| 4 | 回归验证 | ✅ 通过 |

---

## 2. 新增文件

| 文件 | 说明 |
|------|------|
| `scripts/canon_rules_loader.py` | canon 规则统一加载器，优先 `.story-system` → 降级 `templates/` → 报错 |
| `templates/default_canon_patterns.yaml` | 默认 fallback 模板（唯一 fallback 规则源） |
| `.webnovel/state.yaml` | 投影状态文件 |
| `.webnovel/summaries/chapter_001.yaml` | 第一章总结投影 |
| `.webnovel/summaries/chapter_002.yaml` | 第二章总结投影 |
| `.webnovel/summaries/chapter_003.yaml` | 第三章总结投影 |
| `.webnovel/projection/story_bible_projection.md` | Story Bible 投影模板 |
| `.webnovel/projection/outline_projection.md` | 大纲投影模板 |
| `.webnovel/projection/manuscript_projection.md` | 稿本投影模板 |
| `.webnovel/projection/review_projection.md` | 审稿投影模板 |
| `.webnovel/projection/state_projection.md` | 状态摘要投影模板 |
| `.webnovel/memory_scratchpad.yaml` | 临时工作记忆（非持久） |

---

## 3. 修改文件

| 文件 | 变更 |
|------|------|
| `scripts/validate_canon_consistency.py` | 移除内联 FALLBACK_* 常量，改为 `from canon_rules_loader import load_canon_patterns`；报告增加 `canon_rules_source` 字段 |
| `scripts/validate_phase4.py` | 移除 `_load_forbidden_phase4()` 函数和 `_FALLBACK_PHASE4_*` 常量，改为 `from canon_rules_loader import load_canon_patterns`；启动时输出规则源 |
| `AGENTS.md` | 第 148 行：`管理 .story-system 内容更新（状态层）` → `通过 webnovel-state-manager Skill 管理 .story-system 内容更新；Hermes 不直接手改状态文件，除非用户明确要求人工修复。` |
| `webnovel-state-manager Skill` | 第 4 节「生成 .webnovel/ 投影」扩充为完整投影文件清单表格和步骤说明 |

---

## 4. Fallback 统一结果

### 改造前

两个 validator 各自维护不同的 fallback 常量，规则内容相同但存储方式不同：

- `validate_canon_consistency.py`：5 组 Python 列表/字典常量
- `validate_phase4.py`：2 组 unicode-escape 编码的 Python 列表常量

### 改造后

- `canon_rules_loader.py`：统一的加载逻辑，**是规则源的唯一入口**
- 加载顺序：`.story-system/canon_patterns.yaml`（项目级）→ `templates/default_canon_patterns.yaml`（默认 fallback）→ `FileNotFoundError`
- 两个 validator 都调用 `canon_rules_loader.load_canon_patterns()`
- 报告输出中均包含 `canon_rules_source` 字段，可追溯实际使用的规则文件

### 验证输出

```
[validate_canon_consistency] 规则源: /data/webnovel-lab/workspace/novels/price_tag_life/.story-system/canon_patterns.yaml
[validate_phase4] 规则源: /data/webnovel-lab/workspace/novels/price_tag_life/.story-system/canon_patterns.yaml
```

两个 validator 显示**读取的是同一个规则源文件**。

---

## 5. .webnovel 投影层状态

```
.webnovel/
├── state.yaml                          # ✅ 已创建（独立文件）
├── memory_scratchpad.yaml              # ✅ 已创建
├── summaries/
│   ├── chapter_001.yaml                # ✅ 已创建
│   ├── chapter_002.yaml                # ✅ 已创建
│   └── chapter_003.yaml                # ✅ 已创建
└── projection/
    ├── story_bible_projection.md       # ✅ 已创建（模板）
    ├── outline_projection.md           # ✅ 已创建（模板）
    ├── manuscript_projection.md        # ✅ 已创建（模板）
    ├── review_projection.md            # ✅ 已创建（模板）
    └── state_projection.md             # ✅ 已创建（模板）
```

### webnovel-state-manager Skill 职责更新

Skill 的「4. 生成 .webnovel/ 投影」节已补充：
- 每章 commit 确认后需要刷新的全部 8 个投影文件
- 各投影文件的真源来源和用途对应关系
- 具体实现步骤（从读取真源 → 刷新 state.yaml → 刷新 summaries/ → 刷新 projection/）

### 后续生成要求

投影层结构已就绪，但内容（summaries 和 projection 中的具体数据）需要在下一次通过 webnovel-state-manager Skill 运行生产 pipeline 时填充。本轮不重跑完整三章 pipeline。

---

## 6. AGENTS.md 修正情况

### 原表述

```
- 管理 `.story-system` 内容更新（状态层）
```

### 修正后

```
- 通过 webnovel-state-manager Skill 管理 `.story-system` 内容更新；Hermes 不直接手改状态文件，除非用户明确要求人工修复。
```

### 修正要点

- 明确了 **谁** 管理：不是 Hermes 直接管理，而是通过 webnovel-state-manager Skill
- 补充了 **例外条件**：允许在用户明确要求时直接修复
- 消除歧义：Hermes 不应直接操作状态文件作为常规操作

---

## 7. 回归测试结果

### 7.1 `canon_rules_loader.py` 独立测试

```bash
python scripts/canon_rules_loader.py --project price_tag_life
```

```
[canon_rules_loader] 从 .story-system 加载规则: forbidden=25, wide=3, anchors=10, negation=3
✅ 规则加载成功
```

### 7.2 `validate_canon_consistency.py`

```bash
python scripts/validate_canon_consistency.py --mode real
```

```
[canon_rules_loader] 从 .story-system 加载规则: forbidden=25, wide=3, anchors=10, negation=3
[validate_canon_consistency] 规则源: /data/webnovel-lab/workspace/novels/price_tag_life/.story-system/canon_patterns.yaml
Canon consistency: ✅ PASS
```

### 7.3 `validate_phase4.py`

```bash
python scripts/validate_phase4.py --project price_tag_life --chapters 1 --mode mock
```

```
[canon_rules_loader] 从 .story-system 加载规则: forbidden=25, wide=3, anchors=10, negation=3
[validate_phase4] 规则源: /data/webnovel-lab/workspace/novels/price_tag_life/.story-system/canon_patterns.yaml
errors: 0, passed: True
```

### 7.4 `validate_project.py`

```bash
python scripts/validate_project.py
```

```
✅ 项目结构验证通过（共检查所有必要目录和文件）
```

### 回归结论

**所有回归测试通过**。没有破坏现有验证逻辑，没有修改 WPS 文件，没有重写 pipeline。

---

## 8. 未完成事项

| 事项 | 说明 |
|------|------|
| .webnovel 投影内容填充 | 模板已创建，但内容数据需要在下一次通过 webnovel-state-manager Skill 运行生产流程时填充 |
| .story-system 真源校验 | 投影层已准备好阅读真源，但真实 pipeline 尚未运行到 StateManager 步骤 |

这些事项不阻碍收口，属于下一轮生产的准备工作。

---

## 9. 是否可以进入 Phase 6B

**可以。**

四个任务全部完成，回归验证全部通过。

Phase 6B 可在此基准上开展，内容包括但不限于：
- 去 AI 味质量闸门
- 审稿自动化的规范化
- 网文表达一致性检查

---

## 附录：禁止行为检查清单

| 禁止事项 | 是否违反 |
|----------|----------|
| 重写 run_chapter_pipeline.py | ❌ 未修改 |
| 删除 run_chapter_pipeline.py | ❌ 未删除 |
| 改变 WPS 同步链路 | ❌ 未修改 WPS 文件 |
| 新增小说生成能力 | ❌ 未新增 |
| 进入 Phase 6B | ❌ 未进入 |
| 修改正文内容 | ❌ 未修改 |
| 让 Python 承担新的创作决策 | ❌ Python 仅做文件读写和加载 |
