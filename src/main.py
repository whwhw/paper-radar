"""Pipeline orchestration: fetch → dedupe → score → summarize → render → notify."""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

from src.config import (
    ARCHIVE_DIR,
    ARXIV_CATEGORIES,
    ARXIV_MAX_RESULTS,
    DAILY_OUTPUT_TARGET,
    MIN_SCORE_THRESHOLD,
    RSS_FEEDS,
    SCORING_POOL_SIZE,
)
from src.dedupe import load_seen_ids
from src.llm import build_client, load_config_from_env
from src.models import Area, Paper, Score, Summary
from src.render import write_paper_note
from src.scoring import score_paper, select_top
from src.sources import fetch_arxiv, fetch_rss
from src.summarize import generate_summary
from src.telegram import send_paper_notification

log = logging.getLogger("paper_radar")


def gather_candidates() -> list[tuple[Paper, Area]]:
    candidates: list[tuple[Paper, Area]] = []

    for cat in ARXIV_CATEGORIES:
        try:
            papers = fetch_arxiv(category=cat, max_results=ARXIV_MAX_RESULTS)
            candidates.extend((p, "ai") for p in papers)
            log.info("arxiv %s: %d papers", cat, len(papers))
        except Exception as e:
            log.warning("arxiv %s failed: %s", cat, e)

    for feed in RSS_FEEDS:
        try:
            papers = fetch_rss(url=feed["url"], source_name=feed["name"])
            candidates.extend((p, feed["area"]) for p in papers)
            log.info("rss %s: %d papers", feed["name"], len(papers))
        except Exception as e:
            log.warning("rss %s failed: %s", feed["name"], e)

    return candidates


def run_pipeline(
    archive_dir: Path,
    llm_client: OpenAI,
    llm_model: str,
    bot_token: str,
    chat_id: str,
    archive_base_url: str,
    dry_run: bool = False,
) -> list[Path]:
    """Run one full daily pipeline. Returns paths of newly written paper notes."""
    log.info("=== paper-radar starting ===")

    candidates = gather_candidates()
    log.info("total candidates: %d", len(candidates))

    seen = load_seen_ids(archive_dir)
    log.info("already seen: %d", len(seen))

    seen_ids = set(seen)
    fresh_pairs: list[tuple[Paper, Area]] = []
    for p, a in candidates:
        if p.id not in seen_ids:
            fresh_pairs.append((p, a))
            seen_ids.add(p.id)  # dedupe within this batch too
    log.info("fresh after dedupe: %d", len(fresh_pairs))

    if not fresh_pairs:
        log.info("no fresh candidates — exiting")
        return []

    pool = fresh_pairs[:SCORING_POOL_SIZE]
    log.info("scoring %d candidates with LLM (%s)", len(pool), llm_model)

    scored: list[tuple[Paper, Score, Area]] = []
    for paper, area in pool:
        try:
            score = score_paper(paper, client=llm_client, model=llm_model)
            scored.append((paper, score, area))
        except Exception as e:
            log.warning("scoring failed for %s: %s", paper.id, e)

    pairs_for_select = [(p, s) for p, s, _ in scored]
    top = select_top(pairs_for_select, threshold=MIN_SCORE_THRESHOLD, n=DAILY_OUTPUT_TARGET)

    if not top:
        log.info("no candidates ≥ %.1f — shipping nothing today", MIN_SCORE_THRESHOLD)
        return []

    area_map = {p.id: a for p, _, a in scored}

    written: list[Path] = []
    for paper, score in top:
        area = area_map.get(paper.id, "ai")
        try:
            summary = generate_summary(paper, client=llm_client, model=llm_model)
        except Exception as e:
            log.warning("summary failed for %s: %s — skipping", paper.id, e)
            continue

        path = write_paper_note(paper, score, summary, area=area, archive_dir=archive_dir)
        written.append(path)
        log.info("wrote %s (score=%.2f)", path.name, score.total)

        if dry_run:
            continue

        archive_url = f"{archive_base_url.rstrip('/')}/{path.name}"
        try:
            send_paper_notification(
                bot_token=bot_token,
                chat_id=chat_id,
                title=paper.title,
                score=score.total,
                one_liner=summary.one_line_conclusion,
                area=area,
                source=paper.source,
                archive_url=archive_url,
            )
        except Exception as e:
            log.warning("telegram send failed for %s: %s", paper.id, e)

    log.info("=== done. %d papers written ===", len(written))
    return written


def cli() -> int:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    load_dotenv()

    bot_token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = os.environ.get("TELEGRAM_CHAT_ID", "")
    archive_base_url = os.environ.get(
        "ARCHIVE_BASE_URL",
        "https://github.com/your-user/paper-radar/blob/main/archive",
    )
    dry_run = "--dry-run" in sys.argv

    try:
        llm_cfg = load_config_from_env()
    except RuntimeError as e:
        log.error("LLM config error: %s", e)
        return 1

    if not dry_run and (not bot_token or not chat_id):
        log.error("TELEGRAM_BOT_TOKEN/TELEGRAM_CHAT_ID not set (use --dry-run to skip)")
        return 1

    client = build_client(llm_cfg)

    written = run_pipeline(
        archive_dir=ARCHIVE_DIR,
        llm_client=client,
        llm_model=llm_cfg.model,
        bot_token=bot_token,
        chat_id=chat_id,
        archive_base_url=archive_base_url,
        dry_run=dry_run,
    )
    log.info("written: %d", len(written))
    return 0


if __name__ == "__main__":
    raise SystemExit(cli())
