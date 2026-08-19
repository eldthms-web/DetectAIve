# DetectAIve Decision Log

This file records accepted project decisions. Raw brainstorming belongs in notes or discussions; clean rules belong in the relevant specification.

## 2026-08-19 — Project identity

- The public name is **DetectAIve**.
- The core promise is **Paste a case. Solve it with ChatGPT.**
- The earlier **Visual Detective** document is a prototype and historical source, not the current public specification.
- The GitHub repository is the canonical project source.
- The original Gist will remain available and will also be archived in this repository.

## 2026-08-19 — Product scope

- DetectAIve is a format for small community-made detective games.
- No dedicated application will be built until the file format proves itself.
- DetectAIve v0.x targets ChatGPT.
- Other-model compatibility is untested and must not be advertised as working.
- Voice is an optional interaction layer, not a requirement for every scene.
- Cases are overwhelmingly fictional and must not be used for real-world accusations or vigilantism.

## 2026-08-19 — Player experience

- The public introduction and in-game onboarding are separate.
- The onboarding frame is **Who works in your office?**
- Players may quick-start, build an office, use a supplied character, ask for a surprise cast or play without office characters.
- The mystery remains primary; companion-style interaction emerges from shared activity.
- Office cast and tone may change presentation but may not rewrite canonical case truth.

## 2026-08-19 — Mystery integrity

- Authored locked mysteries are the primary format.
- Culprit, timeline, evidence and solution are fixed before play.
- The route may change. The truth may not.
- Runtime-generated procedural cases are not the primary public format. The prototype generator may later survive as an optional Quick Case or creator tool.
- Wrong deductions should usually create story, consequences or detours.
- Evidence images used for deductions require creator verification.

## 2026-08-19 — Debrief philosophy

- The reward is specific recognition of actual play.
- Track a tiny set of Player Moments rather than the entire conversation.
- Do not use generic praise spam, hearts, affection meters or compulsory romance.
- Professional respect, friendship, mentorship, rivalry, flirtation and comedy may all use the same debrief system.

## Provisional distribution direction

- GitHub is the source of truth and version archive.
- A subreddit is the likely discovery, play-sharing and community layer.
- A lightweight catalog website may be added later.
- This becomes final only after the first playable Casefile reveals the real distribution friction.

## Unresolved decisions

- Exact sealed-GM-packet representation.
- Exact evidence-image delivery method.
- Repository license.
- Subreddit name and launch rules.
- First official Casefile and its ID.
- Whether the first public release uses GitHub Releases, raw files or both.
