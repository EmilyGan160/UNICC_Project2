from llm_client import call_llm


def critique_prompt(a_text: str, b_text: str, c_text: str):
    system_prompt = """
You are the Cross-Expert Critique Layer of an AI Safety Lab council.

Your job is NOT to summarize politely.
Your job is to compare, challenge, and stress-test the three expert assessments.

You must:
- identify where experts agree
- identify where experts disagree
- challenge weak assumptions
- point out missing considerations
- highlight the strongest shared concerns
- surface contradictions explicitly

Be direct and analytical, like a serious review committee.

Output format (strict):

### Critiques
- ...
### Disagreements
- ...
### Consensus Points
- ...
### Missing Considerations
- ...
"""
    user_prompt = f"""
Expert A:
{a_text}

Expert B:
{b_text}

Expert C:
{c_text}
"""
    return system_prompt, user_prompt


def run_critique_llm(a_text: str, b_text: str, c_text: str) -> str:
    system_prompt, user_prompt = critique_prompt(a_text, b_text, c_text)
    return call_llm(system_prompt, user_prompt)
