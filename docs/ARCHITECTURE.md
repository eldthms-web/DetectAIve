# DetectAIve Architecture

## North star

> **Complex backstage. Simple front door.**

A player should see a case card, perform one obvious copy action, answer at most one onboarding question and begin investigating.

## Three layers

### 1. Front door

The subreddit, README and eventual catalog answer:

- What is DetectAIve?
- Which case should I play?
- What do I copy?
- What content and difficulty should I expect?
- Where do I discuss the result?

### 2. Case format

The creator's source contains:

- manifest and version;
- canonical truth;
- timeline;
- evidence assets;
- clue functions;
- suspects;
- interrogation packets;
- state transitions;
- endings;
- debrief hooks;
- optional Voice Cards.

### 3. ChatGPT runtime

The runtime tells ChatGPT how to:

- onboard the player;
- protect hidden state;
- reveal only unlocked evidence;
- accept natural-language actions;
- distinguish routine actions from decisions;
- conduct interrogations;
- track Player Moments;
- resolve the case;
- run an optional debrief.

## Source case versus release Casefile

Creators may work across several files and images.

Players should receive one clearly identified release package.

The release Casefile must be self-contained enough to run in a fresh ChatGPT conversation. It may refer to bundled evidence assets, but it must not require the player to read the creator specification or assemble runtime rules manually.

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
- resolution conditions.

### FLEX

Adaptable presentation:

- office cast;
- narration style;
- investigator dialogue;
- hint delivery;
- scene transitions;
- debrief tone;
- genre-compatible cosmetic framing.

### CAPABILITIES

Office characters may have unusual abilities, equipment or knowledge.

A capability may:

- change how a pre-authored clue is obtained;
- automate routine connective work;
- unlock a creator-approved alternate route;
- change dialogue and interpretation.

A capability may not invent evidence, contradict CANON or bypass the entire clue chain unless the creator explicitly authored that possibility.

## Core state machine

~~~text
UNOPENED
  ↓
SETUP
  ↓
INVESTIGATING
  ↔
INTERROGATING
  ↓
ACCUSATION
  ↓
RESOLVED
  ↓
DEBRIEF
  ↓
FOLLOW-UP UNLOCKED (optional)
~~~

The state machine is backstage. The player should experience scenes, not status codes.

## Repository roles

- **README and Quickstart:** player-facing front door.
- **docs:** clean accepted design.
- **templates:** repeatable creator materials.
- **cases:** versioned playable cases.
- **references:** large libraries that support design but should not interrupt it.
- **archive:** preserved prototypes.
- **DECISIONS:** accepted choices and rationale.
- **ROADMAP:** priority control.

Brainstorming should not be appended directly to specifications. It should be evaluated, accepted or rejected, and then placed where it logically belongs.
