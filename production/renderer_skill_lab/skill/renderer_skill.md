# Renderer Skill v0.6 — Public Generic Version

## 0. Purpose

This Skill is a reusable prompt asset for turning a compact chapter seed into natural long-form web novel prose.

It is designed to be public, generic, and project-portable. It must not contain private case details, copyrighted source text, real comparison excerpts, real character names, or story-specific plot notes.

The goal is not to imitate any source text or author. The goal is to encode reusable editorial judgment: how to avoid obvious AI prose, preserve narrative function, and render scenes with natural density.

Priority order:

1. Non-regression red lines
2. Sentence-level natural density
3. Character judgment and desire
4. Emotion through state change
5. Triggered scene rules
6. Chapter-specific seed constraints

A lower-priority goal must never break a higher-priority red line.

---

## 1. Input Boundaries

Allowed inputs:

- Chapter seed
- Minimal setting notes
- Required characters or roles
- Required pressure, conflict, task, or abnormal event
- Required ending hook
- Current Skill
- Word-count range

Forbidden inputs:

- Original copyrighted prose
- Source text excerpts
- Source-text sentence variants
- Private comparison notes
- Specific author style imitation
- Case-specific critique that has not been abstracted

If a term, proper noun, rule, object, or mechanism is not present in the seed, project lexicon, or established prior context, do not invent it merely to create atmosphere.

---

## 2. Public Asset Boundary

This Skill may contain:

- Generic bad patterns
- Generic red lines
- Generic review questions
- Generic scene-triggered rules
- Fully invented examples

This Skill must not contain:

- Real novel titles
- Real chapter titles
- Real character names
- Real task names from private cases
- Real source text or close paraphrases
- Private case conclusions that only apply to one chapter

Specific cases belong in private case notes. Only abstracted, reusable rules belong here.

---

## 3. Non-Regression Red Lines

If any red line appears, the draft fails unless there is a strong scene-specific reason.

### 3.1 Weak transition sentences

Delete sentences that only connect surrounding text but add no new information.

High-risk pattern:

- People also saw it.
- Everyone understood what it meant.
- The matter had reached this point.
- They waited too.
- He knew the problem had arrived.

Review question:

Would deleting this sentence make the paragraph tighter or better? If yes, delete it.

---

### 3.2 Short-sentence scaffolding

Short sentences are allowed, but continuous low-density short sentences are not.

Bad pattern:

- Location.
- Weather.
- Character position.
- Small action.
- Result.
- Emotion label.

This reads like a shot list, not prose.

Rule:

Short sentences must carry weight. Do not use them merely to place camera beats.

---

### 3.3 Emotion labels

Do not directly state that a character is serious, disappointed, embarrassed, conflicted, or feeling absurdity.

Forbidden tendency:

- He waited seriously.
- She felt disappointed.
- He found it absurd.
- His emotions were complicated.
- He was slightly embarrassed.

Replacement:

Let emotion appear through waiting, delayed movement, repeated confirmation, changed action, renewed attention, abandoned action, or a choice made under pressure.

---

### 3.4 Human-flavor plugins

Do not use small gestures merely to make a character seem alive.

High-risk gestures:

- Bitter smile
- Touching the nose
- Awkward cough
- Rubbing the forehead
- Looking down and smiling
- Hiding an object just to create embarrassment

These gestures are not banned absolutely. They fail when they do not change judgment, action, relationship, or consequence.

A character feels alive through desire, judgment, hesitation, old memory being reactivated, discovering usefulness inside absurdity, and changing plans.

---

### 3.5 Unsupported clever metaphor or half-formed terminology

Do not invent stylized terms or metaphors merely for genre flavor.

A term is allowed only if at least one condition is true:

1. It appears in the seed.
2. It appears in the project lexicon.
3. It has been established earlier in the same continuity.
4. It is a clear genre-common term.
5. The immediate context makes it necessary and clear.

Review questions:

- Was this term given to me, or did I create it for atmosphere?
- Is it more accurate than plain wording?
- Would the reader pause to decode it?

If uncertain, use plain wording.

---

### 3.6 Repeated fact in new clothes

State a fact once. Do not repeat it through a metaphor, echo line, or rephrased conclusion.

Bad pattern:

- The expected thing did not appear.
- The door did not open.
- The road did not show.
- This was another failure.

If a fact has already landed, later sentences must show consequence, not restate the same fact.

---

### 3.7 Checklist-style judgment

Do not write a character's perception as a mechanical audit list unless the list itself drives the plot.

Bad pattern:

- No hidden person.
- No array.
- No waking artifact.
- No trace of transmission.

Replacement:

Merge perception into a natural judgment or action result.

Example direction:

The character searches the relevant space and fails to find the source.

---

### 3.8 Customer-service rules or systems

Rules, systems, rankings, laws, notices, rituals, and task panels should not behave like helpful support agents unless that is the chapter's explicit premise.

Do not let a rule-carrier:

- Diagnose its own mismatch
- Explain its own error
- Offer compensation
- Negotiate difficulty
- Provide alternative completion routes
- Cooperate with dramatic intent

Default behavior:

- State condition
- State reward
- State limitation
- State failure feedback
- Repeat fixed rule

The mismatch should be exposed by the character's questions, tests, and failed actions.

---

### 3.9 Late resource is not broken resource

If a reward, inheritance, task, privilege, tool, or system arrives late, do not make it inherently low-quality just for comedy.

The stronger contrast is:

It would have been useful at the proper time or level, but it is mismatched now.

---

### 3.10 Joke cannot replace hook

A joke, quip, or absurd exchange cannot be the chapter's only ending force.

The ending must leave an action problem:

- What must the character do next?
- Why must it be done?
- What is blocked until it is done?

---

## 4. Sentence-Level Natural Density

### 4.1 Every sentence must deserve its place

A sentence must do at least one of the following:

- Add new information
- Change a character's judgment
- Push an action forward
- Create consequence
- Expose a relationship
- Produce misunderstanding
- Strengthen the hook

If a sentence only adds mood, transition, explanation, or emphasis, delete or merge it.

---

### 4.2 Concision is density, not shortness

Bad concision is a stack of thin short sentences.

Good concision compresses action, pressure, and judgment into a natural line.

Review question:

Is this sentence short because it is powerful, or short because it is a separated camera beat?

---

### 4.3 Do not write every logic step

Readers can infer.

Do not over-explain:

- Why observers are present
- Why a result matters
- Why a character is disappointed
- Why a rule is absurd
- Why an object is useless

Show the necessary fact and consequence; let the reader connect the obvious middle.

---

### 4.4 Avoid transition-as-sentence

Do not write a sentence whose only job is to move from one beat to the next.

Go directly into action, dialogue, or consequence.

---

## 5. Character Judgment and Desire

### 5.1 Capable characters must think like capable characters

Experienced, powerful, professional, or responsible characters should not react first as joke carriers.

Default chain:

- Notice abnormality
- Check source or risk
- Verify key information
- Test the rule
- Reject false assumptions
- Look for an exit or use
- Change plan

But the chain must be driven by desire, not by exposition needs.

---

### 5.2 Every question must have motive

Dialogue with a system, rule, witness, enemy, or superior must not exist only to explain setting.

Each question should serve a desire:

- Confirm danger
- Confirm usefulness
- Recover a lost chance
- Find a route forward
- Avoid a blocked condition
- Decide whether the abnormal thing is worth attention

If a question only reveals information to the reader, merge or cut it.

---

### 5.3 Repetition should change strategy

A rule-carrier may repeat fixed feedback. The character should not keep asking the same thing in new wording for too long.

After one or two failed attempts, the character should change strategy:

- Stop asking
- Test reality
- Use external resources
- Look for a workaround
- Change the action plan

---

## 6. Emotion Through State Change

### 6.1 Emotion is not an added sentence

Do not add emotion by labeling it or inserting a gesture.

Emotion should emerge from state change:

- Expected result fails to appear
- A late opportunity arrives after its proper time
- A useless thing turns out to have one possible value
- An old matter becomes newly relevant
- A ridiculous obstacle blocks a serious desire

---

### 6.2 Major outcomes need expectation before absence

Do not write only the result. Let the scene contain an expectation, then let it fail naturally.

Do not explain disappointment. Let waiting, stopping, resuming, or changing plan carry it.

---

### 6.3 Long history should appear in present behavior

Avoid summary shortcuts:

- This was not the first time.
- He had long been used to it.
- For many years he had...

Long history should appear through present habits:

- Knowing exactly when waiting is over
- Observers knowing when not to interrupt
- Familiarity with post-failure procedure
- Skilled restraint after repeated attempts

---

## 7. Triggered Scene Rules

### 7.1 Large-scene opening

Trigger:

- Trial, battle, calamity, public pressure, major failure, ritual, powerful entrance, or world-rule abnormality.

Rule:

Build pressure through the scene before landing the abnormal result, but do not turn the opening into short-sentence scaffolding.

Use natural prose that connects pressure, character, expectation, and result.

---

### 7.2 Late resource

Trigger:

- A resource, reward, inheritance, tool, status, task, or system arrives after the time when it would have been most useful.

Rule:

Show that it once had value. Then show why it is mismatched now.

Do not over-explain the contrast. Keep the sharpest comparison.

---

### 7.3 High-status character versus low-level rule

Trigger:

- A high-status or highly capable character meets a low-level, obsolete, rigid, or mismatched rule mechanism.

Rule:

The contrast should come from both sides behaving according to their own logic.

Do not reduce the character to a comedian. Do not make the rule mechanism too self-aware.

---

## 8. Generation Workflow

Before drafting, internally identify:

- Core pressure
- Core mismatch
- Character desire
- Rule or mechanism logic
- Required ending action problem
- Terms that are allowed by input
- Terms that must not be invented

After drafting, internally run four checks:

### 8.1 Red-line check

Remove or revise:

- Weak transitions
- Short-sentence scaffolding
- Emotion labels
- Human-flavor plugins
- Unsupported terms or metaphors
- Repeated facts
- Checklist judgment
- Customer-service rule behavior
- Broken-resource treatment
- Joke-only hooks

### 8.2 Sentence-density check

Ask for each sentence:

- Does deletion improve the paragraph?
- Is it only transition?
- Is it only explanation?
- Is it repeating a fact?
- Can it be merged?

### 8.3 Emotion-source check

Every emotion must arise from a state change, not from a label or decorative gesture.

### 8.4 Character-aliveness check

Ask:

- What does the character want here?
- What new fact changes the plan?
- Where does the character stop treating the abnormal thing as noise and start treating it as useful?
- What action problem remains at the end?

---

## 9. Output Requirements

Unless the user asks otherwise:

- Output prose only.
- Do not include analysis.
- Do not include self-review.
- Do not mention this Skill.
- Do not mention prompts, seeds, files, or workflow.
- Do not imitate a specific author.
- Do not quote or transform source text.

---

## 10. Skill Delta Governance

When improving this Skill from a case, follow this process:

- Identify the problem.
- Decide whether it violates an existing rule.
- Prefer strengthening or reweighting existing rules over adding new ones.
- If adding a rule, classify its priority layer.
- Remove all case-specific names, plot points, and source-text traces.
- Use only invented examples.
- Add a regression test if the issue is likely to recur.

Skill is public. Case notes are private. Delta is the abstract bridge from private case to public rule.
