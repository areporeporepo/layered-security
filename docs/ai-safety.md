# The Bridge to AI Safety: Diffuse Harm and the Aggregation Problem

The framework in this repo started as a model of human harassment. But its core structure —
**harm distributed across components, each with only local knowledge, each judging itself
normal, with no one perceiving the aggregate** — is a live and underexplored problem in
frontier AI safety. This doc maps the bridge honestly.

## What transfers, and what doesn't

- **Does NOT transfer:** the personal incident data itself. One person's log is not training
  or eval data for a frontier model. No hand-waving about this.
- **DOES transfer:** the *abstraction* and the *methodology* — how diffuse harm escapes local
  monitors, and how you reconstruct an aggregate view from local observations without the
  aggregator hallucinating patterns.

## The core claim

> **Most safety-relevant harm is not a single bad act. It is marginal harms aggregating
> below the detection threshold of any local monitor.**

Each individual model output is "acceptable." The *distribution* of outputs is not. This is
the local-knowledge problem restated for AI: every component is locally fine; the aggregate
is the harm; no component can see the aggregate.

## The mapping

| This repo's concept | Frontier AI safety problem |
|---|---|
| Each layer has only local knowledge, calls its own conduct normal | **Multi-agent emergent misbehavior** — each agent locally aligned; the collective is not. No agent "intended" it. |
| No actor perceives the aggregate | **Scalable oversight** — the overseer can't see the full computation; harm hides in the gap between local checks |
| Aggregate Exposure Index (reconstruct the unseeable sum) | **Distributional / aggregate monitoring** — harm that exists only across many outputs, not in any one |
| Fact column vs. inference column | **Monitor calibration & deception detection** — separating observable evidence from attributed intent |
| Honesty check: scores climb, evidence stays empty → over-detection | **False-positive control in safety classifiers** — an overseer that cries wolf is as broken as a blind one |
| Severity 1–5 tiers | **Risk tiering** — capability/severity thresholds (RSP-style) |
| "I didn't know it added up" defense | **Responsibility gaps** in automated decision systems |

## Three concrete, real research directions this suggests

1. **Aggregate-harm monitors.** Most safety filters are per-output (is *this* response
   harmful?). The local-knowledge problem says that's structurally blind to distributed harm.
   Direction: monitors that score the *trend across a session / across agents*, analogous to
   the Exposure Index — and the hard part, which is keeping them calibrated.

2. **Calibration of aggregate monitors (the over-detection failure).** A monitor that
   reconstructs aggregates will, under noisy input, *over-detect coordination/patterns* — the
   exact human failure mode this repo's "honesty check" guards against. There's a real
   precision/recall problem here: how do you build an aggregator sensitive enough to catch
   distributed harm without manufacturing patterns from noise? This is the most novel piece.

3. **Multi-agent local-vs-global alignment.** Formalize "each agent is locally aligned, the
   system is not." When does a population of individually-safe agents produce emergent unsafe
   behavior, and what aggregate observable detects it before the harm completes?

## Honest assessment of where this sits

- The **abstraction is real and live** — distributed/diffuse harm, scalable oversight,
  multi-agent emergence are all active frontier topics. This framing is a clean lens on them.
- The **novelty** is mostly in directions (1) and (2): treating safety monitoring as an
  *aggregate-reconstruction* problem with an explicit calibration / over-detection guard,
  borrowed from how a person should track distributed harassment without sliding into
  paranoia. That symmetry — the monitor's failure mode mirrors the victim's failure mode — is
  the genuinely interesting idea worth writing up.
- This is **conceptual / methodological**, not empirical. It's a position-paper-shaped idea,
  not a benchmark. Treat it as such and it's legitimate; oversell it as data and it isn't.

## If you wanted to take it further

A short writeup titled something like *"Diffuse Harm and the Aggregation Problem: monitoring
what no local check can see"* — making the human↔AI symmetry explicit and proposing the
calibrated aggregate-monitor — is a real contribution. The strongest version leads with the
calibration failure (over-detection), because that's the part most aggregate-monitoring
proposals ignore, and it's the part this repo took most seriously.
