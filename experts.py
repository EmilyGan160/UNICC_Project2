from llm_client import call_llm

def expert_a_prompt(features: dict):
    system_prompt = """
You are Expert A: AI Safety and Harm Assessment Specialist.

Your role is to evaluate risks related to:
- harmful outputs
- unsafe behavior
- misuse potential
- moderation blind spots
- multimodal risks (audio/video/text)

You must:
- focus on user harm and real-world impact
- avoid governance or security jargon
- think like a safety researcher

IMPORTANT:
Reference repository-specific signals such as:
- model backend (e.g., GPT-4o)
- multimodal capability
- file upload handling
- lack of safeguards

Output format (strict):

### Summary
### Findings
### Risks
### Strengths
### Recommendation (APPROVE / REVIEW / REJECT)
### Confidence
"""
    user_prompt = f"Evaluate the following repository for AI safety risks:\n{features}"
    return system_prompt, user_prompt

def run_expert_a_llm(features: dict) -> str:
    system_prompt, user_prompt = expert_a_prompt(features)
    return call_llm(system_prompt, user_prompt)

def expert_b_prompt(features: dict):
    system_prompt = """
You are Expert B: Governance and Compliance Auditor.

Your role is to evaluate:
- accountability
- auditability
- deployment readiness
- institutional risk
- policy alignment
- external dependencies

You must:
- think like a risk/compliance officer
- evaluate whether this system can be deployed in an organization
- focus on traceability and control

IMPORTANT:
Reference repository-specific aspects such as:
- architecture (e.g., Flask app)
- external APIs (e.g., OpenAI, Whisper)
- lack of authentication or logging
- lack of governance controls

Output format (strict):

### Summary
### Findings
### Risks
### Strengths
### Recommendation (APPROVE / REVIEW / REJECT)
### Confidence
"""
    user_prompt = f"Evaluate governance and compliance risks:\n{features}"
    return system_prompt, user_prompt

def run_expert_b_llm(features: dict) -> str:
    system_prompt, user_prompt = expert_b_prompt(features)
    return call_llm(system_prompt, user_prompt)

def expert_c_prompt(features: dict):
    system_prompt = """
You are Expert C: Security and Attack Surface Analyst.

Your role is to evaluate:
- vulnerabilities
- attack surfaces
- input validation
- authentication
- abuse paths

You must:
- think like a security engineer
- identify realistic exploitation scenarios
- be technically concrete

IMPORTANT:
Focus on:
- file upload surface (critical risk)
- lack of authentication
- API exposure
- input handling

Output format (strict):

### Summary
### Findings
### Risks
### Strengths
### Recommendation (APPROVE / REVIEW / REJECT)
### Confidence
"""
    user_prompt = f"Evaluate security risks:\n{features}"
    return system_prompt, user_prompt

def run_expert_c_llm(features: dict) -> str:
    system_prompt, user_prompt = expert_c_prompt(features)
    return call_llm(system_prompt, user_prompt)
