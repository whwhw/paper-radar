"""Candidate paper fetchers — arXiv API and journal RSS feeds."""

import hashlib
from datetime import datetime
from email.utils import parsedate_to_datetime
from xml.etree import ElementTree as ET

import feedparser
import httpx

from src.models import Paper

ARXIV_API = "https://export.arxiv.org/api/query"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}


def fetch_arxiv(category: str, max_results: int = 50) -> list[Paper]:
    """Fetch recent papers from arXiv for a given category (e.g., 'cs.LG')."""
    params = {
        "search_query": f"cat:{category}",
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": max_results,
    }
    response = httpx.get(ARXIV_API, params=params, timeout=30.0, follow_redirects=True)
    response.raise_for_status()
    return _parse_arxiv_atom(response.text)


def _parse_arxiv_atom(xml_text: str) -> list[Paper]:
    root = ET.fromstring(xml_text)
    papers: list[Paper] = []
    for entry in root.findall("atom:entry", ATOM_NS):
        full_id = entry.findtext("atom:id", default="", namespaces=ATOM_NS)
        # http://arxiv.org/abs/2401.00001v1 → arxiv:2401.00001
        bare_id = full_id.rsplit("/", 1)[-1].rsplit("v", 1)[0]
        title = (entry.findtext("atom:title", default="", namespaces=ATOM_NS) or "").strip()
        abstract = (entry.findtext("atom:summary", default="", namespaces=ATOM_NS) or "").strip()
        published_str = entry.findtext("atom:published", default="", namespaces=ATOM_NS) or ""
        published = datetime.fromisoformat(published_str.replace("Z", "+00:00")).date()
        authors = [
            (a.findtext("atom:name", default="", namespaces=ATOM_NS) or "").strip()
            for a in entry.findall("atom:author", ATOM_NS)
        ]
        url = full_id
        for link in entry.findall("atom:link", ATOM_NS):
            if link.attrib.get("rel") == "alternate":
                url = link.attrib.get("href", url)
                break
        categories = entry.findall("atom:category", ATOM_NS)
        primary = categories[0].attrib.get("term", "unknown") if categories else "unknown"

        papers.append(
            Paper(
                id=f"arxiv:{bare_id}",
                title=title,
                authors=authors,
                abstract=abstract,
                source="arXiv",
                url=url,
                published=published,
                primary_category=primary,
            )
        )
    return papers


def fetch_rss(url: str, source_name: str) -> list[Paper]:
    """Fetch papers from a journal RSS feed."""
    response = httpx.get(url, timeout=30.0, follow_redirects=True)
    response.raise_for_status()
    feed = feedparser.parse(response.text)

    papers: list[Paper] = []
    for entry in feed.entries:
        link = entry.get("link", "")
        # Stable ID: hash the canonical URL
        paper_id = f"rss:{hashlib.sha1(link.encode()).hexdigest()[:16]}"
        title = entry.get("title", "").strip()
        abstract = entry.get("description", "").strip() or entry.get("summary", "").strip()
        published_struct = entry.get("published", "")
        try:
            published = parsedate_to_datetime(published_struct).date()
        except (TypeError, ValueError):
            published = datetime.now().date()
        authors_raw = entry.get("author", "") or entry.get("dc_creator", "")
        authors = [a.strip() for a in authors_raw.split(",") if a.strip()] if authors_raw else []

        papers.append(
            Paper(
                id=paper_id,
                title=title,
                authors=authors,
                abstract=abstract,
                source=source_name,
                url=link,
                published=published,
                primary_category=source_name,
            )
        )
    return papers
