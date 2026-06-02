# Phase 8 Step 7 第二批: Polisher 轻量注入

## 前提
五章连续验证已证明 Planner/Writer/Reviewer 链路可以独立产出合格章节。
Polisher 不再承担救稿职责。
Polisher 只负责轻量增强。

## 注入目标
- target_skill: webnovel_polisher
- do_not_modify: planner, writer, reviewer, statemanager, wpssync, detector

## 注入规则（4个方向）

### 1. 认知对比锐化 (DCQG-C001)
在已有 beat 成立时，增强主角洞察与他人误判之间的对比。
不新增认知碾压桥段，不硬塞爽点。

### 2. 价值观/理念冲突对话增强 (DCQG-C015)
强化关键对话中的立场差异、潜台词和人物态度。
不强加长篇独白，不把人物写成观点接口。

### 3. 规则利用清晰化 (DCQG-C021)
让规则破局的行动链条更清楚。
不改变原有破局逻辑，不新增设定。

### 4. 章尾余味/回环增强 (DCQG-C022)
强化章尾与开章、主线、情绪钩子的呼应。
不强行煽情，不每章都写"初心回归"。

## 明确禁止
- 不重写剧情结构
- 不补主角发动机
- 不补新爽点/新钩子
- 不改变 chapter beat
- 不修改 Planner/Writer/Reviewer
- 不把技法卡全文复制进 Polisher
- 不把 Polisher 改成二次 Writer
