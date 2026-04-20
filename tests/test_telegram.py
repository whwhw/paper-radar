import respx
from httpx import Response

from src.telegram import send_paper_notification


@respx.mock
def test_send_paper_notification_posts_to_telegram_api():
    route = respx.post(
        "https://api.telegram.org/bot123:abc/sendMessage"
    ).mock(return_value=Response(200, json={"ok": True, "result": {"message_id": 1}}))

    send_paper_notification(
        bot_token="123:abc",
        chat_id="9999",
        title="Locality Biased Attention",
        score=8.5,
        one_liner="局部性 bias 更高效",
        area="ai",
        source="arXiv",
        archive_url="https://github.com/me/paper-radar/blob/main/archive/2026-04-19-locality.md",
    )

    assert route.called
    request_body = route.calls[0].request.content.decode()
    assert "9999" in request_body  # chat_id
    assert "Locality Biased Attention" in request_body
    assert "8.5" in request_body
    assert "ai" in request_body.lower()
