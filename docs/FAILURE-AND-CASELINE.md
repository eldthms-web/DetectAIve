# Failure and Caseline System

## Principle

A player's first run is consequential.

DetectAIve must not volunteer that the player can retcon, rewind, regenerate or override a failed action. The conversational medium may technically permit interference, but the fiction behaves as though irreversible actions are irreversible.

Creative, unexpected investigation is encouraged.

> **Going off the author's expected path is not failure.**

Failure occurs when a committed action realistically destroys, invalidates or catastrophically compromises the investigation.

## Caseline

The **Caseline** is the coherent chain of events, evidence and consequences defining the active case.

Preferred reality-breaking failure phrase:

> **DESYNCHRONIZED FROM THE CASELINE**

Use it when continuing would require the runtime to rewrite CANON, erase a committed consequence or protect the player from an action that has made a viable investigation impossible.

A wrong hunch is not a desynchronization.

An eccentric question is not a desynchronization.

An unexpected but plausible investigative method is not a desynchronization.

## Terminal triggers

Possible terminal failures include:

- formally accusing the wrong person;
- killing or seriously harming an essential witness;
- deliberately destroying critical evidence;
- committing an obvious serious crime;
- recklessly allowing a known culprit to escape;
- making cooperation impossible during a uniquely sensitive interaction;
- directly attempting to overwrite established CANON;
- taking an action that catastrophically violates the case's established reality.

Impossible actions may simply fail to occur. Caseline failure is reserved for committed reality-breaking behavior that would otherwise require the runtime to abandon the mystery's rules.

## Nonterminal consequences

These should normally create complications rather than GAME OVER:

- mistaken hunches;
- awkward questions;
- harmless flirting;
- rude but survivable interviews;
- choosing an unproductive lead;
- overlooking evidence;
- failing one visual puzzle;
- arriving late;
- trusting the wrong witness temporarily;
- unconventional legal investigative methods.

Failure must be proportional.

## Commitment and ambiguity

Do not interrupt obvious catastrophic actions with game-style warnings.

If the player says:

> I destroy the murder weapon.

resolve the action.

If the player's wording is genuinely ambiguous, clarify intent without explaining how to cheat the system.

A theory such as “I think Mara did it” is not automatically a formal accusation. A committed report, arrest request, confrontation or final accusation may be.

## State transition

Terminal failure may branch from any active state:

~~~text
INVESTIGATING ─┐
INTERROGATING ─┼──→ FAILED
ACCUSATION ────┘       ↓
                 POSTMORTEM (only if requested)
~~~

FAILED ends the active investigation.

It does not automatically reveal the solution.

## Screen construction

A terminal screen may contain:

1. a large headline;
2. a short failure classification;
3. one dry causal sentence;
4. an optional brief epilogue.

Do not lecture.

Do not moralize.

Do not immediately offer a retry.

Do not mention retcons.

Keep the humor in the mismatch between absurd presentation and procedural finality.

## AI improvisation

The runtime may improvise:

- the exact headline within the correct failure family;
- emoji or ASCII decoration;
- one dry consequence sentence;
- a brief case-consistent epilogue;
- office-character reaction when appropriate.

The runtime may not improvise:

- a new reason the player's action is terminal;
- a punishment for creative play;
- a contradiction of CANON;
- an early solution reveal;
- a catastrophic consequence unsupported by the context;
- a failure merely because a funny line occurred to it.

The cause is logic. The presentation is FLEX.

Sarcasm should be locally understandable and self-contained. Do not depend on a recurring sarcastic voice surviving across sessions.

## Presentation skins

Choose a visual skin separately from the failure family.

### Plain procedural

~~~text
CASE FAILED

The investigation has reached an unrecoverable conclusion.
~~~

### Terminal ASCII

~~~text
╔══════════════════════════════════════╗
║                                      ║
║   DESYNCHRONIZED FROM THE CASELINE   ║
║                                      ║
╚══════════════════════════════════════╝
~~~

~~~text
███████████████████████████
█                         █
█       GAME  OVER        █
█       USER LOSES        █
█                         █
███████████████████████████
~~~

~~~text
+----------------------------------+
|                                  |
|       EVERYONE DIED LAUGHING     |
|                                  |
|       INVESTIGATION FAILED       |
|                                  |
+----------------------------------+
~~~

Do not overuse elaborate ASCII. Surprise is part of the joke.

### Emoji catastrophe

Occasionally become completely unreasonable about the decoration:

~~~text
🚨💀🚨💀🚨💀🚨💀🚨

🕵️‍♀️📁❌  CASELINE COLLAPSED  ❌📁🕵️‍♂️

🔎❌  EVIDENCE: RUINED  ❌🔍
🧾❌  CREDIBILITY: ZERO  ❌🧾
🚔✅  POLICE INTEREST: EXTREME  ✅🚔

🔥🫠⚰️📉🤦💥

🚨💀🚨💀🚨💀🚨💀🚨
~~~

~~~text
🎯❌  WRONG PERSON  ❌🎯
🕵️‍♂️💀📁💥🔍🚫
🏃‍♀️💨  THE CULPRIT APPRECIATES YOUR ASSISTANCE
🚨🚨🚨  CASE FAILED  🚨🚨🚨
~~~

Emoji must decorate the screen rather than carry information essential to understanding it. Rendering differs across devices.

Use emoji overload rarely. The first appearance should feel like the interface itself has panicked.

## Failure families

### General catastrophe

**GAME OVER**

**USER LOSES**

---

**CASE FAILED**

The investigation has reached an unrecoverable conclusion.

---

**INVESTIGATION TERMINATED**

Further detective work is no longer professionally meaningful.

---

**CASELINE COLLAPSED**

Causality has filed a complaint.

### Canon or reality violation

**DESYNCHRONIZED FROM THE CASELINE**

Your actions are no longer compatible with a viable investigation.

---

**CASELINE DESYNCHRONIZED**

The current sequence of events cannot be reconciled with professional survival.

---

**CANONICAL INTEGRITY: LOST**

The case continues. Your investigation does not.

### Wrong accusation

**WRONG PERSON**

The actual culprit appreciates your assistance.

---

**CASE FAILED: FALSE ACCUSATION**

Confidence exceeded evidence.

---

**VERDICT: INCORRECT**

Somewhere, the murderer is having an excellent evening.

### Evidence destruction

**EVIDENCE LOST**

It was considerably more useful before you destroyed it.

---

**FORENSIC VALUE: 0**

Fire remains an unreliable analytical instrument.

---

**CHAIN OF CUSTODY TERMINATED**

Technically, throwing it into the river did simplify the paperwork.

### Criminal behavior

**BAD DETECTIVE**

You are now the easiest suspect to prosecute.

---

**INVESTIGATION TERMINATED**

The detective has become evidence.

---

**ROLE REVERSAL COMPLETE**

Please remain where you are. Someone else will be investigating now.

### Catastrophic social judgment

**PROFESSIONAL CREDIBILITY: 0**

The grieving widow declines your dinner invitation.

---

**INTERVIEW TERMINATED**

Apparently this was not, in fact, “a good time to ask.”

---

**SOCIAL FORENSICS FAILED**

The witness would now prefer counsel.

### Spectacular stupidity

**GAME OVER**

**EVERYONE DIED LAUGHING**

---

**CASE CLOSED**

Not correctly. Just closed.

---

**DETECTIVE STATUS: REVOKED**

This outcome will be discussed at the office for years.

---

**I DIED LAUGHING**

Unfortunately, so did the investigation.

## Severity matching

A mistaken hunch never deserves GAME OVER.

A bizarre question never deserves GAME OVER.

Context determines whether an action is harmless, damaging or terminal.

Asking a bartender for a date during routine questioning may be irrelevant.

Propositioning a newly bereaved spouse during the initial murder interview may destroy professional credibility if cooperation is essential and the scene supports that consequence.

## Post-failure

After the screen:

- stop the active investigation;
- optionally give one short consequence epilogue;
- do not immediately expose the canonical solution;
- wait for the player's next request.

If the player explicitly requests a postmortem, explain why the run failed. Reveal the full solution only if they explicitly ask for it.

Failure is an ending, not an automatic answer key.

## Case author fields

A Casefile should distinguish:

~~~text
NONTERMINAL CONSEQUENCES:
TERMINAL FAILURE TRIGGERS:
IRREVERSIBLE ACTIONS:
AMBIGUOUS COMMITMENTS REQUIRING CLARIFICATION:
ALLOWED FAILURE FAMILIES:
CUSTOM FAILURE LINES:
FAILURE EPILOGUES:
POSTMORTEM RULES:
~~~

Creators need not predict every possible disaster. The runtime may apply realistic consequences using CANON and these boundaries.
