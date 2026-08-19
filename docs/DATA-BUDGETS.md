# Data and Context Budgets

## Repository size is not Casefile size

The DetectAIve repository may contain many documents, cases, images, archives and creator references.

A player should never paste the entire repository into ChatGPT.

A release Casefile contains only:

- the compact runtime kernel;
- one case's CANON;
- its clue and evidence registry;
- relevant suspect packets;
- state transitions;
- optional Voice and debrief hooks.

It does not need prompts whose only purpose is to regenerate canonical evidence during play. Those prompts remain in creator source; the Casefile carries stable asset IDs, links and the verified evidence registry.

Large reference libraries belong in the repository, not in every case.

## Current measurements

Measured on 2026-08-19:

| Material | Words | Characters | Rough tokens |
|---|---:|---:|---:|
| Original Visual Detective prototype | 6,805 | 44,355 | about 9,000–11,000 |
| Active organized documentation, excluding archive | 5,693 | 38,013 | about 7,500–9,500 |
| Entire repository documentation, including duplicated archive | 12,498 | 82,368 | about 16,500–20,500 |

Token counts are estimates. Tokenization varies by model and content. Emoji, ASCII art and unusual formatting may consume more tokens than ordinary prose.

The original Gist is not technically enormous. It became organizationally wrong before it became mechanically too large.

## Design budget for one playable case

Recommended v0.x targets:

| Component | Target |
|---|---:|
| Runtime kernel | 1,000–2,500 tokens |
| Case CANON and timeline | 2,000–4,000 tokens |
| Clues, evidence and state rules | 1,000–2,500 tokens |
| Suspect/interrogation packets | 1,000–2,500 tokens |
| Voice and debrief hooks | 500–1,500 tokens |
| **Typical complete micro-case** | **5,000–10,000 tokens** |

### Review thresholds

- **Under 10,000:** healthy target for a micro-case.
- **10,000–15,000:** acceptable when complexity earns it.
- **15,000–20,000:** mandatory compression and playtest review.
- **Over 20,000:** split the case or justify every section.
- **Over 30,000:** no longer a micro-case; packaging and retention risk are serious.

These are reliability budgets, not claimed ChatGPT platform limits.

## Why headroom matters

The initial Casefile is only the beginning.

The same conversation must still hold:

- player actions;
- investigation narration;
- evidence discussion;
- interrogations;
- Voice turns or transcripts;
- Player Moments;
- resolution;
- debrief.

A prompt may fit technically and still perform poorly if it buries important rules or leaves too little working room for play.

## Compression rules

Prefer:

- stable IDs;
- compact field names;
- one canonical statement of each fact;
- tables for repeated structures;
- short runtime rules;
- case-specific packets only;
- external image assets;
- creator-time image prompts kept outside the runtime capsule;
- referenced optional annexes opened when unlocked.

Remove:

- marketing copy from the playable payload;
- creator explanations;
- repeated examples;
- the full trope library;
- unrelated genre possibilities;
- archived prototype language;
- documentation intended only for authors;
- prompts for evidence images that have already been generated and published.

## Split before bloating

If a case grows, separate:

- Part I and Part II;
- evidence annex;
- interrogation annex;
- follow-up Casefile;
- creator commentary;
- solution/postmortem document.

The public package should remain obvious even when the authoring source becomes complex.

## Transfer between AI systems

File size and context size are different constraints.

A system may accept a large file but retrieve only parts of it, summarize it, truncate content or give less attention to instructions buried in the middle.

Therefore portable Casefiles should be tested by behavior:

1. Does the runtime preserve CANON?
2. Can it locate required clue rules?
3. Does it prevent premature evidence?
4. Does interrogation state survive several turns?
5. Does failure trigger only when justified?
6. Can it still perform the debrief accurately?

Passing one test prompt is more meaningful than merely confirming that the file uploaded.
