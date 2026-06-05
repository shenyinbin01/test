# Experiment Design

## 实验目的

验证长篇热路径结构是否能改善三章连续中的主线稳定、关系债继承、知识状态一致、读者问题管理和状态写回追溯。

本文件只设计实验框架：

- 不生成真实小说正文。
- 不使用具体作者。
- 不使用 raw corpus。
- 不创建真实长篇小说大纲。

## 组别

### A = current baseline

使用现有 `chapter_beat` / `runtime_canon` 粗回写。它代表当前逐章链路。

### B = longform structure

使用 `single_book_story` + `volume_card` + `chapter_card` + `state_delta` + ledger reducers，但不加 `scene_agency_packet`。

该组测试：仅靠长篇车架与写回，是否已经能改善连续性。

### C = longform + engine

在 B 基础上加入 `scene_agency_packet` + Story Orchestrator Lite + Renderer blocker。

该组测试：场景发动机与边界调度是否进一步改善人物主动感和状态继承，同时不引入主线偏航。

## 对照重点

| 项目 | A | B | C |
|---|---|---|---|
| 单书脊梁 | optional | required | required |
| 卷卡 | no | required | required |
| 章节卡 | no | required | required |
| 场景行动包 | no | no | required |
| state_delta | rough writeback | required | required |
| ledger reducers | no | required | required |
| Orchestrator Lite | no | no | required |
| Renderer blocker | no | no | required |

## 不在本轮验证

- 不验证完整 IP 宇宙。
- 不验证一卷十章。
- 不验证完整多 agent。
- 不验证正式 skill-pack patch。
- 不验证具体正文审美质量。
