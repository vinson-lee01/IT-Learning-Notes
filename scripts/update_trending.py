#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 仓库资源整理脚本
"""

import urllib.request
import urllib.parse
import json
import os
import time
from datetime import datetime, timezone, timedelta
from collections import defaultdict

# ══════════════════════════════════════
# 配置
# ══════════════════════════════════════

GH_TOKEN = os.environ.get("GH_TOKEN", "")
CACHE_FILE_ZH = "resources/.cache_zh.json"
CACHE_FILE_EN = "resources/.cache_en.json"

ZH_SEARCHES = [
    {"q": "devops linux 自动化运维",          "label": "DevOps 运维自动化"},
    {"q": "docker kubernetes 容器 部署",      "label": "Docker 容器部署"},
    {"q": "python 自动化运维 脚本",            "label": "Python 运维开发"},
    {"q": "prometheus grafana 监控 告警",     "label": "监控告警"},
    {"q": "ci/cd jenkins gitlab 流水线",      "label": "CI/CD 流水线"},
    {"q": "kubernetes k8s 生产 实践",        "label": "K8s 生产实践"},
    {"q": "nginx 反向代理 负载均衡",           "label": "Nginx 反向代理"},
    {"q": "mysql redis 数据库 优化",            "label": "数据库优化"},
    {"q": "linux shell 脚本 系统管理",          "label": "Linux Shell 脚本"},
    {"q": "ansible terraform 基础设施",         "label": "基础设施即代码"},
]

EN_SEARCHES = [
    {"q": "devops sre infrastructure automation",       "label": "DevOps & SRE"},
    {"q": "docker kubernetes container orchestration",   "label": "Containers & K8s"},
    {"q": "prometheus grafana observability",           "label": "Observability"},
    {"q": "ci/cd pipeline github-actions gitlab",      "label": "CI/CD Pipelines"},
    {"q": "terraform ansible iac infrastructure",        "label": "IaC & Config"},
    {"q": "python automation cloud aws azure",          "label": "Cloud & Python"},
    {"q": "linux administration security hardening",     "label": "Linux & Security"},
    {"q": "mysql postgres redis database clustering",    "label": "Databases"},
    {"q": "llm aiops machine-learning mcp agent",      "label": "AI & AIOps"},
    {"q": "opensource self-hosted privacy tools",        "label": "Self-Hosted"},
    {"q": "kubernetes helm service-mesh istio",        "label": "Service Mesh"},
]


def api_get(url, use_token=True):
    req = urllib.request.Request(url)
    if use_token and GH_TOKEN:
        req.add_header("Authorization", f"token {GH_TOKEN}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "Mozilla/5.0")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode())
    except Exception as e:
        print(f"  API error: {e}")
        return {}


def search_repos(query, label=""):
    url = ("https://api.github.com/search/repositories?" +
            urllib.parse.urlencode({
                "q": query + " stars:>100",
                "sort": "stars",
                "order": "desc",
                "per_page": 30,
            }))
    print(f"  [{label}] {query[:45]}")
    data = api_get(url)
    items = data.get("items", [])
    print(f"     found {len(items)}")
    time.sleep(3)
    return items


def fmt_num(n):
    if n >= 10000:
        return f"{n / 10000:.1f}w"
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


def fmt_date(s):
    if not s:
        return "-"
    try:
        dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
        now = datetime.now(timezone.utc)
        diff = now - dt
        if diff.days == 0:
            return "today"
        if diff.days == 1:
            return "yesterday"
        if diff.days < 30:
            return f"{diff.days}d ago"
        return dt.strftime("%Y-%m-%d")
    except Exception:
        return s[:10]


def quality_score(r):
    stars = r.get("stargazers_count", 0) or 0
    forks = r.get("forks_count", 0) or 0
    score = stars * 10 + forks * 5
    updated = r.get("updated_at", "")
    if updated:
        try:
            dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
            days = (datetime.now(timezone.utc) - dt).days
            if days < 7:
                score += 5000
            elif days < 30:
                score += 2000
        except Exception:
            pass
    return score


def get_level(r):
    stars = r.get("stargazers_count", 0) or 0
    topics = r.get("topics", [])
    desc = (r.get("description") or "").lower()
    if any(w in desc + " ".join(topics) for w in ["tutorial", "入门", "beginner", "从零", "零基础", "guide"]):
        return "Basic"
    if stars < 5000:
        return "Intermediate"
    return "Advanced"


def get_reason(r):
    topics = r.get("topics", [])
    desc = (r.get("description") or "")[:60]
    if "monitoring" in topics or "prometheus" in topics:
        return "Production monitoring essentials"
    if "kubernetes" in topics or "k8s" in topics or "kuber" in r.get("full_name", "").lower():
        return "Container orchestration core tool"
    if "ci-cd" in topics or "pipeline" in topics or "jenkins" in topics:
        return "CI/CD pipeline tool"
    if "docker" in topics:
        return "Container fundamentals"
    if "database" in topics or "mysql" in topics or "redis" in topics:
        return "Database optimization resource"
    if "security" in topics or "hardening" in topics:
        return "Security hardening guide"
    if "tutorial" in topics or "awesome" in topics or "roadmap" in topics:
        return "Curated resource collection"
    if "llm" in topics or "ai" in topics or "mcp" in topics:
        return "AI/Ops emerging topic"
    return desc or "Open source project"


def load_cache(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {"seen": {}, "star_history": {}, "updated": ""}


def save_cache(path, cache):
    cache["updated"] = datetime.now(timezone.utc).isoformat()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)


def run_search(searches, cache, max_new=15):
    all_repos = {}
    new_repos = []
    seen_set = set(cache.get("seen", {}))

    for s in searches:
        items = search_repos(s["q"], s["label"])
        for r in items:
            fn = r["full_name"]
            updated = r.get("updated_at", "")
            try:
                dt = datetime.fromisoformat(updated.replace("Z", "+00:00"))
                if (datetime.now(timezone.utc) - dt).days > 365:
                    continue
            except Exception:
                pass
            if r.get("archived"):
                continue

            all_repos[fn] = r
            r["_dir"] = s["label"]

            if fn not in seen_set:
                seen_set.add(fn)
                new_repos.append(r)
                cache.setdefault("seen", {})[fn] = datetime.now(timezone.utc).isoformat()
                cache.setdefault("star_history", {})[fn] = r.get("stargazers_count", 0) or 0

    new_repos.sort(key=quality_score, reverse=True)
    new_repos = new_repos[:max_new]
    must_see = [r for r in all_repos.values() if quality_score(r) > 200000]
    return new_repos, must_see, all_repos


def render_md(new_repos, must_see, all_repos, cache, lang="zh", searches=None):
    now = datetime.now(timezone(timedelta(hours=8)))
    is_zh = lang == "zh"
    title = "国内优质仓库（中文社区）" if is_zh else "International Repos (English Community)"
    col_desc = "推荐理由" if is_zh else "Reason"
    dir_count = len(searches) if searches else "multiple"

    lines = []
    lines.append(f"# {'CN' if is_zh else 'EN'} Repos\n")
    lines.append(f"> Updated: {now.strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"> New: **{len(new_repos)}** repos | Total: **{len(cache.get('seen', {}))}**\n")
    lines.append("\n---\n")

    if must_see:
        lines.append("\n## Top Picks\n")
        lines.append("| Repo | Stars | Level | Note |\n")
        lines.append("|------|-------|-------|------|\n")
        for r in sorted(must_see, key=quality_score, reverse=True)[:8]:
            fn = r["full_name"]
            url = r["html_url"]
            stars = r.get("stargazers_count", 0) or 0
            level = get_level(r)
            reason = get_reason(r)
            lines.append(f"| [{fn}]({url}) | {fmt_num(stars)} | {level} | {reason} |\n")
        lines.append("\n")

    lines.append("\n## New\n")
    lines.append(f"| Repo | Stars | Forks | Level | {col_desc} |\n")
    lines.append("|------|-------|-------|-------|----------|\n")
    for r in new_repos:
        fn = r["full_name"]
        url = r["html_url"]
        stars = r.get("stargazers_count", 0) or 0
        forks = r.get("forks_count", 0) or 0
        level = get_level(r)
        reason = get_reason(r)
        lines.append(f"| [{fn}]({url}) | {fmt_num(stars)} | {fmt_num(forks)} | {level} | {reason} |\n")

    lines.append("\n---\n\n## By Category\n")
    by_dir = defaultdict(list)
    for r in new_repos:
        by_dir[r.get("_dir", "Other")].append(r)

    for d, repos in by_dir.items():
        lines.append(f"\n### {d} ({len(repos)})\n")
        for r in repos:
            fn = r["full_name"]
            url = r["html_url"]
            stars = r.get("stargazers_count", 0) or 0
            desc = (r.get("description") or "-")[:80]
            lines.append(f"- **[{fn}]({url})** {fmt_num(stars)} - {desc}\n")

    lines.append("\n---\n")
    lines.append(f"\n*{now.strftime('%Y-%m-%d %H:%M')}*")
    return "".join(lines)


def main():
    print("searching repos...")

    print("\n[CN]")
    cache_zh = load_cache(CACHE_FILE_ZH)
    new_zh, must_zh, all_zh = run_search(ZH_SEARCHES, cache_zh, max_new=15)
    md_zh = render_md(new_zh, must_zh, all_zh, cache_zh, lang="zh", searches=ZH_SEARCHES)
    out_zh = "resources/trending_zh.md"
    with open(out_zh, "w", encoding="utf-8") as f:
        f.write(md_zh)
    print(f"  done: {out_zh}")
    save_cache(CACHE_FILE_ZH, cache_zh)

    print("\n[EN]")
    cache_en = load_cache(CACHE_FILE_EN)
    new_en, must_en, all_en = run_search(EN_SEARCHES, cache_en, max_new=15)
    md_en = render_md(new_en, must_en, all_en, cache_en, lang="en", searches=EN_SEARCHES)
    out_en = "resources/trending_en.md"
    with open(out_en, "w", encoding="utf-8") as f:
        f.write(md_en)
    print(f"  done: {out_en}")
    save_cache(CACHE_FILE_EN, cache_en)

    print("\nindex...")
    now = datetime.now(timezone(timedelta(hours=8)))
    top_zh = new_zh[0] if new_zh else None
    top_en = new_en[0] if new_en else None
    summary = f"""# Resources

> Updated: {now.strftime('%Y-%m-%d %H:%M')}

---

## CN

- [Full list](./trending_zh.md)
- New: **{len(new_zh)}**
{(f"- Top: [{top_zh['full_name']}]({top_zh['html_url']}) {fmt_num(top_zh.get('stargazers_count', 0) or 0)}") if top_zh else ""}

## EN

- [Full list](./trending_en.md)
- New: **{len(new_en)}**
{(f"- Top: [{top_en['full_name']}]({top_en['html_url']}) {fmt_num(top_en.get('stargazers_count', 0) or 0)}") if top_en else ""}

---

| File | Desc |
|------|------|
| [trending_zh.md](./trending_zh.md) | CN repos |
| [trending_en.md](./trending_en.md) | EN repos |
| [books.md](./books.md) | Books |
| [communities.md](./communities.md) | Communities |
| [online-labs.md](./online-labs.md) | Labs |

---

*{now.strftime('%Y-%m-%d %H:%M')}*
"""
    with open("resources/trending.md", "w", encoding="utf-8") as f:
        f.write(summary)
    print("  done: trending.md")


if __name__ == "__main__":
    main()
