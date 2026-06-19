#!/usr/bin/env python3
"""Backfill raw/sources snapshots for URL-only ingests."""
import importlib.util
import json
import re
import urllib.request
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
SOURCES = VAULT / "raw" / "sources"
TODAY = date.today().isoformat()

_ht = importlib.util.spec_from_file_location(
    "html_to_text", Path(__file__).parent / "html-to-text.py"
)
_ht_mod = importlib.util.module_from_spec(_ht)
_ht.loader.exec_module(_ht_mod)
html_to_text = _ht_mod.html_to_text
is_html = _ht_mod.is_html


def write_source(filename: str, title: str, meta: dict, body: str) -> None:
    lines = ["---", f'title: "{title}"']
    for k, v in meta.items():
        if isinstance(v, str) and (":" in v or '"' in v):
            lines.append(f'{k}: "{v}"')
        else:
            lines.append(f"{k}: {v}")
    lines.extend([f"fetched: {TODAY}", "---", "", f"# {title}", "", body.strip(), ""])
    path = SOURCES / filename
    path.write_text("\n".join(lines), encoding="utf-8")
    print("wrote", path)


def fetch_url(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "llm-wiki-ingest/1.0"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_article_text(url: str) -> str:
    """Return markdown/plain text for raw/sources. Never store raw HTML."""
    if url.endswith(".md") or "/topic/" in url and url.endswith(".md"):
        return fetch_url(url).strip()
    body = fetch_url(url)
    if is_html(body):
        body = html_to_text(body)
    if is_html(body):
        raise ValueError(f"HTML→text conversion failed: {url}")
    return body.strip()


def discourse_body(json_url: str) -> str:
    data = json.loads(fetch_url(json_url))
    post = data["post_stream"]["posts"][0]
    body = post.get("raw") or ""
    if not body.strip():
        cooked = post.get("cooked", "")
        body = re.sub(r"<br\s*/?>", "\n", cooked)
        body = re.sub(r"</p>", "\n\n", body)
        body = re.sub(r"<[^>]+>", "", body)
        body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def main():
    write_source(
        "2026-06-16-discuss-pytorchkr-obsidian-second-brain-10730.md",
        "obsidian-second-brain: Obsidian Vault AI 세컨드 브레인",
        {
            "source_url": "https://discuss.pytorch.kr/t/obsidian-second-brain-obsidian-vault-ai/10730",
            "author": "9bow(박정환)",
            "published": "2026-06-16",
            "assets": "raw/assets/obsidian-second-brain_1.png, raw/assets/obsidian-second-brain_2.png",
            "note": "PyTorchKR 커뮤니티 게시물. GPT로 정리된 글 기반이며 원문 의도와 다를 수 있음.",
        },
        discourse_body("https://discuss.pytorch.kr/t/obsidian-second-brain-obsidian-vault-ai/10730.json"),
    )
    write_source(
        "2026-06-17-discuss-pytorchkr-vibethinker-3b-10748.md",
        "VibeThinker-3B: 3B 파라미터 프론티어급 추론",
        {
            "source_url": "https://discuss.pytorch.kr/t/vibethinker-3b-3b-feat-weibo-ai/10748",
            "author": "9bow(박정환)",
            "published": "2026-06-17",
            "assets": "raw/assets/vibethinker_1.png .. vibethinker_4.png",
            "note": "PyTorchKR 커뮤니티 게시물. GPT로 정리된 글 기반이며 원문 의도와 다를 수 있음.",
        },
        discourse_body("https://discuss.pytorch.kr/t/vibethinker-3b-3b-feat-weibo-ai/10748.json"),
    )
    write_source(
        "2025-10-20-geeknews-sdd-tools-23776.md",
        "스펙 주도 개발(SDD) — Kiro, Spec-Kit, Tessl",
        {
            "source_url": "https://news.hada.io/topic?id=23776",
            "original_url": "https://martinfowler.com/articles/exploring-gen-ai/sdd-tools.html",
            "author": "Birgitta Böckeler (via GeekNews xguru)",
            "published": "2025-10-20",
            "note": "GeekNews #23776 요약. 원문 Fowler 기사 병행 확인 권장.",
        },
        fetch_url("https://news.hada.io/topic/23776.md"),
    )
    write_source(
        "2026-06-15-kakaopay-ifkakao-agentic-coding-spec-kit.md",
        "SDD (Spec-kit) 에이전트 코딩 실전기 — 카카오페이",
        {
            "source_url": "https://tech.kakaopay.com/post/ifkakao-agentic-coding/",
            "author": "wayne (카카오페이 AI 플랫폼팀)",
            "event": "if(kakao)25",
            "note": "카카오페이 기술 블로그. HTML→텍스트 추출. 일부 생성형 AI 사용 콘텐츠 포함.",
        },
        fetch_article_text("https://tech.kakaopay.com/post/ifkakao-agentic-coding/"),
    )
    write_source(
        "2026-06-15-tsyang-sdd-context-engineering-224.md",
        "스펙 주도 개발 (SDD) — Context Engineering 관점",
        {
            "source_url": "https://tsyang.tistory.com/224",
            "author": "tsyang",
            "blog": "게임 클라 개발",
            "note": "티스토리 AI코딩 카테고리. HTML→텍스트 추출.",
        },
        fetch_article_text("https://tsyang.tistory.com/224"),
    )


if __name__ == "__main__":
    main()
