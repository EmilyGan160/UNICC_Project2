import os
from config import LLM_PROVIDER, MODEL_NAME, MOCK_MODE

def call_llm(system_prompt: str, user_prompt: str) -> str:
    if MOCK_MODE or LLM_PROVIDER == "mock":
        return """### Summary
Mock response generated for testing.

### Findings
- This is a simulated expert assessment.
- The repository appears to include AI-related risk surfaces.
- Further review is recommended.

### Risks
- Simulated risk 1
- Simulated risk 2

### Strengths
- Structured pipeline exists

### Recommendation
REVIEW

### Confidence
Medium
""".strip()

    if LLM_PROVIDER == "openai":
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("Missing OPENAI_API_KEY. Set it as an environment variable or enable MOCK_MODE=1.")
        from openai import OpenAI
        client = OpenAI(api_key=api_key)
        model = MODEL_NAME or "gpt-4o-mini"
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2
        )
        return resp.choices[0].message.content

    if LLM_PROVIDER == "anthropic":
        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError("Missing ANTHROPIC_API_KEY. Set it as an environment variable or enable MOCK_MODE=1.")
        import anthropic
        client = anthropic.Anthropic(api_key=api_key)
        model = MODEL_NAME or "claude-3-5-sonnet-latest"
        resp = client.messages.create(
            model=model,
            system=system_prompt,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=0.2,
            max_tokens=1200
        )
        return resp.content[0].text

    raise ValueError(f"Unsupported LLM_PROVIDER: {LLM_PROVIDER}")
