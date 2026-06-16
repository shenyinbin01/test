# Codex Task：使用 Renderer Skill v0.7 中文执行版单次生成第一章

## 0. 任务性质

这是一次单章生成测试。

不要迭代。不要修改主 Skill。不要修改 working skill。不要生成多轮候选。不要做 LOOP。不要做 Skill Delta。不要做治理文件。

只做一件事：按照本分支中的 Renderer Skill v0.7 中文执行版，生成一篇完整第一章样稿。

Skill 文件路径：

```text
production/renderer_skill_lab/skill_variants/renderer_skill_v0.7_zh_exec.md
```

## 1. 仓库与分支

仓库：

```text
shenyinbin01/test
```

分支：

```text
skill/v07-zh-exec-baseline
```

请先拉取并切换到该分支：

```bash
git fetch origin skill/v07-zh-exec-baseline
git checkout skill/v07-zh-exec-baseline
git pull origin skill/v07-zh-exec-baseline
```

新建输出目录：

```text
production/renderer_skill_lab/experiments/ch001_v07_zh_codex_single/
```

只允许新增以下文件：

```text
production/renderer_skill_lab/experiments/ch001_v07_zh_codex_single/output.md
production/renderer_skill_lab/experiments/ch001_v07_zh_codex_single/self_check.md
```

禁止修改：

```text
production/renderer_skill_lab/skill/renderer_skill.md
production/renderer_skill_lab/skill/skill_changelog.md
production/renderer_skill_lab/skill/regression_tests.md
production/renderer_skill_lab/skill_variants/renderer_skill_v0.7_zh_exec.md
production/renderer_skill_lab/skill_variants/ch001_v07_zh_codex_single_task.md
```

也不要读取或使用：

```text
production/renderer_skill_lab/experiments/ch001_loop_01/working_skill/
production/renderer_skill_lab/experiments/ch001_loop_01/final_recommended_output.md
```

ch001_loop_01 是失败样本，不得作为写作模板。

## 2. 本章最小故事上下文

只使用以下上下文。没有明确给出的，不要擅自新增。

### 世界与主角

```text
九州大陆。
飞升路已经断绝很久。
江离是当代人皇，修为极高，处在大乘期/九州顶点。
江离正在尝试渡成仙劫，但飞升失败。
```

### 系统事件

```text
江离飞升失败后，识海中出现迟到的逆袭系统。
系统绑定对象是江离。
系统绑定时间停留在五百年前。
系统给出新手礼包。
系统发布新手任务：战胜江一星。
```

### 新手礼包

礼包可以包含低阶修士才需要的资源，例如低阶丹药、符箓、灵石等。

但不要写成长清单，不要逐项解释。只突出一两个物件，证明：

```text
五百年前的江离确实需要它；
现在的江离已经完全不需要；
系统仍停留在五百年前。
```

### 江一星

```text
江一星与五百年前的江离有关。
他对当年的江离有旧账、压力或冲突。
但现在江离已经是人皇/大乘期，双方层级完全错位。
```

如果素材没有明确说明江一星已经死亡，不要直接写死。可以让江离把“江一星现在在哪里、是否还活着、系统如何认定目标”作为下一步要核验的问题。

## 3. 本章必须完成的剧情功能

正文必须完成：

```text
1. 飞升失败的大场面开局；
2. 迟到系统出现；
3. 新手礼包制造强烈错位；
4. 新手任务“战胜江一星”抛出荒唐目标；
5. 江离认真拆解任务边界；
6. 结尾给出下一章行动苗头。
```

## 4. 硬性禁止

```text
1. 不要写成梗概。
2. 不要低于 2500 中文字。
3. 不要超过 3500 中文字。
4. 不要新增任务期限。
5. 不要新增系统商店。
6. 不要新增系统奖励。
7. 不要新增未确认的重要组织功能。
8. 不要新增未确认的重要配角承担关键剧情功能。
9. 不要把江一星写成当前阶段的大反派。
10. 不要直接写死江一星已死亡，除非有明确 seed。
11. 不要用现代吐槽制造人味。
12. 不要逐项解释礼包。
13. 不要让配角替作者解释。
14. 不要用作者总结句收尾。
15. 不要为了 canon 安全而删掉场面、人物反应和章节厚度。
16. 不要使用 ch001_loop_01 的写法。
```

## 5. 输出要求

### output.md

只放小说正文。

不要标题。不要分析。不要自检。不要 markdown 表格。不要解释你如何写作。

### self_check.md

写简短自检：

```markdown
# Self Check

## v0.7 执行情况

- 是否保留大场面开头：
- 是否没有冷却核心前提：
- 是否有章节完整度：
- 是否有人物在场感：
- 是否有迟到资源的价值反差：
- 是否有荒唐任务的执行钩子：

## 风险

- 是否存在 canon drift：
- 是否存在解释膨胀：
- 是否存在配角捧哏：
- 是否存在旧史过载：
- 是否像梗概：

## 自判

- 是否明显强于 ch001_loop_01 final：
- 是否接近 v0.7 审美基线：
- 最大问题：
```

## 6. 提交要求

完成后提交并推送到同一分支：

```text
skill/v07-zh-exec-baseline
```

提交范围只能包含：

```text
production/renderer_skill_lab/experiments/ch001_v07_zh_codex_single/output.md
production/renderer_skill_lab/experiments/ch001_v07_zh_codex_single/self_check.md
```

回传：

```text
1. commit SHA
2. 文件清单
3. output.md 路径
4. self_check.md 路径
```

然后停止，等待外部审计。
