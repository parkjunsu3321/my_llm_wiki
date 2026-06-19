#!/usr/bin/env python3
"""Replace HTML dumps in raw/sources with extracted plain text."""
import importlib.util
import urllib.request
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
SOURCES = VAULT / "raw" / "sources"
TODAY = date.today().isoformat()

_ht = importlib.util.spec_from_file_location(
    "html_to_text", Path(__file__).parent / "html-to-text.py"
)
ht = importlib.util.module_from_spec(_ht)
_ht.loader.exec_module(ht)


def fetch_url(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "llm-wiki-ingest/1.0"})
    with urllib.request.urlopen(req) as resp:
        return resp.read().decode("utf-8", errors="replace")


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
    print("fixed", path)


FIXES = [
    (
        "2026-06-15-kakaopay-ifkakao-agentic-coding-spec-kit.md",
        "SDD (Spec-kit) 에이전트 코딩 실전기 — 카카오페이",
        {
            "source_url": "https://tech.kakaopay.com/post/ifkakao-agentic-coding/",
            "author": "wayne (카카오페이 AI 플랫폼팀)",
            "event": "if(kakao)25",
            "note": "카카오페이 기술 블로그. HTML→텍스트 추출(article). 일부 생성형 AI 사용 콘텐츠 포함.",
        },
        "https://tech.kakaopay.com/post/ifkakao-agentic-coding/",
    ),
    (
        "2026-06-15-tsyang-sdd-context-engineering-224.md",
        "스펙 주도 개발 (SDD) — Context Engineering 관점",
        {
            "source_url": "https://tsyang.tistory.com/224",
            "author": "tsyang",
            "blog": "게임 클라 개발",
            "note": "티스토리 AI코딩 카테고리. HTML→텍스트 추출(article).",
        },
        "https://tsyang.tistory.com/224",
    ),
]


def main():
    force = "--force" in __import__("sys").argv
    for filename, title, meta, url in FIXES:
        path = SOURCES / filename
        if path.exists() and not force:
            body_part = path.read_text(encoding="utf-8").split("---", 2)[-1]
            if not ht.is_html(body_part):
                print("skip (already text)", path)
                continue
        raw = fetch_url(url)
        body = ht.html_to_text(raw, article_only=True)
        if ht.is_html(body):
            raise SystemExit(f"conversion failed for {url}")
        write_source(filename, title, meta, body)


if __name__ == "__main__":
    main()
