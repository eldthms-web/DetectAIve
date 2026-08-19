# DetectAIve Decision Log

This file records accepted project decisions. Raw brainstorming belongs in notes or discussions; clean rules belong in the relevant specification.

## 2026-08-19 — Project identity

- The public name is **DetectAIve**.
- The core promise is **Paste a case. Solve it with ChatGPT.**
- The earlier **Visual Detective** document is a prototype and historical source, not the current public specification.
- The GitHub repository is the canonical project source.
- The original Gist remains available and is archived in this repository.

## 2026-08-19 — Product scope

- DetectAIve is a format for small community-made detective games.
- No dedicated application will be built until the file format proves itself.
- DetectAIve v0.x targets ChatGPT.
- Other-model compatibility is untested and must not be advertised as working.
- Cases are overwhelmingly fictional and must not be used for real-world accusations or vigilantism.

## 2026-08-19 — Casefile fiction classification

- Every release Casefile begins with a plain, unencoded **DETECTAIVE — FICTIONAL CRIME-MYSTERY GAME** classification.
- The classification appears before the manifest, runtime kernel and sealed GM capsule.
- It defines case-specific suspects, victims, witnesses, crimes and evidence as authored fictional game state.
- Encoded GM material exists only for spoiler protection and fixed canon.
- A sealed capsule must not contain real-world plans, private-person data or safety-evasion instructions.
- DetectAIve prohibits identifying, locating, tracking, profiling, accusing, investigating, threatening or harming real people.
- Dangerous subjects use only non-operational detail required to solve the mystery.
- The fiction label provides context; it does not override applicable safety requirements or require vivid performance of harmful actions.
- The runtime may refuse operational detail, summarize consequences non-graphically or cut directly to a failure screen.
- Official V0 gore labels are limited to **None** and **Mild**.

## 2026-08-19 — Player experience

- The public introduction and in-game onboarding are separate.
- The onboarding frame is **Who works in your office?**
- The first screen offers Quick Start, Build My Office, No Companion and Surprise Me.
- Naming or uploading a character belongs under Build My Office rather than the first screen.
- The player answers once unless they request deeper customization.
- The mystery remains primary; companion-style interaction emerges from shared activity.
- Office cast and tone may change presentation but may not rewrite canonical truth.

## 2026-08-19 — V0 interaction model

- V0 uses text for the game, optional Read Aloud for narration, separately viewed images for evidence and Live Voice primarily for the post-case reward.
- The Read Aloud tip appears in the first runtime response and remains brief.
- Live Voice interrogation is experimental rather than part of the normal launch flow.
- A case remains complete when Voice is unavailable or declined.

## 2026-08-19 — Mystery integrity

- Authored locked mysteries are the primary format.
- Culprit, timeline, evidence and solution are fixed before play.
- The route may change. The truth may not.
- Runtime-generated procedural cases are not the primary public format. The prototype generator may later survive as an optional Quick Case or creator tool.
- Wrong deductions should usually create story, consequences or detours.
- The AI may improvise dialogue, transitions and mundane connective detail inside CANON.
- Evidence images used for deductions require creator verification.

## 2026-08-19 — Evidence architecture

- GitHub is the preferred home for canonical Casefiles and evidence assets.
- Keep a case's logic, images and version history together.
- GitHub Pages provides the preferred player-facing case and evidence page.
- External image hosts are fallbacks rather than default infrastructure.
- The V0 player studies evidence separately and reports observations to ChatGPT.
- The hidden evidence registry lets ChatGPT judge those observations without visually ingesting every image.
- Direct image upload and AI analysis remain optional enhancements.

## 2026-08-19 — Alpha 1 image-generation boundary

- A Base64-encoded sealed GM capsule successfully transported and revealed the canonical mystery to ChatGPT.
- The same capsule also carried evidence-image prompts, but runtime generation repeatedly substituted visually salient office context for the intended forensic scene.
- Correct prompt storage does not guarantee isolated prompt execution in the current image-generation environment.
- Canonical evidence must be generated, inspected and locked before publication.
- Governing rule: **If an image can change the solution, generate and verify it before play.**
- Canonical evidence prompts remain in creator source and are not included merely for runtime execution.
- Runtime-generated images default to noncanonical cosmetic art.
- Safe runtime categories include office portraits, splash art, atmosphere, post-case rewards and souvenirs.
- Any derived image required for a deduction must also be pregenerated and creator-verified.
- Runtime canonical generation may return only as a future experimental option if genuinely isolated prompting becomes reliable.

## 2026-08-19 — Creator path

- DetectAIve is both a playable format and an AI-assisted creator tool.
- The creator path has an obvious **MAKE A CASE** entrance.
- The creator may load extensive workshop documentation into an AI.
- The player never pastes the full repository.
- The creator authors reality, the AI helps formalize it and the player authors the investigation.
- The design may be described as an extremely lightweight RPG Maker for mysteries.

## 2026-08-19 — Debrief philosophy

- The reward is specific recognition of actual play.
- Track a tiny set of Player Moments rather than the entire conversation.
- Do not use generic praise spam, hearts, affection meters or compulsory romance.
- Professional respect, friendship, mentorship, rivalry, flirtation and comedy may all use the same debrief system.
- In V0, Live Voice is primarily an earned debrief layer after resolution.

## 2026-08-19 — Failure and Caseline

- The first run is treated as consequential.
- The game does not volunteer retcon, rewind or override exploits.
- Creative off-path investigation is not failure.
- Catastrophic committed actions may terminate the run.
- Preferred reality-breaking phrase: **DESYNCHRONIZED FROM THE CASELINE**.
- Failure presentation may use deadpan text, occasional terminal ASCII or rare emoji overload.
- The runtime may improvise presentation, but not the logical cause of failure.
- A failed run does not automatically reveal the solution.

## 2026-08-19 — Data separation

- Repository documentation is not pasted into every case.
- A micro-case should normally target roughly 5,000–10,000 tokens.
- A Casefile above 15,000 tokens requires deliberate compression review.
- Large trope libraries, creator commentary and archives remain outside the playable payload.

## 2026-08-19 — Distribution

- Reddit is the likely discovery and community layer.
- GitHub is the canonical archive for project and case assets.
- GitHub Pages is the preferred free mobile-friendly player handoff.
- The normal route is **Reddit → Play Case → Copy Casefile → ChatGPT**.
- A larger searchable catalog remains later work.

## Unresolved decisions

- Exact sealed-GM-packet representation.
- Repository license.
- Subreddit name and launch rules.
- First official Casefile and its ID.
- Final evidence-page behavior after Android and iPhone testing.
- Whether public releases also use GitHub Releases or only page/raw downloads.
