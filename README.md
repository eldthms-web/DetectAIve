# DetectAIve

> **Paste a case. Solve it with ChatGPT.**

**What if a mystery was something you could simply paste into ChatGPT and play?**

DetectAIve is a format for community-made detective games. There is no game client to download, no API bill and no dialogue tree to outguess.

A creator builds a fixed mystery with suspects, visual evidence, secrets, red herrings and a real solution. A player copies the Casefile into ChatGPT. ChatGPT becomes the game master, and the player investigates in ordinary language.

Ask to examine the chair. Compare two photographs. Question a witness about an inconsistency. Follow a completely different lead because something in the crime-scene image bothered you.

**You say what you would actually do, and the mystery responds.**

## Play a case

The intended V0 experience is:

1. Find a case on Reddit or through a shared link.
2. Select **PLAY CASE**.
3. Select **COPY CASEFILE**.
4. Paste it into ChatGPT.
5. Read normally or use Read Aloud.
6. Open numbered evidence images when instructed.
7. Tell ChatGPT what you noticed and continue investigating.
8. Solve the mystery and optionally return to the office for a debrief.

The player should be investigating within roughly one minute. They should not need to understand repositories, prompts, evidence registries or runtime state.

See [Play DetectAIve in Sixty Seconds](QUICKSTART.md).

## Who works in your office?

After the Casefile is pasted, ChatGPT asks one question:

> **Who works in your office?**

Quick-start with an invented detective, build a custom office, ask for a surprise cast or play without a companion. Then the case begins.

The office gives the investigation a recurring human frame. Its characters may help, disagree, offer hints and return after the case for a debrief. They may not change the culprit, evidence or solution.

## Study the evidence

Canonical evidence images are generated, inspected and locked by the creator before publication. They live with the case on GitHub and appear on a simple player-facing case page.

> **If an image can change the solution, generate and verify it before play.**

When ChatGPT says **OPEN EVIDENCE E-02**, the player opens that image, studies it and reports what they noticed. The Casefile already contains the hidden evidence registry, so ChatGPT can judge the observation without having to re-analyze every image itself.

Direct image upload and AI image analysis may still be offered as optional enhancements. They are not required for the normal V0 loop.

Runtime image generation is reserved for noncanonical material such as office portraits, mood pieces and post-case rewards. A live-generated image may decorate the experience; it may not become evidence merely because it appeared during play.

## A fair mystery

In a proper DetectAIve case, the culprit and evidence are fixed before play begins.

A persuasive theory does not become true because ChatGPT likes it. You can be clever. You can be wrong. You can miss optional evidence, accuse an innocent person, follow a false lead or notice something the creator expected almost nobody to catch.

**The route may change. The truth may not.**

## After the case

DetectAIve can remember a few specific Player Moments:

- the first clue you noticed;
- an optional detail you caught;
- an amusing but plausible wrong theory;
- a contradiction you exposed;
- a difficult decision you made;
- something another player might easily have missed.

Those moments shape an optional office debrief, Voice conversation, epilogue or reward image.

Specific recognition is the reward. DetectAIve does not need affection meters, experience points or generic praise spam.

## Make a case

DetectAIve is also a creator system for people who do not know programming.

Load the creator guide into your AI and say:

> **Help me make a case.**

The AI can help turn an idea into locked canon, suspects, timelines, interrogation logic, visual puzzles, creator-time evidence prompts, failure conditions and a portable Casefile. Conceptually, it is a very lightweight RPG Maker for mysteries.

**The creator authors reality. The AI helps formalize it. The player authors the investigation.**

See the [AI-Assisted Creator Guide](docs/CREATOR-GUIDE.md).

## Current scope

DetectAIve is currently a **ChatGPT-first experimental format**.

The normal V0 interface is:

- **Text** for the game;
- **Read Aloud** for optional narration;
- **Images** for evidence;
- **Voice** primarily for an optional earned post-case debrief.

Live Voice interrogation remains experimental. Compatibility with other AI systems is not promised until tested.

We are deliberately not building a dedicated application. The experiment is whether one person can make a fair text-and-image Casefile, give it to another person, and have that person play it through the AI they already use.

## Project documents

### Play

- [Play in sixty seconds](QUICKSTART.md)
- [Runtime player onboarding](docs/PLAYER-ONBOARDING.md)
- [Office and debrief system](docs/OFFICE-AND-DEBRIEF.md)
- [Mobile-first case delivery](docs/MOBILE-DISTRIBUTION.md)

### Create

- [AI-assisted creator guide](docs/CREATOR-GUIDE.md)
- [Draft Casefile format](docs/CASE-FORMAT.md)
- [Visual evidence guide](docs/VISUAL-EVIDENCE.md)
- [Read Aloud, Voice and interrogation guide](docs/VOICE-AND-INTERROGATION.md)
- [Failure and Caseline system](docs/FAILURE-AND-CASELINE.md)
- [Fiction classification and creator content rules](docs/CONTENT-RULES.md)
- [Data and context budgets](docs/DATA-BUDGETS.md)

### Project

- [Architecture](docs/ARCHITECTURE.md)
- [Community and distribution plan](docs/COMMUNITY-PLAN.md)
- [Terminology](docs/GLOSSARY.md)
- [Roadmap](ROADMAP.md)
- [Decision log](DECISIONS.md)

## Safety boundary

DetectAIve cases are fictional.

Do not use the format to accuse real private people, crowdsource active investigations, identify strangers from social-media photographs, dox anyone, or present AI deduction as evidence of real guilt.

Every release Casefile begins with a plain-language fictional-game classification before any encoded GM state. The classification establishes context; it does not override applicable safety requirements or require the runtime to provide dangerous operational detail.

Professional knowledge is welcome. Internet vigilantism is not.

---

**Make authorship powerful. Make play effortless.**
