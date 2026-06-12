# Renderer Skill Public Regression Tests

This file contains invented, public-safe regression tests for `renderer_skill.md`.

No example in this file should contain real novel titles, real character names, real chapter details, source text, or private case traces.

---

## RT-001 Weak transition sentence

### Bad pattern

```text
The people below also saw it.
Everyone understood what that meant.
```

### Failure

The sentences only bridge surrounding beats. They add no new action, consequence, or changed judgment.

### Fix direction

Delete them. Let the result and the next action connect directly.

---

## RT-002 Short-sentence scaffolding

### Bad pattern

```text
North Gate.
Snow had stopped.
The general stood there.
He looked up.
No signal came.
```

### Failure

The paragraph reads like a shot list. Each sentence is low-density.

### Fix direction

Merge pressure, position, expectation, and result into natural prose.

---

## RT-003 Emotion label

### Bad pattern

```text
He waited seriously.
She felt disappointed.
The situation seemed absurd to him.
```

### Failure

Emotion is labeled instead of appearing through state change.

### Fix direction

Show waiting, a delayed action, a repeated confirmation, or a plan changing under pressure.

---

## RT-004 Human-flavor plugin

### Bad pattern

```text
He rubbed his forehead and gave a bitter smile.
```

### Failure

The gesture exists only to make the character feel human. It changes no judgment, action, or relationship.

### Fix direction

Replace with a choice or question that reveals desire, restraint, irritation, or renewed attention.

---

## RT-005 Unsupported genre term

### Bad pattern

```text
The Celestial Resonance Gate refused to echo.
```

### Failure

The term is stylized but unsupported by seed, lexicon, or prior context.

### Fix direction

Use the provided term from input, or plain wording.

---

## RT-006 Repeated fact in new clothes

### Bad pattern

```text
The bridge did not appear.
The road remained closed.
The answer was still absence.
```

### Failure

Three sentences restate the same absence.

### Fix direction

State the absence once. Use later sentences for consequence or action.

---

## RT-007 Checklist judgment

### Bad pattern

```text
No hidden guard.
No array.
No talisman.
No trace of spellwork.
```

### Failure

The character's perception is written as an audit checklist.

### Fix direction

Merge into a natural judgment: the character searches the relevant space and fails to find a source.

---

## RT-008 Customer-service rule carrier

### Bad pattern

```text
Mismatch detected. Suggested alternatives: submit a symbolic victory, choose a substitute target, or request task downgrade.
```

### Failure

The rule carrier explains and solves its own mismatch.

### Fix direction

Let the rule carrier repeat condition and limitation. Let the character discover the mismatch.

---

## RT-009 Late resource as broken resource

### Bad pattern

```text
The starter reward was moldy, cracked, and nearly useless.
```

### Failure

The contrast is downgraded into garbage comedy.

### Fix direction

Show that the reward would have mattered at the proper time or level, but is mismatched now.

---

## RT-010 Joke-only hook

### Bad pattern

```text
He asked whether the shop sold funeral wreaths, and the chapter ended on the joke.
```

### Failure

The ending leaves a joke, not an action problem.

### Fix direction

End with what must be done next, why it matters, and what remains blocked.

---

## RT-011 Cooling down absurdity

### Bad pattern

```text
The character verified the rule, logged the mismatch, assigned someone to investigate, and moved on.
```

### Failure

The absurd premise is processed like a workflow. The character has no reactive warmth or comic pressure.

### Fix direction

Let humor arise from the mismatch itself: a serious character asks practical questions that expose the ridiculous condition.

---

## RT-012 Over-certifying contrast

### Bad pattern

```text
The object was useful for beginners. The protagonist was no longer a beginner. The protagonist had better resources. Other people might still need it. This proved it was mismatched.
```

### Failure

The same contrast is certified too many times.

### Fix direction

Keep the sharpest comparison and cut the rest.

---

## RT-013 Unsupported value judgment

### Bad pattern

```text
The manual was correct and valuable.
```

### Failure

The value is asserted without evidence.

### Fix direction

Show a support point: visible structure, concrete use, authority source, comparison object, or character recognition basis.

---

## RT-014 Decorative backstory

### Bad pattern

```text
He remembered the old alley, the rain, and the nights when he had nothing, but the memory does not affect his current decision.
```

### Failure

Backstory is inserted for atmosphere and does not serve present contrast.

### Fix direction

Use past detail only if it clarifies what was once lacking, why a late resource matters, or why an old issue becomes relevant now.

---

## RT-015 Passive secondary characters

### Bad pattern

```text
The elders stood aside, waited, received orders, and left.
```

### Failure

Secondary characters function only as scenery or task executors.

### Fix direction

Give them a structural role: public pressure, mistaken reading, world-rule exposure, trigger for a new thought, or constraint on the next action.

---

## RT-016 Absurd task with no solution seeds

### Bad pattern

```text
The task was impossible, so the character decided to investigate.
```

### Failure

The ending has direction but no solution texture.

### Fix direction

Leave a few possible workarounds that are absurd but follow the character's logic. The reader should want to see how the serious character solves the ridiculous condition.
