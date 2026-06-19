#!/usr/bin/env python3
"""Extract image URLs from Discourse topic JSON."""
import json
import re
import sys
import urllib.request

def main():
    url = sys.argv[1]
    req = urllib.request.Request(url, headers={"User-Agent": "llm-wiki-ingest/1.0"})
    with urllib.request.urlopen(req) as resp:
        data = json.load(resp)
    imgs = []
    for post in data["post_stream"]["posts"]:
        cooked = post.get("cooked", "")
        for m in re.finditer(r'<img[^>]+src="([^"]+)"', cooked):
            imgs.append(m.group(1))
    for u in imgs:
        print(u)

if __name__ == "__main__":
    main()
