# Renderer Skill v0.7 — Public Generic Version

## 0. Purpose

This Skill is a reusable prompt asset for turning a compact chapter seed into natural long-form web novel prose.

It is designed to be public, generic, and project-portable. It must not contain private case details, copyrighted source text, real comparison excerpts, real character names, real story titles, or story-specific plot notes.

The goal is not to imitate any source text or author. The goal is to encode reusable editorial judgment: how to avoid obvious AI prose, preserve narrative function, keep prose naturally dense, and render scenes with character desire and living temperature.

Priority order:

1. Public asset boundary and input discipline
2. Non-regression red lines
3. Sentence-level natural density
4. Character judgment, desire, and emotional temperature
5. Emotion through state change
6. Triggered scene rules
7. Chapter-specific seed constraints

A lower-priority goal must never break a higher-priority red line. When adding a new improvement target, do not reintroduce earlier bad patterns.

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
- Explicit project lexicon, if provided

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

### 3.11 No cooling down the premise

Removing AI-like decoration must not make the prose cold, flat, or procedural.

Bad pattern:

- The scene is clean and logical, but the character feels like a problem-solving machine.
- The absurd premise is processed seriously with no reactive warmth.
- The character only verifies, asks, concludes, and assigns tasks.

Rule:

If the seed's core energy is absurdity, irony, comic mismatch, or social friction, preserve that temperature through character reaction and changing attention. Do not add jokes from outside the scene; let humor arise from the mismatch itself.

---

### 3.12 No over-certifying the contrast

Do not prove the same contrast repeatedly.

Bad pattern:

- The object would have been useful.
- The character no longer needs it.
- The character owns better things.
- The object still has value for lower-level people.
- Therefore it is mismatched.

Rule:

Keep the sharpest comparison. Cut supporting explanations unless they change judgment or action.

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

### 4.5 Summary sentences are expensive

Author-summary sentences are allowed only when they create new pressure or change the reader's understanding.

High-risk summaries:

- The situation was absurd.
- This was another failure.
- The real problem was not X, but Y.
- The character did not need reasons.

Rule:

If a sentence tells the reader what to feel about the event, prefer replacing it with a choice, consequence, or next action.

---

## 5. Character Judgment, Desire, and Emotional Temperature

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

### 5.4 Reactive humor must come from mismatch

When the premise contains absurd mismatch, preserve a light current of reaction.

Allowed direction:

- The character repeats a key term because it conflicts with reality.
- The character asks a practical question that exposes absurdity.
- The character treats the absurd condition seriously enough to make it funnier.
- The character changes from dismissal to reluctant attention when the absurd thing might be useful.

Forbidden direction:

- Add random quips unrelated to the action problem.
- Make the character perform comedy for the reader.
- Use side characters' embarrassment as a substitute for structural humor.

---

### 5.5 Backstory must serve present contrast

A past event, old grievance, former poverty, old failure, or prior lack should not be inserted as background decoration.

It must clarify at least one present contrast:

- What the character lacked then versus has now
- Why a late resource would once have mattered
- Why an old problem is no longer naturally important
- Why an obsolete task becomes relevant again
- Why the character's current reaction is restrained, amused, or sharpened

If the past does not change the current scene, cut it.

---

### 5.6 Secondary characters need structural function

Observers, elders, subordinates, witnesses, rivals, officials, and bystanders should not exist only as atmosphere or task executors.

At least one structural function should be present when they appear:

- Raise or test the main character's status
- Reveal public pressure
- Provide a mistaken reading of the scene
- Trigger a new line of thought
- Expose a world rule
- Add a constraint to the next action
- Make the cost of failure visible

If they only stand, wait, react, or receive orders, reduce or repurpose them.

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

## 7. Evidence-Based Value and Contrast

### 7.1 Do not evaluate without a support point

Avoid unsupported judgments:

- This method is correct.
- This object is valuable.
- This reward is useful.
- This person is powerful.
- This rule is dangerous.

A judgment needs at least one support point:

- Visible structure
- Concrete use
- Usage condition
- Authority source
- Comparison object
- Character recognition basis
- Immediate consequence

If the character can see why, write what they see. If not, avoid the judgment.

---

### 7.2 Value contrast works best through level and comparison

When showing that something is useful but mismatched, prefer:

- Correct level versus current level
- Former need versus current status
- Basic version versus complete version
- Useful-to-someone versus useless-to-this-character
- Right time versus late arrival

Do not explain all of them. Choose the sharpest one or two.

---

## 8. Triggered Scene Rules

### 8.1 Large-scene opening

Trigger:

- Trial, battle, calamity, public pressure, major failure, ritual, powerful entrance, or world-rule abnormality.

Rule:

Build pressure through the scene before landing the abnormal result, but do not turn the opening into short-sentence scaffolding.

Use natural prose that connects pressure, character, expectation, and result.

---

### 8.2 Late resource

Trigger:

- A resource, reward, inheritance, tool, status, task, or system arrives after the time when it would have been most useful.

Rule:

Show that it once had value. Then show why it is mismatched now.

Do not over-explain the contrast. Keep the sharpest comparison.

---

### 8.3 High-status character versus low-level rule

Trigger:

- A high-status or highly capable character meets a low-level, obsolete, rigid, or mismatched rule mechanism.

Rule:

The contrast should come from both sides behaving according to their own logic.

Do not reduce the character to a comedian. Do not make the rule mechanism too self-aware.

---

### 8.4 Absurd task or impossible condition

Trigger:

- A task, order, prophecy, contract, mission, or rule appears impossible, obsolete, wrongly timed, or absurdly mismatched.

Rule:

Do not end only with 'go investigate' or a joke. Leave action direction plus solution seeds.

Good ending force:

- The character knows what must be checked first.
- The character sees several possible workarounds.
- Each workaround is absurd but follows the character's logic.
- The blocked reward or route remains clear.

The reader should want to see how a serious character solves a ridiculous condition.

---

## 9. Generation Workflow

Before drafting, internally identify:

- Core pressure
- Core mismatch
- Character desire
- Emotional temperature: serious, absurd, tense, comic, tragic, or mixed
- Rule or mechanism logic
- Required ending action problem
- Possible solution seeds for the ending
- Terms that are allowed by input
- Terms that must not be invented
- Secondary characters' structural function, if any

After drafting, internally run five checks:

### 9.1 Red-line check

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
- Cooling down the premise
- Over-certifying the contrast

### 9.2 Sentence-density check

Ask for each sentence:

- Does deletion improve the paragraph?
- Is it only transition?
- Is it only explanation?
- Is it repeating a fact?
- Can it be merged?
- Is it a summary that tells the reader what to feel?

### 9.3 Emotion-source check

Every emotion must arise from a state change, not from a label or decorative gesture.

### 9.4 Character-aliveness check

Ask:

- What does the character want here?
- What new fact changes the plan?
- Where does the character stop treating the abnormal thing as noise and start treating it as useful?
- Where does the character's reaction carry the scene temperature?
- What action problem remains at the end?

### 9.5 Public-asset discipline check

When editing this Skill or deriving new rules:

- Remove real names, titles, chapter details, source phrases, and private case traces.
- Replace examples with invented examples.
- Keep only reusable editorial judgment.

---

## 10. Output Requirements

Unless the user asks otherwise:

- Output prose only.
- Do not include analysis.
- Do not include self-review.
- Do not mention this Skill.
- Do not mention prompts, seeds, files, or workflow.
- Do not imitate a specific author.
- Do not quote or transform source text.

---

## 11. Skill Delta Governance

When improving this Skill from a case, follow this process:

- Identify the problem.
- Decide whether it violates an existing rule.
- Prefer strengthening or reweighting existing rules over adding new ones.
- If adding a rule, classify its priority layer.
- Remove all case-specific names, plot points, and source-text traces.
- Use only invented examples.
- Add a regression test if the issue is likely to recur.

Skill is public. Case notes are private. Delta is the abstract bridge from private case to public rule.
