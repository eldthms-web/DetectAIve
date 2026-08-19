# Read Aloud, Voice and Interrogation Guide

Read Aloud, Live Voice and interrogation are different systems. V0 should not make the player learn them all at once.

## V0 channel model

> **TEXT = game**
> **READ ALOUD = narration**
> **IMAGES = evidence**
> **VOICE = primarily post-case reward**

Every case must remain fully playable in text. Voice interrogation is experimental and enabled only by a case that explicitly declares it.

## Read Aloud

The first runtime response briefly says:

> *Tip: this case works well with Read Aloud. When evidence appears, pause and inspect it for as long as you like.*

That is enough. Keep prose readable, stop at natural decision points and end cleanly before evidence inspection. Do not turn Read Aloud into a device tutorial.

## Text interrogation baseline

Important suspects/witnesses define:

~~~text
IDENTITY:
ROLE:
CURRENT EMOTIONAL STATE:
KNOWS:
BELIEVES:
CLAIMS:
HIDES:
LIES ABOUT:
DOES NOT KNOW:
PRESSURE / CONTRADICTIONS:
BREAKPOINT:
AFTER BREAKPOINT:
~~~

The runtime may improvise phrasing and ordinary reactions. It may not invent knowledge, reveal locked facts early, change the timeline or make a suspect collapse merely because the player says “I know you are lying.” Pressure comes from evidence and creator-defined contradictions.

When interrogation begins, make the modality visible with one short line, for example:

> **INTERROGATION — Question Nolan normally here in chat. There is no dialogue menu.**

## Post-case Voice debrief

After successful resolution, a case may offer:

~~~text
CASE CLOSED

Someone is waiting back at the office.

VOICE DEBRIEF AVAILABLE
~~~

Voice is optional. The same debrief must work in text.

A compact debrief card should specify:

~~~text
VOICE CARD: VD-01
CHARACTER: Office debrief character
START WHEN: Case is RESOLVED
PLAYER MOMENTS: Two or three actual events
OPENING INTENT: Return to the office
ASK: One genuine question
STOP: End the first response and let the player answer
AFTER ANSWER: React naturally using Player Moments
CLOSE WHEN: One or two exchanges are complete
~~~

Specific recognition matters more than speech length.

## Voice handoff: tested V0 workflow

Do not assume a Voice session will reliably inherit all hidden text-runtime state.

When the player accepts the Voice debrief:

1. In text, build **one complete portable handoff** containing the Voice Card, selected Player Moments, character demeanor, non-spoken control rules and opening intent.
2. Keep spoken dialogue separate from control directions so Voice does not read stage directions aloud.
3. The player copies that complete handoff.
4. The player starts Voice Mode.
5. Once Voice Mode is active, the player pastes/sends the handoff once.
6. Voice performs the first character turn, asks one question and stops for the player's spoken answer.
7. Continue naturally for one or two exchanges, then close.

If the interface does not support that workflow, continue the debrief in text. Voice is enrichment, never a gate.

A player-facing instruction can be as short as:

> **Copy the debrief handoff below. Start Voice Mode, then paste/send it once Voice is active.**

## Conversation turns are control

Reliable performed rhythm:

1. character speaks;
2. character asks one question;
3. response ends;
4. player answers;
5. character reacts;
6. next turn continues or closes.

Do not place speakable directions such as `[WAIT]`, `SMILES` or `LOOKS AWAY` inside dialogue intended for performance. Some systems will say them aloud.

## Experimental Voice interrogation

A creator may optionally test one major voiced interrogation. It must be:

- explicitly declared by the case;
- clearly labeled experimental;
- optional and rare;
- unnecessary for solving the case;
- backed by the same locked interrogation packet as text;
- easy to leave without losing the investigation.

A short case should not repeatedly bounce the player between voices or modes.

Example card:

~~~text
VOICE CARD: VI-01
CHARACTER: Mara Venn
SCENE: Primary interrogation
START WHEN: Evidence E-03 is revealed
OPENING INTENT: Guarded professionalism
ASK: Why the player doubts her timeline
STOP: End response and let player answer
AFTER ANSWER: React using current locked interrogation state
EXIT WHEN: Breakpoint reached or player returns to text
~~~

If a Voice interrogation needs a portable handoff, use the same self-contained transfer principle as the debrief. No solution-critical fact may exist only in Voice.

## Portability rule

Voice performance may enrich presentation but never alter CANON or contain required information unavailable through the text path.
