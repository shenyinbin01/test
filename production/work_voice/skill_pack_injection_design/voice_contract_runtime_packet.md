# Voice Contract Runtime Packet

The runtime packet is the only Work Voice artifact that should enter future generation prompts. It is compact, abstract, and contamination-checked.

## Non-Inputs

Do not pass:

- raw observation cards.
- source text.
- raw corpus paths.
- `source_work_id` as a style label.
- non-transferable source elements as usable material.
- author imitation targets.

## YAML Structure

```yaml
work_voice_runtime_packet:
  version:
  status:
  voice_type:
  default_narrator_position:
  default_reader_relationship:
  default_protagonist_distance:
  default_world_attitude:
  scene_type_rules:
    - scene_type:
      narrator_position:
      protagonist_distance:
      reader_relationship:
      world_attitude:
      allowed_interventions: []
      forbidden_interventions: []
      rhythm_hint:
      detail_bias:
  stable_flaws_to_keep: []
  forbidden_original_elements: []
  anti_ai_voice_rules: []
  contamination_guards: []
  human_texture_interaction:
    compatible_fields: []
    conflict_resolution:
  reviewer_focus: []
```

## Field Users

| Field | Planner uses | Writer uses | Reviewer uses | Polisher uses / does not use |
|---|---|---|---|---|
| `version`, `status` | confirm packet lifecycle | confirm approved input | verify packet state | does not use |
| `voice_type` | orient chapter-level stance | high-level tone of narrator relation | check output matches abstract contract | does not use as style target |
| `default_narrator_position` | choose scene defaults | maintain baseline stance | check stance stability | does not repair |
| `default_reader_relationship` | align hooks and exposition | avoid system-report address | check reader role clarity | does not repair |
| `default_protagonist_distance` | align beat focus | control closeness | check distance drift | does not repair |
| `default_world_attitude` | align rules / pressure | maintain world posture | check consistency | local tone only after pass |
| `scene_type_rules` | create scene-level `work_voice` blocks | execute per-scene brief | check scene switch correctness | does not change switching |
| `stable_flaws_to_keep` | preserve narrator imperfection | avoid generic smoothness | check stable flaw is safe and not imitation | may preserve in local polish |
| `forbidden_original_elements` | avoid contamination in plan | avoid contamination in draft | hard gate | must not introduce |
| `anti_ai_voice_rules` | align beat against AI-camera risk | execute as draft constraints | check compliance | may reduce local AI-like phrasing |
| `contamination_guards` | prevent bad inputs | prevent bad output | hard gate | must not bypass |
| `human_texture_interaction` | align focus fields | coordinate scene material and stance | route failures | does not own conflicts |
| `reviewer_focus` | anticipate gate | not directly content | review dimensions | does not use |

## Compile Rule

The packet is compiled only after observation cards, transferable assets, non-transferable elements, and voice contract pass human review. A draft or unchecked contract must not enter Writer.
