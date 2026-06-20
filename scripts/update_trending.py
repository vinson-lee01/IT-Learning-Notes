#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Trending Repos Fetcher
- Searches CN & EN DevOps/SRE repos daily
- Deduplicates across runs (cache)
- Outputs: resources/trending_zh.md + trending_en.md + trending.md
"""

import urllib.request
import urllib.parse
import json
import os
import time
from datetime import datetime, timezone, timedelta
from collections import defaultdict

# ──────────────────────────────────────────
# Config
# ──────────────────────────────────────────

GH_TOKEN = os.environ.get("GH_TOKEN", "")
CACHE_FILE_ZH = "resources/.cache_zh.json"
CACHE_FILE_EN = "resources/.cache_en.json"

ZH_SEARCHES = [
    {"q": "devops linux 自动化运维 脚本",           "label": "DevOps 运维自动化"},
    {"q": "docker kubernetes 容器 编排 部署",       "label": "Docker 容器编排"},
    {"q": "python 自动化运维 ansible",              "label": "Python 运维开发"},
    {"q": "prometheus grafana 监控 告警 可视化",    "label": "监控告警"},
    {"q": "ci/cd jenkins gitlab github-actions",    "label": "CI/CD 流水线"},
    {"q": "kubernetes k8s ingress service 生产",    "label": "K8s 生产实践"},
    {"q": "nginx 反向代理 负载均衡 高可用",          "label": "Nginx 反向代理"},
    {"q": "mysql redis postgresql 数据库 优化 备份", "label": "数据库优化"},
    {"q": "linux shell 脚本 系统管理 安全加固",       "label": "Linux Shell 脚本"},
    {"q": "terraform ansible 基础设施 即代码 iac",   "label": "基础设施即代码"},
    {"q": "云原生 微服务 service-mesh istio",         "label": "云原生 & Service Mesh"},
    {"q": "sre 站点可靠性 错误预算 告警管理",          "label": "SRE 方法论"},
]

EN_SEARCHES = [
    {"q": "devops sre infrastructure automation platform",       "label": "DevOps & SRE"},
    {"q": "docker kubernetes container orchestration production", "label": "Containers & K8s"},
    {"q": "prometheus grafana observability monitoring alerting", "label": "Observability"},
    {"q": "ci/cd pipeline github-actions gitlab-jenkins",        "label": "CI/CD Pipelines"},
    {"q": "terraform ansible iac infrastructure provisioning",     "label": "IaC & Config"},
    {"q": "python automation cloud aws azure gcp",               "label": "Cloud & Python"},
    {"q": "linux administration security hardening audit",         "label": "Linux & Security"},
    {"q": "postgres mysql redis database clustering backup",      "label": "Databases"},
    {"q": "llm aiops machine-learning mcp agent automation",    "label": "AI & AIOps"},
    {"q": "self-hosted privacy opensource homelab",              "label": "Self-Hosted"},
    {"q": "kubernetes helm service-mesh istio envoy",           "label": "Service Mesh"},
    {"q": "gitops flux argo-cd deployment automation",           "label": "GitOps"},
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
        print(f"    API error: {e}")
        return {}


def search_repos(query, label=""):
    url = ("https://api.github.com/search/repositories?" +
            urllib.parse.urlencode({
                "q": query + " stars:>50 pushed:>2024-01-01",
                "sort": "stars",
                "order": "desc",
                "per_page": 30,
            }))
    print(f"  [{label}] {query[:50]}")
    data = api_get(url)
    items = data.get("items", [])
    total = data.get("total_count", 0)
    print(f"     found {len(items)} / {total} total")
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
            elif days < 90:
                score += 500
        except Exception:
            pass
    return score


def get_level(r):
    stars = r.get("stargazers_count", 0) or 0
    topics = r.get("topics", [])
    desc = (r.get("description") or "").lower()
    name = r.get("name", "").lower()
    if any(w in desc + " " + " ".join(topics) + " " + name
           for w in ["tutorial", "入门", "beginner", "guide", "101", "getting-started"]):
        return "Basic"
    if stars < 3000:
        return "Intermediate"
    return "Advanced"


def get_badge(r):
    stars = r.get("stargazers_count", 0) or 0
    topics = r.get("topics", [])
    desc = (r.get("description") or "").lower()
    full_name = r.get("full_name", "").lower()
    name = r.get("name", "").lower()
    if "awesome" in topics or "awesome" in full_name or "curated" in desc:
        return "collection"
    if "tutorial" in topics or "tutorial" in full_name or "learn" in desc:
        return "tutorial"
    if "tool" in desc or "cli" in desc or r.get("topics"):
        return "tool"
    return "project"


def get_reason(r, lang="zh"):
    topics = r.get("topics", [])
    desc = (r.get("description") or "")[:80]
    full_name = r.get("full_name", "").lower()
    name = r.get("name", "").lower()

    if "prometheus" in full_name or "grafana" in full_name:
        return "生产监控核心组件" if lang == "zh" else "Core monitoring component"
    if "kubernetes" in full_name or "k8s" in full_name or "kuber" in full_name:
        return "容器编排核心工具" if lang == "zh" else "Container orchestration"
    if "jenkins" in full_name or "gitlab" in full_name or "github-actions" in full_name:
        return "CI/CD 流水线工具" if lang == "zh" else "CI/CD pipeline tool"
    if "docker" in full_name:
        return "容器化基础工具" if lang == "zh" else "Container fundamentals"
    if "terraform" in full_name or "ansible" in full_name:
        return "基础设施即代码" if lang == "zh" else "Infrastructure as Code"
    if "nginx" in full_name:
        return "高性能反向代理" if lang == "zh" else "High-perf reverse proxy"
    if "mysql" in full_name or "redis" in full_name or "postgres" in full_name:
        return "数据库优化资源" if lang == "zh" else "Database optimization"
    if "awesome" in full_name or "awesome" in name:
        return "精选资源合集" if lang == "zh" else "Curated resource list"
    if "tutorial" in full_name or "guide" in full_name:
        return "系统学习教程" if lang == "zh" else "Systematic tutorial"
    if "aiops" in full_name or "llm" in full_name or "mcp" in full_name:
        return "AI运维新兴方向" if lang == "zh" else "AI/Ops emerging topic"
    return desc or ("Open source project" if lang == "en" else "开源项目")


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


def run_search(searches, cache, max_new=20):
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
    title = "国内优质仓库（中文社区）" if is_zh else "International Repos (Global Community)"
    col_desc = "推荐理由" if is_zh else "Why recommended"
    col_updated = "最近更新" if is_zh else "Last updated"

    total_seen = len(cache.get("seen", {}))

    lines = []
    lines.append(f"# {'🇨🇳' if is_zh else '🌍'} Trending Repos\n")
    lines.append(f"> Updated: {now.strftime('%Y-%m-%d %H:%M')} (Beijing Time)\n")
    lines.append(f"> 🆕 New today: **{len(new_repos)}** | 📦 Total tracked: **{total_seen}** | 🔥 Hot: **{len(must_see)}**\n")
    lines.append("\n---\n")

    # Hot picks (high quality score)
    if must_see:
        lines.append("\n## 🔥 Hot Picks (100k+ quality score)\n")
        lines.append("| Repo | ⭐ Stars | 🍴 Forks | Level | Note |\n")
        lines.append("|------|---------|----------|-------|------|\n")
        for r in sorted(must_see, key=quality_score, reverse=True)[:8]:
            fn = r["full_name"]
            url = r["html_url"]
            stars = r.get("stargazers_count", 0) or 0
            forks = r.get("forks_count", 0) or 0
            level = get_level(r)
            reason = get_reason(r, lang=lang)
            lines.append(f"| [{fn}]({url}) | {fmt_num(stars)} | {fmt_num(forks)} | {level} | {reason} |\n")
        lines.append("\n")

    # New repos
    lines.append("\n## 🆕 Newly Discovered\n")
    lines.append(f"| Repo | ⭐ Stars | 🍴 Forks | Level | {col_desc} |\n")
    lines.append(f"|------|---------|----------|-------|----------|\n")
    for r in new_repos:
        fn = r["full_name"]
        url = r["html_url"]
        stars = r.get("stargazers_count", 0) or 0
        forks = r.get("forks_count", 0) or 0
        level = get_level(r)
        reason = get_reason(r, lang=lang)
        lines.append(f"| [{fn}]({url}) | {fmt_num(stars)} | {fmt_num(forks)} | {level} | {reason} |\n")

    # By category
    lines.append("\n---\n\n## 📂 By Category\n")
    by_dir = defaultdict(list)
    for r in new_repos:
        by_dir[r.get("_dir", "Other")].append(r)

    for d, repos in sorted(by_dir.items()):
        lines.append(f"\n### {d} ({len(repos)} new)\n")
        for r in repos:
            fn = r["full_name"]
            url = r["html_url"]
            stars = r.get("stargazers_count", 0) or 0
            desc = (r.get("description") or "-")[:100]
            lines.append(f"- **[{fn}]({url})** ⭐{fmt_num(stars)} — {desc}\n")

    # Language distribution (top repos)
    lines.append("\n---\n\n## 📊 This Week's Stats\n")
    lang_count = defaultdict(int)
    for r in list(all_repos.values())[:50]:
        lang = r.get("language") or "Other"
        lang_count[lang] += 1
    lines.append("\n**Language distribution (top 50):**\n")
    for lang, cnt in sorted(lang_count.items(), key=lambda x: -x[1])[:8]:
        lines.append(f"- `{lang}`: {cnt} repos\n")

    lines.append(f"\n---\n")
    lines.append(f"\n*Updated: {now.strftime('%Y-%m-%d %H:%M')} (Beijing Time)*  \n")
    lines.append(f"*Maintained by [vinson-lee](https://github.com/vinson-lee01)*\n")
    return "".join(lines)


def main():
    print("🚀 Searching repos (CN + EN)...")

    print("\n[CN] Chinese community repos")
    print("-" * 50)
    cache_zh = load_cache(CACHE_FILE_ZH)
    new_zh, must_zh, all_zh = run_search(ZH_SEARCHES, cache_zh, max_new=20)
    md_zh = render_md(new_zh, must_zh, all_zh, cache_zh, lang="zh", searches=ZH_SEARCHES)
    out_zh = "resources/trending_zh.md"
    with open(out_zh, "w", encoding="utf-8") as f:
        f.write(md_zh)
    print(f"  ✅ Done: {out_zh} ({len(new_zh)} new, {len(cache_zh.get('seen', {}))} total)")
    save_cache(CACHE_FILE_ZH, cache_zh)

    print("\n[EN] International community repos")
    print("-" * 50)
    cache_en = load_cache(CACHE_FILE_EN)
    new_en, must_en, all_en = run_search(EN_SEARCHES, cache_en, max_new=20)
    md_en = render_md(new_en, must_en, all_en, cache_en, lang="en", searches=EN_SEARCHES)
    out_en = "resources/trending_en.md"
    with open(out_en, "w", encoding="utf-8") as f:
        f.write(md_en)
    print(f"  ✅ Done: {out_en} ({len(new_en)} new, {len(cache_en.get('seen', {}))} total)")
    save_cache(CACHE_FILE_EN, cache_en)

    # Index file — build with lines list to avoid f-string syntax errors
    print("\n📊 Index...")
    now = datetime.now(timezone(timedelta(hours=8)))

    idx_lines = []
    idx_lines.append("# 📊 Resources Index\n\n")
    idx_lines.append(f"> 🕐 Updated: {now.strftime('%Y-%m-%d %H:%M')} (Beijing Time)\n\n")
    idx_lines.append("---\n\n")

    # CN section
    idx_lines.append("## 🇨🇳 Chinese Community (CN)\n\n")
    idx_lines.append("- 📄 [Full list](./trending_zh.md)\n")
    idx_lines.append(f"- 🆕 New today: **{len(new_zh)}**\n")
    if new_zh:
        top = new_zh[0]
        stars_str = fmt_num(top.get("stargazers_count", 0) or 0)
        idx_lines.append(f"- 🔥 Top pick: [{top['full_name']}]({top['html_url']}) ⭐{stars_str}\n")
    else:
        idx_lines.append("- 🔥 Top pick: (none today)\n")
    idx_lines.append("\n---\n\n")

    # EN section
    idx_lines.append("## 🌍 International (EN)\n\n")
    idx_lines.append("- 📄 [Full list](./trending_en.md)\n")
    idx_lines.append(f"- 🆕 New today: **{len(new_en)}**\n")
    if new_en:
        top = new_en[0]
        stars_str = fmt_num(top.get("stargazers_count", 0) or 0)
        idx_lines.append(f"- 🔥 Top pick: [{top['full_name']}]({top['html_url']}) ⭐{stars_str}\n")
    else:
        idx_lines.append("- 🔥 Top pick: (none today)\n")
    idx_lines.append("\n---\n\n")

    # All resources table
    idx_lines.append("## 📚 All Resources\n\n")
    idx_lines.append("| File | Description |\n")
    idx_lines.append("|------|-------------|\n")
    idx_lines.append("| [trending_zh.md](./trending_zh.md) | 🇨🇳 CN repos (updated daily) |\n")
    idx_lines.append("| [trending_en.md](./trending_en.md) | 🌍 EN repos (updated daily) |\n")
    idx_lines.append("| [books.md](./books.md) | 📚 Recommended books |\n")
    idx_lines.append("| [communities.md](./communities.md) | 💬 Communities & Forums |\n")
    idx_lines.append("| [online-labs.md](./online-labs.md) | 🧪 Online labs & Sandboxes |\n")
    idx_lines.append("\n---\n\n")
    idx_lines.append(f"*Updated: {now.strftime('%Y-%m-%d %H:%M')} (Beijing Time)*  \n")
    idx_lines.append("*Maintained by [vinson-lee](https://github.com/vinson-lee01)*\n")

    with open("resources/trending.md", "w", encoding="utf-8") as f:
        f.write("".join(idx_lines))
    print("  ✅ Done: resources/trending.md")

    print("\n✅ All done!")


if __name__ == "__main__":
    main()
