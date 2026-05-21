# chapter_writer Prompt Input Snapshot

## Time: 2026-05-21T22:17:39.728114

## System Prompt: /opt/webnovel-hermes-wps/templates/prompts/chapter_writer.md

### System Prompt Content (truncated to show canon injection):
# role
你是一个中文网文写手。你的任务是根据章节规划（beat）和写作上下文，写出一章可读的网文正文。

# input
- chapter_beat：场景序列、叙事功能、关键台词
- preflight_context：当前状态、角色状态、注意事项
- deai_rules：去 AI 腔规则（必须严格遵守）

# output format
输出纯文本（Markdown），格式要求：

1. 标题：第 X 章 章节名
2. 正文：按场景顺序书写，每个场景之间用 `---` 分隔
3. 字数：2000-3000 字

# quality
- 每段对话必须让人能听出是谁在说话（口吻差异）
- 钩子必须放在章尾，不能提前泄底
- 情绪必须有推进：不能让读者在同一情绪下停留超过 1/3 章的篇幅
- 不能使用总结性旁白替代实际场景
- 严格检查 deai_rules：全文不得出现 AI 腔句式

# forbidden
- 不可使用以下词汇/句式：仿佛、似乎、好像、突然、瞬间、他意识到、他感到、一种说不出的
- 不可使用总结代替场景：比如用"他们谈了很久"代替实际对话
- 不可在章尾用

...

### Canon Injection Evidence:
- canon_text file used: /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_canon.txt
- hard_rules file used: /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_hard_rules.txt
- canonical tell (hardcoded in canon_text var): present

## User Prompt Input:

# Chapter 001 Draft Writing

## Chapter Beat
```json
{
  "chapter_number": 1,
  "chapter_title": "归零",
  "total_scenes": 5,
  "scenes": [
    {
      "order": 1,
      "title": "第一次看见",
      "location": "城区写字楼电梯口",
      "characters": ["林砚", "外卖站长（电话）", "保安"],
      "scene_goal": "林砚在送餐途中第一次看见价格标签，引发困惑",
      "conflict_progression": "林砚正被站长电话催促超时配送，抬头看见一个穿着普通工装的老人从电梯出来，老人头顶浮现一行数字——'1,200,000'。林砚愣住，以为眼花了，揉眼再看，数字还在。保安推了他一把，他才回神。冲突从'送餐压力'转向'认知冲击'。",
      "cool_point": "林砚发现自己的视觉出现了'异常'——他能看见别人头顶的数字，而且这个数字与对方的穿着、身份完全不匹配。",
      "emotion_change": "烦躁→困惑→震惊",
      "cliffhanger_hook": "林砚回头想再看那个老人，对方已经消失在街角，但数字'1,200,000'像烙印一样留在视网膜上。"
    },
    {
      "order": 2,
      "title": "光鲜的裂痕",
      "location": "高档小区客户家门口",
      "characters": ["林砚", "女客户"],
      "scene_goal": "林砚发现第二个价格标签，与第一个形成强烈反差",
      "conflict_progression": "林砚送餐到一栋高档公寓，开门的是一位穿着精致、妆容得体的年轻女性，室内是名牌包和进口家具。林砚下意识看了一眼她头顶——'85,000'，而且数字正在下降，每几秒跳一次，已经跌到'83,200'。林砚递餐时手顿了一下，女客户不耐烦地皱眉。冲突从'富人更值钱'的直觉判断，转向'为什么她在下跌'的困惑。",
      "cool_point": "表面光鲜的客户头顶价格正在快速下跌，而刚才那个穿工装的老人头顶却高达百万——林砚第一次意识到'表面身份'与'价格'之间存在巨大鸿沟。",
      "emotion_change": "困惑→好奇→紧张",
      "cliffhanger_hook": "林砚下楼时听见那户人家传来摔东西的声音和男人的吼叫，数字在他脑海里继续下跌。"
    },
    {
      "order": 3,
      "title": "误判",
      "location": "街边快餐店",
      "characters": ["林砚", "快餐店老板", "外卖员同行"],
      "scene_goal": "林砚试图验证标签与财富的关系，结果第一次判断失误",
      "conflict_progression": "林砚在等餐时，看见一个穿西装、戴名表的中年男人走进隔壁银行，头顶数字是'450,000'。林砚心想：果然有钱人价格高。但随后他看见快餐店老板——一个满手油污、穿着褪色围裙的中年女人——头顶数字是'680,000'。林砚呆住了。老板催他拿餐，他脱口而出：'老板娘，你这店生意不错吧？'老板白了他一眼：'关你什么事？'冲突从'标签=财富'的假设，转向'标签不等于财富'的认知崩塌。",
      "cool_point": "林砚用自己的'常识'判断价格高低，结果两次都被打脸——穿着普通的女老板比西装精英价格更高，这让他意识到标签背后有更复杂的逻辑。",
      "emotion_change": "自信→困惑→挫败",
      "cliffhanger_hook": "林砚骑车离开时，头痛突然袭来，视线模糊了一瞬——能力使用开始产生代价。"
    },
    {
      "order": 4,
      "title": "归零",
      "location": "市立医院住院部缴费窗口",
      "characters": ["林砚", "收费员", "排队病患家属"],
      "scene_goal": "林砚在医院缴费时，看见父亲头顶的价格标签正在归零，形成全章最强悬念",
      "conflict_progression": "林砚接到医院电话说父亲病情恶化需要补缴费用，他骑车赶到缴费窗口。排队时，他下意识抬头看向父亲病房的方向，隔着走廊看见父亲头顶浮现一个数字——'5,000'。但数字正在下降：4,800、4,200、3,100、1,500……林砚心跳加速，推开排队的人群往前挤，收费员喊他排队，他充耳不闻。数字继续下降：800、300、50、0。归零。标签消失了。冲突从'理解标签'的认知问题，升级为'父亲怎么了'的生存危机。",
      "cool_point": "林砚终于将标签与自身联系起来——父亲头顶的价格正在归零，而这不是财富，也不是寿命，是一种他尚未理解但直觉感受到的'危险信号'。",
      "emotion_change": "焦虑→恐惧→绝望",
      "cliffhanger_hook": "林砚手里的银行卡掉在柜台台面上，他转身就跑向走廊尽头的ICU方向。"
    },
    {
      "order": 5,
      "title": "走廊尽头",
      "location": "ICU走廊",
      "characters": ["林砚", "护士（远处）", "父亲（病床上，不出声）"],
      "scene_goal": "林砚跑到ICU门口，看见父亲躺在里面，悬疑与情感双重收束",
      "conflict_progression": "林砚冲到ICU门口，透过玻璃窗看见父亲躺在病床上，身上插满管子。护士正在里面做检查。林砚想推门进去，被另一个护士拦住：'家属在外面等。'他攥着那张掉在地上的银行卡，手在抖。他再次看向父亲头顶——没有数字了，什么都没有。但父亲还在呼吸。冲突从'价格归零=死亡'的恐惧，转向'价格归零≠死亡'的困惑——父亲还活着，但标签没了，那归零到底意味着什么？",
      "cool_point": "林砚在极端情绪中保持观察——父亲还活着，但标签归零，这打破了他之前所有关于标签的猜测，留下最强悬疑。",
      "emotion_change": "绝望→困惑→压抑的决意",
      "cliffhanger_hook": "林砚站在玻璃窗前，脑海里闪过今天看见的三个数字：老人的百万、女客户的下跌、父亲的归零。他低声说：'我必须弄懂这到底是什么。'"
    }
  ],
  "full_chapter_summary": "外卖员林砚在送餐途中，第一次看见普通人头顶浮现'价格标签'。一个穿工装的

## Preflight Context
# Preflight Context — 第一章

## 当前状态概要

上一章结束时：林砚在医院缴费窗口，看见父亲头顶标签从5000逐步下降至归零消失，得知父亲已转ICU，银行卡掉在柜台，他转身跑向走廊尽头。

角色位置：医院缴费窗口→ICU方向走廊。状态：极度焦虑、震惊、困惑。

待解决线索：
- 父亲价格归零意味着什么（不是死亡，但迫在眉睫）
- 标签真实含义仍未知
- 老人身份未揭示
- 光鲜客户暴跌原因未完全揭示

## 本章写作注意事项

### 角色一致性
- **林砚**：克制、敏感、观察力强。此刻应呈现“压抑的慌乱”——行动迅速但沉默，内心有大量未说出口的推演。口吻保持现实感，不煽情。
- **父亲**：不出场对话，只作为病床上的存在。不写死亡。

### 设定一致性
- 价格归零 ≠ 死亡。不能写“心电图成直线”“生命倒计时”。
- 标签不是系统面板，不显示说明文字、任务提示、倒计时。
- 禁止出现：天秤会、组织、系统、等级、异能组织。

### 节奏控制
本章位于：**悬念释放+情感重压**阶段。
- 开篇直接从医院走廊开始，承接上章结尾。
- 中间穿插林砚回忆白天老人和客户的标签反差，形成对照。
- 结尾停在ICU门口，不进入病房，留白。

### 钩子衔接
本章开头需接：林砚跑向走廊尽头，ICU门在视线尽头。
- 建议：以动作和感官细节开场（脚步声、消毒水味、走廊灯光），不解释。

## 去AI腔提醒

1. **“他意识到”句式**：本章林砚处于困惑和直觉驱动状态，不要写“他意识到标签代表XXX”。他还不懂。
2. **心理描写过度**：避免大段内心独白。用动作、停顿、视线转移替代。
3. **标签数字出现场景**：只在林砚主动看的时候出现。不自动弹出、不闪烁、不伴随音效。
4. **“突然”“瞬间”滥用**：父亲价格归零是逐步下降（5000→归零），不是瞬间崩盘。用过程感替代突袭感。
5. **煽情收尾**：ICU门口不要写“他握紧拳头，眼里燃起火焰”。写他停下脚步，看见玻璃窗里的父亲，手里攥着那张掉在柜台的银行卡。

## Output
写第一章正文（1200-1800中文字）。
场景必须包括：外卖配送→老人标签高价→光鲜客户标签下跌→林砚思考→医院缴费窗口→父亲价格归零。
结尾必须落在父亲头顶价格正在趋近于零。
不要解释完整能力机制，只让林砚产生初步误判与困惑。

## Command:
python scripts/call_deepseek.py --real --system /opt/webnovel-hermes-wps/templates/prompts/chapter_writer.md --input /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/prompt_input_chapter_writer.md --output /data/webnovel-lab/demo_output/phase4b_real_run/chapter_001/draft.md --task-name chapter_writer --max-tokens 2500 --canon-text /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_canon.txt --hard-rules /data/webnovel-lab/demo_output/phase4b_logs/chapter_001_hard_rules.txt --log /data/webnovel-lab/demo_output/phase4b_logs/deepseek_calls_phase4b.jsonl
## ⚠️ API Key: [REDACTED — not included in snapshot]
