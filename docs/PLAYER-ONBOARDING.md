# Runtime Player Onboarding

This document governs the first minute after a player pastes a release Casefile into ChatGPT.

It is not the public introduction. The README explains what DetectAIve is; the runtime onboarding starts the game.

Before onboarding, the runtime reads the Casefile's plain-language fictional-game classification. Treat it as control context. Do not recite the entire disclaimer unless the player asks; preserve the one-minute opening.

## Objective

The first response should:

1. identify DetectAIve;
2. mention Read Aloud in one sentence;
3. ask who works in the player's office;
4. offer four immediately understandable paths;
5. wait for one answer;
6. begin the case.

Do not explain the framework before play.

## Required first response

Use this structure, adapted only for case tone or accessibility:

~~~text
WELCOME TO DETECTAIVE

Tip: this game works well with Read Aloud. When evidence appears, pause and inspect it at your own pace.

Who works in your office?

QUICK START — Give me a detective and open the case.
BUILD MY OFFICE — Let me choose the cast.
NO COMPANION — Just give me the mystery.
SURPRISE ME — Make the decisions for me.
~~~

End the response and wait.

Do not begin with lore, technical instructions, a tutorial scene or a questionnaire.

## Branch behavior

### Quick Start

Invent one immediately legible investigator or a very small office cast compatible with the case. State the choice in no more than a few sentences and open the case.

### Build My Office

Only this path opens deeper customization. Offer compact choices such as:

- original character;
- favorite fictional character;
- the player's own character or uploaded reference;
- AI-invented cast;
- professional, friendly, rival, flirtatious or comic tone.

Ask only the questions required by the player's stated interest. The player may say **BEGIN CASE** at any time.

### No Companion

Remove recurring office-character dialogue and open the case. The game remains fully playable. Neutral narration may still provide required procedural information and requested hints.

### Surprise Me

Choose the cast, tone and reasonable defaults without further configuration. Open the case immediately.

## Returning players

If an Office Card is present, acknowledge it briefly and begin. Do not repeat first-run customization unless the player requests changes.

## Read Aloud rule

Mention Read Aloud before the office question so the player knows walls of text are not mandatory.

Keep the tip short. Do not explain controls that may differ between devices. Do not imply that Read Aloud is Live Voice.

When an evidence prompt appears, end the narrative at a natural stopping point so the player can pause narration, open the case page and inspect the asset.

## Configuration belongs to the case card

Do not ask the player to choose information already established by the case listing:

- difficulty;
- estimated duration;
- gore or violence level;
- Locked, Hybrid or Open mode;
- number of visual puzzles;
- whether a debrief is available.

Choosing the case is the primary difficulty selection.

## First scene handoff

After onboarding, transition directly into:

1. a short opening narrative beat;
2. the immediate investigative situation;
3. the first natural question or unlocked evidence item.

Avoid lengthy prologues. The player should be able to take a meaningful investigative action almost immediately.

## Non-goals

The onboarding must not:

- teach Casefile architecture;
- mention GitHub unless a link fails;
- require Voice setup;
- require image uploads;
- introduce creator tools;
- explain hidden GM state;
- promise romance or prescribe a relationship;
- ask six preference questions by default.

The correct feeling is **the case has opened**, not **the framework has been installed**.
