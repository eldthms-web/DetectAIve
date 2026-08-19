# Read Aloud, Voice and Interrogation Guide

Read Aloud, Live Voice and interrogation are three different systems.

V0 should not make the player learn them all at once.

## V0 channel model

> **TEXT = game**
>
> **READ ALOUD = narration**
>
> **IMAGES = evidence**
>
> **VOICE = post-case reward**

Live Voice interrogation is experimental. Every interrogation must work completely in text.

## Read Aloud

The runtime mentions Read Aloud in the first response:

> *Tip: this game works well with Read Aloud. When evidence appears, pause and inspect it at your own pace.*

That is enough. Do not explain the full interface or require setup.

Narrative responses should:

- use readable paragraphs;
- avoid enormous unbroken monologues;
- stop at natural decision points;
- end cleanly before the player studies an evidence image;
- keep control syntax out of player-facing narration.

Read Aloud is optional. The text remains the authoritative game transcript.

## Text interrogation baseline

An important suspect or witness should define:

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

NERVOUS EVIDENCE:
CONTRADICTIONS:
BREAKPOINT:
AFTER BREAKPOINT:
CANNOT REVEAL BEFORE:
~~~

The character may improvise phrasing and ordinary reactions. They may not invent knowledge, reveal locked facts early or change the canonical timeline.

A story should not collapse merely because the player says “I know you are lying.” Pressure comes from evidence, incompatible claims or a creator-defined combination.

## Voice primarily follows resolution

After a successful case, the runtime may offer:

~~~text
CASE CLOSED

Someone is waiting back at the office.

VOICE DEBRIEF AVAILABLE
~~~

Voice is an escalation in intimacy and presentation. It is not something the player must manage throughout the investigation.

The debrief must also work in text. Interface availability, plan limits and device behavior may vary.

## Voice debrief card

A V0 Voice Card should remain small:

~~~text
VOICE CARD: VD-01
CHARACTER: Office debrief character
START WHEN: Case is RESOLVED
PLAYER MOMENTS: Select two or three actual events
OPENING INTENT: Private return to the office
ASK: One genuine question about the investigation
STOP: End the response and let the player answer
AFTER ANSWER: React naturally using the recorded Player Moments
CLOSE WHEN: One or two exchanges are complete
~~~

Specific recognition matters more than speech length.

Weak:

> Great work, Detective.

Strong:

> You noticed the chair had been put upright. Most people would have called the room less suspicious. You asked who had touched it.

## Conversation turns are control

Reliable performed rhythm:

1. character speaks;
2. character asks one question;
3. response ends;
4. player answers;
5. character reacts;
6. the next turn continues or closes.

Do not place speakable directions such as `[WAIT]`, `SMALL PAUSE`, `SMILES` or `LOOKS AWAY` inside dialogue intended for performance. Some systems may say them aloud.

Keep non-spoken instructions in the Voice Card and spoken words in dialogue fields.

## Experimental Voice interrogation

A creator may optionally test one major voiced interrogation. It must be:

- clearly labeled experimental;
- optional;
- rare;
- unnecessary for solving the case;
- backed by the same locked interrogation packet used in text;
- easy to leave without losing state.

A short case should not ask the player to change voices or modes repeatedly.

## Experimental interrogation Voice Card

~~~text
VOICE CARD: VI-01
CHARACTER: Mara Venn
SCENE: Primary interrogation
START WHEN: Evidence E-03 is revealed
OPENING INTENT: Guarded professionalism
ASK: Why the player doubts her timeline
STOP: End the response and let the player answer
AFTER ANSWER: React using current interrogation state
EXIT WHEN: Breakpoint reached or player returns to text
~~~

Dialogue examples may be included, but the runtime responds naturally to the player's actual words.

## Portability rule

Voice performance may enrich a case but may never contain solution-critical information unavailable in text.

If Voice fails, is unavailable or is declined, the investigation and debrief continue in text without penalty.

