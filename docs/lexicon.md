# A Personal-Security Lexicon

The vocabulary of professional security and frontier-AI safety, mapped to the personal layers.
Precise words make vague experience **legible and actionable**: "someone's been weird around my
place" is dismissible; *"personal-level espionage, here's the logged evidence"* is not.

> **Use-the-word rule (the calibration guard):** apply a term only when your
> [log](../incidents.csv) supports it. The vocabulary is a precision tool, not permission to read
> espionage into every coincidence. Evidence first, then the word. A term with no evidence column
> behind it is the [over-detection trap](the-mechanism.md#the-guard-read-this), not analysis.

---

| Security / RSP term | Personal-level meaning | What justifies the word (evidence) |
|---|---|---|
| **Threat model** | Who or what can harm you, across which layers, and how | A written list per layer — not a feeling |
| **Personal-level espionage / surveillance** | Someone monitoring your routine, going through your belongings, tracking your movements, or stalkerware on a device | Tampering you photographed, a device check, a pattern of "knowing" things they shouldn't, dated sightings |
| **Theft / exfiltration** | Assets leaving without authorization — property, mail/packages, identity, *or* credit and ideas (your work attributed to someone else) | A dated inventory of what's missing (photos, receipts, account/mail statements); for credit theft, the timeline of who presented your work and when |
| **Insider threat** | Harm from someone *with trusted access* — a household member, coworker, "friend" | The most damaging and most documentable, because access is established. Log what only an insider could do |
| **Attack surface** | Every place you're exposed: accounts, home entry points, daily routines, devices, who knows your schedule | An inventory of exposures — then reduce it |
| **Access control** | Who holds keys, passwords, entry, and account recovery | A list; revoke what shouldn't be there (re-key, rotate passwords, 2FA) |
| **Defense-in-depth** | Layered protections so no single failure exposes you | The [five-layer model](layers.md) |
| **Aggregate risk / exposure** | The cross-layer total no single actor sees | The [Exposure Index](scoring.md) from `score.py` |
| **"Eyes on everything"** | One searchable record across all layers | Your [incident log](incident-log-template.md) |
| **Capability / severity thresholds** | When harm escalates from friction → policy/legal → safety/criminal | [Severity 1–5](scoring.md); a sev-4/5 changes the response |
| **Red-teaming** | Adversarially stress-testing your own read — trying to *disprove* the pattern | The fact-vs-inference split; if it survives an honest attempt to refute it, it's solid |
| **Calibration / over-detection** | Telling real signal from noise; not manufacturing coordination | The evidence column; if the score climbs but evidence stays empty, that gap *is* the finding |
| **Containment / incident response** | Stopping the harm and acting | The [PLAYBOOK](../PLAYBOOK.md) + [escalation](escalation.md): protective order, exit, lawyer, agency |

---

## Why borrow the vocabulary at all

Two reasons, both practical:

1. **It's legible to people with power.** HR, a lawyer, police, and a court respond to precise,
   categorized, evidenced claims — not to "it's all happening everywhere." The lexicon forces the
   vague into the actionable.
2. **It keeps you honest.** Each term comes with an evidence test. "Is this *actually* insider-
   threat access, or am I inferring?" is a question that protects you from your own over-detection
   as much as it documents the harm. The same discipline frontier labs use to avoid false alarms is
   the discipline that keeps *you* calibrated.

The words are sharp. Earn each one with the log, and they cut. Use them without it, and they're
just a more sophisticated way to feel hunted.
