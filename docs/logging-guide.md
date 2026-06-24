# Logging Guide: How to Keep a Record That Holds Up

This is the practical companion to the [`incident-log-template.md`](incident-log-template.md).
The template tells you the columns; this tells you how to fill them so the record stays
credible — to a future reader who wasn't there, and to you on a day when the dread is loud.

No single entry is the case. The dated aggregate is the case. Every habit below exists to
protect that aggregate.

---

## 1. Log at the time it happens

Memory degrades and reshapes within hours. An entry written that evening is already weaker
than one written in the moment; an entry written "sometime that week" is close to unusable
because the date and time are vague, and vague time is what gets a record dismissed.

Keep entry friction near zero: a note on your phone, a voice memo you transcribe later, a row
in `incidents.csv`. Capture the date, time, and the bare facts first. You can clean up wording
afterward — but the timestamp and the raw observation should be recorded while they're fresh.

---

## 2. Facts and inference are two different columns — and why

The log has `what_happened_factual` and `my_inference` as **separate** columns on purpose.

- **Facts are what HR, police, and lawyers can use.** They act on observable, datable events,
  not on conclusions about why. A fact column full of clean observations is a record an
  outsider can verify and act on.
- **Inference is for you.** It's where your read of the situation lives — and keeping it in
  its own column turns it into a self-honesty check. Over weeks you can look back and ask:
  are the facts bearing the inferences out, or are the inferences running ahead of the facts?

Both readings matter. If facts and inferences track together, you're building a case. If the
inference column is full and the fact column is thin, that gap is itself a signal worth
paying attention to (see the honesty check in [`scoring.md`](scoring.md)).

The discipline is simple: **never let an inference leak into the facts column.**

---

## 3. Write the facts column like a camera

A camera records what is in front of it. It does not record intent, motive, or "again." Write
the same way: observable, specific, neutral.

| Inference-loaded (don't) | Camera-style (do) |
|---|---|
| "They broke in again to mess with me" | "Front deadbolt found unlocked at 08:05; I locked it at 22:30 the night before" |
| "She deliberately cut me out of the meeting" | "Not on the invite for the 14:00 planning meeting I attended last week" |
| "He was following me, obviously" | "Same person behind me from the lot to the lobby, ~4 min" |

Rules of thumb:

- **No intent words.** Drop "deliberately," "to provoke me," "obviously," "again."
- **Numbers over adjectives.** Times, durations, counts, distances.
- **One event per row.** If two things happened, that's two rows.
- The "again" you want to write belongs in the *aggregate*, not the entry — the dated stack
  is what proves recurrence, not the word.

The inference ("possible entry," "feels targeted") goes in `my_inference`, where it's
honest and useful and can't undermine the fact.

---

## 4. Severity 1–5

Tag every row with a severity so the aggregate can be measured. Use the scale defined in
[`scoring.md`](scoring.md) — don't invent your own. In short: 1 is friction that may be
nothing, 3 is a clear, documentable boundary issue, 5 is safety/criminal. Score the **event
as a camera would see it**, not how heavy it felt in the moment; the trend across many honest
scores is more telling than any single inflated one.

If you're unsure between two numbers, pick the lower and note why in `my_inference`.
Consistent scoring is what makes the weekly trend meaningful.

---

## 5. Evidence discipline

The `evidence_ref` column points to the artifact, not the artifact itself. Keep it specific:

- **Screenshots** with the timestamp and URL visible in-frame. A cropped screenshot with no
  date or source is weak; capture the clock and the address bar.
- **Photos** with a filename you can find again (e.g. `photo_deadbolt_0805.jpg`). Phone photos
  carry their own timestamp metadata — don't strip it.
- **Report numbers** when you've filed (e.g. a police report number). Put the number in
  `report_id` and reference it here too.
- **"none" is an honest answer.** Most friction-level events have no artifact, and writing
  "none" is correct — far better than implying evidence you don't have. A column full of
  honest "none"s alongside a rising count is itself information (again, see the honesty check
  in [`scoring.md`](scoring.md)).

Store the actual files somewhere stable and back them up. The log is the index; don't let the
files it points to disappear.

---

## 6. Witnesses

If someone else saw or heard it, note who in `witnesses` — even just a first name or a role
("building manager," "coworker at the next desk"). A second person who can corroborate a
single event is worth more than ten unwitnessed entries. If there were no witnesses, leave it
blank or write "none"; don't pad it.

---

## 7. Why the dated aggregate beats any single entry

Each layer's actors defend themselves with *"that's normal,"* and any one entry, read alone,
usually is. The person who stared once experienced one forgettable moment; you experienced the
tenth one this week. No single actor in any layer can see the stack — which is exactly why the
stack is the most important thing you have.

That's the whole purpose of logging this way: you're not trying to win an argument about one
event. You're building a dated, neutral, cross-layer timeline so that recurrence and trend
become visible and measurable. Run [`score.py`](../score.py) over the log to turn it into a
weekly Aggregate Exposure Index, and when one layer dominates or severity climbs, take it to
the right channel via [`escalation.md`](escalation.md).

One log. Every layer. One timeline.
