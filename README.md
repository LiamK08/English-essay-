# 📖 Essay Memoriser — *The Curious Incident of the Dog in the Night-Time* (Module B)

A browser **game** for memorising your Module B essay word-for-word, because flashcards are boring.
It's built around a **science-backed 3-Day Coach** that tells you exactly what to practise and when — plus a ladder of practice modes and a timed **exam** that marks you word-by-word.

## 🧭 The 3-Day Coach (start here)
The Coach splits the essay into ~65 bite-size lines and drills each one with **recall + feedback**, spaced out and revisited until it sticks — the method researchers call **successive relearning**. It implements retrieval practice, spacing, Read–Recite–Review (with reciting **aloud**), errorful generation, chunking + chaining, interleaving and overlearning. Tap **“Why this works”** in-app for the citations, or read [`RESEARCH.md`](RESEARCH.md).

- **Day 1** — encode every line (read → say aloud → recall with feedback).
- **Day 2** — spaced retrieval, rehearse sentence joins, interleave paragraphs.
- **Day 3** — overlearn & simulate: first-letter recitation, then timed exam write-outs.

It schedules reviews at expanding intervals and nudges you to **space sessions and sleep between them** (that's what makes 3 days work). Just open it and press **▶ Start session**.

> The **Quote Bank** is intentionally left out (as requested). Only the five prose paragraphs are loaded:
> **Introduction · Body 1 (Perception) · Body 2 (Truth) · Body 3 (Agency) · Conclusion.**

## ▶️ How to play

**Right now (any device):** open **`index.html`** in a browser. It works **offline** and needs no install.

**On your phone (recommended):** host it free with GitHub Pages, then add it to your home screen as an app:
1. On GitHub: **Settings → Pages → Build and deployment → Source: “Deploy from a branch” → Branch: `main` / `/ (root)` → Save.**
2. Wait ~1 min, then open the link GitHub shows (e.g. `https://liamk08.github.io/english-essay-/`).
3. In the browser menu choose **“Add to Home Screen”** — it installs as a real, offline app with its own icon.

Your XP, levels, streak, best scores and weak-words list all save automatically on the device (`localStorage`).

## 🎮 The modes (recommended order)

| # | Mode | What it does |
|---|------|--------------|
| 1 | 📖 **Study** | Reads the paragraph nicely, highlights quotes, can read it **aloud**, marks the `[adaptable]` hook/concept parts. |
| 2 | 🕳️ **Fill the Gaps** | Type the missing words. **Easy → Medium → Hard → Expert** (Expert blanks *everything*). Correct words turn green and auto-advance. |
| 3 | 🔤 **First Letters** | Every word shrinks to its first letter (`H····· e····· t···`). Recite it, tap any word to check. |
| 4 | ⌨️ **Type It Out** | Write the whole paragraph from memory with **shrinking hints** (full words → first letters → nothing). Wrong words flash the answer. Live accuracy, WPM, combo. |
| 5 | 🧩 **Unscramble** | Rebuild each sentence from shuffled word tiles. |
| ★ | 📝 **Exam** | The real test: write it under a **timer with no hints**, then get a **word-accurate report** — green = correct, red = missed/out of place. |
| 🎯 | **Weak Words** | Auto-collects every word you slip up on (in Gaps/Type/Exam) and re-drills it in context. Spaced, targeted practice. |

There's also a 👑 **Whole Essay** option — chain all five paragraphs for the ultimate Type-It-Out or Exam.

## 🏆 Game layer
- **Smart dashboard**: overall % memorised, a “Continue / Start” button that sends you to your weakest paragraph and the right next mode.
- **XP & levels**, **🔥 daily streak**, **combo meter**, **per-paragraph mastery rings** (100% requires acing Type It Out / Exam).
- Confetti on 90%+, optional sound effects, installable **PWA** that works fully offline.

## 💡 Tips for memorising fast
1. **Study → Easy gaps**, then climb to Expert on one paragraph.
2. Switch to **First Letters** and recite **aloud** — saying it sticks far better than reading.
3. **Type It Out**, cycling the hint down to *none*.
4. Run the **Exam**, then hit **🎯 Drill misses** to mop up the red words.
5. One paragraph a day; keep the streak alive so all five stay warm.

---
*Files: `index.html` (the whole game, self-contained), plus `manifest.webmanifest`, `sw.js` and icons for offline install. No dependencies, no tracking.*
