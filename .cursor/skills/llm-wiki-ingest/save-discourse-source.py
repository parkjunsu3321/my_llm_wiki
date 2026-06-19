#!/usr/bin/env python3
"""Save Discourse topic first post as raw/sources markdown snapshot."""
import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]


def discourse_to_md(json_url: str, out_name: str, title: str, meta: dict) -> Path:
    req = urllib.request.Request(json_url, headers={"User-Agent": "llm-wiki-ingest/1.0"})
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    post = data["post_stream"]["posts"][0]
    body = post.get("raw") or post.get("cooked", "")
    if "<" in body and ">" in body:
        body = re.sub(r"<br\s*/?>", "\n", body)
        body = re.sub(r"</p>", "\n\n", body)
        body = re.sub(r"<[^>]+>", "", body)
        body = re.sub(r"\n{3,}", "\n\n", body).strip()
    fm = ["---"]
    fm.append(f'title: "{title}"')
    for k, v in meta.items():
        fm.append(f"{k}: {v}")
    fm.append(f"fetched: {date.today().isoformat()}")
    fm.append("---")
    fm.append("")
    content = "\n".join(fm) + f"\n# {title}\n\n{body}\n"
    out = VAULT / "raw" / "sources" / out_name
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(content, encoding="utf-8")
    print(out)
    return out


if __name__ == "__main__":
    discourse_to_md(sys.argv[1], sys.argv[2], sys.argv[3], json.loads(sys.argv[4]))
