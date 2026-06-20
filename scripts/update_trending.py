#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub Trending Repos Fetcher - Optimized Version
- Searches CN & EN DevOps/SRE repos daily
- Deduplicates across runs (cache)
- Outputs: resources/trending_zh.md + trending_en.md + trending.md
- Improved: better error handling, rate limit detection, detailed logging
"""

import urllib.request
import urllib.parse
import json
import os
import time
import sys
from datetime import datetime, timezone, timedelta
from collections import defaultdict

# ──────────────────────────────────────────
# Config
# ──────────────────────────────────────────

GH_TOKEN = os.environ.get("GH_TOKEN", "")
CACHE_FILE_ZH = "resources/.cache_zh.json"
CACHE_FILE_EN = "resources/.cache_en.json"
RATE_LIMIT_WAIT = 60  # seconds to wait if rate limited

ZH_SEARCHES = [
    {"q": "language:zh devops",                    "label": "DevOps 中文"},
    {"q": "language:zh docker k8s",               "label": "Docker K8s 中文"},
    {"q": "language:zh prometheus grafana",        "label": "监控 中文"},
    {"q": "language:zh ci/cd",                     "label": "CI/CD 中文"},
    {"q": "language:zh terraform ansible",          "label": "IaC 中文"},
    {"q": "language:zh sre 运维",                  "label": "SRE 中文"},
]

EN_SEARCHES = [
    {"q": "devops stars:>1000",                     "label": "DevOps"},
    {"q": "kubernetes stars:>1000",                 "label": "Kubernetes"},
    {"q": "prometheus monitoring stars:>1000",       "label": "Monitoring"},
    {"q": "terraform ansible stars:>1000",          "label": "IaC"},
    {"q": "ci/cd github-actions stars:>1000",      "label": "CI/CD"},
    {"q": "sre site-reliability stars:>1000",       "label": "SRE"},
]


def log(msg, level="INFO"):
    """Print log with timestamp."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    prefix = {"INFO": "ℹ️", "WARN": "⚠️", "ERROR": "❌", "SUCCESS": "✅"}[level]
    print(f"[{timestamp}] {prefix} {msg}", flush=True)


def api_get(url, use_token=True, max_retries=3):
    """Make API request with retry and rate limit handling."""
    for attempt in range(max_retries):
        try:
            req = urllib.request.Request(url)
            if use_token and GH_TOKEN:
                req.add_header("Authorization", f"token {GH_TOKEN}")
            req.add_header("Accept", "application/vnd.github.v3+json")
            req.add_header("User-Agent", "OpsRoadmapBot/1.0")
            
            with urllib.request.urlopen(req, timeout=15) as resp:
                # Check rate limit headers
                remaining = resp.getheader("X-RateLimit-Remaining")
                reset_time = resp.getheader("X-RateLimit-Reset")
                
                if remaining and int(remaining) < 5:
                    log(f"Rate limit low: {remaining} remaining", "WARN")
                    if reset_time:
                        reset_dt = datetime.fromtimestamp(int(reset_time))
                        wait_sec = (reset_dt - datetime.now()).total_seconds()
                        if wait_sec > 0:
                            log(f"Waiting {wait_sec:.0f}s for rate limit reset", "WARN")
                            time.sleep(min(wait_sec + 5, RATE_LIMIT_WAIT))
                
                return json.loads(resp.read().decode())
                
        except urllib.error.HTTPError as e:
            if e.code == 403:  # Rate limited
                log(f"Rate limited (attempt {attempt+1}/{max_retries})", "WARN")
                time.sleep(RATE_LIMIT_WAIT)
            elif e.code == 404:
                log(f"Not found: {url[:100]}", "ERROR")
                return {}
            else:
                log(f"HTTP error {e.code}: {e.reason}", "ERROR")
                if attempt == max_retries - 1:
                    return {}
                time.sleep(5)
        except Exception as e:
            log(f"API error: {e} (attempt {attempt+1}/{max_retries})", "ERROR")
            if attempt == max_retries - 1:
                return {}
            time.sleep(3)
    
    return {}


def search_repos(query, label=""):
    """Search GitHub repositories with error handling."""
    params = {
        "q": query + " stars:>50 pushed:>2024-01-01",
        "sort": "stars",
        "order": "desc",
        "per_page": 30,
    }
    url = "https://api.github.com/search/repositories?" + urllib.parse.urlencode(params)
    
    log(f"[{label}] Searching: {query[:50]}")
    data = api_get(url)
    
    if not data:
        log(f"[{label}] No data returned", "WARN")
        return []
    
    items = data.get("items", [])
    total = data.get("total_count", 0)
    log(f"[{label}] Found {len(items)} / {total} total repos")
    time.sleep(2)  # Reduced from 3 to 2 seconds
    return items


def fmt_num(n):
    """Format number with k/w suffix."""
    try:
        n = int(n)
        if n >= 10000:
            return f"{n / 10000:.1f}w"
        if n >= 1000:
            return f"{n / 1000:.1f}k"
        return str(n)
    except (ValueError, TypeError):
        return str(n)


def fmt_date(s):
    """Format date string to relative time."""
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
    """Calculate quality score for ranking."""
    stars = r.get("stargazers_count", 0) or 0
    forks = r.get("forks_count", 0) or 0
    score = stars * 10 + forks * 5
    
    # Bonus for recent updates
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
    
    # Bonus for good description
    desc = r.get("description") or ""
    if desc and len(desc) > 50:
        score += 500
    
    return score


def get_level(r):
    """Determine difficulty level."""
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
    """Determine repo type badge."""
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
    """Generate recommendation reason."""
    topics = r.get("topics", [])
    desc = (r.get("description") or "")[:80]
    full_name = r.get("full_name", "").lower()
    name = r.get("name", "").lower()
    
    # Smart matching
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
    """Load cache from file."""
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        log(f"Cache not found: {path}", "WARN")
        return {"seen": {}, "star_history": {}, "updated": ""}


def save_cache(path, cache):
    """Save cache to file."""
    cache["updated"] = datetime.now(timezone.utc).isoformat()
    with open(path, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)
    log(f"Cache saved: {path}", "SUCCESS")


def run_search(searches, cache, max_new=20):
    """Run searches and return new repos."""
    all_repos = {}
    new_repos = []
    seen_set = set(cache.get("seen", {}))
    
    log(f"Starting {len(searches)} searches...")
    
    for i, s in enumerate(searches):
        log(f"Progress: {i+1}/{len(searches)} - {s['label']}")
        items = search_repos(s["q"], s["label"])
        
        for r in items:
            fn = r["full_name"]
            updated = r.get("updated_at", "")
            
            # Filter old or archived repos
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
            
            # Check if new
            if fn not in seen_set:
                seen_set.add(fn)
                new_repos.append(r)
                cache.setdefault("seen", {})[fn] = datetime.now(timezone.utc).isoformat()
                cache.setdefault("star_history", {})[fn] = r.get("stargazers_count", 0) or 0
    
    new_repos.sort(key=quality_score, reverse=True)
    new_repos = new_repos[:max_new]
    
    must_see = [r for r in all_repos.values() if quality_score(r) > 200000]
    
    log(f"Found {len(new_repos)} new repos, {len(must_see)} hot repos", "SUCCESS")
    return new_repos, must_see, all_repos


def render_md(new_repos, must_see, all_repos, cache, lang="zh", searches=None):
    """Render markdown output."""
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
    
    # Hot picks
    if must_see:
        lines.append("\n## 🔥 Hot Picks (200k+ quality score)\n")
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
    if new_repos:
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
    else:
        lines.append("\n## 🆕 Newly Discovered\n")
        lines.append("> No new repos today. Check back tomorrow!\n")
    
    # By category
    if new_repos:
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
    
    # Language distribution
    lines.append("\n---\n\n## 📊 This Week's Stats\n")
    lang_count = defaultdict(int)
    for r in list(all_repos.values())[:50]:
        lang = r.get("language") or "Other"
        lang_count[lang] += 1
    
    if lang_count:
        lines.append("\n**Language distribution (top 50):**\n")
        for lang_name, cnt in sorted(lang_count.items(), key=lambda x: -x[1])[:8]:
            lines.append(f"- `{lang_name}`: {cnt} repos\n")
    
    lines.append(f"\n---\n")
    lines.append(f"\n*Updated: {now.strftime('%Y-%m-%d %H:%M')} (Beijing Time)*  \n")
    lines.append(f"*Maintained by [vinson-lee](https://github.com/vinson-lee01)*\n")
    
    return "".join(lines)


def main():
    """Main function."""
    log("🚀 Starting repo search (CN + EN)...")
    start_time = time.time()
    
    # CN searches
    log("[CN] Chinese community repos", "INFO")
    print("-" * 50, flush=True)
    cache_zh = load_cache(CACHE_FILE_ZH)
    new_zh, must_zh, all_zh = run_search(ZH_SEARCHES, cache_zh, max_new=20)
    
    md_zh = render_md(new_zh, must_zh, all_zh, cache_zh, lang="zh", searches=ZH_SEARCHES)
    out_zh = "resources/trending_zh.md"
    with open(out_zh, "w", encoding="utf-8") as f:
        f.write(md_zh)
    log(f"Done: {out_zh} ({len(new_zh)} new, {len(cache_zh.get('seen', {}))} total)", "SUCCESS")
    save_cache(CACHE_FILE_ZH, cache_zh)
    
    # EN searches
    log("[EN] International community repos", "INFO")
    print("-" * 50, flush=True)
    cache_en = load_cache(CACHE_FILE_EN)
    new_en, must_en, all_en = run_search(EN_SEARCHES, cache_en, max_new=20)
    
    md_en = render_md(new_en, must_en, all_en, cache_en, lang="en", searches=EN_SEARCHES)
    out_en = "resources/trending_en.md"
    with open(out_en, "w", encoding="utf-8") as f:
        f.write(md_en)
    log(f"Done: {out_en} ({len(new_en)} new, {len(cache_en.get('seen', {}))} total)", "SUCCESS")
    save_cache(CACHE_FILE_EN, cache_en)
    
    # Index file
    log("📊 Generating index...", "INFO")
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
    log("Done: resources/trending.md", "SUCCESS")
    
    elapsed = time.time() - start_time
    log(f"✅ All done! Elapsed time: {elapsed:.1f}s", "SUCCESS")


if __name__ == "__main__":
    main()
