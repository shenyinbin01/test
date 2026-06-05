# Combined Research Route Reframe

两轮 Deep Research 之后，当前主线不再是：

```text
Human Texture -> Work Voice -> Character Agency -> Reader Immersion -> Agentic Engine
```

这条旧路线的问题是把场景质感、叙述合同、因果发动机、读者结果和运行时架构放在同一条线性队列里，容易误以为每个模块都是同类 prompt patch。

## 新主线

### 第一层：热路径长篇车架

职责：让一本书能稳定从单书承诺推进到卷目标、章节合同和下一章检索。

- `world_slice`：当前热路径需要的最小世界切片。
- `single_book_story`：单书脊梁 / Book Spine。
- `volume_card`：卷级导航与回收窗口。
- `chapter_card`：章节状态变化合同。

### 第二层：场景发动机

职责：让人物在场景内基于目标、信念、误判、策略和代价推动局面。

- `scene_agency_packet`
- `consequence_ledger`
- `relationship_debt_ledger`

### 第三层：正文渲染

职责：在不改因果的前提下，把事件、状态、人物质感和叙述合同转成正文。

- `human_texture_packet`
- `work_voice_contract`
- `renderer_contract`

### 第四层：状态回写

职责：把写后变化转为可追溯增量事实，再归并成运行时视图。

- `state_delta`
- `ledger_reducers`
- runtime views

### 第五层：评价治理层

职责：阻止系统滑向顺滑但空心、连续但机械、账本正确但阅读无生气。

- `longform_reviewer_gate`
- `drift_detection`
- `anti_feed_quality_gate`
- `reader_question_ledger`

## 路线含义

1. Human Texture 是底座，不是全部答案。
2. Work Voice 是 Renderer 合同的一部分，不是因果发动机。
3. Character Agency 是场景发动机，必须早于叙述修辞。
4. Reader Immersion 通过章节卡、读者问题账本和 reviewer gate 生效。
5. Agentic Narrative Engine 继续作为长线 sandbox，不进入当前热路径。
6. IP 宇宙暂缓，当前只允许 `world_slice` 进入最小闭环。
