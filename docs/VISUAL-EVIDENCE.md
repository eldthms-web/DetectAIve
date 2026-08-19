# Visual Evidence Guide

This guide preserves the strongest design work from the Visual Detective prototype while adapting it to authored Casefiles.

## Central law

> **A clue needs neighbors.**

A clue by itself is an answer.

A clue surrounded by meaningless junk is a hidden-object exercise.

A clue surrounded by plausible alternative clues becomes detective play.

## Canonical storage

Keep verified evidence assets in the same GitHub case folder as the Casefile whenever possible:

~~~text
cases/DA-001-case-name/
└── evidence/
    ├── E-01.jpg
    ├── E-02.jpg
    └── E-03.jpg
~~~

GitHub provides one authoritative version history for case logic and evidence. A GitHub Pages case page may display those same assets without exposing repository navigation to the player.

External image hosts are fallbacks, not the default.

## Human observation is the V0 baseline

The player, not the runtime AI, is the primary viewer of evidence.

When an image unlocks:

1. ChatGPT names the evidence ID.
2. The player opens the canonical image on the case page.
3. The player studies it.
4. The player describes what they noticed or asks to examine something.
5. ChatGPT compares that report against the hidden evidence registry.

The Casefile already knows what the image canonically contains and means. Direct AI image analysis is optional and must not replace the verified registry.

## Story art versus evidence art

Story art may prioritize atmosphere, beauty, expression, costume and cinematic composition.

Evidence art must prioritize:

- puzzle integrity;
- readable spatial relationships;
- controlled differences;
- plausible decoys;
- fair clue visibility;
- continuity.

Beautiful but mechanically useless evidence art is a failed evidence image.

## Difficulty

### Easy

- few decoys;
- clean scenes;
- clear differences;
- low memory demand;
- one major clue may be enough.

### Medium

- several plausible candidates;
- two or three details may need combining;
- meaningful decoys;
- moderate visual memory;
- visible clues that are not emphasized.

### Hard

- partial occlusion;
- deliberate near-matches;
- misleading salience;
- memory across images;
- multi-stage inference;
- subtle but fair contradictions.

Hard must never mean microscopic pixel hunting.

The ideal hard clue is **visually available but cognitively buried**.

## Density and decoys

Do not make true clues glow, sit alone, occupy the center or become the only unusual objects.

At Medium and Hard difficulty, deliberately include candidates that match individual features. The correct answer should emerge from a combination.

## Surveillance

CCTV and security evidence should look like surveillance:

- grayscale or black and white;
- grain and low contrast;
- awkward framing;
- high or oblique angles;
- distance, rain, glare or motion;
- partial obstruction;
- ordinary concealment such as hats, hoods, glasses or scarves.

Do not present a clean portrait and call it security footage.

Identification may rely on profile, posture, gait, handedness, jewelry, scars, clothing construction or a combination of details.

## Reflections

Reflections place evidence on a secondary surface the player must discover.

Possible surfaces include glass doors, windows, mirrors, vehicle glass, puddles, polished metal and screens.

At Medium or Hard difficulty, do not announce the reflection before the player examines it.

Enhancement may reveal information already captured. It may not manufacture detail.

## Before and after

Reconstructed comparisons may ask what disappeared, appeared, moved, opened, closed or changed condition.

Differences should be controlled and relevant. Avoid accidental continuity noise.

## Canonical and derived evidence

**Canonical Evidence** is the immutable original asset.

**Derived Evidence** includes approved crops, zooms, scans, diagrams or reconstructions made from canonical material.

Derived evidence must not add facts absent from the source. When a deduction depends on enhancement, creators should preferably supply and test the derived asset in advance.

## Evidence registry writing

For each image, record:

- what is visibly present;
- observations the player may reasonably phrase in different ways;
- which facts are merely decorative;
- which deductions are permitted;
- which deduction requires another clue;
- plausible but incorrect interpretations;
- any accidental artifact declared noncanonical.

The AI may understand paraphrase. It should not demand that the player recite a password-like description.

## Verification pass

Before publication, inspect every important evidence asset:

- Is the intended clue actually present?
- Is it visible enough to be fair on a phone?
- Is the intended answer unique when required?
- Did generation remove, duplicate or distort something important?
- Are decoys plausible?
- Is the target accidentally centered or highlighted?
- Did malformed text break the puzzle?
- Does the image reveal the solution too early?
- Could an innocent interpretation remain plausible until enough evidence appears?
- Does the written CANON agree with the image?
- Do filename, thumbnail, URL and alt text avoid spoilers?

If the image fails, revise or replace it before publication.

## Accessibility

Do not hide essential instructions inside an image. Provide high-resolution originals and, where practical, an alternate text-investigation route.

If a puzzle fundamentally requires sight, label that honestly rather than pretending a spoiler-filled description is equivalent.

## Fairness standard

The desired reaction after a missed clue is:

> “Damn. I could have seen that.”

Never:

> “There was no possible way to know.”

