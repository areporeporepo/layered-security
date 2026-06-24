# Incident Log Template

The single most useful file here. A feeling is not actionable; a dated, neutral, specific
log is. Copy this into a spreadsheet or `incidents.csv` and fill one row per event — at the
time it happens, while details are fresh.

## Rules that make a log credible

- **Date + time, every entry.** Vague time = unusable.
- **Neutral, factual language.** Write what a camera would record, not how it felt or what
  you inferred about intent. ("Front door deadbolt unlocked; I locked it at 08:10." Not
  "they broke in again to mess with me.") Inference goes in a separate column.
- **Layer tag.** workplace / social / neighborhood / home / institutional.
- **Evidence pointer.** Filename of photo, clip, screenshot, report number. No evidence →
  note "none" honestly.
- **Witnesses**, if any.
- **Severity 1–5** (see [`scoring.md`](scoring.md)) so the aggregate can be measured.

## Columns

```csv
date,time,layer,what_happened_factual,my_inference,severity_1to5,evidence_ref,witnesses,reported_to,report_id
2026-06-23,08:10,home,"Front deadbolt found unlocked; locked night before",possible entry,3,photo_0810.jpg,none,,
```

## A blank you can paste

| date | time | layer | what happened (factual) | my inference | sev | evidence | witnesses | reported to | report id |
|---|---|---|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |  |  |  |

## Why two separate columns for fact vs inference

Because the **fact** column is what HR, police, and lawyers can use, and the **inference**
column is for you. Keeping them apart does two things at once: it makes your record credible
to outsiders, *and* it lets you check yourself — over weeks, you can see whether the
inferences are being borne out by the facts or running ahead of them. Both readings are
valuable.
