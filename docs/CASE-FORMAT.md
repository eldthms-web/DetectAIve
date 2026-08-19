# Draft Casefile Format

**Status:** structural draft for playtesting. This is not yet a stable standard.

A Casefile is the portable cartridge a player pastes into ChatGPT. It is not the complete creator repository.

## Canonical case folder

GitHub is the preferred home for the editable case source and evidence assets:

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

The player-facing page may be published with GitHub Pages. The player should receive a direct link rather than instructions for navigating branches or folders.

## Manifest

Every published case begins with compact spoiler-free metadata.

~~~text
CASE ID: DA-001
TITLE: The Empty Platform
VERSION: 0.1
CREATOR: Name
STATUS: Playtest
FORMAT VERSION: DetectAIve 0.1
MODE: Locked Mystery
DIFFICULTY: Medium
ESTIMATED TIME: 8–12 minutes
EVIDENCE IMAGES: 3
CANONICAL EVIDENCE: Pregenerated and creator-verified
PLAYER INTERFACE: Text + optional Read Aloud
EVIDENCE DELIVERY: GitHub Pages
VOICE DEBRIEF: Available
VOICE INTERROGATION: None
OFFICE COMPATIBILITY: Universal
STRUCTURE: Standalone
CONTENT: No gore
CHATGPT TESTING: Untested
~~~

The case listing carries configuration so the runtime does not ask for it again.

## Required layers

### Runtime kernel

Compact instructions governing:

- the Read Aloud tip;
- one-question office setup;
- hidden information;
- natural-language play;
- state changes;
- evidence handling;
- allowed improvisation;
- resolution, failure and debrief behavior.

Every release Casefile carries the runtime behavior it needs. The player does not paste a separate engine manual.

### Sealed GM packet

Contains the immutable CANON:

- true explanation;
- responsible parties;
- victim status;
- timeline;
- motive;
- means;
- opportunity;
- suspect knowledge;
- genuine clues;
- red herrings;
- consequences;
- endings.

The first alpha successfully used a Base64-encoded GM capsule: ChatGPT decoded and understood the locked mystery. That validates the basic transport idea, but not yet cross-interface reliability or spoiler resistance. The exact stable representation remains subject to playtesting. Obfuscation is spoiler resistance, not security.

### Player-facing opening

Contains only information legitimately available before play:

- premise;
- office-compatible role;
- initial location;
- case-specific content warning;
- first unlocked evidence or lead.

### Evidence registry

Each evidence item should define:

~~~text
EVIDENCE ID:
TITLE:
SOURCE PATH:
PLAYER URL:
ASSET VERSION OR HASH:
UNLOCK CONDITION:
CANONICAL CONTENTS:
ACCEPTED OBSERVATIONS:
PERMITTED DEDUCTIONS:
MISLEADING APPEARANCES:
DERIVED ASSETS:
ACCESSIBILITY FALLBACK:
DIRECT AI ANALYSIS: Optional / Supported / Not tested
RUNTIME GENERATION: Prohibited for canonical evidence
VERIFICATION STATUS:
~~~

The canonical contents let ChatGPT judge the player's report without visually ingesting the image. The player studies the original asset on the case page.

If the player uploads the image, ChatGPT may discuss visible details, but image analysis must not overwrite the creator-verified registry or manufacture facts absent from CANON.

Canonical evidence must already exist before the player starts. A generation prompt used during authoring belongs in creator notes or source files. Do not put it in the release capsule for ChatGPT to execute during play.

Pregenerated, creator-verified zooms or reconstructions may clarify captured information. They may not invent new information. A runtime-generated derivative cannot be required for a deduction.

### Clue registry

Each clue has a function:

- **REQUIRED** — needed for the intended solution;
- **SUPPORTING** — strengthens a conclusion;
- **OPTIONAL** — rewards unusual attention;
- **RED HERRING** — misleading but honestly explainable;
- **DECORATION** — atmospheric and non-evidentiary;
- **ACCIDENTAL ARTIFACT** — a generation mistake explicitly declared noncanonical.

Each required deduction must be supported by evidence the player can actually receive.

### Suspect and witness packets

Important NPCs define:

- what they know;
- what they believe;
- what they claim;
- what they hide;
- what they lie about;
- what they genuinely do not know;
- evidence that changes their behavior;
- contradiction threshold;
- collapse condition;
- post-collapse truth or action.

Text interrogation is the V0 baseline. Voice performance is optional and may not change the underlying state.

### State transitions

The case identifies which discoveries or choices permit movement into interrogation, accusation, resolution, failure and optional follow-up states.

The runtime must not begin a debrief while the investigation remains unresolved.

### Player Moments

Track a very small dynamic set:

- `FIRST_USEFUL_OBSERVATION`;
- `OPTIONAL_CLUE_FOUND`;
- `MEMORABLE_WRONG_THEORY`;
- `CONTRADICTION_EXPOSED`;
- `DIFFICULT_DECISION`;
- `FINAL_ACCUSATION`;
- `MISSED_CLUE_WORTH_CALLBACK`.

These are debrief hooks, not persistent psychological profiling.

### Voice debrief card

When offered, the V0 Voice Card should specify:

- character;
- scene purpose;
- relevant Player Moments;
- opening intent;
- one question per turn;
- stopping point;
- allowed reactions after the player answers;
- closing line or condition.

Non-spoken control instructions remain separate from dialogue.

Voice interrogation cards use the same structure but are experimental in V0.

### Noncanonical image hooks

A case may optionally offer runtime-generated cosmetic art:

~~~text
IMAGE HOOK ID:
PURPOSE: Office / atmosphere / reward / souvenir
UNLOCK CONDITION:
PROMPT INPUTS:
CANONICALITY: Noncanonical
MUST NOT DEPICT OR ADD:
~~~

These hooks may use the office cast and Player Moments. They must not represent forensic evidence, introduce solution-relevant facts or retroactively alter the case registry.

### Failure packet

A case distinguishes:

- nonterminal consequences;
- terminal failure triggers;
- irreversible actions;
- ambiguous commitments requiring clarification;
- permitted failure-screen families;
- custom failure lines or epilogues;
- postmortem behavior.

The runtime may improvise presentation within these boundaries. It may not invent a terminal cause merely because a funny screen is available.

See [Failure and Caseline System](FAILURE-AND-CASELINE.md).

### Resolution and debrief

The case defines:

- sufficient evidence for a correct accusation;
- plausible incomplete outcomes;
- consequences of error;
- moral choice, if any;
- epilogue variations;
- debrief hooks;
- optional continuation unlock.

## Release rule

The creator source may be extensive. The release Casefile must be obvious, versioned and compact.

Do not place creator instructions, unused dialogue libraries, image-generation prompts or the full project specification inside the player's Casefile.
