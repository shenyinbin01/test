# Contamination Checklist

任何一项为 fail，C 组样本不得通过。

| 检查项 | pass/fail | 备注 |
|---|---|---|
| 是否复制原文句子 |  |  |
| 是否保留原作专属名词 |  |  |
| 是否模仿具体作者口癖 |  |  |
| 是否复用可识别桥段 |  |  |
| 是否把 `source_work_id` 写成风格标签 |  |  |
| 是否出现“像某某作者一样写” |  |  |
| 是否出现 “Author Fingerprint / 作者指纹” 表述 |  |  |
| 是否把不可迁移元素写进 `voice_contract` |  |  |
| 是否把 raw corpus 存入仓库 |  |  |
| 是否使用来源作品专属世界观表达 |  |  |
| 是否使用专属句式或高风险修辞习惯 |  |  |
| 是否把原作人物关系模式迁移为新作关系 |  |  |

## Required Result

```yaml
contamination_result:
  copied_source_sentences: pass
  source_specific_terms: pass
  author_mimicry: pass
  recognizable_plot_bridge: pass
  source_work_as_style_label: pass
  forbidden_fingerprint_language: pass
  non_transferable_in_contract: pass
  raw_corpus_saved: pass
  overall: pass
  checked_by:
  checked_at:
```

## Failure Policy

- 原文句子、raw corpus、可识别桥段、具体作者模仿：直接 fail。
- 不可迁移元素进入 contract：退回 aggregation / contract。
- `source_work_id` 被当作风格标签：退回 Work Voice Contract。
- 只存在抽象度不足但无污染：needs_review，不得直接进入验证。
