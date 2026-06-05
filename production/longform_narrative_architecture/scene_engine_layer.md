# Scene Engine Layer

场景发动机层把章节要求转成具体人物选择。

## 输入

- `chapter_card`
- Human Texture compact packet
- Work Voice runtime packet
- `scene_agency_packet`
- 当前 consequence ledger
- 当前 relationship debt ledger

## 核心问题

场景不应只是“展示设定、触发规则、抛出钩子”。它必须回答：

1. 谁在场景里主动处理局面。
2. 这个人物想要什么。
3. 他误判了什么。
4. 他做了什么取舍。
5. 他的选择改变了什么。
6. 哪些后果进入下一场景。

## 与 scene_agency_packet 的关系

`scene_agency_packet` 是场景发动机的最小 contract。它不写正文，只提供人物在局面中的决策骨架。
