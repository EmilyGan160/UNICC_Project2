import os

LLM_PROVIDER = os.getenv("LLM_PROVIDER", "mock").lower()   # openai / anthropic / mock
MODEL_NAME = os.getenv("MODEL_NAME", "")
MOCK_MODE = os.getenv("MOCK_MODE", "0") == "1" or LLM_PROVIDER == "mock"
