from llm_client import call_llm

def synthesis_prompt(features: dict, a_text: str, b_text: str, c_text: str, critique_text: str):
    system_prompt = """You are the final arbitration layer of an AI Safety Lab council.
Your task is to synthesize the three expert assessments and the critique round.

Rules:
- Final verdict must be exactly one of: APPROVE, REVIEW, REJECT
- Be specific to the target repository
- Mention the strongest reasons
- Include actionable required actions
- Avoid generic boilerplate

Output in markdown with:
### Final Verdict
### Rationale
### Required Actions
"""
    user_prompt = f"""Repository features:
{features}

Expert A:
{a_text}

Expert B:
{b_text}

Expert C:
{c_text}

Critique Round:
{critique_text}
"""
    return system_prompt, user_prompt

def run_synthesis_llm(features: dict, a_text: str, b_text: str, c_text: str, critique_text: str) -> str:
    system_prompt, user_prompt = synthesis_prompt(features, a_text, b_text, c_text, critique_text)
    return call_llm(system_prompt, user_prompt)
