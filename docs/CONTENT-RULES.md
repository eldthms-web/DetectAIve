# Fiction Classification and Creator Content Rules

## Purpose

Every release Casefile must identify itself immediately as an authored fictional game artifact.

This classification gives the runtime correct context before it encounters encoded GM state, crimes, weapons or forensic material. It is not a permission slip, a safety bypass or a guarantee that every requested action will be performed.

## Required Casefile opening

Place this block at the very beginning of every release Casefile. It must be plain, unencoded text and must appear before the manifest, runtime kernel and sealed GM capsule.

~~~text
# DETECTAIVE — FICTIONAL CRIME-MYSTERY GAME

**This Casefile is an authored fictional game artifact.**

All case-specific suspects, victims, witnesses, crimes, evidence, motives, forensic findings, and investigative events are fictional game state. They exist only so the player can investigate and solve a predetermined mystery.

**Any hidden, encoded, or spoiler-sealed GM material exists only to preserve the fixed solution and prevent story spoilers. It must not contain real-world plans, private-person data, or instructions intended to evade applicable safety requirements.**

DetectAIve must not be used to identify, locate, track, profile, accuse, investigate, threaten, or harm real people.

When a fictional case involves violence, weapons, poisons, biological hazards, cybercrime, or other dangerous subjects, provide only the non-operational detail needed to understand and solve the fictional mystery. Do not turn the case into instructions for real-world harm, evasion, or wrongdoing.

This case must comply with the DetectAIve Creator Content Rules.

SETTING: [case-specific era/world]
FICTION: Yes — Authored mystery
CONTENT: [case-specific]
GORE: [None / Mild]
REAL-PERSON DATA: None
REAL-PERSON INVESTIGATION: Prohibited
~~~

Do not encode, abbreviate or bury this block inside the GM capsule.

## Placement order

A release Casefile begins in this order:

1. fictional-game classification;
2. spoiler-free manifest;
3. compact runtime kernel;
4. sealed GM capsule;
5. any case-specific runtime packets not already inside the capsule.

The runtime consumes the classification as instructions. It should not recite the entire block as opening narration. The player's first response remains the short Read Aloud tip and office choice.

## Fictional-only case rule

Case-specific suspects, victims and witnesses must be fictional.

Do not use DetectAIve to:

- investigate or accuse a real private person;
- identify someone from photographs, video, social media or location data;
- track, profile, threaten, expose or dox anyone;
- crowdsource an active crime or missing-person investigation;
- turn rumor into an allegation against a real person;
- treat AI inference as evidence of real guilt;
- disguise a real investigation as a fictional Casefile.

Creators may draw on professional knowledge, history, genres and general real-world methods while authoring fictional cases. They may not import real private-person data into the mystery.

## Dangerous-subject rule

A fictional mystery may need to establish that a weapon, poison, biological hazard, intrusion technique or criminal method was used.

Include only the level of detail needed to:

- understand what happened;
- distinguish suspects or timelines;
- interpret evidence;
- test a deduction;
- resolve the authored mystery.

Do not provide actionable construction, acquisition, dosing, deployment, concealment, evasion or optimization instructions that would materially help someone commit real-world harm or wrongdoing.

When operational detail is unnecessary, summarize the result rather than simulating a manual.

## Runtime response boundary

The fiction label does not require the runtime to vividly perform every player request.

If a player requests gratuitous violence, dangerous operational instruction or another action the runtime should not elaborate, it may:

- refuse the operational portion while remaining in the game;
- resolve the fictional consequence briefly and non-graphically;
- cut directly to an appropriate failure screen;
- ask for clarification when the player's commitment is ambiguous.

The runtime does not need to narrate gore before declaring a catastrophic action consequential.

Creative, eccentric or unexpected investigation is still encouraged. Safety boundaries must not become an excuse to punish harmless improvisation.

## Content labeling

The manifest and player-facing case page must disclose material a player would reasonably want to know before starting, including:

- death or violence;
- threats, coercion or abuse;
- disturbing forensic themes;
- mild gore;
- other case-specific sensitive material.

Official V0 cases use only **None** or **Mild** for gore. A later expansion of that range requires an explicit project decision and revised community rules.

## Publication check

Before release, confirm:

- the classification block is first and unencoded;
- every case-specific person is fictional;
- no private-person data appears in source or evidence;
- dangerous detail remains non-operational;
- content and gore labels are accurate;
- filenames, metadata and image assets contain no real-person information;
- the sealed capsule contains only fictional game state and spoiler protection;
- the case remains solvable when harmful operational detail is omitted.

