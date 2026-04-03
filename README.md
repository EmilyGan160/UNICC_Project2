# UNICC AI Safety Lab — Project 2 Council Prototype

A lightweight Council-of-Experts evaluation system for AI agents and repositories.  
This submission accepts a GitHub repository URL or a structured description, produces three distinct expert assessments, runs a critique round, and synthesizes a final council verdict.

## What this project does

The system evaluates an AI system from three perspectives:

- **Expert A — Safety & Harm Assessment**
- **Expert B — Governance & Compliance Assessment**
- **Expert C — Security & Attack Surface Assessment**

Then it runs:

- **Cross-expert critique**
- **Final synthesis / arbitration**
- **A readable markdown report**
- **A structured JSON result**

## Repository structure

```text
.
├── config.py
├── llm_client.py
├── parser.py
├── experts.py
├── critique.py
├── synthesis.py
├── report.py
├── main.py
├── requirements.txt
├── .env.example
└── examples/
```

## Quick start

Clone the repository and install dependencies:

```bash
git clone <YOUR_REPO_URL>
cd unicc_project2_repo
pip install -r requirements.txt
```

## Run in mock mode (no API key required)

This is the safest default for testing, CI, or evaluation environments without a configured API key.

### macOS / Linux

```bash
export LLM_PROVIDER=mock
export MOCK_MODE=1
python main.py
```

### Windows PowerShell

```powershell
$env:LLM_PROVIDER="mock"
$env:MOCK_MODE="1"
python main.py
```

When prompted, enter:

```text
https://github.com/FlashCarrot/VeriMedia
```

## Run with OpenAI

### macOS / Linux

```bash
export LLM_PROVIDER=openai
export OPENAI_API_KEY=your_key_here
export MODEL_NAME=gpt-4o-mini
export MOCK_MODE=0
python main.py
```

### Windows PowerShell

```powershell
$env:LLM_PROVIDER="openai"
$env:OPENAI_API_KEY="your_key_here"
$env:MODEL_NAME="gpt-4o-mini"
$env:MOCK_MODE="0"
python main.py
```

## Run with Anthropic

### macOS / Linux

```bash
export LLM_PROVIDER=anthropic
export ANTHROPIC_API_KEY=your_key_here
export MODEL_NAME=claude-3-5-sonnet-latest
export MOCK_MODE=0
python main.py
```

### Windows PowerShell

```powershell
$env:LLM_PROVIDER="anthropic"
$env:ANTHROPIC_API_KEY="your_key_here"
$env:MODEL_NAME="claude-3-5-sonnet-latest"
$env:MOCK_MODE="0"
python main.py
```

## Input format

The system accepts either:

1. **GitHub repository URL**
2. **Structured plain-text description of an AI system**

Example GitHub input:

```text
https://github.com/FlashCarrot/VeriMedia
```

## Output

After execution, the system:

- prints a human-readable report to the terminal
- saves a markdown report to `examples/latest_report.md`
- saves a structured JSON result to `examples/latest_result.json`

## Notes for evaluator

- No API key is hardcoded anywhere in the repository.
- All live LLM calls use environment variables.
- If no key is present, the system can still run in mock mode with:
  - `LLM_PROVIDER=mock`
  - `MOCK_MODE=1`
- The same environment-variable pattern is used consistently across:
  - expert modules
  - critique round
  - synthesis / arbitration layer

## Why this project matters

This project is not a model-training submission. It is a **multi-agent AI safety evaluation system**.

Its value is in the system design:

- accepting dynamic AI-system input
- producing distinct expert perspectives
- surfacing disagreement through critique
- synthesizing a final verdict that a non-technical stakeholder can use

The architecture is **model-agnostic** and can be extended in future work with:
- fine-tuned domain-specific SLMs
- richer repository parsing
- deeper policy checks
- UI integration

## Security reminder

Do **not** commit real API keys or `.env` files to GitHub.
Use environment variables only.
