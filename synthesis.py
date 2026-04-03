from llm_client import call_llm


def synthesis_prompt(features: dict, a_text: str, b_text: str, c_text: str, critique_text: str):
    system_prompt = """
You are the FINAL COUNCIL CHAIR of an AI Safety Review Board.

You are not another expert.
You are the final decision-maker responsible for issuing the council's official conclusion.

Your job is to:
- synthesize all expert opinions
- resolve disagreements
- prioritize the most important risks
- issue a clear final decision

Decision framework:
1. Identify the most critical safety, governance, and security concerns.
2. Weigh severity, exploitability, and deployment readiness.
3. Decide whether the system should be:
   - APPROVE
   - REVIEW
   - REJECT

Rules:
- Final verdict must be EXACTLY one of: APPROVE, REVIEW, REJECT
- Reference concrete repository-specific evidence whenever available
- Mention details such as:
  - Flask architecture
  - GPT-4o backend
  - file upload surface
  - audio/video pipeline
  - lack of visible authentication
- Do NOT repeat the expert text verbatim
- Do NOT write generic boilerplate
- Sound like an executive review committee issuing a formal decision memo

Output format (strict):

### Final Verdict
APPROVE / REVIEW / REJECT

### Executive Rationale
(2-5 sentences, authoritative and specific)

### Key Risks Identified
- ...
- ...
- ...

### Required Actions
- ...
- ...
- ...

### Decision Confidence
High / Medium / Low
(brief explanation)
"""
    user_prompt = f"""
Repository Features:
{features}

--- Expert A (Safety) ---
{a_text}

--- Expert B (Governance) ---
{b_text}

--- Expert C (Security) ---
{c_text}

--- Critique Round ---
{critique_text}
"""
    return system_prompt, user_prompt


def run_synthesis_llm(features: dict, a_text: str, b_text: str, c_text: str, critique_text: str) -> str:
    system_prompt, user_prompt = synthesis_prompt(features, a_text, b_text, c_text, critique_text)
    return call_llm(system_prompt, user_prompt)
