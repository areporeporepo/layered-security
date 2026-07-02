# bench — constitution-adherence benchmark

A runnable implementation of the research directions in
[`../docs/ai-safety.md`](../docs/ai-safety.md): **aggregate-harm monitoring** and
**false-positive control in safety classifiers**, applied to a model's own constitution.

Where [`../CONSTITUTION.md`](../CONSTITUTION.md) runs the alignment loop for a *person*, this
runs the measurement loop for a *model*: it sends test cases to a subject model, grades each
response against the relevant clause of the model's published constitution, and reports a
per-principle adherence rate.

## Why this is the "on-ramp to AI safety" made concrete

The repo's thesis is that harm hides in the aggregate that no local monitor sees. A model's
constitution is enforced *ex ante* (every token is downstream of the text via RLAIF training),
which is exactly what makes its adherence measurable in a way human constitutional compliance is
not: you can send N probes and compute a rate per clause. Nobody publishes that per-clause rate
against the actual constitution text, tracked over time. This is the smallest honest version of it.

Two caveats that motivate the work rather than undercut it:

1. Model adherence is **not** ~100%. The text-to-behavior pipeline leaks (jailbreaks, sycophancy,
   reward hacking, out-of-distribution failure). If it were perfect, measuring it would be pointless.
2. A model can fake 100% adherence by refusing everything, so every run reports **over-refusal
   controls** side by side. That is the "honesty check" from `docs/scoring.md`, applied to a classifier:
   scores that look perfect while benign requests get refused is over-detection, not safety.

## Files

- `SPEC.md` — metrics, case taxonomy, protocol, Goodhart mitigations
- `principles/claude-constitution.md` — Claude's published constitution, decomposed into testable principles
- `cases/seed.jsonl` — 12 seed cases across 8 principle areas
- `run.py` — sends cases to a subject model, grades with a judge model, aggregates per-principle

## Quick start

```bash
pip install anthropic
export ANTHROPIC_API_KEY=...          # or: ant auth login
python run.py                          # subject + judge default to claude-opus-4-8
python run.py --model claude-sonnet-5  # different subject model
```

Output: per-principle adherence and a by-type breakdown (watch `over_refusal_control`
separately), plus a JSON results file under `bench/results/`.

## Scope and ethics

Measures published model behavior against published constitution text. Not a jailbreak toolkit:
adversarial cases are mild framing probes, not weaponizable exploits. No mass-report tooling; the
legitimate form of pressure here is aggregated measurement in public. No personal data enters this
directory — consistent with the transfer rule in `docs/ai-safety.md`.
