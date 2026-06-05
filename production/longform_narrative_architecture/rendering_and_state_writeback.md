# Rendering And State Writeback

正文渲染完成后，必须回写状态。没有状态回写，长篇会变成一串局部有效但无法继承的片段。

## state_delta 草案

```yaml
state_delta:
  plot_progress: ""
  character_state_change: ""
  relationship_debt_change: ""
  resource_change: ""
  knowledge_change: ""
  unresolved_threads:
    - ""
  reader_questions:
    - ""
  next_chapter_seed: ""
```

## 回写原则

- 只回写会影响后续选择的变化。
- 不把每个细节都写进账本。
- 情绪只有造成行动后果，才进入状态。
- 关系只有改变下一次互动，才进入关系债。
- 信息只有改变谁能做什么，才进入信息账本。

## Polisher 边界

Polisher 不能补状态回写。它只能在结构通过后处理语言显性、节奏压缩和已有余味。
