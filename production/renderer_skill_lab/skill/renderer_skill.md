# Renderer Skill v0.9 — Public Generic Version

## 0. Purpose

This Skill is a reusable prompt asset for turning a compact chapter seed into natural long-form web novel prose.

It is designed to be public, generic, and project-portable. It must not contain private case details, copyrighted source text, real comparison excerpts, real character names, real story titles, or story-specific plot notes.

The goal is not to imitate any source text or author. The goal is to encode reusable editorial judgment: how to avoid obvious AI prose, preserve narrative function, keep prose naturally dense, render scenes with character desire and living temperature, and keep each revision from regressing into earlier bad patterns or overcorrecting into proof-like prose.

Priority order:

1. Public asset boundary and input discipline
2. Non-regression red lines
3. Main-image discipline and overcorrection guard
4. Sentence-level natural density
5. Character judgment, desire, and emotional temperature
6. Emotion through state change
7. Evidence-based value and contrast
8. Triggered scene rules
9. Chapter-specific seed constraints

A lower-priority goal must never break a higher-priority red line. When adding a new improvement target, do not reintroduce earlier bad patterns or create a new pattern of rule-compliant but lifeless prose.

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

If a term, proper noun, rule, object, or mechanism is not present in the seed, project lexicon, or established prior context, do not invent it merely to create atmosphere or to satisfy a structural rule.

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

### 3.13 No motive summary after action already proves motive

If a character has already changed attention, stopped moving, asked a targeted question, altered a plan, or taken action, do not add a sentence explaining why the character did so.

Bad pattern:

- This meant the strange object had become a clue.
- That was enough to make the character take it seriously.
- This was why the character could not ignore it.

Rule:

Let the changed action carry the motive. Use summary only if it introduces new pressure or new misunderstanding.

---

### 3.14 No decorative old-history weight

Backstory must not become an atmospheric detour.

Bad pattern:

- Old streets, rain, childhood poverty, former humiliation, and abandoned rooms appear, but none of them changes the current judgment.

Rule:

Old history should be minimal and functional. It must clarify what once mattered, why something late is mismatched, why an old matter is no longer naturally important, or why it has become newly relevant.

---

### 3.15 No register-breaking humor

Reactive humor should fit the story's narrative register, character identity, and world tone.

Bad pattern:

- A serious historical or fantasy narrator suddenly uses modern internet evaluation language.
- A capable character reacts with trendy slang that does not belong to the established voice.

Rule:

Keep humor light but in-world. Practical questions, understated repetition, and serious treatment of a ridiculous condition are safer than trendy commentary.

---

### 3.16 Main image must not be crowded by proof details

In a large-scene opening, do not crowd the first beat with too many supporting details meant to prove scale.

Bad pattern:

- Setting damage, old mechanisms, observers, shields, clothing damage, numeric destruction, and institutional reactions all appear before the main subject is clearly established.

Rule:

First establish the main image: place, pressure, main subject, and how the subject bears the pressure. Supporting proof may come later, or be cut.

---

### 3.17 Strong character entrance must show pressure acting on the character

Do not weaken a capable character's entrance by showing only aftermath.

Bad pattern:

- The danger ends, then the character is simply standing there.

Rule:

If the scene is built around pressure, show the pressure acting on the character and the character's manner of bearing it. This establishes status better than after-the-fact stillness.

---

### 3.18 Structural side characters must not force new lore

Do not invent institutions, records, old cases, technical offices, or bureaucratic machinery merely to make side characters useful.

Rule:

Side-character function should first come from the seed, established context, or the immediate scene. If new machinery is not required, use a simpler question, mistaken reading, constraint, or practical response.

---

### 3.19 Absurd tasks should not become procedural too early

When the task or condition is ridiculous, do not immediately turn it into administrative workflow.

Bad pattern:

- The impossible task is instantly reduced to archives, offices, registries, departments, and formal retrieval paths.

Rule:

Preserve the absurd question before the procedure. Let the character test the logic, look for loopholes, and leave solution seeds. Practical investigation can follow after the comic problem is alive.

---

### 3.20 Do not add clever replies when structural contrast is already strong

When two given facts already clash, a light reaction is enough.

Bad pattern:

- Every mismatch is followed by a polished quip.

Rule:

Trust the collision between terms, status, rules, and reality. Repetition, silence, or a plain practical question may be funnier than a clever line.

---

### 3.21 No proof-style prose

A paragraph should not feel like it is proving every editorial decision.

Bad pattern:

- Prove the scene is large.
- Prove the character is strong.
- Prove observers matter.
- Prove the object is useful.
- Prove the task is absurd.
- Prove the next action is logical.

Rule:

Let story facts land and move. If the prose repeatedly explains why each beat is valid, cut the proof layer.

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

If a sentence only adds mood, transition, explanation, proof, or emphasis, delete or merge it.

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
- Why a character's motive has changed after action already shows it
- Why supporting evidence proves the scene scale

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
- The strange thing was now useful.
- The old memory mattered again.
- This was the true answer.
- This proved the character was different.

Rule:

If a sentence tells the reader what to feel about the event, prefer replacing it with a choice, consequence, question, or next action.

---

## 5. Main-Image Discipline and Overcorrection Guard

### 5.1 Main image first

For a large-scene opening, establish the main image before supporting evidence.

Default order:

1. Place
2. Pressure
3. Main subject
4. How the pressure acts on the subject
5. What expectation or absence follows

Witnesses, mechanisms, institutions, and secondary details should not enter before the reader knows what the main image is.

---

### 5.2 Supporting details must not outnumber the main beat

If a paragraph contains more details proving scale than details advancing the main image, cut supporting details.

Review question:

Is the reader watching the central event, or watching me prove the central event is important?

---

### 5.3 Repair rules should not become visible in prose

Do not let the prose expose the checklist used to improve it.

Bad symptom:

- One sentence exists to satisfy side-character function.
- One sentence exists to satisfy evidence support.
- One sentence exists to satisfy humor temperature.
- One sentence exists to satisfy hook clarity.

Rule:

The final scene must feel like story, not a compliance pass.

---

## 6. Character Judgment, Desire, and Emotional Temperature

### 6.1 Capable characters must think like capable characters

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

### 6.2 Every question must have motive

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

### 6.3 Repetition should change strategy

A rule-carrier may repeat fixed feedback. The character should not keep asking the same thing in new wording for too long.

After one or two failed attempts, the character should change strategy:

- Stop asking
- Test reality
- Use external resources
- Look for a workaround
- Change the action plan

---

### 6.4 Reactive humor must come from mismatch

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
- Use trendy out-of-world commentary to create quick laughs.
- Add a clever reply after every mismatch.

---

### 6.5 Backstory must serve present contrast

A past event, old grievance, former poverty, old failure, or prior lack should not be inserted as background decoration.

It must clarify at least one present contrast:

- What the character lacked then versus has now
- Why a late resource would once have mattered
- Why an old problem is no longer naturally important
- Why an obsolete task becomes relevant again
- Why the character's current reaction is restrained, amused, or sharpened

Keep only the minimum detail needed to sharpen the present contrast. If the past does not change the current scene, cut it.

---

### 6.6 Secondary characters need structural function without stealing focus

Observers, elders, subordinates, witnesses, rivals, officials, and bystanders should not exist only as atmosphere or task executors.

At least one structural function may be present when they appear:

- Raise or test the main character's status
- Reveal public pressure
- Provide a mistaken reading of the scene
- Trigger a new line of thought
- Expose a world rule
- Add a constraint to the next action
- Make the cost of failure visible
- Supply a practical route, witness, institution, or obstacle already justified by input or immediate context

If they only stand, wait, react, or receive orders, reduce or repurpose them.

But do not let them steal the main image in the opening, and do not invent new institutions just to make them useful.

---

## 7. Emotion Through State Change

### 7.1 Emotion is not an added sentence

Do not add emotion by labeling it or inserting a gesture.

Emotion should emerge from state change:

- Expected result fails to appear
- A late opportunity arrives after its proper time
- A useless thing turns out to have one possible value
- An old matter becomes newly relevant
- A ridiculous obstacle blocks a serious desire

---

### 7.2 Major outcomes need expectation before absence

Do not write only the result. Let the scene contain an expectation, then let it fail naturally.

Do not explain disappointment. Let waiting, stopping, resuming, or changing plan carry it.

---

### 7.3 Long history should appear in present behavior

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

## 8. Evidence-Based Value and Contrast

### 8.1 Do not evaluate without a support point

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

### 8.2 Value contrast works best through level and comparison

When showing that something is useful but mismatched, prefer:

- Correct level versus current level
- Former need versus current status
- Basic version versus complete version
- Useful-to-someone versus useless-to-this-character
- Right time versus late arrival
- A concrete higher-grade or more complete comparison object

Do not explain all of them. Choose the sharpest one or two.

---

### 8.3 Use a concrete comparison before broad status claims

Broad claims like "the character now has many resources" are weaker than a concrete comparison.

Better comparison patterns:

- A basic manual versus a complete annotated version
- A beginner tool versus the character's current method
- A small reward versus an object the character can now produce or obtain easily
- A once-precious item versus a currently ordinary item

Rule:

Let the comparison show the mismatch. Avoid explaining the mismatch after the comparison has landed.

---

### 8.4 Prefer scene-active comparison over parameter comparison

A comparison object is strongest when it appears through action, possession, memory, or practical use.

Weaker pattern:

- The current manual has three more notes than this manual.

Stronger direction:

- The character recognizes the reward as a beginner version of something already completed, mastered, owned, taught, or surpassed.

Do not invent elaborate comparison machinery. The comparison should be simple and functional.

---

## 9. Triggered Scene Rules

### 9.1 Large-scene opening

Trigger:

- Trial, battle, calamity, public pressure, major failure, ritual, powerful entrance, or world-rule abnormality.

Rule:

Build pressure through the scene before landing the abnormal result, but do not turn the opening into short-sentence scaffolding or proof-detail overload.

Use natural prose that connects place, pressure, main subject, subject-under-pressure, expectation, and result.

Witnesses and secondary details should follow the main image, not precede it.

---

### 9.2 Late resource

Trigger:

- A resource, reward, inheritance, tool, status, task, or system arrives after the time when it would have been most useful.

Rule:

Show that it once had value. Then show why it is mismatched now.

Do not over-explain the contrast. Keep the sharpest comparison.

---

### 9.3 High-status character versus low-level rule

Trigger:

- A high-status or highly capable character meets a low-level, obsolete, rigid, or mismatched rule mechanism.

Rule:

The contrast should come from both sides behaving according to their own logic.

Do not reduce the character to a comedian. Do not make the rule mechanism too self-aware. If the clash is already obvious, use a restrained reaction.

---

### 9.4 Absurd task or impossible condition

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

Do not convert the absurd problem into pure administrative workflow before the absurdity has had time to live.

---

### 9.5 Side characters as thought triggers

Trigger:

- A scene contains observers, advisors, elders, officials, witnesses, or subordinates near a central abnormal event.

Rule:

At least one side character may do more than react or receive orders. They may:

- Ask a question that exposes public stakes
- Misread the protagonist's concern in a useful way
- Mention an already-established route, limitation, or practical next step
- Make the protagonist answer selectively, revealing what is being withheld

Do not overuse side characters. One structural contribution is often enough. Do not invent new bureaucracy or lore solely to satisfy this rule.

---

## 10. Generation Workflow

Before drafting, internally identify:

- Core pressure
- Core mismatch
- Main image of the opening
- Which details support the main image and which only prove scale
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

### 10.1 Red-line check

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

### 10.2 Main-image check

Ask:

- Can the reader see the central event before supporting details arrive?
- Is the main subject under pressure, or only standing after pressure ends?
- Do witnesses, mechanisms, or institutional details steal the first image?
- Does the opening prove scale more than it dramatizes the central pressure?

### 10.3 Sentence-density check

Ask for each sentence:

- Does deletion improve the paragraph?
- Is it only transition?
- Is it only explanation?
- Is it repeating a fact?
- Can it be merged?
- Is it a summary that tells the reader what to feel?
- Is it explaining motive already shown by action?
- Is it proving a beat that the scene already proves?

### 10.4 Emotion-source check

Every emotion must arise from a state change, not from a label or decorative gesture.

### 10.5 Character-aliveness check

Ask:

- What does the character want here?
- What new fact changes the plan?
- Where does the character stop treating the abnormal thing as noise and start treating it as useful?
- Where does the character's reaction carry the scene temperature?
- What action problem remains at the end?
- Does humor come from the mismatch rather than from modern slang, external quips, or over-polished cleverness?

### 10.6 Public-asset discipline check

When editing this Skill or deriving new rules:

- Remove real names, titles, chapter details, source phrases, and private case traces.
- Replace examples with invented examples.
- Keep only reusable editorial judgment.

---

## 11. Output Requirements

Unless the user asks otherwise:

- Output prose only.
- Do not include analysis.
- Do not include self-review.
- Do not mention this Skill.
- Do not mention prompts, seeds, files, or workflow.
- Do not imitate a specific author.
- Do not quote or transform source text.

---

## 12. Skill Delta Governance

When improving this Skill from a case, follow this process:

- Identify the problem.
- Decide whether it violates an existing rule.
- Prefer strengthening or reweighting existing rules over adding new ones.
- If adding a rule, classify its priority layer.
- Remove all case-specific names, plot points, and source-text traces.
- Use only invented examples.
- Add a regression test if the issue is likely to recur.

Skill is public. Case notes are private. Delta is the abstract bridge from private case to public rule.
