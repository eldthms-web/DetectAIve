# Draft Casefile Format

**Status:** structural draft for playtesting. This is not yet a stable standard.

A Casefile is the portable package a player gives ChatGPT.

## Manifest

Every published case should begin with compact spoiler-free metadata.

~~~text
CASE ID: DA-001
TITLE: The Empty Platform
VERSION: 0.1
CREATOR: Name
STATUS: Playtest
FORMAT VERSION: DetectAIve 0.1
DIFFICULTY: Medium
ESTIMATED TIME: 8–12 minutes
EVIDENCE IMAGES: 3
VOICE: Optional interrogation
OFFICE COMPATIBILITY: Universal
STRUCTURE: Standalone
CONTENT: No gore
CHATGPT TESTING: Untested
~~~

Useful fields may later include genre, accessibility notes, content warnings, official/community status and sequel links.

## Required layers

### Runtime kernel

Compact instructions governing setup, hidden information, natural-language play, state changes, evidence handling and debrief behavior.

Every release Casefile must carry the runtime behavior it needs. The player should not paste a separate engine prompt.

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

The exact spoiler-resistant representation is unresolved and must be tested.

### Player-facing opening

Contains only information legitimately available before play:

- premise;
- office-compatible role;
- initial location;
- case-specific content warning;
- first unlocked evidence or lead.

### Evidence registry

Each evidence item should have:

- stable ID;
- file or asset reference;
- unlock condition;
- canonical contents;
- permitted deductions;
- misleading appearances;
- derived assets, if any;
- verification status.

Generated zooms or reconstructions may clarify captured information. They may not invent new information.

### Clue registry

Each clue has a function:

- **REQUIRED** — needed for the intended solution;
- **SUPPORTING** — strengthens a conclusion;
- **OPTIONAL** — rewards unusual attention;
- **RED HERRING** — misleading but honestly explainable;
- **DECORATION** — atmospheric and non-evidentiary;
- **ACCIDENTAL ARTIFACT** — a generation mistake that is explicitly noncanonical.

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

### State transitions

The case identifies which discoveries or choices permit movement into interrogation, accusation, resolution and optional follow-up states.

The runtime must not begin a debrief while the investigation remains unresolved.

### Player Moments

Track a very small dynamic set:

- FIRST_USEFUL_OBSERVATION;
- OPTIONAL_CLUE_FOUND;
- MEMORABLE_WRONG_THEORY;
- CONTRADICTION_EXPOSED;
- DIFFICULT_DECISION;
- MISSED_CLUE_WORTH_CALLBACK.

These are debrief hooks, not persistent psychological profiling.

### Voice Cards

Optional Voice Cards specify:

- character;
- scene purpose;
- known state;
- desired opening line or intent;
- one question per turn;
- stopping point;
- allowed reactions after the player answers;
- exit condition.

Control instructions must remain separate from spoken dialogue.

### Failure packet

A case should distinguish:

- nonterminal consequences;
- terminal failure triggers;
- irreversible actions;
- ambiguous commitments requiring clarification;
- permitted failure-screen families;
- custom failure lines or epilogues;
- postmortem behavior.

The runtime may improvise failure presentation within these boundaries. It may not invent a terminal cause merely because a funny screen is available.

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

## Authoring source

A creator may maintain a case as:

~~~text
cases/DA-001-case-name/
├── README.md
├── CASEFILE.md
├── CREATOR-NOTES.md
└── evidence/
~~~

The release package presented to the player must remain obvious and versioned.
