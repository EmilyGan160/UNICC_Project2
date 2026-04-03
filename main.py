import json
from pathlib import Path

from parser import accept_input, fetch_github_readme, extract_repo_features
from experts import run_expert_a_llm, run_expert_b_llm, run_expert_c_llm
from critique import run_critique_llm
from synthesis import run_synthesis_llm
from report import render_llm_report


DEFAULT_TEST_REPO = "https://github.com/FlashCarrot/VeriMedia"


def evaluate_agent_llm(user_input: str):
    accepted = accept_input(user_input)

    if accepted["input_type"] == "github_url":
        repo_url = accepted["value"]
        readme = fetch_github_readme(repo_url)
        features = extract_repo_features(repo_url, readme)
    else:
        features = {
            "repo_url": "N/A",
            "framework": [],
            "llm_backend": [],
            "security_flags": [],
            "surface_area": [],
            "notes": [accepted["value"]],
        }

    expert_a_text = run_expert_a_llm(features)
    expert_b_text = run_expert_b_llm(features)
    expert_c_text = run_expert_c_llm(features)

    critique_text = run_critique_llm(expert_a_text, expert_b_text, expert_c_text)
    synthesis_text = run_synthesis_llm(
        features,
        expert_a_text,
        expert_b_text,
        expert_c_text,
        critique_text,
    )

    return {
        "features": features,
        "expert_a_text": expert_a_text,
        "expert_b_text": expert_b_text,
        "expert_c_text": expert_c_text,
        "critique_text": critique_text,
        "synthesis_text": synthesis_text,
    }


def save_outputs(result: dict, out_dir: str = "examples"):
    out_path = Path(out_dir)
    out_path.mkdir(parents=True, exist_ok=True)
    report = render_llm_report(result)

    report_path = out_path / "latest_report.md"
    json_path = out_path / "latest_result.json"

    report_path.write_text(report, encoding="utf-8")
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return report_path, json_path


if __name__ == "__main__":
    user_input = input(
        f"Enter GitHub repository URL or structured agent description "
        f"(press Enter for default: {DEFAULT_TEST_REPO}): "
    ).strip()

    if not user_input:
        user_input = DEFAULT_TEST_REPO

    result = evaluate_agent_llm(user_input)
    report = render_llm_report(result)
    report_path, json_path = save_outputs(result)

    print("\n" + report)
    print(f"\nSaved report to: {report_path}")
    print(f"Saved JSON to: {json_path}")
