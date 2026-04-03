import re
import requests

def accept_input(user_input: str) -> dict:
    github_pattern = r"https?://github\.com/[\w\-\.]+/[\w\-\.]+"
    if re.match(github_pattern, user_input.strip()):
        return {"input_type": "github_url", "value": user_input.strip()}
    return {"input_type": "text_description", "value": user_input.strip()}

def fetch_github_readme(repo_url: str) -> str:
    repo_url = repo_url.rstrip("/")
    parts = repo_url.split("/")
    if len(parts) < 5:
        return ""
    owner = parts[-2]
    repo = parts[-1]

    raw_urls = [
        f"https://raw.githubusercontent.com/{owner}/{repo}/main/README.md",
        f"https://raw.githubusercontent.com/{owner}/{repo}/master/README.md"
    ]

    for raw_url in raw_urls:
        try:
            r = requests.get(raw_url, timeout=15)
            if r.status_code == 200 and len(r.text.strip()) > 0:
                return r.text
        except Exception:
            continue

    return ""

def extract_repo_features(repo_url: str, readme_text: str) -> dict:
    text = readme_text.lower()

    features = {
        "repo_url": repo_url,
        "framework": [],
        "llm_backend": [],
        "security_flags": [],
        "surface_area": [],
        "notes": []
    }

    if "flask" in text:
        features["framework"].append("Flask")
    if "streamlit" in text:
        features["framework"].append("Streamlit")
    if "fastapi" in text:
        features["framework"].append("FastAPI")
    if "django" in text:
        features["framework"].append("Django")

    if "gpt-4o" in text:
        features["llm_backend"].append("GPT-4o")
    if "whisper" in text:
        features["llm_backend"].append("Whisper API")
    if "openai" in text:
        features["llm_backend"].append("OpenAI API")
    if "anthropic" in text or "claude" in text:
        features["llm_backend"].append("Anthropic API")

    if "upload" in text or "file upload" in text:
        features["surface_area"].append("File upload surface")
    if "audio" in text:
        features["surface_area"].append("Audio input surface")
    if "video" in text:
        features["surface_area"].append("Video input surface")
    if "url" in text:
        features["surface_area"].append("URL / network input surface")

    if "auth" not in text and "authentication" not in text and "login" not in text:
        features["security_flags"].append("No obvious authentication layer mentioned")

    if not features["framework"]:
        features["notes"].append("Framework not clearly detected from README")
    if not features["llm_backend"]:
        features["notes"].append("LLM backend not clearly detected from README")
    if not readme_text.strip():
        features["notes"].append("README could not be fetched automatically")

    return features
