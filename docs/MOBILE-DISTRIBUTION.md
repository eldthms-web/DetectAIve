# Mobile-First Distribution

## Constraint

DetectAIve must remain free to publish and play.

It will not require:

- a dedicated application;
- API calls;
- paid hosting;
- user accounts beyond Reddit, GitHub and ChatGPT;
- creator-operated databases;
- downloaded software.

## Recommended player flow

~~~text
Reddit post
   ↓ tap PLAY CASE
Static case page
   ↓ tap COPY CASEFILE
ChatGPT mobile app or website
   ↓ paste and send
Investigation begins
~~~

Reddit is the social doorway. GitHub stores the canonical source. A static GitHub Pages page provides the mobile-friendly handoff.

The static page is not the game engine. It is a case card, copy button and numbered evidence folder.

## Reddit post

A mobile-friendly case post should contain:

1. short title and case ID;
2. one-paragraph premise;
3. compact manifest;
4. content warning;
5. one large **PLAY CASE** link;
6. spoiler-discussion reminder.

Do not require the player to copy the entire Reddit post.

Do not make the player locate a raw file inside a GitHub repository.

## Static case page

Each case page should provide:

- **COPY CASEFILE**;
- **OPEN CHATGPT**;
- estimated time and difficulty;
- numbered evidence panels;
- full-resolution, zoomable images;
- fallback plain-text selection if clipboard access fails;
- link back to the Reddit discussion;
- version and canonical GitHub link.

A small amount of local JavaScript may copy text to the clipboard. It requires no server, API, database or running cost.

## Evidence on mobile

Do not force players to download and upload a folder of images before play.

Recommended method:

1. The Casefile gives ChatGPT the evidence registry and hidden canonical meaning.
2. The player page keeps evidence in closed, numbered panels.
3. ChatGPT says **OPEN EVIDENCE E-01** when an item unlocks.
4. The player switches to the case page, opens E-01, zooms and examines it.
5. The player returns to ChatGPT and explains what they notice.

This keeps later evidence hidden, works without an image-hosting API and makes the web page feel like a physical case folder.

The exact interaction must be tested on both Android and iPhone before becoming part of the stable format.

## Visual design rules for phones

- Never require a desktop-sized overview to understand the scene.
- Evidence must remain legible when zoomed.
- Avoid clues that disappear under mobile image compression.
- Avoid essential text rendered inside generated images.
- Provide high-resolution originals.
- Keep buttons large and separated.
- Avoid wide code blocks and horizontal scrolling.
- Use short paragraphs and compact case manifests.
- Test dark mode and light mode.
- Do not reveal answers in filenames, thumbnails or image alt text.

Accessibility may require a creator-supplied text investigation mode. It should be labeled honestly when a puzzle is fundamentally visual.

## Copy fallback

Clipboard buttons sometimes fail because of browser permissions.

Every case page should also offer:

- a visible Casefile text box;
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

## Desktop support

The same page should work on desktop. Desktop players may keep the evidence page beside ChatGPT; mobile players switch between browser and app.

One Casefile, one page, two screen sizes.
