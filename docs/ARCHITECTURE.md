# DetectAIve Architecture

## North star

> **Make authorship powerful. Make play effortless.**

Internally, DetectAIve may become sophisticated. Publicly, a player should see a case card, perform one obvious copy action, answer at most one onboarding question and begin investigating.

Player-facing promise:

> **Paste a case. Solve it with your AI.**

Interaction promise:

> **Read the story. Study the evidence. Solve the case. Then talk about it.**

## Three layers

### 1. Front door

Reddit, the README and eventual catalog answer:

- What is DetectAIve?
- Do I want to play or create?
- Which case should I play?
- What do I select and copy?
- What content, difficulty and duration should I expect?

The player should encounter **PLAY A CASE**. The prospective creator should encounter **MAKE A CASE**.

### 2. Authoring system

The repository is the workshop and instruction manual. It contains:

- creator guidance;
- Casefile specification;
- runtime kernel source;
- templates;
- fairness and QA rules;
- visual-evidence design;
- Voice and debrief guidance;
- versioned case source;
- canonical evidence assets.

A creator may load these materials into an AI and ask it to help build a case. The creator does not need to program.

### 3. Player runtime

The release Casefile tells ChatGPT how to:

- onboard the player;
- protect hidden state;
- accept natural-language actions;
- reveal only unlocked evidence IDs;
- compare player observations against the evidence registry;
- improvise within CANON;
- conduct text interrogations;
- track Player Moments;
- resolve success or failure;
- offer an optional post-case debrief.

The player receives only the compact Casefile and case page, not the full authoring system.

## V0 media responsibilities

| Layer | Primary job in V0 |
|---|---|
| Text | The game, choices, investigation and interrogation |
| Read Aloud | Optional narration of text responses |
| Images | Pregenerated, creator-verified canonical evidence studied by the player |
| Live Voice | Primarily the optional earned post-case debrief |

Voice interrogation remains an experimental extension, not a launch dependency.

## One-minute launch path

~~~text
Reddit or shared link
  ↓
PLAY CASE
  ↓
COPY CASEFILE
  ↓
Paste into ChatGPT
  ↓
Read Aloud tip + one office choice
  ↓
Investigation begins
~~~

Do not front-load rules, creator information, Voice setup, GitHub vocabulary or Casefile mechanics.

## Canonical GitHub source

GitHub is the preferred home for case source and canonical evidence:

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

This keeps logic, images, versions and corrections together. A GitHub Pages page may expose the same assets through a clean player interface.

The player should not need to navigate the repository. They receive a direct **PLAY CASE** link.

## Evidence boundary

The Casefile contains the canonical evidence registry. The case page contains the human-viewable assets.

Normal loop:

1. ChatGPT unlocks an evidence ID.
2. The player opens the image separately.
3. The player studies it privately.
4. The player describes an observation or proposed action.
5. ChatGPT resolves it against the registry and current case state.

The AI does not need to visually ingest every image. Direct upload and AI image analysis are optional enhancements, not prerequisites.

## Canonical evidence generation boundary

> **If an image can change the solution, generate and verify it before play.**

The first alpha established that a correct evidence prompt inside the sealed GM capsule can still produce the wrong image at runtime. Recent office descriptions, character aesthetics and earlier generated art may contaminate the image-generation context.

Therefore V0 must not ask ChatGPT to generate canonical evidence during the active case.

- Canonical evidence is generated during authoring.
- The creator verifies the final pixels against the evidence registry.
- The verified asset is stored and versioned with the case.
- The runtime unlocks the existing asset by evidence ID.
- Generation prompts used to create it remain in creator source, not in the release capsule merely for runtime execution.

Runtime image generation may be used for:

- office portraits and splash art;
- atmospheric or transitional illustrations;
- post-case reward images;
- explicitly noncanonical visual jokes or souvenirs.

Every runtime-generated image defaults to **noncanonical cosmetic art**. It cannot add clues, change evidence meaning or unlock a deduction.

Any derived image needed for a puzzle—a crop, enhancement, reconstruction or comparison—must also be created and verified before publication. A runtime transformation may be offered for amusement or accessibility experimentation, but it cannot become the sole source of a solution-relevant fact.

## Source case versus release Casefile

The creator source may contain many documents, prompts, rejected concepts and high-resolution assets.

The release Casefile is the compact cartridge pasted into ChatGPT. It contains only the runtime instructions and one case's playable state.

Never require a player to paste the repository.

## Information boundaries

### CANON

Immutable facts:

- responsible parties;
- true timeline;
- motive, means and opportunity;
- victim status;
- evidence meaning;
- suspect knowledge;
- red-herring explanations;
- resolution and failure conditions.

### FLEX

Adaptable presentation:

- office cast;
- narration style;
- investigator dialogue;
- hint delivery;
- scene transitions;
- debrief tone;
- genre-compatible cosmetic framing.

The AI may improvise connective tissue, dialogue, reasonable reactions and unimportant environmental detail. It may not improvise new solution-critical facts or rewrite CANON around the player.

### CAPABILITIES

Office characters may have unusual abilities, equipment or knowledge.

A capability may change how a pre-authored clue is obtained, automate routine connective work or unlock a creator-approved alternate route. It may not invent evidence or bypass the entire clue chain unless the creator explicitly authored that possibility.

## Core state machine

~~~text
UNOPENED
  ↓
SETUP
  ↓
INVESTIGATING ↔ INTERROGATING
  ↓
ACCUSATION
  ↓
RESOLVED
  ↓
DEBRIEF
  ↓
FOLLOW-UP UNLOCKED (optional)

Any active investigative state may also transition to:

FAILED
  ↓
POSTMORTEM (only if requested)
~~~

FAILED is terminal for the active run. It does not automatically reveal the solution.

The state machine is backstage. The player should experience scenes, not status codes.

## Repository roles

- **README and Quickstart:** public player-facing front door.
- **Player Onboarding:** first-response runtime behavior.
- **Creator Guide:** AI-assisted authoring path.
- **docs:** clean accepted design.
- **templates:** repeatable creator materials.
- **cases:** versioned playable cases and evidence.
- **archive:** preserved prototypes.
- **DECISIONS:** accepted choices and rationale.
- **ROADMAP:** priority control.

Brainstorming is evaluated and integrated where it belongs rather than appended chronologically to the specification.
