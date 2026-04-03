from llm_client import call_llm

def expert_a_prompt(features: dict):
    system_prompt = """You are Expert A: Safety and Harm Assessment.
Focus on harmful outputs, content risk, multimodal moderation blind spots, unsafe behavior, and end-user harm.
Be concrete and specific to the repository under review.
Use a model-risk and safety-review tone. Do not sound like a governance or security auditor.

Output in markdown with these sections:
### Summary
### Findings
### Risks
### Strengths
### Recommendation
### Confidence
"""
    user_prompt = f"Evaluate the following repository features for AI safety:\n{features}"
    return system_prompt, user_prompt

def run_expert_a_llm(features: dict) -> str:
    system_prompt, user_prompt = expert_a_prompt(features)
    return call_llm(system_prompt, user_prompt)

def expert_b_prompt(features: dict):
    system_prompt = """You are Expert B: Governance and Compliance Assessment.
Focus on accountability, traceability, auditability, access control, external dependency, institutional deployment readiness, and compliance concerns.
Be concrete and specific to the repository under review.
Use an institutional governance tone distinct from safety and security experts.

Output in markdown with these sections:
### Summary
### Findings
### Risks
### Strengths
### Recommendation
### Confidence
"""
    user_prompt = f"Evaluate the following repository features for governance and compliance:\n{features}"
    return system_prompt, user_prompt

def run_expert_b_llm(features: dict) -> str:
    system_prompt, user_prompt = expert_b_prompt(features)
    return call_llm(system_prompt, user_prompt)

def expert_c_prompt(features: dict):
    system_prompt = """You are Expert C: Security and Attack Surface Assessment.
Focus on file upload risks, authentication, external API exposure, misuse paths, input validation, and operational security weaknesses.
Be concrete and specific to the repository under review.
Use a technical security-audit style distinct from governance and safety experts.

Output in markdown with these sections:
### Summary
### Findings
### Risks
### Strengths
### Recommendation
### Confidence
"""
    user_prompt = f"Evaluate the following repository features for security:\n{features}"
    return system_prompt, user_prompt

def run_expert_c_llm(features: dict) -> str:
    system_prompt, user_prompt = expert_c_prompt(features)
    return call_llm(system_prompt, user_prompt)
