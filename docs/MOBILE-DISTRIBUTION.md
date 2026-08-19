# Mobile-First Distribution

## Constraint

DetectAIve must remain free to publish and play.

It will not require:

- a dedicated application;
- API calls;
- paid hosting;
- creator-operated databases;
- downloaded software.

## Platform roles

- **Reddit:** discovery, discussion and community.
- **GitHub:** canonical Casefiles, evidence assets, versions and corrections.
- **GitHub Pages:** clean player-facing case pages backed by the repository.
- **ChatGPT:** the game runtime and conversation state.

GitHub is backstage infrastructure. The player should not need to understand it.

## One-minute player flow

~~~text
Reddit or shared link
   ↓ tap PLAY CASE
Static case page
   ↓ tap COPY CASEFILE
ChatGPT app or website
   ↓ paste and send
Read Aloud tip + one office choice
   ↓
Investigation begins
~~~

The static page is not a game application. It is a case card, copy surface and numbered evidence folder.

## Preferred GitHub layout

Keep the Casefile and canonical evidence together:

~~~text
cases/DA-001-case-name/
├── casefile.txt
├── evidence/
│   ├── E-01.jpg
│   ├── E-02.jpg
│   └── E-03.jpg
└── page/
    └── index.html
~~~

GitHub Pages may publish `page/index.html` and the evidence assets without a server or API. Imgur and other image hosts are fallbacks, not the default architecture.

## Reddit post

A mobile-friendly case post contains:

1. short title and case ID;
2. one-paragraph premise;
3. compact manifest;
4. content warning;
5. one large **PLAY CASE** link;
6. spoiler-discussion reminder.

Do not require the player to copy the Reddit post or navigate a repository.

## Static case page

Each page should provide:

- **COPY CASEFILE**;
- a clear instruction to paste into ChatGPT;
- estimated time, difficulty and content information;
- numbered evidence panels;
- full-resolution, zoomable images;
- fallback plain-text selection;
- raw and downloadable Casefile links;
- link back to the Reddit discussion;
- version and canonical GitHub source link.

A small amount of local JavaScript may copy text to the clipboard. It requires no server, database, login or API expense.

## Evidence loop

Do not force players to download and upload a folder before play.

Preferred method:

1. The Casefile gives ChatGPT the hidden evidence registry.
2. The case page keeps evidence in closed, numbered panels.
3. ChatGPT says **OPEN EVIDENCE E-01** when the item unlocks.
4. The player switches to the case page, opens E-01, zooms and studies it.
5. The player returns to ChatGPT and describes what they noticed or want to inspect.
6. ChatGPT compares the report against CANON and advances the investigation appropriately.

This workflow does not depend on ChatGPT visually ingesting the image. Direct image upload remains optional.

On desktop, the player may keep ChatGPT and the case page side by side. On mobile, they switch between browser and ChatGPT. Both use the same Casefile and evidence IDs.

## Read Aloud handoff

The first runtime response briefly mentions Read Aloud. Narrative responses should end cleanly when evidence unlocks so the player can pause, inspect the asset and return without Voice-mode setup.

Do not front-load a device tutorial. Interface controls may vary. The player only needs to know that listening is an option.

## Visual design rules for phones

- Never require a desktop-sized overview to understand the scene.
- Evidence must remain legible when zoomed.
- Avoid clues that disappear under mobile compression.
- Avoid essential text rendered inside generated images.
- Provide high-resolution originals.
- Keep buttons large and separated.
- Avoid wide code blocks and horizontal scrolling.
- Use short paragraphs and compact manifests.
- Test dark mode and light mode.
- Do not reveal answers in filenames, thumbnails, URLs or alt text.

Accessibility may require a creator-supplied text investigation mode. Label honestly when a puzzle is fundamentally visual.

## Copy fallbacks

Clipboard access sometimes fails. Every case page should also offer:

- a visible Casefile text area;
- **SELECT ALL** guidance;
- a raw Casefile link;
- a downloadable plain-text or Markdown file.

The fallback must remain usable without JavaScript.

## Privacy and cost

The static page should not need:

- cookies;
- analytics;
- authentication;
- cloud functions;
- API keys;
- stored player progress.

The player's ChatGPT conversation is the game state.

## Required V0 test

Before stabilizing the format, test the entire handoff on:

- desktop browser;
- Android browser plus ChatGPT;
- iPhone browser plus ChatGPT;
- clipboard-denied fallback;
- slow connection;
- large-text accessibility settings.

One Casefile, one page, two screen sizes.

