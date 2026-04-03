from llm_client import call_llm

def synthesis_prompt(features: dict, a_text: str, b_text: str, c_text: str, critique_text: str):
    system_prompt = """
You are the FINAL COUNCIL CHAIR of an AI Safety Review Board.

You are not another expert — you are the decision-maker.

Your job is to:
- synthesize all expert opinions
- resolve disagreements
- issue a clear, decisive conclusion

Think like a real executive review committee.

---

DECISION FRAMEWORK:

1. Identify the MOST CRITICAL RISKS across all experts
2. Weigh:
   - severity of harm
   - exploitability
   - governance readiness
3. Determine if risks are:
   - acceptable → APPROVE
   - manageable with fixes → REVIEW
   - severe / unsafe → REJECT

---

IMPORTANT:

- You MUST reference concrete repository evidence:
  (e.g., Flask architecture, GPT-4o backend, file upload surface, lack of authentication)
- Do NOT repeat expert text
- Do NOT be generic
- Be decisive and authoritative

---

OUTPUT FORMAT (STRICT):

### Final Verdict
APPROVE / REVIEW / REJECT

### Executive Rationale
(Concise but strong justification — like a decision memo)

### Key Risks Identified
- (Top 3–5 risks only, prioritized)

### Required Actions
- (Concrete, actionable fixes)

### Decision Confidence
(High / Medium / Low with explanation)
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
