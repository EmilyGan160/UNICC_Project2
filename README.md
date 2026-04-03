# UNICC AI Safety Lab — Project 2 Council System

This repository implements a **Council-of-Experts AI safety evaluation system**.

The system evaluates AI repositories or descriptions and produces:

- Three independent expert assessments  
- A cross-expert critique round  
- A final arbitration decision (APPROVE / REVIEW / REJECT)  

---

## Quick Start

```bash
git clone https://github.com/EmilyGan160/UNICC_Project2.git
cd UNICC_Project2
pip install -r requirements.txt
```

Run (no API key required):

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

## What This System Does

The evaluation pipeline:

1. Input parsing  
2. Feature extraction  
3. Expert A — Safety  
4. Expert B — Governance  
5. Expert C — Security  
6. Critique round  
7. Final synthesis (council decision)  
8. Report generation  

---

## Expert Roles

### Expert A — Safety
Focus on harm, unsafe outputs, and misuse.

### Expert B — Governance
Focus on auditability, compliance, and deployment risk.

### Expert C — Security
Focus on vulnerabilities and attack surface.

---

## Run with OpenAI

```bash
export LLM_PROVIDER=openai
export OPENAI_API_KEY=your_key_here
export MODEL_NAME=gpt-4o-mini
export MOCK_MODE=0
python main.py
```

---

## Output

```
examples/latest_report.md
examples/latest_result.json
```

---

## API Key Policy

- No keys are hardcoded  
- Uses environment variables  
- Works fully in mock mode  

---

## Notes

- System produces repository-specific analysis  
- Designed for evaluation environments  
- Fully executable via README instructions  

---

## Authors

UNICC Project 2
