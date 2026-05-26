# Phase 6 — 架构回归与质量底座 · 闭包报告

> 生成日期：2026-05-26
> 最终提交：`cfcaf33`
> 项目：webnovel-hermes-wps / price_tag_life (人生价格标签)

---

## 0. 阶段定位

Phase 6 是 webnovel-hermes-wps 项目的**架构回归与质量底座**阶段。核心目标是：在前期 Pipeline 创作能力的基础上，补上状态管理、质量闸门、WPS 输出三条基础设施，为后续规模化创作建立可信底座。

**三个子阶段的关系：**

```
6A 状态层回归 ──→ 6B 去 AI 味质量闸门 ──→ 6C WPS 项目化管理
  (可信真源)        (输出质量保障)          (交付链路)
```

---

## 1. Phase 6A — 状态层回归

### 目标

建立 `.story-system` 作为唯一故事真源，统一 canon 校验规则加载，修正 AGENTS.md 中的角色职责歧义。

### 已完成

| 交付物 | 状态 | 说明 |
|--------|------|------|
| `canon_rules_loader.py` | ✅ | 优先读 `.story-system/canon_patterns.yaml`，fallback 到 `templates/default_canon_patterns.yaml`，两者皆无时报错 |
| `templates/default_canon_patterns.yaml` | ✅ | 两个 validator 的唯一 fallback 规则源 |
| `validate_canon_consistency.py` 改造 | ✅ | 不再维护内联 fallback 常量，统一调用 canon_rules_loader |
| `validate_phase4.py` 改造 | ✅ | 同上 |
| AGENTS.md 修正 | ✅ | Hermes 职责改为"通过 webnovel-state-manager Skill 管理 .story-system；不直接手改" |
| `.webnovel` 投影层结构 | ✅ | `state.yaml`、`summaries/`、`projection/`、`memory_scratchpad.yaml` 结构已定义 |

### 关键文件

- `scripts/canon_rules_loader.py`
- `templates/default_canon_patterns.yaml`
- `docs/phase6a_fix_result.md`
- `docs/phase6a_state_manager_result.md`

---

## 2. Phase 6B — 去 AI 味质量闸门

### 目标

建立 Detector → Reviewer → Polisher 三层质量闸门，将 AI 生成文本的机器感降至可控风险以下。

### 已完成

| 交付物 | 状态 | 说明 |
|--------|------|------|
| 检测层（6B-A） | ✅ | 10 项去 AI 味规则 + `analyze_sentence_rhythm.py` + detect Skill |
| 审稿层（6B-B） | ✅ | 十维度 Reviewer Skill + 166 行审稿 Prompt |
| 润色层（6B-C） | ✅ | Polisher Skill + 63 行润色 Prompt + chapter_001 润色样例 |
| 最终验证 | ✅ | polished 版重跑检测：AI 味分数 2/10（低风险），段长标准差 0.85→1.53（↑79%），句首重复完全消除 |

### 关键文件

- `skills/detect_webnovel_ai_flavor/SKILL.md`
- `skills/webnovel_reviewer/SKILL.md`
- `skills/webnovel_polisher/SKILL.md`
- `templates/prompts/chapter_review.md`（166 行）
- `templates/prompts/chapter_polish.md`（63 行）
- `templates/deai_rules/`（10 个规则文件）
- `docs/phase6b_summary.md`

---

## 3. Phase 6C — WPS 项目化管理

### 目标

将本地 story-system 真源投影为 WPS 线上项目结构，实现 build → sync → validate 工具链。

### 已完成

| 交付物 | 状态 | 说明 |
|--------|------|------|
| `build_wps_project_projection.py` | ✅ | 从 story-system 构建本地投影（16 个文件） |
| `sync_wps_project.py` | ✅ | 同步到 WPS，支持 dry-run 和 real 模式 |
| `validate_wps_project.py` | ✅ | 验证投影完整性和安全性 |
| 本地投影（16 文件） | ✅ | publish / story_bible / wiki / index / archive |
| dry-run 同步 | ✅ | 通过，0 errors |
| **real 同步** | **✅ 4/4 success** | **sync_wps_project.py --real 执行，business_code=0** |
| 脚本兼容性修复 | ✅ | `kdocs_env()` + `KDOCS_BIN` + PermissionError fallback，支持 sudo 和非 sudo 场景 |
| 安全脱敏 | ✅ | 复审包无真实 WPS URL / file_id / folder_id / token |
| Token 持久化 | ✅ | 已写入 Hermes 记忆，加密 keychain 存储 |

### 关键文件

- `scripts/build_wps_project_projection.py`
- `scripts/sync_wps_project.py`
- `scripts/validate_wps_project.py`
- `full_review/webnovel_hermes_phase6c_review_bundle/`（完整复审包）
- `docs/phase6c_wps_project_result.md`

### real 同步验证结果

```
$ python3 scripts/sync_wps_project.py --project price_tag_life --real
✅ [volume_current] 人生价格标签_第一卷_当前版 → 00_发布稿
✅ [story_bible]   人生价格标签_Story_Bible_当前版 → 01_设定资料
✅ [wiki]          人生价格标签_小说Wiki_当前版 → 02_小说Wiki
✅ [archive]       2026-05-26_v001_第一卷前三章 → 99_归档版本
📊 状态: success | 成功: 4/4 | business_code: 全部 0
```

---

## 4. 安全扫描结果

| 检查项 | 结果 |
|--------|------|
| 真实 WPS URL | ✅ 无 |
| 真实 file_id/folder_id/link_id/doc_link | ✅ 无 |
| API Key / token / cookie / password | ✅ 无 |
| 真实 .env 内容 | ✅ 无 |
| .story-system 原始文件上传 | ✅ 无 |
| sha256 等完整性哈希 | 允许（非敏感信息） |

**结论：安全扫描通过。** 复审包中所有敏感字段均已脱敏。

---

## 5. 凭据治理说明

本项目涉及以下凭据：

### 5.1 WPS/kdocs-cli 个人 Token

| 属性 | 说明 |
|------|------|
| 存储方式 | kdocs-cli 加密 keychain（`~/.config/kdocs-cli/token.enc`）+ Hermes 永久记忆 |
| 获取方式 | 用户从 `kdocs.cn → 设置 → 开发者选项` 生成 |
| 恢复方式 | 加密文件丢失后从 Hermes 记忆重新 `kdocs-cli auth set-token` |
| 失效条件 | Token 过期或用户手动撤销 |
| 重置流程 | 重新生成 Token → `kdocs-cli auth set-token "新token"` → 更新 Hermes 记忆 |
| 禁止行为 | ❌ 明文记录在日志/文件/commit 中 |

### 5.2 GitHub Personal Access Token

| 属性 | 说明 |
|------|------|
| 存储方式 | 会话内变量（未持久保存） |
| 获取方式 | 用户每次提供 |
| 恢复方式 | 重新提供 |
| 禁止行为 | ❌ 写入任何文件/commit |

### 5.3 DeepSeek API Key

| 属性 | 说明 |
|------|------|
| 存储方式 | `~/.deepcode_key.b64`（base64 编码） |
| 获取方式 | 初始配置时用户提供 |
| 禁止行为 | ❌ 明文出现在对话/日志/commit 中 |

### 5.4 sudo / HOME / PATH 处理原则

当 `sync_wps_project.py` 需要在 sudo 环境下调用 kdocs-cli 时：

```python
# 脚本内置以下保护机制：
KDOCS_BIN = "/home/agentuser/.local/bin/kdocs-cli"   # 绝对路径
KDOCS_HOME = "/home/agentuser"                        # 显式指定 HOME

def kdocs_env():
    env = {**os.environ}
    env["HOME"] = KDOCS_HOME
    # KDOCS_PATH 自动加入 PATH
    return env

# 推荐用法（非 sudo 直跑）：
python3 scripts/sync_wps_project.py --real

# sudo 备用（需指定 HOME）：
sudo HOME=/home/agentuser python3 scripts/sync_wps_project.py --real
```

---

## 6. 验收清单

### 用户回来后需要检查以下 4 项

#### a. WPS 项目是否实际同步成功

登录 https://www.kdocs.cn → 我的云文档 → `小说` 文件夹，应看到 4 个 docx：

| 文件名 | 预期存在 |
|--------|----------|
| 人生价格标签_第一卷_当前版.docx | ✅ |
| 人生价格标签_Story_Bible_当前版.docx | ✅ |
| 人生价格标签_小说Wiki_当前版.docx | ✅ |
| 2026-05-26_v001_第一卷前三章.docx | ✅ |

#### b. 目标文件数量是否一致

复审包 `manifest.txt` 应包含 30 个文件：

```
command_logs/         — 9 个（含 dry-run + real 日志）
phase6c_outputs/      — 11 个（投影 + 状态文件）
project_files/        — 8 个（代码 + 文档）
manifest.txt + file_tree.txt + security_scan.log + REVIEW_README.md — 4 个
```

#### c. 仓库中是否没有敏感信息

```bash
# 在仓库根目录执行安全扫描检查
grep -rn "kdocs\.cn/l/" full_review/   # 应无输出
grep -rn "sk-[A-Za-z0-9]" full_review/ # 应无输出
```

安全扫描报告：`full_review/.../security_scan.log`（真实敏感值命中=0）

#### d. README / 状态文件是否和真实状态一致

| 文件 | 应写状态 |
|------|----------|
| `docs/phase6c_wps_project_result.md` | 全部完成 |
| `full_review/.../REVIEW_README.md` | real 同步 ✅ 通过 |
| `full_review/.../wps_project_doc_meta.json` | mode=real, status=success |
| `full_review/.../wps_project_sync_log.json` | 含 real 成功记录 |

---

## 7. 已知边界与注意事项

### 已完成 but 不完美

| 边界 | 说明 | 后续处理建议 |
|------|------|------------|
| WPS 子文件夹未自动创建 | 4 个 docx 上传到了"小说"根目录，未按结构分配到 00_发布稿/01_设定资料/02_小说Wiki/03_章节索引/99_归档版本 | 后续增强 `sync_wps_project.py` 支持自动创建子文件夹 |
| 单章/审稿报告未同步到 WPS | Phase 6C 限定只同步 4 个核心文档 | 后续阶段可按需放开 |
| 多项目未支持 | 只验证了 price_tag_life 一个项目 | 后续接入新故事时扩展 |
| 版本回收未实现 | 同名文件上传会覆盖 | 后续增加版本编号逻辑 |

### Token 维护注意事项

- Token 不会自动过期（kdocs 个人 Token 长期有效），但如果手动撤销需要重新设置
- 加密文件 `~/.config/kdocs-cli/token.enc` 权限为 `600`，属于 agentuser
- sudo 场景下需显式指定 `HOME=/home/agentuser` 或使用 `sudo -u agentuser`
- Hermes 记忆中的 Token 仅用于恢复，不自动注入 keychain（需手动 `kdocs-cli auth set-token`）

---

## 8. 提交记录

| 提交 | 说明 |
|------|------|
| `d4213d5` | Phase 6C: WPS project management — build/sync/validate scripts, projection, state, review bundle |
| `949b8cc` | Phase 6B final validation |
| `a95364b` | Phase 6B-C: polisher layer |
| `edde2bb` | unify reviewer skill path |
| `0d12ebe` | Phase 6B-2: reviewer upgrade with deai gate |
| `7e284db` | Phase 6C real sync: WPS_FOLDER_ID configured |
| `db8818c` | Phase 6C 尾修：修复复审包状态文件与事实不一致 |
| **`cfcaf33`** | **Phase 6C real 验收通过：tool fix + real success 4/4** |

---

## 9. 最终状态

```
Phase 6 整体状态: completed / pending-human-acceptance
下一阶段状态:    not-started
```

**Phase 6 工具链全部就绪，等待主控方验收。**
