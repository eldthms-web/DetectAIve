# AI-Assisted Creator Guide

DetectAIve lets ordinary people make small detective games with AI assistance. No programming is required. The output is a portable Casefile plus verified evidence assets.

> **The creator authors reality.**
> **The AI helps formalize it.**
> **The player authors the investigation.**

## Start here

Give this guide to your AI and say:

> **Help me make a DetectAIve case. Guide me one decision at a time. Do not change locked canon without asking me.**

Do not make the creator study the repository before beginning. Ask only the next useful question and consult deeper specs when the work reaches them.

The whole process should feel like one flow:

> **Generate / Invent → Lock → Verify Evidence → Package → Lint → Playtest**

### AI-generated mysteries

The creator may ask the AI to invent most or all of the mystery. That is fine. The integrity rule is the same:

> **Generate first. Lock second. Play third.**

Before any player-facing investigation begins, establish the complete responsible party, timeline, motive, means, opportunity, evidence meanings, suspect knowledge and resolution conditions. Do not generate the culprit dynamically in response to the player's theories.

## 1. Generate / invent the promise

Decide what happened, who is responsible, why it is interesting, what should become satisfying or surprising when the truth is understood, the canonical setting/era, expected length/difficulty and content/gore labels.

Exploration is welcome here.

## 2. Lock reality

Before building puzzles, freeze the culprit or responsible party, motive, means, opportunity, true timeline, victim status if relevant, innocent explanations and final resolution conditions.

After this pass, do not rewrite truth merely because a later theory sounds better.

## 3. Build the clue chain

For every required deduction, identify evidence the player can actually receive. Classify clues as **required, supporting, optional, red herring, decoration** or **accidental artifact**.

Motive, means and opportunity are useful structures, not mandatory puzzle slots.

Natural-language matching should remain semantic. Record canonical observations and a few obvious paraphrase families when useful, but do not build giant phrase-password tables. If a player's wording is too vague, the runtime can ask a natural clarifying question.

## 4. Verify evidence

Decide what the player must actually notice, then create, photograph, draw, render or commission the asset.

> **If an image can change the solution, generate and verify it before play.**

The AI may help write creator-time image prompts and propose decoys, but the creator must inspect the final pixels. Runtime generation is not canonical evidence.

For each approved asset, give it a stable evidence ID, store it in `evidence/`, make the registry match the actual file, test phone legibility, avoid spoiler filenames/alt text and add an accessibility fallback where practical.

User-supplied photographs, hand art, 3D renders and creator-generated images all work. DetectAIve cares that the published evidence is fixed and verified, not how it was made.

See [Visual Evidence](VISUAL-EVIDENCE.md) for puzzle design and QA.

## 5. Build people, not answer dispensers

For every important suspect or witness define the player-safe public summary separately from hidden canonical facts. Use explicit disclosure gates for important facts that become available only after a clue or request.

Interrogation state may then define what the person knows, believes, claims, hides or lies about, which evidence changes their behavior, their contradiction/breakpoint logic and what happens afterward.

Not every suspect needs the same fields or a full interrogation packet. What matters is that **public, private and gated information are unambiguous**. See [Casefile Format](CASE-FORMAT.md).

## 6. Define consequences

Separate harmless off-path investigation, nonterminal complications, irreversible actions, rare terminal failures and ambiguous commitments that require clarification.

A theory is not automatically an accusation. Catastrophic committed actions may end the run, but unexpected creativity is not failure. Terminal screens are concise UI events; do not require narrated gore.

See [Failure and Caseline](FAILURE-AND-CASELINE.md).

## 7. Plant debrief hooks

Choose only a few Player Moments worth remembering: first strong deduction, optional clue, memorable wrong theory, exposed contradiction, clever request, interrogation success, difficult decision or final accusation.

Specific recognition is the reward. Do not build generic praise meters.

## 8. Package

Use the current case structure:

~~~text
cases/DA-001-case-name/
├── README.md              optional creator/player note
├── casefile.txt            portable cartridge
├── index.html              or page/index.html for the PLAY CASE page
└── evidence/
    ├── E-01.*
    ├── E-02.*
    └── E-03.*
~~~

A release Casefile begins with the exact unencoded fictional-game classification from [Content Rules](CONTENT-RULES.md), followed by a spoiler-free manifest, the compact [Runtime Kernel](RUNTIME-KERNEL.md), then sealed case-specific GM state.

The release should contain canonical evidence facts and stable asset links—not creator image prompts intended for live execution.

## 9. Run the packaging lint

Before the human fairness pass, run the small creator-side smoke test:

~~~bash
python3 tools/detectaive_lint.py cases/DA-001
~~~

It is intentionally modest. It catches packaging mistakes such as malformed/dangling evidence IDs, missing local evidence files, missing recommended accessibility fallbacks, unclear suspect public/private/disclosure grouping and obvious context-budget problems.

It does **not** decide whether the mystery is good, fair or logically solvable. It does not replace visual inspection or playtesting.

> **Let automated linting catch stupid packaging mistakes; do not let it become a new game engine.**

## 10. Fairness pass

Ask the AI to act as a hostile Case Editor, then verify the findings yourself:

- Can the intended solution be proved from available evidence?
- Can every required clue actually be reached?
- Does any deduction require mind-reading or password phrasing?
- Does the registry agree with the published asset?
- Is any required image too small or ambiguous on a phone?
- Are important suspect facts explicitly public, private or disclosure-gated?
- Can a suspect leak knowledge they should not have?
- Does the runtime preserve locked truth when challenged by an attractive wrong theory?
- Are red herrings honestly explainable?
- Does the ending account for the strange details?
- Is the fictional classification first and unencoded?
- Are all case-specific people fictional and all dangerous details non-operational?

## 11. Playtest fresh

Open a fresh ChatGPT conversation and use only what a stranger would receive.

Test Quick Start and No Companion; the intended clue route; one unexpected reasonable route; one wrong theory; natural-language paraphrases; one interrogation; one accusation; the actual evidence-page handoff on desktop and mobile; and specific Player Moment recall in the debrief.

For the next V0 tests, measure four things rather than inventing more systems:

1. CANON integrity;
2. natural-language clue recognition;
3. evidence handoff friction;
4. specific debrief memory.

The milestone is one stranger completing one case without creator coaching.

## Creation and play stay separate

Creators may use the full workshop. Players receive only the case page, release Casefile and evidence it unlocks.

The complicated part belongs to the workshop, not to the player.
