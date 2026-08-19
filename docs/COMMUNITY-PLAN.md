# Community and Distribution Plan

## Recommendation

Use three layers:

1. **Subreddit:** discovery, discussion, play reports and creator culture.
2. **GitHub:** canonical Casefiles, evidence assets, versions and project development.
3. **GitHub Pages:** free player-facing case pages with copy and evidence controls.

Do not ask one platform to perform all three jobs.

## Two entrances

The community should make two intentions immediately obvious:

- **PLAY A CASE**
- **MAKE A CASE**

A player should not land in a specification. A prospective creator should not have to reverse-engineer a finished Casefile.

## Subreddit role

Reddit is suited to:

- discovering new cases;
- browsing by flair;
- image previews;
- theories and play reports;
- creator commentary;
- community playtests;
- highlighting official cases;
- finding collaborators.

Recommended early flairs:

- OFFICIAL CASE;
- COMMUNITY CASE;
- PLAYTEST;
- CREATOR HELP;
- CASE CLOSED / SPOILERS;
- OFFICE SHOWCASE;
- WILDEST WRONG THEORY.

Reddit should not be the canonical file host. Posts are awkward for corrected releases, multi-file cases and stable evidence URLs.

## GitHub role

This repository should remain the source of truth for:

- the specification and creator guide;
- templates;
- official cases;
- stable case IDs and versions;
- canonical evidence images;
- change history and corrections;
- creator contributions;
- downloadable releases.

Keep each case's logic and evidence together. Imgur or other image hosts are fallbacks rather than the default architecture.

GitHub is excellent backstage infrastructure but unfamiliar to many players. Public links should lead directly to a case page, not to branches and folders.

## GitHub Pages role

A static case page can provide:

- case card and manifest;
- **COPY CASEFILE**;
- raw/download fallback;
- closed numbered evidence panels;
- full-resolution images;
- Reddit discussion link;
- canonical version link.

It requires no API, user account, database or creator-operated server.

A broader searchable catalog may come later, after several cases reveal what filters are actually needed.

## Player handoff

~~~text
Reddit → PLAY CASE → COPY CASEFILE → ChatGPT
~~~

After paste, the runtime mentions Read Aloud, asks one office question and begins. When evidence unlocks, the player returns to the same page, opens the numbered asset and tells ChatGPT what they noticed.

See [Mobile-First Distribution](MOBILE-DISTRIBUTION.md).

## Creator handoff

The creator entrance should point to the [AI-Assisted Creator Guide](CREATOR-GUIDE.md) and a future blank template.

The basic promise is:

> Load the creator material into your AI and say **Help me make a case.**

The AI assists with formalization and QA. The human creator retains authority over canon.

## Case posting pattern

A subreddit case post should contain:

- spoiler-free title;
- case manifest;
- short premise;
- evidence preview that does not reveal answers;
- one obvious **PLAY CASE** link;
- content warnings;
- version number;
- discussion rules.

The complete canonical package lives in GitHub.

## Spoiler infrastructure

- Titles never contain solutions.
- Discussion uses spoiler tags.
- Solution and creator commentary are separated from the player package.
- Screenshots must not expose answers.
- Updated cases keep stable IDs and increment versions.
- Broken evidence is corrected visibly, not silently.
- Wrong theories are celebrated as play stories rather than treated as failure.

## Multi-part cases

Optional later structures may include Part I and Part II, locked evidence annexes, dedicated interrogation packets, follow-up cases, alternate lead branches, creator commentary and solution breakdowns.

A simple standalone Casefile remains the default.

## Other platforms

Discord may help live collaboration but is a poor canonical archive and discovery surface.

Itch.io may become a useful mirror for polished downloadable packages, but it should not define the format.

A dedicated web application is explicitly deferred.

