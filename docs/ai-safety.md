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

## The constructive flip: AI as the cross-layer architect

Everything above frames AI as carrying the *same disease* — distributed harm no local monitor
sees. But flip it. The human problem was never that the harm is unbeatable; it's that **no single
human actor can span the layers.** Each person sees one slice, the aggregate is unseeable, and
verification is manual so it gets skipped.

**AI is the first agent that can actually operate across all layers and applications, at a low
level.** That makes it the missing piece on the solution side:

- **Aggregator** — it can hold the column no human layer can see: read the incident log, the
  workplace record, the home sensors, the conduct trackers, and compute the true cross-layer
  aggregate (the harm-side Exposure Index *and* the solution-side verification).
- **Verifier** — it can check that the positive-sum practice is *real and logged*, not asserted,
  across every application at once. "Care + action — verified" stops being a slogan you grade
  yourself on and becomes something checkable end-to-end. (See [`../SOLUTIONS.md`](../SOLUTIONS.md).)
- **Architect** — it can build the solution stack *into* each layer, low-level, so positive-sum
  conduct is the default the system makes easy, instead of the costly path humans skip.

### The double-edge (why the calibration guard is not optional)

This is the same cross-layer span that made AI **dangerous** above — harm that propagates across
every layer with no one seeing the whole. **Same power, both directions.** An AI that can verify
positive-sum conduct across all layers can also enforce harm across all layers, and an aggregate
monitor sensitive enough to catch distributed harm will, miscalibrated, *manufacture* coordination
from noise — the exact over-detection trap a stressed human falls into.

So the cross-layer architect only dissolves the substrate if it carries the two guards this repo
keeps insisting on: **calibration** (the fact-vs-inference / over-detection discipline) and
**verification** (logged, falsifiable, public — not claimed). Cross-layer power without those is
just the harm mechanism with a bigger reach. With them, it's the first thing that can actually see
and dissolve the local-knowledge problem at the root.

### External corroboration: Anthropic's Frontier Safety Roadmap

This framework was derived from the *human* side — and it lands on the same architecture that
frontier labs are building for AI. Anthropic's
[Responsible Scaling Policy roadmap](https://www.anthropic.com/responsible-scaling-policy/roadmap)
maps onto it almost element-for-element:

| This repo | RSP roadmap |
|---|---|
| Severity 1–5 / risk tiering ([`scoring.md`](scoring.md)) | **ASL capability thresholds** — safeguards escalate per capability tier |
| AI as cross-layer aggregator reading every layer's log (above) | **"Eyes on everything"** — centralized, searchable logs analyzed by AI for insider/security threats |
| The five-layer defense model ([`layers.md`](layers.md)) | **Defense-in-depth** across security, safeguards, alignment, and policy |
| Calibration + adversarial-verification guard | **Alignment assessments validated against adversarially-designed models** |

The convergence is **structural, not literal** — the personal case is not the RSP. But arriving
at the same shapes from a completely different starting point is a signal the lens is aimed at
something real: layered harm, aggregate monitoring, AI-held oversight, and calibrated thresholds
are load-bearing on both the human side and the frontier-AI side.

## Implemented here: the constitution-adherence benchmark

Research direction 1 (aggregate-harm monitors) and the over-detection warning above are no
longer only a proposal in this repo — [`../bench/`](../bench/) is a runnable first cut. It sends
test cases to a subject model, grades each response against the relevant clause of the model's
**published constitution** with a judge model, and reports a per-principle adherence rate — with
**over-refusal controls scored alongside**, so a classifier that looks perfect only because it
refuses everything is caught. That over-detection check is the same honesty guard as
[`scoring.md`](scoring.md), applied to a model instead of an incident log. See
[`../bench/SPEC.md`](../bench/SPEC.md) for metrics and Goodhart mitigations.

## If you wanted to take it further

A short writeup titled something like *"Diffuse Harm and the Aggregation Problem: monitoring
what no local check can see"* — making the human↔AI symmetry explicit and proposing the
calibrated aggregate-monitor — is a real contribution. The strongest version leads with the
calibration failure (over-detection), because that's the part most aggregate-monitoring
proposals ignore, and it's the part this repo took most seriously.
