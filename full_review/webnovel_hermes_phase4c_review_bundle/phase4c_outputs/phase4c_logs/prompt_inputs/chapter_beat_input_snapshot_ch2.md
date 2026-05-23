# chapter_beat Prompt Input Snapshot (Chapter 2)

## Time: 2026-05-23T09:27:19.163643

## Run ID: phase4c_20260523_092706

## System Prompt: /opt/webnovel-hermes-wps/templates/prompts/chapter_beat.md

### System Prompt Content (truncated):
# role
你是一个小说章节节奏设计师。你的任务是根据《人生价格标签》第一章设定，将第一章拆解为具体的场景序列（beats）。

# input
- chapter_outline：包含章节号、标题、核心冲突、钩子（围绕林砚第一次看见价格标签）
- preflight_context：包含当前状态和写作注意事项
- 项目设定：都市脑洞题材，主角林砚是24岁外卖员

# output format
输出严格 JSON 格式（不是 YAML），包含以下字段：

- chapter_number: 1
- chapter_title: "归零"
- total_scenes: 4-6
- scenes: 列表，每个元素包含：
  - order: 场景序号
  - title: 场景名
  - location: 具体地点
  - characters: 出场人物
  - scene_goal: 本场景目标（一句话）
  - conflict_progression: 冲突推进方式
  - cool_point: 爽点设计
  - emotion_change: 情绪变化曲线（起点→终点）

...

### Canon Injection Evidence:
- canon_text file used: /data/webnovel-lab/demo_output/phase4c_logs/phase4c_canon.txt
- hard_rules file used: /data/webnovel-lab/demo_output/phase4c_logs/chapter_002_hard_rules.txt
## User Prompt Input:

# Chapter 002 Beat Generation

## Outline
chapter: 2
goal: 林砚发现价格不是财富，尝试通过标签筹钱，选择代价浮现，回收费城客户线索，标签暴跌对应现实危险
must_include:
- 父亲仍病重存活
- 医院缴费窗口承接
- 林砚急需筹钱
- 林砚误解被动摇
- 选择代价浮现
- 能力副作用
- 光鲜客户线索回收
- 新钩子
scenes:
- location: 医院
  order: 1
  purpose: 承接第一章结尾，缴费压力持续
  title: 医院缴费窗口
- location: 望江路18号
  order: 2
  purpose: 尝试筹集资金，发现线索
  title: 回访光鲜客户
- location: 公寓地下室
  order: 3
  purpose: 发现标签与现实危险的关联
  title: 标签暴跌对应危险
- location: 路上
  order: 4
  purpose: 能力副作用显现，选择代价浮现
  title: 代价浮现
- location: 医院
  order: 5
  purpose: 开头钩子：新线索与新代价
  title: 医院返回
title: 误判代价


## Preflight Context
# Chapter 002 Preflight Context

## 当前状态概要

**上一章结束时：**
- 林砚在第三人民医院缴费窗口余额不足（差3100元），父亲药费面临停药
- 父亲病房门口，林砚看见父亲头顶价格从五位数碎裂归零，最终彻底消失
- 林砚已确认：价格标签不等于财富（老人讨价还价三毛六），但标签真实含义仍未知
- 老人给出警告“眼神太好有时候不是好事”

**角色位置与状态：**
- 林砚：站在父亲病房门口，刚目睹价格归零，经济压力达临界点（差3100元+欠费三天停药）
- 林父：病重住院，呼吸机维持，价格归零但仍存活
- 老人：老旧小区，身份未明，已察觉林砚能力
- 光鲜客户：高档公寓，价格暴跌，电话透露资金问题

**待解决线索：**
1. 父亲价格归零但未死亡——标签与生命的关系是悬疑核心
2. 老人真实身份与价格来源
3. 光鲜客户价格暴跌原因
4. 标签真实机制（林砚仍完全误解）

---

## 本章写作注意事项

### 角色一致性
| 角色 | 必须保持的口吻/行为 |
|------|---------------------|
| 林砚 | 克制、敏感、观察力强、不圣母但有底线；经济压力下会冒险，但不会突然变聪明或变勇敢 |
| 林父 | 病重存活状态，不能苏醒说话，不能有互动 |
| 老人 | 神秘但自然，不能突然出现帮忙或解释能力 |

### 设定一致性
- **父亲必须存活**：价格归零不等于死亡，不能用“生命倒计时”解释
- **标签机制保持悬疑**：林砚只能“理解推进一步”，不能完全搞懂
- **价格暴跌≠破产**：光鲜客户线索回收时，需与治安/危险事件关联，而非单纯财务问题
- **能力副作用**：头痛/短暂失明必须在林砚主动使用能力时出现

### 节奏控制
本章位于**第一幕中段**：危机升级期（父亲归零→急需筹钱→尝试使用能力→发现代价）
- 情绪曲线：紧迫（筹钱）→ 希望（发现机会）→ 落差（代价浮现）→ 更深的悬疑（新线索）
- 不能解决核心问题，只能加深困境

### 钩子衔接
**本章开头必须接：**
- 林砚站在父亲病房门口，看见价格归零后的空白
- 手机震动（医院催缴/平台派单）
- 内心状态：震惊+恐慌+必须行动的紧迫感

---

## 去 AI 腔提醒

### 本章最容易出现 AI 腔的环节

1. **林砚内心独白**：避免“他意识到……”“他明白……”这类总结性陈述
   - ✅ 正确写法：他盯着那片空白，脑子里嗡嗡响。3100。三天。他攥紧手机。
   - ❌ 错误写法：他意识到这串数字的消失意味着某种危机正在逼近。

2. **能力使用时的描写**：避免“他集中精神，试图看清标签的变化”
   - ✅ 正确写法：他盯着下一个外卖客户，太阳穴开始跳，数字边缘模糊了一瞬，疼得他眯起眼。
   - ❌ 错误写法：他调动全部精神力，试图解析标签背后的深层含义。

3. **光鲜客户线索回收**：避免“原来如此，他恍然大悟”
   - ✅ 正确写法：公寓楼下拉着警戒线，警车灯在夜色里转。他听见围观人群说“昨晚出的事”。
   - ❌ 错误写法：他终于明白，价格暴跌代表着这个人正面临巨大的危险。

4. **选择代价描写**：避免“每一次使用能力都在消耗他的生命力”
   - ✅ 正确写法：他靠在墙上，眼前发黑，耳鸣持续了十几秒。手机屏幕上的字看不清了。
   - ❌ 错误写法：他的能力使用次数是有限的，每一次窥探都在透支他的未来。

### 具体场景对应

| 场景 | 避免的AI腔 | 正确的现实写法 |
|------|-----------|---------------|
| 林砚决定再使用能力 | “他下定决心，要利用这个能力改变命运” | 他盯着手机里催缴短信，咬了咬牙，点开下一单 |
| 头痛发作时 | “能力反噬让他的大脑承受巨大负荷” | 他眼前一黑，扶住墙，胃里翻了一下 |
| 回收客户线索时 | “他验证了自己的猜想，价格确实与人生轨迹相关” | 警车灯映在他脸上，他想起昨晚那个男人头顶掉落的数字 |
| 结尾新钩子 | “更大的阴谋正在暗中酝酿” | 手机屏幕亮起，一条陌生号码的短信：“你看见了对吧” |

## Output
生成严格 JSON 格式的 beat 文件，4-6个场景，包含完整情绪弧和 canon_check。

## Command:
python scripts/call_deepseek.py --real --system /opt/webnovel-hermes-wps/templates/prompts/chapter_beat.md --input /data/webnovel-lab/demo_output/phase4c_real_run/chapter_002/prompt_input_chapter_beat.md --output /data/webnovel-lab/demo_output/phase4c_real_run/chapter_002/beat.md --task-name chapter_beat --max-tokens 1500 --canon-text /data/webnovel-lab/demo_output/phase4c_logs/phase4c_canon.txt --hard-rules /data/webnovel-lab/demo_output/phase4c_logs/chapter_002_hard_rules.txt --log /data/webnovel-lab/demo_output/phase4c_logs/deepseek_calls_phase4c_20260523_092706.jsonl
## ⚠️ API Key: [REDACTED — not included in snapshot]
