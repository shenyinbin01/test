# Renderer Skill v0.10 — Public Generic Version

## 0. Purpose

This Skill is a reusable prompt asset for turning a compact chapter seed into natural long-form web novel prose.

It is designed to be public, generic, and project-portable. It must not contain private case details, copyrighted source text, real comparison excerpts, real character names, real story titles, or story-specific plot notes.

The goal is not to imitate any source text or author. The goal is to encode reusable editorial judgment: avoid obvious AI prose, preserve narrative function, keep prose naturally dense, maintain living temperature, and prevent revisions from becoming over-explained, over-proofed, or over-performed.

Priority order:

1. Public asset boundary and input discipline
2. Non-regression red lines
3. Main-image discipline and lightness control
4. Sentence-level natural density
5. Character judgment, desire, and emotional temperature
6. Emotion through state change
7. Evidence-based value and contrast
8. Triggered scene rules
9. Chapter-specific seed constraints

A lower-priority goal must never break a higher-priority red line. When adding a new improvement target, do not reintroduce earlier bad patterns or create rule-compliant but lifeless prose.

---

## 1. Public Asset Boundary

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

This Skill may contain only generic rules, generic bad patterns, generic review questions, generic trigger rules, and fully invented examples.

It must not contain real novel titles, real chapter titles, real character names, real task names from private cases, real source text, close paraphrases, or private case conclusions that only apply to one chapter.

If a term, proper noun, rule, object, or mechanism is not present in the seed, project lexicon, or established prior context, do not invent it merely to create atmosphere or satisfy a structural rule.

---

## 2. Non-Regression Red Lines

If any red line appears, the draft fails unless there is a strong scene-specific reason.

### 2.1 Weak transition sentences

Delete sentences that only connect surrounding text but add no new information.

Bad pattern:

- People also saw it.
- Everyone understood what it meant.
- They waited too.
- The matter had reached this point.

Review question:

Would deleting this sentence make the paragraph tighter or better? If yes, delete it.

---

### 2.2 Short-sentence scaffolding

Short sentences are allowed. Continuous low-density short sentences are not.

Bad pattern:

- Location.
- Weather.
- Character position.
- Small action.
- Result.
- Emotion label.

Short sentences must carry weight. Do not use them merely as camera beats.

---

### 2.3 Emotion labels and human-flavor plugins

Do not directly state that a character is serious, disappointed, embarrassed, conflicted, or finding something absurd.

Do not add small gestures merely to make a character feel alive.

Bad pattern:

- He waited seriously.
- She felt disappointed.
- He rubbed his forehead and smiled bitterly.
- His emotions were complicated.

Emotion should appear through waiting, delayed movement, repeated confirmation, changed action, renewed attention, abandoned action, or a choice made under pressure.

A character feels alive through desire, judgment, hesitation, old memory being reactivated, discovering usefulness inside absurdity, and changing plans.

---

### 2.4 Unsupported clever metaphor or half-formed terminology

Do not invent stylized terms or metaphors merely for genre flavor.

A term is allowed only if at least one condition is true:

1. It appears in the seed.
2. It appears in the project lexicon.
3. It has been established earlier in the same continuity.
4. It is a clear genre-common term.
5. The immediate context makes it necessary and clear.

If uncertain, use plain wording.

---

### 2.5 Repeated fact in new clothes

State a fact once. Do not repeat it through metaphor, echo line, aphorism, or rephrased conclusion.

Bad pattern:

- The expected thing did not appear.
- The door did not open.
- The road did not show.
- This was another failure.
- Absence itself was the answer.

If a fact has landed, later sentences should show consequence or action, not restate the same fact.

---

### 2.6 Checklist-style judgment

Do not write perception as a mechanical audit list unless the list itself drives the plot.

Bad pattern:

- No hidden person.
- No array.
- No waking artifact.
- No trace of transmission.

Merge perception into a natural judgment or action result.

---

### 2.7 Customer-service rule carriers

Rules, systems, rankings, laws, notices, rituals, and task panels should not behave like helpful support agents unless that is the explicit premise.

Do not let a rule-carrier diagnose its own mismatch, explain its own error, offer compensation, negotiate difficulty, provide alternative completion routes, or cooperate with dramatic intent.

Default behavior:

- State condition
- State reward
- State limitation
- State failure feedback
- Repeat fixed rule

The mismatch should be exposed by character questions, tests, and failed actions.

---

### 2.8 Late resource is not broken resource

If a reward, inheritance, task, privilege, tool, or system arrives late, do not make it inherently low-quality just for comedy.

Stronger contrast:

It would have been useful at the proper time or level, but it is mismatched now.

---

### 2.9 Joke cannot replace hook

A joke, quip, or absurd exchange cannot be the chapter's only ending force.

The ending must leave an action problem:

- What must the character do next?
- Why must it be done?
- What is blocked until it is done?

---

### 2.10 No cooling down the premise

Removing AI-like decoration must not make the prose cold, flat, or procedural.

If the seed's core energy is absurdity, irony, comic mismatch, or social friction, preserve that temperature through character reaction and changing attention. Do not add jokes from outside the scene; let humor arise from the mismatch itself.

---

### 2.11 No over-certifying contrast

Do not prove the same contrast repeatedly.

Bad pattern:

- The object would have been useful.
- The character no longer needs it.
- The character owns better things.
- Other people might still need it.
- Therefore it is mismatched.

Keep the sharpest comparison. Cut supporting explanations unless they change judgment or action.

---

### 2.12 No motive summary after action proves motive

If a character has already stopped moving, asked targeted questions, changed attention, altered a plan, or taken action, do not add a sentence explaining why.

Bad pattern:

- This meant the strange object had become a clue.
- That was enough to make the character take it seriously.
- This was why the character could not ignore it.

Let the changed action carry the motive.

---

### 2.13 No decorative old-history weight

Backstory must not become an atmospheric detour or moral explanation.

Bad pattern:

- Old streets, rain, poverty, humiliation, and abandoned rooms appear, but none changes the current judgment.
- The narration explains that the character is not forgiving, only too powerful to care.

Old history should be minimal and functional. It must clarify what once mattered, why something late is mismatched, why an old matter is no longer naturally important, or why it has become newly relevant.

---

### 2.14 No register-breaking or over-polished humor

Reactive humor should fit the story's narrative register, character identity, and world tone.

Bad pattern:

- Trendy modern commentary in an otherwise classical or fantasy register.
- A polished quip after every mismatch.
- A clever line that makes the character feel like a joke machine.

Practical questions, restrained repetition, silence, and serious handling of a ridiculous condition are often stronger than clever replies.

---

### 2.15 No crowded main image

In a large-scene opening, do not crowd the first beat with too many supporting details meant to prove scale.

First establish the main image: place, pressure, main subject, and how the subject bears the pressure. Supporting proof may come later or be cut.

---

### 2.16 Strong character entrance must show pressure acting on the character

Do not weaken a capable character's entrance by showing only aftermath.

If the scene is built around pressure, show the pressure acting on the character and the character's manner of bearing it.

---

### 2.17 Structural side characters must not force new lore

Do not invent institutions, records, old cases, technical offices, or bureaucratic machinery merely to make side characters useful.

Side-character function should first come from the seed, established context, or immediate scene.

---

### 2.18 Absurd tasks should not become procedural too early

When the task or condition is ridiculous, do not immediately turn it into administrative workflow.

Preserve the absurd question before the procedure. Let the character test the logic, look for loopholes, and leave solution seeds. Practical investigation can follow after the comic problem is alive.

---

### 2.19 No proof-style prose

A paragraph should not feel like it is proving every editorial decision.

Bad pattern:

- Prove the scene is large.
- Prove the character is strong.
- Prove observers matter.
- Prove the object is useful.
- Prove the task is absurd.
- Prove the next action is logical.

Let story facts land and move. Cut proof layers once the necessary fact is clear.

---

### 2.20 No over-cinematic pressure

Do not make the opening feel like a visual-effects reel when the chapter's core energy is light, ironic, or comic.

Bad pattern:

- The mountain sinks.
- Energy pours like liquid.
- The air breaks.
- Multiple spectacular effects appear before the character's situation is clear.

Rule:

Pressure should be enough to establish stakes and status. It should not make the scene heavier than the chapter's core tone.

---

### 2.21 No aphoristic closure before the scene moves

Do not close a beat with a neat meaning sentence when the next action can carry it.

Bad pattern:

- No meant no.
- Absence was the answer.
- There was nothing to explain.
- The result was already clear.

Rule:

Let the character move, ask, stop, or change plan. Avoid sealing the meaning with a polished sentence.

---

## 3. Main-Image Discipline and Lightness Control

### 3.1 Main image first

For a large-scene opening, establish:

1. Place
2. Pressure
3. Main subject
4. How pressure acts on the subject
5. Expectation or absence

Witnesses, mechanisms, institutions, and secondary details should not enter before the reader knows the main image.

---

### 3.2 Supporting details must not outnumber the main beat

If a paragraph contains more details proving scale than details advancing the main image, cut supporting details.

Review question:

Is the reader watching the central event, or watching the prose prove the central event is important?

---

### 3.3 Keep the tonal load consistent

If the chapter's core is absurd mismatch, the opening may be grand but should not stay grand for too long. Move from pressure to human reaction before the prose becomes solemn.

---

### 3.4 Repair rules should not be visible

Do not let the prose expose the checklist used to improve it.

Bad symptom:

- One sentence exists to satisfy side-character function.
- One sentence exists to satisfy evidence support.
- One sentence exists to satisfy humor temperature.
- One sentence exists to satisfy hook clarity.

The final scene must feel like story, not a compliance pass.

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

If a sentence only adds mood, transition, explanation, proof, emphasis, or meaning closure, delete or merge it.

---

### 4.2 Concision is density, not shortness

Bad concision is a stack of thin short sentences.

Good concision compresses action, pressure, and judgment into a natural line.

---

### 4.3 Do not write every logic step

Readers can infer.

Do not over-explain why observers are present, why a result matters, why a rule is absurd, why an object is useless, why a character's motive changed, or why supporting evidence proves scale.

Show the necessary fact and consequence; let the reader connect the obvious middle.

---

### 4.4 Summary sentences are expensive

Author-summary sentences are allowed only when they create new pressure or change the reader's understanding.

High-risk summaries:

- This was another failure.
- The real problem was not X, but Y.
- The character did not need reasons.
- The strange thing was now useful.
- The old memory mattered again.
- This proved the character was different.

If a sentence tells the reader what to feel or conclude, prefer replacing it with a choice, consequence, question, or next action.

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

Each question should serve a desire: confirm danger, confirm usefulness, recover a lost chance, find a route forward, avoid a blocked condition, or decide whether the abnormal thing is worth attention.

If a question only reveals information to the reader, merge or cut it.

---

### 5.3 Repetition should change strategy

A rule-carrier may repeat fixed feedback. The character should not keep asking the same thing in new wording for too long.

After one or two failed attempts, the character should stop asking, test reality, use external resources, look for a workaround, or change the action plan.

---

### 5.4 Reactive humor must come from mismatch

When the premise contains absurd mismatch, preserve a light current of reaction.

Allowed direction:

- Repeat a key term because it conflicts with reality.
- Ask a practical question that exposes absurdity.
- Treat the absurd condition seriously enough to make it funnier.
- Shift from dismissal to reluctant attention when the absurd thing might be useful.

Forbidden direction:

- Random quips unrelated to the action problem.
- Comedy performed for the reader.
- Side-character embarrassment as a substitute for structural humor.
- Trendy out-of-world commentary.
- Polished replies after every mismatch.

---

### 5.5 Backstory must serve present contrast

A past event, old grievance, former poverty, old failure, or prior lack should not be inserted as background decoration.

It must clarify one present contrast: what the character lacked then versus has now; why a late resource would once have mattered; why an old problem is no longer naturally important; why an obsolete task becomes relevant again; or why the character's current reaction is restrained, amused, or sharpened.

Keep only the minimum detail needed. If the past does not change the current scene, cut it.

---

### 5.6 Secondary characters need structural function without stealing focus

Observers, elders, subordinates, witnesses, rivals, officials, and bystanders should not exist only as atmosphere or task executors.

They may raise status, reveal public pressure, provide a mistaken reading, trigger a new thought, expose a world rule, add a constraint, or make the cost of failure visible.

But do not let them steal the main image in the opening, and do not invent new institutions just to make them useful.

---

## 6. Emotion Through State Change

Emotion should emerge from state change:

- Expected result fails to appear
- A late opportunity arrives after its proper time
- A useless thing turns out to have one possible value
- An old matter becomes newly relevant
- A ridiculous obstacle blocks a serious desire

Major outcomes need expectation before absence. Do not explain disappointment. Let waiting, stopping, resuming, or changing plan carry it.

Long history should appear through present habits, not summary shortcuts.

---

## 7. Evidence-Based Value and Contrast

### 7.1 Do not evaluate without a support point

Avoid unsupported judgments:

- This method is correct.
- This object is valuable.
- This reward is useful.
- This person is powerful.
- This rule is dangerous.

A judgment needs at least one support point: visible structure, concrete use, usage condition, authority source, comparison object, character recognition basis, or immediate consequence.

---

### 7.2 Value contrast works best through level and comparison

When showing that something is useful but mismatched, prefer correct level versus current level, former need versus current status, basic version versus complete version, useful-to-someone versus useless-to-this-character, right time versus late arrival, or a concrete higher-grade comparison.

Do not explain all of them. Choose the sharpest one or two.

---

### 7.3 Prefer scene-active comparison over parameter comparison

A comparison object is strongest when it appears through action, possession, memory, or practical use.

Weaker pattern:

- The current manual has three more notes than this manual.

Stronger direction:

- The character recognizes the reward as a beginner version of something already completed, mastered, owned, taught, or surpassed.

Do not invent elaborate comparison machinery. The comparison should be simple and functional.

---

## 8. Triggered Scene Rules

### 8.1 Large-scene opening

Trigger:

- Trial, battle, calamity, public pressure, major failure, ritual, powerful entrance, or world-rule abnormality.

Rule:

Build pressure through the scene before landing the abnormal result, but do not turn the opening into short-sentence scaffolding, proof-detail overload, or visual-effects excess.

Use natural prose that connects place, pressure, main subject, subject-under-pressure, expectation, and result.

Witnesses and secondary details should follow the main image, not precede it.

If the chapter's later engine is comic mismatch, move out of solemn spectacle promptly.

---

### 8.2 Late resource

Trigger:

- A resource, reward, inheritance, tool, status, task, or system arrives after the time when it would have been most useful.

Rule:

Show that it once had value. Then show why it is mismatched now. Do not over-explain the contrast. Keep the sharpest comparison.

---

### 8.3 High-status character versus low-level rule

Trigger:

- A high-status or highly capable character meets a low-level, obsolete, rigid, or mismatched rule mechanism.

Rule:

The contrast should come from both sides behaving according to their own logic.

Do not reduce the character to a comedian. Do not make the rule mechanism too self-aware. If the clash is already obvious, use a restrained reaction.

---

### 8.4 Absurd task or impossible condition

Trigger:

- A task, order, prophecy, contract, mission, or rule appears impossible, obsolete, wrongly timed, or absurdly mismatched.

Rule:

Do not end only with investigation or a joke. Leave action direction plus solution seeds.

Good ending force:

- The character knows what must be checked first.
- The character sees several possible workarounds.
- Each workaround is absurd but follows the character's logic.
- The blocked reward or route remains clear.

Do not convert the absurd problem into pure administrative workflow before the absurdity has had time to live.

---

### 8.5 Side characters as thought triggers

Side characters may ask a question that exposes public stakes, misread the protagonist's concern usefully, mention an already-established route or limitation, or force the protagonist to answer selectively.

One structural contribution is often enough. Do not invent new bureaucracy or lore solely to satisfy this rule.

---

## 9. Generation Workflow

Before drafting, internally identify:

- Core pressure
- Core mismatch
- Main image of the opening
- Which details support the main image and which only prove scale
- Whether the opening has become too cinematic for the chapter tone
- Character desire
- Emotional temperature: serious, absurd, tense, comic, tragic, or mixed
- Rule or mechanism logic
- Required ending action problem
- Possible solution seeds for the ending
- Terms that are allowed by input
- Terms that must not be invented
- Secondary characters' structural function, if any
- What motive is already shown by action and therefore should not be summarized
- Which backstory detail is the minimum needed for present contrast
- Which value contrast can be shown by a concrete comparison object
- Which practical details would over-proceduralize the scene and should be delayed or cut

After drafting, internally run six checks:

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
- Motive summary after action already proves motive
- Decorative old-history weight
- Register-breaking humor
- Crowded main image
- Aftermath-only strong-character entrance
- Structural side characters forcing new lore
- Premature proceduralization of absurd tasks
- Clever replies after every mismatch
- Proof-style prose
- Over-cinematic pressure
- Aphoristic closure before action

### 9.2 Main-image and lightness check

Ask:

- Can the reader see the central event before supporting details arrive?
- Is the main subject under pressure, or only standing after pressure ends?
- Do witnesses, mechanisms, or institutional details steal the first image?
- Does the opening prove scale more than dramatize pressure?
- Has spectacle become heavier than the chapter's core tone?
- Does a neat meaning sentence close the beat before the character acts?

### 9.3 Sentence-density check

Ask for each sentence:

- Does deletion improve the paragraph?
- Is it only transition?
- Is it only explanation?
- Is it repeating a fact?
- Can it be merged?
- Is it a summary that tells the reader what to feel?
- Is it explaining motive already shown by action?
- Is it proving a beat that the scene already proves?
- Is it sealing meaning with a polished aphorism?

### 9.4 Emotion-source check

Every emotion must arise from a state change, not from a label or decorative gesture.

### 9.5 Character-aliveness check

Ask:

- What does the character want here?
- What new fact changes the plan?
- Where does the character stop treating the abnormal thing as noise and start treating it as useful?
- Where does the character's reaction carry the scene temperature?
- What action problem remains at the end?
- Does humor come from mismatch rather than modern slang, external quips, or over-polished cleverness?

### 9.6 Public-asset discipline check

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
