"""LLM client factory — wraps OpenAI SDK for provider-agnostic LLM calls.

Configured via 3 env vars:
  LLM_API_KEY  — provider's API key
  LLM_BASE_URL — provider's OpenAI-compatible endpoint
  LLM_MODEL    — model identifier for this provider

Default config in .env.example uses OpenRouter (Claude). Swap to DeepSeek/OpenAI/Gemini/Ollama
by changing only those 3 vars — no code changes.
"""

import os
from dataclasses import dataclass

from openai import OpenAI


@dataclass(frozen=True)
class LLMConfig:
    api_key: str
    base_url: str
    model: str


def load_config_from_env() -> LLMConfig:
    api_key = os.environ.get("LLM_API_KEY")
    base_url = os.environ.get("LLM_BASE_URL")
    model = os.environ.get("LLM_MODEL")

    if not api_key:
        raise RuntimeError("LLM_API_KEY env var is required")
    if not base_url:
        raise RuntimeError("LLM_BASE_URL env var is required (e.g. https://api.openai.com/v1)")
    if not model:
        raise RuntimeError("LLM_MODEL env var is required (e.g. gpt-4o)")

    return LLMConfig(api_key=api_key, base_url=base_url, model=model)


def build_client(cfg: LLMConfig) -> OpenAI:
    return OpenAI(api_key=cfg.api_key, base_url=cfg.base_url)
