# Layered Security: The Local-Knowledge Problem

A framework for the kind of harm that no single person admits to causing — because
each person can only see their own layer, judges their own conduct in isolation,
and sincerely calls it normal.

---

## The thesis

Serious harm to a person is rarely one big act. More often it's distributed across
**layers** — work, neighborhood, home, public space, institutions — where each actor:

1. **Has only local knowledge.** They see their own slice and nothing else.
2. **Judges their conduct in isolation.** "I just looked away." "I just didn't reply."
   "I just made a joke." Each act is defensible *alone*.
3. **Calls it normal.** Because in their layer, in isolation, it is.

No single actor holds the **aggregate**. So nobody feels responsible, and the standard
defense — *"that's not a big deal"* — is technically true at the level of one act and
catastrophically false at the level of the sum.

This is a well-documented failure mode under other names: **diffusion of responsibility**,
the **aggregation problem**, **death by a thousand cuts**. Naming it is the first move.
Making it *visible and accountable* is the rest.

```
   LAYER            sees only its own conduct → calls it "normal"
   ─────────────────────────────────────────────────────────────
   Workplace        a cold shoulder, a stalled promotion
   Social / online  a pile-on, an exclusion, a rumor
   Neighborhood     a "joke," a stare, a small provocation
   Home / physical  entry, tampering, a safety threat
   Institutional    a form lost, a complaint ignored
   ─────────────────────────────────────────────────────────────
                    ↑ each layer is blind to the others ↑
              THE AGGREGATE  ←  no one is looking at this column
```

The point of this repo is to **look at the column.**

---

## Two things this framework does

### 1. Sets the standard explicitly, per layer
Each layer's actors hide behind "I didn't know." So we write down, per layer, what is
acceptable and what crosses the line. Once it's explicit, ignorance stops being a defense.
See [`docs/layers.md`](docs/layers.md).

### 2. Makes the aggregate visible
The one thing no layer can see is the sum. So we log it — dated, factual, neutral — until
the pattern is undeniable to someone with the power to act on it (HR, a lawyer, police, a
court, an oversight body). A feeling is not actionable. A timeline is.
See [`docs/incident-log-template.md`](docs/incident-log-template.md).

---

## How to actually use this

| If you are... | Start with |
|---|---|
| Experiencing this and want to act | [`docs/incident-log-template.md`](docs/incident-log-template.md) — log today. Evidence is the highest-leverage first move. |
| Trying to decide if a behavior crosses a line | [`docs/layers.md`](docs/layers.md) — the per-layer standards |
| Ready to escalate | [`docs/escalation.md`](docs/escalation.md) — the right channel per layer, with real organizations |
| Building your own baseline | [`docs/baseline.md`](docs/baseline.md) — the layer that protects your judgment under stress |

---

## An honest note from the author of this scaffolding

This framework is strongest as a tool for **documentation and accountability** — turning
vague, totalizing dread into specific, dated, escalatable facts. That's its real power.

It is **weakest, and can become harmful, when used to confirm that *everyone* is
coordinating.** Diffuse harm is real; so is the human tendency, under sustained stress, to
read coordination into noise. The incident log is the test for both: if you log it and a
genuine pattern emerges, you now have the evidence to act. If you log it and it doesn't
hold together, that's information too — and worth talking through with someone you trust,
including a doctor, because carrying a sense of being targeted *everywhere* is itself a
heavy load that deserves support, not just a spreadsheet.

The log doesn't just build a case. It keeps you honest with yourself. Both matter.
