# Billy Elliot Recall

An active-recall trainer for the **Common Module shell essay** on Stephen Daldry's *Billy Elliot* — Texts and Human Experiences, Paper 1 Section II.

It holds all 55 pieces of the essay: **9 quotes and scenes, 9 technique sets, 18 evaluation bullets, 6 Turns and Closes, and the shell sentences** — and drills each one until you can produce it from memory.

Open **`index.html`** in any browser. It works offline, saves your progress on the device, and installs to a phone home screen.

## How it decides you know something

A line counts as learnt after **three correct recalls spread across separate sittings** — not three in a row tonight. Between recalls it schedules the line at widening gaps (9 min → 55 min → 5 h → 1 day → 3 days), which is the part that makes it survive to the exam rather than to bedtime. Reviews are pulled across paragraphs rather than one paragraph at a time, so Body 2's techniques stop leaking into Body 1.

The reasoning behind the whole plan — what to learn word for word, what to leave flexible, the traps in this particular essay, and what to do on each of the three days before the exam — is in [`MEMORISE.md`](MEMORISE.md), and in the app under **The method**.

## The modes

| Mode | What it does |
|---|---|
| **Coach** | One spaced session. Picks what's due, mixes the paragraphs, drills each line to criterion. Start here. |
| **Drill** | Pick a paragraph and a layer — quotes, techniques, evaluations, Turns and Closes — and hammer just that. |
| **Read** | The whole shell, annotated in the doc's own colours, with read-aloud. |
| **Sort** | Which piece of evidence does this technique belong to? Targets the four confusions in this essay. |
| **First letters** | Turns, Closes and shell sentences shrink to initials. Recite aloud, tap any word to check. |
| **Blurt** | Write a whole paragraph from the cues alone, then check every component off against the model. |
| **Adapt** | A real question stem plus your six red clauses. Rewrite each to answer it; your versions are saved. |
| **Exam** | 40 minutes, a real stem, no cues — marked against every quote, technique and evaluation. |
| **Weak lines** | Everything you've slipped on, hardest first. |
| **The method** | The analysis: tiers, traps, the spine, the order, the research. |

Typing is marked word by word and **forgives small typos** — the point is whether you retrieved the line, not whether you can spell "cacophony" at speed. Technique answers are checked term by term; evaluation clauses are marked on the key ideas, since you're meant to join and bend those on the day.

## The colour key

Straight from the source document, and used throughout the app:

- <span style="color:#456D1D">**Green**</span> — fixed theme wording, never changes.
- <span style="color:#A82C23">**Red**</span> — adapt to the question. Don't memorise these; rehearse rewriting them.
- <span style="color:#9C6608">**Amber**</span> — the Turn.
- <span style="color:#215B93">**Blue**</span> — the Close.

## Put it on your phone

1. On GitHub: **Settings → Pages → Source: "Deploy from a branch" → Branch: `main` / `/ (root)` → Save.**
2. Open the link GitHub gives you (e.g. `https://liamk08.github.io/english-essay-/`).
3. Browser menu → **Add to Home Screen**. It installs as an offline app.

Progress lives in `localStorage` on that device.

---
*`index.html` is the whole app, self-contained. No dependencies, no tracking, no network calls.*
