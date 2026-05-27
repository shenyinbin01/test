# Phase 7 审计修正报告

生成时间：2026-05-27

## 1. 修正目标

| # | 修正项 | 状态 |
|---|--------|------|
| 1 | 通用 Prompt 去项目绑定 | ✅ 完成 |
| 2 | StateManager apply_commit 安全顺序 | ✅ 完成 |
| 3 | 统一 Skill frontmatter name | ✅ 完成 |
| 4 | skill-pack README 和 AGENTS 状态修正 | ✅ 完成 |
| 5 | 输出修正报告 | ✅ 完成 |

## 2. 修改文件清单

### 2.1 Prompt 模板（6 个文件修改）

| 文件 | 修改内容 |
|------|----------|
| `templates/prompts/story_bible.md` | 移除"人生价格标签核心脑洞"专属约束；将 forbidden drift 替换为通用 canon_drift_rules 引用；将 initial_price_tag/price_tag_meaning 改为通用 initial_power_state/power_meaning；输出格式中的 story_synopsis 改为"围绕项目核心脑洞" |
| `templates/prompts/chapter_beat.md` | 全面重写：移除"人生价格标签"专属约束（生命倒计时、天秤会、系统面板等 9 条）；移除"阶段四B real 执行强化"章节；移除第一章 5 个核心目标约束；移除 forbidden drift 中的 10 条项目专属规则；移除 correct examples 中的项目示例；新增通用的 canon drift 引用 + self-check strict |
| `templates/prompts/chapter_writer.md` | 移除"阶段四B real 执行强化"章节（写外卖场景、老人、光鲜客户、医院缴费窗口、父亲价格即将归零等）；移除"围绕《人生价格标签》"；移除 max_tokens 1800-2500 等运行期参数；保留通用 canon 约束、写作约束、连续性要求 |
| `templates/prompts/chapter_commit.md` | 移除"阶段四B real 执行强化"章节；移除 father 状态"病重存活"专属约束；移除"ability_rule_updates 只记录林砚理解变化"专属约束；移除"不得将价格标签写成寿命"等 canon 约束（这些应来自 canon_drift_rules 而非 Prompt） |
| `templates/prompts/chapter_review.md` | 移除"林砚、父亲、老人、客户"角色绑定，改为通用"每个角色的行为是否符合人设" |
| `templates/prompts/projection.md` | 无项目绑定内容，未修改 |
| `templates/prompts/chapter_outline.md` | 无项目绑定内容，未修改 |
| `templates/prompts/chapter_polish.md` | 无项目绑定内容，未修改 |

### 2.2 webnovel_state_manager/SKILL.md

| 修改项 | 旧行为 | 新行为 |
|--------|--------|--------|
| apply_commit 执行顺序 | 先写入正式文件，再运行 validator | 先生成临时 next_* 文件 → 运行 validator → validator pass 后才写入正式文件 |
| validator fail 处理 | 报告不一致项，不阻止写入 | 阻止写入正式文件，仅记录 audit_log |
| 临时文件机制 | 无 | 新增 inner_tmp_next_runtime_canon / next_reader_debts / next_webnovel_state |
| audit_log 记录 | 统一记录 | 区分 validated: pass 和 validated: fail + issues |

### 2.3 Skill frontmatter name 统一（3 个 source + 3 个 skill-pack 拷贝）

| 文件 | 旧 name | 新 name |
|------|---------|---------|
| `skills/detect_webnovel_ai_flavor/SKILL.md` | detect-webnovel-ai-flavor | detect_webnovel_ai_flavor |
| `skills/webnovel_reviewer/SKILL.md` | webnovel-reviewer | webnovel_reviewer |
| `skills/webnovel_polisher/SKILL.md` | webnovel-polisher | webnovel_polisher |
| `skill-pack/creation_skills/detect-ai-flavor/SKILL.md` | detect-webnovel-ai-flavor | detect_webnovel_ai_flavor |
| `skill-pack/creation_skills/webnovel-reviewer/SKILL.md` | webnovel-reviewer | webnovel_reviewer |
| `skill-pack/creation_skills/webnovel-polisher/SKILL.md` | webnovel-polisher | webnovel_polisher |

同时将 skill-pack/creation_skills 中 3 个 hyphen 目录重命名为 underscore：
- `detect-ai-flavor/` → `detect_webnovel_ai_flavor/`
- `webnovel-reviewer/` → `webnovel_reviewer/`
- `webnovel-polisher/` → `webnovel_polisher/`

### 2.4 skill-pack 文档更新

| 文件 | 修改内容 |
|------|----------|
| `skill-pack/README.md` | 目录树更新为 underscore 目录名；删除"已定义但未实现"旧表项；保留 7 个创作 Skill 全部已实现 |
| `skill-pack/mapping.md` | 文件路径更新为 underscore 命名；支撑文档表新增 Phase 7 审计修正报告 |
| `AGENTS.md` | Phase 7 状态从 🔄 in_progress → 🔍 pending_audit；新增子阶段 7.4 审计修正 ✅ |
| `skill-pack/AGENTS.md` | 同上 |

## 3. 禁止事项遵守情况

| 禁止事项 | 状态 |
|----------|------|
| 是否生成正式章节 | ❌ 未生成 |
| 是否修改正式正文（price_tag_life 正文 | ❌ 未修改 |
| 是否修改正式 .story-system | ❌ 未修改 |
| 是否同步 WPS | ❌ 未执行 |
| 是否修改 run_chapter_pipeline.py | ❌ 未修改 |
| 是否进入正式 chapter_007 生产 | ❌ 未进入 |
| 是否修改沙盒项目 | ❌ 未修改 |

## 4. 是否可进入正式章节生产试运行

**状态：🔍 pending_audit，待主控方验收**

修正完成后 Phase 7 多角色 Skill 体系的阻点已全部清除：
- ✅ Prompt 模板不再绑定特定项目，可泛化到任何网文项目
- ✅ StateManager apply_commit 有安全顺序，validator fail 不污染正典
- ✅ 7 个 creation Skill 的 frontmatter name 全部统一为 underscore
- ✅ skill-pack README 和 AGENTS.md 反映最新状态

**等待主控方验收通过后**，即可进入正式章节生产试运行（Phase 8）。
