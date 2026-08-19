# DetectAIve

> **Paste a case. Solve it with ChatGPT.**

DetectAIve is a ChatGPT-first format for small authored detective games. A creator locks the mystery, publishes a compact Casefile plus verified evidence, and the player investigates in ordinary language.

> **CURRENT SPECIFICATION:** The root documents, `/docs`, and `/cases` describe current DetectAIve. Everything under `/archive` is historical and non-authoritative. Do not combine archived prototype rules with the current specification.

If two current documents genuinely contradict each other, treat that as a documentation bug to fix rather than inventing a hierarchy of competing rules.

## PLAY

The V0 player flow is deliberately small:

1. Open a **PLAY CASE** page.
2. Select **COPY CASEFILE**.
3. Paste it into ChatGPT.
4. Answer one short office question.
5. Investigate in natural language.
6. When ChatGPT says **OPEN EVIDENCE E-01**, inspect that numbered asset on the case page and return with what you noticed.
7. Solve the case and optionally use a post-case debrief.

**Current runnable scaffold:** [DA-001 — The Brass Star](https://eldthms-web.github.io/DetectAIve/cases/DA-001/page/)

Start with [Play DetectAIve in Sixty Seconds](QUICKSTART.md). Runtime onboarding details live in [Player Onboarding](docs/PLAYER-ONBOARDING.md).

## CREATE

A new creator should start in one place:

**[AI-Assisted Creator Guide](docs/CREATOR-GUIDE.md)**

Give it to your AI and say:

> **Help me make a DetectAIve case. Guide me one decision at a time. Do not change locked canon without asking me.**

The working flow is:

> **Generate / Invent → Lock → Verify Evidence → Package → Playtest**

The creator decides what is true. The AI helps formalize, stress-test and package it. The player authors the investigation.

AI-authored Quick Cases use the same integrity rule: generate the complete mystery first, lock it, then begin play. The culprit and solution do not emerge dynamically in response to the player.

## The V0 contract

**CANON is fixed.** Culprit, timeline, evidence meaning, suspect knowledge and resolution conditions are established before play. A persuasive player theory does not become true because ChatGPT likes it.

**Natural language is the interface.** Reasonable paraphrases of observations count. If a report is too vague to establish a clue, ask a natural clarifying question rather than requiring a password-like phrase.

**Canonical evidence already exists.** If an image can change the solution, create and verify it before play. Store the approved asset with the case. Runtime image generation is noncanonical cosmetic art only.

**Text is the game.** Read Aloud is optional narration. Images are evidence. Voice is primarily an optional post-case reward; Voice interrogation is case-specific and experimental.

**Failure is consequential but rare.** A theory is not a formal accusation. Clearly committed catastrophic actions may end a run. Terminal violence is handled with a concise GAME OVER / CASELINE screen, not a narrated gore scene. The game does not proactively advertise retcons or reloads.

## SPEC / REFERENCE

These are the current detailed rules. Read only what the task requires.

- [Runtime Kernel](docs/RUNTIME-KERNEL.md) — compact shared behavior copied into release Casefiles.
- [Casefile Format](docs/CASE-FORMAT.md) — release cartridge and case-folder structure.
- [Fiction Classification and Creator Content Rules](docs/CONTENT-RULES.md) — fictional-only and conservative content boundary.
- [Visual Evidence Guide](docs/VISUAL-EVIDENCE.md) — fair visual clues and immutable evidence.
- [Read Aloud, Voice and Interrogation](docs/VOICE-AND-INTERROGATION.md) — modality responsibilities and Voice handoff.
- [Failure and Caseline](docs/FAILURE-AND-CASELINE.md) — committed consequences and terminal presentation.
- [Office and Debrief](docs/OFFICE-AND-DEBRIEF.md) — office framing and Player Moments.
- [Mobile-First Distribution](docs/MOBILE-DISTRIBUTION.md) — GitHub Pages handoff and phone testing.
- [Architecture](docs/ARCHITECTURE.md) — system boundaries and state model.
- [Data and Context Budgets](docs/DATA-BUDGETS.md) — keep playable payloads compact.
- [Glossary](docs/GLOSSARY.md) — project terminology.
- [Community and Distribution Plan](docs/COMMUNITY-PLAN.md) — discovery and publishing assumptions.
- [Decision Log](DECISIONS.md) — accepted project decisions and rationale.
- [Roadmap](ROADMAP.md) — current priorities.

## ARCHIVE / HISTORY

The [archive](archive/) preserves superseded experiments for project history. It is **not** creator guidance and **not** runtime specification.

In particular, the archived pre-DetectAIve procedural prototype contains obsolete assumptions about live evidence generation and other runtime behavior. Those assumptions must not be imported into current cases.

## Safety boundary

DetectAIve cases are fictional. Do not use the format to identify, locate, track, profile, accuse or investigate real private people, crowdsource active investigations, dox anyone or present AI deduction as evidence of real guilt.

Every release Casefile begins with the plain-language fictional-game classification defined in [Content Rules](docs/CONTENT-RULES.md). Dangerous subjects receive only the non-operational detail needed to understand and solve the fictional mystery. Official V0 gore labels are **None** or **Mild**.

## Current scope

DetectAIve v0.x is **ChatGPT-first**. Other-model compatibility is not a launch requirement. There is no dedicated app, account system, API dependency, marketplace or catalog requirement for V0.

The next proof is practical: one stranger, one case page, one Casefile, fixed evidence, and a complete solve without creator coaching.

---

**Make authorship powerful. Make play effortless.**
