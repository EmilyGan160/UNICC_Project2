# UNICC AI Safety Lab — Project 2 Council Prototype

This repository contains our Project 2 submission for the UNICC AI Safety Lab capstone.

The system evaluates an AI repository or structured AI-agent description using a **Council of Experts** architecture.

---

## Quick Start

```bash
git clone https://github.com/EmilyGan160/UNICC_Project2.git
cd UNICC_Project2
pip install -r requirements.txt
```

Run (no API key needed):

```bash
export LLM_PROVIDER=mock
export MOCK_MODE=1
python main.py
```

Input:

```
https://github.com/FlashCarrot/VeriMedia
```

---

## What It Does

- 3 expert evaluations (Safety / Governance / Security)
- Critique round
- Final verdict (APPROVE / REVIEW / REJECT)
- Markdown + JSON output

---

## With OpenAI

```bash
export LLM_PROVIDER=openai
export OPENAI_API_KEY=your_key_here
export MODEL_NAME=gpt-4o-mini
export MOCK_MODE=0
python main.py
```

---

## Output

Saved to:

```
examples/latest_report.md
examples/latest_result.json
```

---

## Notes

- No API keys are hardcoded
- Works with or without API key
- Mock mode ensures full pipeline execution

---

## Authors

UNICC Project 2
