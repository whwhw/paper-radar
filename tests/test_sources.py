from datetime import date

import respx
from httpx import Response

from src.sources import fetch_arxiv, fetch_rss


@respx.mock
def test_fetch_arxiv_parses_atom_feed(fixtures_dir):
    fixture = (fixtures_dir / "arxiv_response.xml").read_text()
    respx.get("https://export.arxiv.org/api/query").mock(
        return_value=Response(200, text=fixture)
    )

    papers = fetch_arxiv(category="cs.LG", max_results=10)

    assert len(papers) == 2
    p = papers[0]
    assert p.id == "arxiv:2401.00001"
    assert p.title == "Attention Mechanisms Revisited"
    assert p.authors == ["Alice Author", "Bob Researcher"]
    assert "locality bias" in p.abstract
    assert p.source == "arXiv"
    assert p.url == "http://arxiv.org/abs/2401.00001v1"
    assert p.published == date(2026, 4, 18)
    assert p.primary_category == "cs.LG"


@respx.mock
def test_fetch_arxiv_handles_empty_feed():
    respx.get("https://export.arxiv.org/api/query").mock(
        return_value=Response(200, text='<?xml version="1.0"?><feed xmlns="http://www.w3.org/2005/Atom"/>')
    )

    papers = fetch_arxiv(category="cs.LG", max_results=10)
    assert papers == []


def test_fetch_rss_parses_feed_with_local_file(fixtures_dir, mocker):
    fixture_text = (fixtures_dir / "nature_rss.xml").read_text()
    mocker.patch("src.sources.httpx.get",
                 return_value=mocker.Mock(text=fixture_text, status_code=200,
                                          raise_for_status=lambda: None))

    papers = fetch_rss(
        url="https://www.nature.com/nm.rss",
        source_name="Nature Medicine",
    )

    assert len(papers) == 1
    p = papers[0]
    assert "GLP-1" in p.title
    assert p.source == "Nature Medicine"
    assert p.url == "https://www.nature.com/articles/s41591-026-12345"
    assert p.published == date(2026, 4, 18)
    assert "Jane Researcher" in p.authors
