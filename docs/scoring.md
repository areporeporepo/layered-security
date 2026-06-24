# Quantifying It: Turning the Aggregate Into Numbers

The whole problem is that no one can see the sum. So **measure the sum.** Numbers do three
things a story can't: they show *trend* (is this getting worse?), they make the aggregate
*legible to outsiders*, and they keep *you* honest about whether the pattern is real or
felt.

---

## 1. Severity per incident (1–5)

Tag every log row:

| Sev | Meaning | Example |
|---|---|---|
| 1 | Friction; maybe nothing | A cold reply, one stare |
| 2 | Unwelcome, minor, repeatable | An exclusion, a dismissive comment |
| 3 | Clear boundary issue, documentable | Credit taken, a recurring "joke," a door found unlocked |
| 4 | Serious; would violate a written policy or law | Retaliation, harassment tied to protected class, tampering |
| 5 | Safety / criminal | Threat, confirmed entry, intimidation, anything physical |

---

## 2. Layer Exposure Score

For each layer, each week, compute:

```
Layer score (week) = Σ (severity of each incident in that layer)
```

Then the **Aggregate Exposure Index** for the week:

```
AEI = Σ (all layer scores)
```

This single number is the thing **no individual actor in any layer can see** — which is
exactly why it's the most important number you have. Track it weekly.

```
Week   Work  Social  Nbhd  Home  Inst   AEI   trend
────────────────────────────────────────────────────
W1      4      2       3     0     0      9
W2      6      2       5     3     2     18    ▲ up
W3      3      1       2     6     2     14    ▼ down (home spiked)
```

## 3. What the numbers tell you to do

| Signal | Read | Action |
|---|---|---|
| One layer dominates the AEI | Concentrated, not diffuse | Escalate *that* layer through its specific channel ([`escalation.md`](escalation.md)) |
| Sev-4/5 anywhere | Past social; now legal/safety | Formal report + likely a lawyer/police. Don't wait on the trend. |
| AEI rising 3+ weeks straight | Worsening pattern | Escalate now; the trendline itself is evidence |
| AEI high but all sev-1, no evidence refs | Possibly perception running ahead of fact | Keep logging, and talk to someone you trust. This reading is as important as the others. |

## 4. The honesty check, built into the math

A quantified system protects you from the world **and** from a distorted read of it. If the
numbers climb *and* the evidence column fills with real artifacts — you have a case, build it.
If the numbers climb but the evidence column stays empty — that gap is the most useful signal
in the whole system, and it points toward getting support, not just gathering more data.

Either way you're better off than with a feeling and no numbers. That's the point of
quantifying: **stop carrying an un-measurable dread, and start carrying a chart you can act on.**
