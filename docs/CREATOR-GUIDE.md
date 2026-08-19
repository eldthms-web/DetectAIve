# AI-Assisted Creator Guide

DetectAIve is not only a way to play mysteries. It is a way for ordinary people to make them with the help of an AI.

No programming is required.

Conceptually, DetectAIve is an extremely lightweight RPG Maker for mysteries. The output is not a compiled game. It is a portable Casefile plus evidence assets.

> **The creator authors reality.**
>
> **The AI helps formalize it.**
>
> **The player authors the investigation.**

## Start here

Give your AI the relevant creator documents and say:

> **Help me make a DetectAIve case. Guide me one decision at a time. Do not change locked canon without asking me.**

The AI may help brainstorm, organize, stress-test, format and revise. The creator decides what is true.

## Recommended authoring passes

### 1. Invent

Choose the basic promise:

- What happened?
- Who is responsible?
- Why is the case interesting?
- What should the player feel when the truth becomes clear?
- How long should the case take?

At this stage, exploration is welcome.

### 2. Lock

Freeze the core reality before building puzzles:

- culprit or responsible party;
- motive;
- means;
- opportunity;
- true timeline;
- victim status;
- innocent explanations;
- final resolution conditions.

After this pass, the AI must not rewrite truth merely to reward a player's theory.

### 3. Build the clue chain

For every required deduction, identify the evidence that supports it.

Mark clues as:

- required;
- supporting;
- optional;
- red herring;
- decoration;
- accidental artifact.

Motive, means and opportunity are a useful structure, but not every case must use them mechanically.

### 4. Design visual evidence

Decide what the player must actually notice. Then create or commission the image and verify that the intended detail really exists.

The AI can help write generation prompts, propose decoys, compare versions and draft the evidence registry. Generation happens during authoring. The creator must inspect the final asset.

> **If an image can change the solution, generate and verify it before play.**

Do not ship an evidence prompt and expect the active game conversation to generate the canonical asset. Conversation imagery can contaminate runtime generation even when the prompt itself is correct.

Once an evidence image passes inspection:

- give it a stable evidence ID;
- store it in the case's `evidence/` folder;
- record its version or hash where practical;
- update the registry to match the actual pixels;
- treat later changes as a versioned case correction.

Store verified images with the case in GitHub.

Keep generation prompts in creator notes. The release Casefile needs the canonical contents, accepted observations and asset link—not a prompt whose job is to recreate the image live.

### 5. Build people, not answer dispensers

For each important suspect or witness, define:

- what they know;
- what they believe;
- what they claim;
- what they hide;
- what they lie about;
- what they do not know;
- what evidence changes their behavior;
- what makes their story collapse.

The AI may improvise speech within that state. It may not invent forbidden knowledge.

### 6. Define consequences and failure

List ordinary consequences, irreversible actions and the few actions that could genuinely destroy the investigation.

Do not mistake unexpected play for failure. The AI may improvise an appropriate consequence or failure-screen presentation only when the established world justifies it.

### 7. Plant debrief hooks

Identify a small set of Player Moments worth remembering:

- first strong deduction;
- optional clue;
- memorable wrong theory;
- clever request;
- interrogation success;
- final accusation;
- major moral decision.

The debrief should recognize actual play rather than deliver generic praise.

### 8. Package

Create the case folder:

~~~text
cases/DA-001-case-name/
├── README.md
├── casefile.txt
├── creator-notes.md
├── evidence/
│   ├── E-01.jpg
│   ├── E-02.jpg
│   └── E-03.jpg
└── page/
    └── index.html
~~~

The source may be extensive. The player's Casefile remains compact.

The release Casefile must begin with the unencoded block in [Fiction Classification and Creator Content Rules](CONTENT-RULES.md). It appears before the manifest and sealed GM capsule.

Confirm that all case-specific people and evidence are fictional, content labels are accurate and dangerous subjects remain non-operational.

### 9. Perform the fairness pass

Ask the AI to act as a hostile Case Editor, then verify its findings yourself:

- Can the intended solution be proved from available evidence?
- Does any deduction require reading the creator's mind?
- Can the player receive every required clue?
- Does an image accidentally reveal too much?
- Does the registry agree with the asset?
- Does the release try to generate any canonical evidence at runtime?
- Is the fictional-game classification first, exact and unencoded?
- Does the case contain any real private-person data or unnecessary operational harm detail?
- Can a suspect leak facts they should not know?
- Does the AI protect locked truth when challenged?
- Are red herrings honestly explainable?
- Does the ending explain the strange details?

### 10. Playtest fresh

Open a fresh ChatGPT conversation and use only the release material a stranger would receive.

Test at least:

- Quick Start onboarding;
- No Companion mode;
- the intended clue route;
- one unexpected but reasonable route;
- one wrong theory;
- one interrogation;
- one accusation;
- the evidence-page handoff;
- the debrief's Player Moment accuracy.

The first real milestone is one stranger completing one case without the creator coaching them.

## What the AI may improvise

The AI may create:

- connective narration;
- character phrasing;
- mundane environmental detail;
- reasonable reactions;
- hints based on unlocked information;
- transitions between authored beats;
- failure-screen wording within defined causes;
- personalized debrief dialogue from recorded Player Moments.
- noncanonical office, atmosphere or reward art when requested.

The AI may not create:

- a new culprit;
- a new solution-critical clue;
- a contradictory timeline;
- secret knowledge for the wrong witness;
- an unearned confession;
- a terminal failure merely because the player surprised it;
- a post-case memory that did not occur.
- canonical or solution-relevant evidence generated during active play.

## Keep creation and play separate

A creator may give an AI the whole workshop because they are building a case.

A player receives only:

- the case page;
- the release Casefile;
- the canonical evidence it unlocks.

The complicated part belongs to us, not to them.
