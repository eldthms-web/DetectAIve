# Draft Casefile Format

**Status:** structural draft for playtesting.

A Casefile is the portable cartridge a player pastes into ChatGPT. It contains one case's runtime instructions and locked game state; it is not the full creator repository.

## Release order

Every release Casefile begins in this order:

1. exact plain-language fictional-game classification from [Content Rules](CONTENT-RULES.md);
2. spoiler-free manifest;
3. current compact [Runtime Kernel](RUNTIME-KERNEL.md);
4. sealed case-specific GM packet.

The runtime must not have to reconstruct shared behavior by reading the entire repository.

## Case folder

Preferred V0 layout:

~~~text
cases/DA-001-case-name/
├── README.md          optional note/source pointer
├── casefile.txt
├── index.html         or page/index.html
└── evidence/
    ├── E-01.*
    ├── E-02.*
    └── E-03.*
~~~

The player receives a direct **PLAY CASE** link. They should not navigate GitHub folders.

## Manifest

Keep it compact and spoiler-free. Recommended fields:

~~~text
CASE ID: DA-001
TITLE: The Empty Platform
VERSION: 0.1
CREATOR: Name
STATUS: Playtest
FORMAT VERSION: DetectAIve 0.1
MODE: Locked Mystery
SETTING: Contemporary fictional city
DIFFICULTY: Medium
ESTIMATED TIME: 8–12 minutes
EVIDENCE ITEMS: 3
CANONICAL EVIDENCE: Pregenerated/creator-supplied and verified
PLAYER INTERFACE: Text + optional Read Aloud
EVIDENCE DELIVERY: GitHub Pages
VOICE DEBRIEF: Available / None
VOICE INTERROGATION: None / Experimental
OFFICE COMPATIBILITY: Universal
CONTENT: Theft; no death
GORE: None
CHATGPT TESTING: Untested
~~~

Do not ask the player to reconfigure fields already established here.

## Sealed GM packet

The sealed packet contains immutable case-specific CANON: true explanation, timeline, motive/means/opportunity, suspect and witness state, evidence registry, state transitions, success/failure conditions, hints and debrief hooks.

Base64 worked as spoiler-resistant transport in Alpha A01. It is obfuscation, not security, and the stable representation remains subject to testing. Do not place creator-time image-generation prompts in the release packet for runtime execution.

## Evidence registry

Each canonical evidence item should define enough for the runtime to identify the asset, gate it and judge natural-language observations:

~~~text
EVIDENCE ID:
TITLE:
SOURCE PATH / PLAYER URL:
UNLOCK CONDITION:
CANONICAL CONTENTS:
ACCEPTED OBSERVATIONS:
PERMITTED DEDUCTIONS:
MISLEADING APPEARANCES: optional
ACCESSIBILITY FALLBACK: recommended
VERIFICATION STATUS:
RUNTIME GENERATION: Prohibited for canonical evidence
~~~

Use canonical two-digit evidence IDs such as `E-01`, `E-02`, `E-03` consistently in the registry and all cross-references.

The player is the primary viewer. ChatGPT judges their report against the registry. Accepted observations are semantic, not passwords. If a report is too vague to establish a clue, ask a natural clarifying question rather than silently granting or denying it.

`ACCESSIBILITY FALLBACK` is recommended for every evidence item but is not currently a launch-blocking requirement. It should provide an equivalent text investigation route without stating the deduction or culprit for the player. A fundamentally visual puzzle may instead be labeled honestly as such.

If the player uploads an image, AI analysis may discuss visible details but cannot override creator-verified CANON. Any derived evidence required for a deduction—crop, zoom, scan, comparison or reconstruction—must also exist and be verified before publication.

## Suspect and witness packets

V0 does **not** require every suspect to have an identical field set. Innocent bystanders do not need a culprit-sized interrogation dossier.

The runtime does need an explicit information boundary. The recommended packet pattern is:

~~~text
NAME / ROLE:
STATUS: hidden canonical truth
PUBLIC: safe to present before investigation
PRIVATE: hidden canonical facts used by the runtime
DISCLOSURES: optional gated facts with explicit reveal conditions
INTERROGATION: optional state packet
~~~

A JSON-shaped example:

~~~json
{
  "name": "Nolan Pierce",
  "role": "night security supervisor",
  "status": "culprit",
  "public": "Claims he remained at the east stairwell.",
  "private": {
    "appearance": "Pale vertical scar through right eyebrow.",
    "boots": "Issued hexagonal-tread security boots."
  },
  "disclosures": [
    {
      "id": "scar_match",
      "fact": "Nolan has the matching eyebrow scar.",
      "reveal_when": "after E-02 if the player notices the scar or asks for suspect comparison"
    }
  ],
  "interrogation": {
    "claims": [],
    "lies": [],
    "pressure": [],
    "breakpoint": "...",
    "after_breakpoint": "..."
  }
}
~~~

`PUBLIC` is safe to narrate when the suspect is introduced. `PRIVATE` does not become player knowledge merely because it exists in the capsule. `DISCLOSURES` make important gated revelations explicit instead of relying on vague runtime prose. The disclosure may point to a private field or simply contain the fact to reveal.

Interrogation packets may contain only the state that person actually needs: knows, believes, claims, lies, pressure/contradictions, breakpoint and after-breakpoint behavior. Dialogue wording is FLEX; knowledge, disclosure gates and breakpoint logic are CANON.

## State and commitment

The case defines which discoveries permit investigation, interrogation, accusation, resolution, failure and debrief transitions.

A theory is not automatically a formal accusation. Clarify only genuinely ambiguous commitment. Creative off-path play is not failure; rare terminal failure requires a case-consistent committed cause.

## Player Moments

Track only a small dynamic set useful for specific debrief recognition, such as first useful observation, optional clue, memorable wrong theory, exposed contradiction, difficult decision and final accusation. Do not store an uncontrolled biography.

## Voice

Text interrogation is the V0 baseline. Voice interrogation is case-specific and experimental.

When a post-case Voice debrief is available, the runtime uses actual Player Moments to create a compact portable handoff. The tested workflow is: copy the complete handoff, start Voice Mode, then paste/send that block once Voice is active. The debrief must also work in text.

See [Voice and Interrogation](VOICE-AND-INTERROGATION.md).

## Failure

The packet distinguishes nonterminal consequences, irreversible actions, terminal triggers and ambiguous commitments. Terminal presentation is concise and non-graphic; `DESYNCHRONIZED FROM THE CASELINE` remains the preferred reality-breaking phrase.

A failed run does not automatically reveal the solution or advertise a retry/retcon.

## Release rule

The creator source may be extensive. The release Casefile should remain compact, obvious and versioned.

Do not include unused dialogue libraries, rejected brainstorming, the full project manual or live canonical-evidence prompts. Do not encode or omit the required fictional-game classification.
