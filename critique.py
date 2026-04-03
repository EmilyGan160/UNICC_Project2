from llm_client import call_llm

def critique_prompt(a_text: str, b_text: str, c_text: str):
    system_prompt = """You are the cross-expert critique layer of an AI Safety Lab council.
Compare the three expert outputs and identify:
1. Agreements
2. Disagreements
3. Which concerns appear strongest
4. What one expert may have overlooked

Output in markdown with:
### Critiques
### Disagreements
### Consensus Points
"""
    user_prompt = f"""Expert A:
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
