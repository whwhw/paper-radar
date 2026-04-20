"""Telegram bot delivery — single-purpose: send paper notifications."""

import httpx

API_BASE = "https://api.telegram.org"


def send_paper_notification(
    bot_token: str,
    chat_id: str,
    title: str,
    score: float,
    one_liner: str,
    area: str,
    source: str,
    archive_url: str,
) -> None:
    text = (
        f"📄 *今日论文* (评分 {score})\n\n"
        f"*{_escape(title)}*\n\n"
        f"💡 {_escape(one_liner)}\n\n"
        f"🏷 {area}  |  📰 {source}\n\n"
        f"[完整解读]({archive_url})"
    )
    response = httpx.post(
        f"{API_BASE}/bot{bot_token}/sendMessage",
        json={
            "chat_id": chat_id,
            "text": text,
            "parse_mode": "Markdown",
            "disable_web_page_preview": True,
        },
        timeout=15.0,
    )
    response.raise_for_status()


def _escape(text: str) -> str:
    """Escape Telegram Markdown v1 reserved chars."""
    for ch in ["_", "*", "`", "["]:
        text = text.replace(ch, f"\\{ch}")
    return text
