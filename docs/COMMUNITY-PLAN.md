# Community and Distribution Plan

## Recommendation

Use three layers over time:

1. **Subreddit:** discovery, discussion, play reports and creator culture.
2. **GitHub:** canonical files, versions, evidence assets and project development.
3. **Simple catalog website:** a later player-friendly front door with case cards and copy/download actions.

Do not ask one platform to perform all three jobs.

## Subreddit role

Reddit is well suited to:

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

Reddit should not be the only canonical storage location. Posts are awkward for multi-file versioning, packaged assets and corrected releases.

## GitHub role

This repository should remain the source of truth for:

- the specification;
- templates;
- official cases;
- stable case IDs and versions;
- change history;
- corrected evidence;
- issue tracking;
- creator contributions;
- downloadable releases.

GitHub is excellent backstage infrastructure but unfamiliar to many players. Public instructions should link directly to the exact Casefile or download rather than telling newcomers to navigate branches and folders.

GitHub Discussions may support creator design conversations, but it should not replace the player-facing community unless the audience naturally moves there.

## Catalog website

A small static website can eventually provide:

- Play and Create entrances;
- filters for time, difficulty and content;
- case cards;
- one clear copy or download action;
- tested-interface badges;
- links to subreddit discussion;
- links to canonical GitHub versions.

This does not require an application or database. It can be generated from the same repository after the format stabilizes.

Do not build it before at least several cases have exposed what the catalog actually needs.

## Mobile-first delivery

Reddit should send players to one mobile-friendly static case page rather than asking them to copy a long post or navigate GitHub.

The intended handoff is:

~~~text
Reddit → PLAY CASE → COPY CASEFILE → ChatGPT
~~~

The case page may also hold closed, numbered evidence panels. ChatGPT instructs the player which evidence ID to open, and the player returns with their observation. This requires no API or dedicated application.

See [Mobile-First Distribution](MOBILE-DISTRIBUTION.md).

## Case posting pattern

A subreddit case post should contain:

- spoiler-free title;
- case manifest;
- short premise;
- evidence preview that does not reveal answers;
- one obvious PLAY / GET CASEFILE link;
- content warnings;
- version number;
- discussion rules.

The complete canonical package should live in GitHub or a release download.

## Spoiler infrastructure

- Titles never contain solutions.
- Discussion uses spoiler tags.
- Solution and creator commentary are separated from the player package.
- Screenshots must not expose answers.
- Updated cases keep stable IDs and increment versions.
- Broken evidence is corrected visibly, not silently.
- Wrong theories are celebrated as play stories rather than treated as failure.

## Multi-part cases

Optional later structures may include:

- Part I and Part II;
- locked evidence annexes;
- dedicated interrogation packets;
- follow-up cases;
- alternate lead branches;
- creator commentary;
- solution breakdowns.

A simple standalone Casefile remains the default.

## Other platforms

Discord may be useful for live collaboration but is a poor canonical archive and discovery surface.

Itch.io may become a useful mirror if cases are distributed as polished downloadable packages, but it should not define the format.

A dedicated web application is explicitly deferred.
