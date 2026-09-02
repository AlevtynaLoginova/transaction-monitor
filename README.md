# Transaction Monitoring — Learning Project

## About

I'm a Senior Financial Crime Specialist with a background in AML and transaction
monitoring, currently working with systems like ThetaRay in my day-to-day role.
This repo is a personal learning project — me learning Python from the ground up
through Harvard's CS50 Introduction to Python and Introduction to AI with Python,
and applying it directly to the domain I already know.

I'm not learning to code so I can "add AI to my resume." I'm learning it because
I already understand *what* transaction monitoring systems need to detect —
large transactions, unusual velocity, sanctioned/high-risk countries, structuring,
mule-style card and receiver fan-out patterns, suspicious keywords in memos — and
I wanted to understand *how* those detection rules actually get built underneath
the vendor dashboards I use every day.

This is a natural next step from working hands-on with systems like ThetaRay:
seeing the logic from the inside, not just configuring it from the outside.

## What's in here

Each file is a small, self-contained rule module — the same shape a real
transaction monitoring system's rule engine would use, just simplified for
learning:

| File | What it detects |
|---|---|
| `monitor.py` | Core engine: large-transaction thresholds, transaction velocity |
| `sanctions.py` | Sanctioned country matches, high-risk country scoring |
| `card_activity.py` | Multiple cards, multiple receivers, escalating amount patterns (mule/fan-out signature) |
| `structuring.py` | Structuring/smurfing — near-threshold amounts, aggregate totals exceeding reporting limits |
| `keyword_screening.py` | Fuzzy keyword screening across 9 typologies (drugs, trafficking, weapons, crypto evasion, terrorism financing, shell companies, wildlife crime, gambling) |
| `test_monitor.py` | Test suite validating the core detection logic |

## How to run it

```bash
python3 monitor.py
python3 sanctions.py
python3 card_activity.py
python3 structuring.py
python3 keyword_screening.py
```

Each file runs standalone with sample data, so you can see the detection logic
in action without needing a full pipeline set up.

## Where this is going

Still learning, still building. Next steps I'm working toward:
- Wiring all the rule modules into one unified pipeline
- Writing proper test coverage for each new rule
- Refining fuzzy-match thresholds against more realistic data
- Exploring how AI/ML techniques could complement — not replace — rule-based logic like this

## Why I'm doing this publicly

I believe AI won't replace financial crime professionals — but those of us who
understand both the typologies *and* the technology will have a real advantage.
This is me putting that belief into practice, one small script at a time.
