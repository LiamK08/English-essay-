# 📖 Essay Memoriser — *The Curious Incident of the Dog in the Night-Time* (Module B)

A little browser **game** for memorising your Module B essay word-for-word, because flashcards are boring.
Pick a paragraph, then climb a ladder of modes that hide a bit more each time — until you can write the whole thing from memory.

> The **Quote Bank** is intentionally left out (as requested). Only the five prose paragraphs are loaded:
> **Introduction · Body 1 (Perception) · Body 2 (Truth) · Body 3 (Agency) · Conclusion.**

## ▶️ How to play

**Easiest:** just double-click **`index.html`** — it opens in any browser (phone or laptop), works **offline**, and needs no install.

Your XP, levels, streak and best scores save automatically in the browser (via `localStorage`).

### Optional: play it online from your phone
Host it free with GitHub Pages:
1. Push this repo to GitHub.
2. Repo **Settings → Pages → Build from branch → `main` (root)**.
3. Open the link it gives you on your phone and bookmark it to your home screen.

## 🎮 The five modes (recommended order)

| # | Mode | What it does | Best for |
|---|------|--------------|----------|
| 1 | 📖 **Study** | Reads the paragraph nicely, highlights quotes, can read it **aloud**, and marks the `[adaptable]` hook/concept parts you swap per question. | First contact |
| 2 | 🕳️ **Fill the Gaps** | Type the missing words. Four difficulties — **Easy → Medium → Hard → Expert** (Expert blanks *everything*). Correct words turn green and auto-jump to the next blank. | Building recall |
| 3 | 🔤 **First Letters** | Every word shrinks to its first letter (`H····· e····· t···`). Recite it, tap any word you blank on to check. | Mid-stage drilling |
| 4 | ⌨️ **Type It Out** | The boss battle. Write the whole paragraph from memory with **shrinking hints** (full words → first letters → nothing). Live accuracy, WPM and combo. | Proving you know it |
| 5 | 🧩 **Unscramble** | Rebuild each sentence from shuffled word tiles. | Locking in sentence order |

There's also a 👑 **Whole Essay** card — chain all five paragraphs together for the ultimate Type-It-Out / First-Letters test.

## 🏆 Game bits
- **XP & levels** for every round you finish (harder modes = more XP).
- **🔥 Daily streak** — come back each day to keep it alive.
- **Combo meter** for consecutive correct words.
- **Mastery %** ring on each paragraph card. To hit 100% you have to ace **Type It Out** — gaps/first-letters cap lower on purpose.
- Confetti when you smash 90%+. 🎉

## 💡 Tips for memorising fast
1. **Study → Easy gaps** on one paragraph until green, then go Medium/Hard/Expert.
2. Switch to **First Letters** and recite aloud — saying it out loud sticks far better than reading.
3. Finish with **Type It Out**, cycling the hint button down to **none**.
4. Do **one paragraph a day**, then use the streak to keep all five warm.
5. The dotted-italic `[bits]` are the only parts you change per question — memorise a default version, but know they flex.

---
*Single self-contained `index.html` — no dependencies, no tracking, fully offline. Built to make a boring task slightly less boring.*
