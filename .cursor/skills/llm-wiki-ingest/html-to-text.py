#!/usr/bin/env python3
"""Minimal HTML → plain text/markdown-ish (stdlib only). For raw/sources snapshots."""
import html as html_module
import re


def extract_article_html(html: str) -> str:
    m = re.search(r"(?is)<article[^>]*>([\s\S]*?)</article>", html)
    if m:
        return m.group(1)
    m = re.search(r'(?is)itemprop="articleBody"[^>]*>([\s\S]*?)</', html)
    if m:
        return m.group(1)
    return html


def html_to_text(html: str, *, article_only: bool = True) -> str:
    if article_only:
        html = extract_article_html(html)
    html = re.sub(r"(?is)<script[^>]*>.*?</script>", "", html)
    html = re.sub(r"(?is)<style[^>]*>.*?</style>", "", html)
    html = re.sub(r"(?is)<noscript[^>]*>.*?</noscript>", "", html)
    html = re.sub(r"(?i)<br\s*/?>", "\n", html)
    html = re.sub(r"(?i)</p>", "\n\n", html)
    html = re.sub(r"(?i)</h([1-6])>", r"\n\n", html)
    html = re.sub(r"(?i)<h([1-6])[^>]*>", r"\n\n# ", html)
    html = re.sub(r"(?i)<li[^>]*>", "\n- ", html)
    html = re.sub(r"<[^>]+>", "", html)
    text = html_module.unescape(html)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def is_html(content: str) -> bool:
    head = content.lstrip()[:800].lower()
    return head.startswith("<!doctype") or "<html" in head
