# 阶段三点五二次修复：强制 Canon 入模 + chapter_beat 重新收敛 — 执行结果

---

## 一、执行结论

**状态：部分完成**

**一句话总结：** canon 已成功强制注入 DeepSeek 请求的 system+user message，三个输出文件的实际内容已全部收敛（零设定发散）。但关键词级一致性检查发现 2 个伪阳性（"不是死亡倒计时"和"请充值"），导致自动检查 passed=false。

---

## 二、本轮修复内容

### 1. canon 直接注入 system/user message ✅

修改 `call_deepseek.py`：
- 新增 `--canon-text` 参数：接收完整 canon_constraints.yaml 文本
- 新增 `--hard-rules` 参数：接收章节级硬约束文本
- `real_call()` 函数将 canon 文本同时注入：
  - system message 末尾
  - user message 开头
- 如果同时提供了 hard_rules_text，也注入 user message

修改 `run_demo.py`：
- 新增 `render_canon_text_block()`：将 canon_constraints.yaml 渲染为 `【CANON_CONSTRAINTS_BEGIN】...【CANON_CONSTRAINTS_END】`
- 新增 `render_chapter_beat_hard_rules()`：渲染 7 条硬约束
- 三个 phase3 函数在 real 模式均通过 `--canon-text` / `--hard-rules` 传临时文件
- mock 模式不受影响

### 2. chapter_beat hard rules 注入 ✅

chapter_beat 在 real 模式下额外注入：
```text
【CHAPTER_BEAT_HARD_RULES】
1. 禁止使用"生命倒计时"
2. 禁止使用"倒计时"描述标签
3. 禁止把"即将归零"解释为寿命、生命剩余时间、死亡倒计时
4. "即将归零"只能表达综合显影逼近危险临界点
5. 父亲仍然病重存活，不能写已死
6. 不允许新增天秤会、系统、组织、寿命交换、触碰改命
7. 只能写"综合数值趋近于零"或"价格标签正在归零"
```

### 3. chapter_beat prompt 反例增强 ✅

修改 `chapter_beat.md`，新增三段：
- **# forbidden examples** — 9 条禁止写法（"父亲头顶是生命倒计时"等）
- **# correct examples** — 5 条正确写法
- **# self-check strict** — 6 条输出前自检，违规必须重写

### 4. validate_canon_consistency.py 修复 ✅

- forbidden_hits 进入 errors（不再是 warnings）
- errors 格式改为结构化对象：`{type, file, pattern, match}`
- 新增排除 canon_check 段的逻辑

### 5. validate_phase3.py 增强 ✅

- 检查 prompt_inputs 中 canon_injected、hard_rules_injected
- 检查 rendered_system_prompt_preview 包含 CANON_CONSTRAINTS_BEGIN
- 检查 rendered_user_payload_preview 包含 CHAPTER_BEAT_HARD_RULES（仅 chapter_beat）

### 6. Retry 机制（已实现但本次未触发）

- run_demo.py 的 retry 逻辑已实现
- 本次未触发 retry，因为正文输出本身没有禁止词命中

---

## 三、chapter_beat 收敛结果

| 检查项 | 结果 |
|--------|:----:|
| 是否仍出现"生命倒计时" | ✅ **否 — 已收敛** |
| 是否仍出现"倒计时" | ✅ **否 — 正文已无** |
| 是否将标签写为寿命 | ✅ **否** |
| 是否保留"综合显影/选择代价/归零钩子" | ✅ **是** |
| 是否新增天秤会/系统/触碰改命 | ✅ **否** |
| 父亲是否病重存活 | ✅ **是** |

---

## 四、验证命令结果

| 命令 | 退出码 | 结果 | 说明 |
|------|:------:|:----:|------|
| `python scripts/env_check.py` | 0 | ✅ | |
| `python scripts/validate_project.py` | 0 | ✅ | |
| `python -m compileall scripts` | 0 | ✅ | |
| `python scripts/run_demo.py --phase3 --mock` | 0 | ✅ | |
| `python scripts/validate_phase3.py --mode mock` | 0 | ✅ | |
| `python scripts/run_demo.py --phase3 --real` | 1 | ⚠️ | 实际内容已收敛，但 canon consistency 检查发现伪阳性 |
| `python scripts/validate_canon_consistency.py --mode real` | 1 | ⚠️ | failed due to 2 false positives |
| `python scripts/validate_phase3.py --mode real` | — | 🔴 | 因上一步 has_failure=true 未通过 |
| `python scripts/sync_wps.py --dry-run` | 0 | ✅ | |

### 伪阳性详情

canon_consistency_report.json 中的 2 个 errors：

1. **story_bible_real.md — 命中"倒计时"**
   - 实际文本：`"父亲的归零，不是死亡倒计时，而是某个关键选择的代价即将到期"`
   - 分析：这是在**否定**禁止设定，不是设定发散

2. **chapter_beat_real.md — 命中"充值"**
   - 实际文本：`"缴费窗口的电子提示音：‘余额不足，请充值。’"`
   - 分析：这是现实场景中的医院缴费提示音，不是系统文的"充值/商城"概念

---

## 五、输出文件

| 文件 | 状态 |
|------|:----:|
| canon_constraints.yaml | ✅ 已创建 |
| prompt_inputs/chapter_beat_input.json | ✅ canon_injected=true, hard_rules_injected=true |
| prompt_inputs/story_bible_input.json | ✅ canon_injected=true |
| prompt_inputs/humanize_input.json | ✅ canon_injected=true |
| chapter_beat_real.md | ✅ 已收敛（无生命倒计时） |
| canon_consistency_report.json | ✅ 已生成（passed: false, 伪阳性） |
| deepseek_calls.jsonl | ✅ 3 条记录 |

---

## 六、安全检查

| 检查项 | 结果 |
|--------|:----:|
| 是否发现 API Key | ✅ 否 |
| 是否发现 token/cookie/password | ✅ 否 |
| 是否发现 WPS URL/file_id/doc_link | ✅ 否 |
| 是否包含真实 .env | ✅ 否 |
| 是否执行 WPS 真实上传 | ✅ 否 |

---

## 七、最终判断

**是否建议主控方复审：是**
- canon 注入机制已正常工作
- 三个输出文件的实质内容已全部收敛
- 伪阳性属于关键词检查的局限，可通过细化正则或人工判断解决

**是否建议进入阶段四：视主控方复审结果而定**

**下一步优化方向：**
- 细化 forbidden patterns 的正则，排除"不是[禁止词]"的否定句式
- 将"充值"约束更加精确（仅禁止系统文中的"充值/商城"概念，不禁止医院缴费提示）
- 可考虑在 validate_canon_consistency.py 中引入否定词检测豁免
