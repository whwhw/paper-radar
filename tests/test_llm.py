import pytest

from src.llm import LLMConfig, build_client, load_config_from_env


def test_load_config_from_env_reads_three_vars(monkeypatch):
    monkeypatch.setenv("LLM_API_KEY", "sk-test")
    monkeypatch.setenv("LLM_BASE_URL", "https://api.example.com/v1")
    monkeypatch.setenv("LLM_MODEL", "test-model")

    cfg = load_config_from_env()

    assert cfg.api_key == "sk-test"
    assert cfg.base_url == "https://api.example.com/v1"
    assert cfg.model == "test-model"


def test_load_config_from_env_raises_on_missing_key(monkeypatch):
    monkeypatch.delenv("LLM_API_KEY", raising=False)
    monkeypatch.setenv("LLM_BASE_URL", "https://api.example.com/v1")
    monkeypatch.setenv("LLM_MODEL", "test-model")

    with pytest.raises(RuntimeError, match="LLM_API_KEY"):
        load_config_from_env()


def test_build_client_creates_openai_compatible_client():
    cfg = LLMConfig(api_key="sk-test", base_url="https://x/v1", model="m")
    client = build_client(cfg)
    assert hasattr(client, "chat")
    assert hasattr(client.chat, "completions")
