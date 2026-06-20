#!/usr/bin/env python3
"""
Share text generator
"""

import json
import os
import re
from datetime import datetime, timezone, timedelta

CST = timezone(timedelta(hours=8))
TODAY = datetime.now(CST).strftime("%Y-%m-%d")
OUTPUT_FILE = "resources/share_text.md"
CACHE_FILE = "resources/.cache.json"
TRENDING_FILE = "resources/trending.md"

def load_cache():
    if os.path.exists(CACHE_FILE):
        try:
            with open(CACHE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def load_trending_highlights():
    highlights = {"top_repos": [], "new_count": 0}
    if not os.path.exists(TRENDING_FILE):
        return highlights
    try:
        with open(TRENDING_FILE, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r"New: \*\*(\d+)\*\*", content)
            if match:
                highlights["new_count"] = int(match.group(1))
            for line in content.split("\n"):
                if line.startswith("| [") and "Stars" in line:
                    parts = line.split("|")
                    if len(parts) > 2:
                        repo_link = parts[1].strip()
                        repo_name = repo_link.split("]")[0].replace("[", "") if "[" in repo_link else ""
                        if repo_name:
                            highlights["top_repos"].append(repo_name)
    except Exception:
        pass
    return highlights

def generate_twitter(cache, highlights):
    stars = cache.get("seen", [])
    lines = []
    lines.append("Twitter:\n")
    lines.append(f"DevOps learning roadmap updated {TODAY}\n")
    lines.append(f"{len(stars)} resources curated\n")
    if highlights["new_count"] > 0:
        lines.append(f"+{highlights['new_count']} new repos\n")
    lines.append("#DevOps #SRE #Linux #Docker #Kubernetes\n")
    lines.append("https://github.com/vinson-lee01/ops-engineering-roadmap\n")
    return "\n".join(lines)

def generate_reddit(highlights):
    lines = []
    lines.append("\n---\n\nReddit (r/devops):\n")
    lines.append("**Title**: DevOps/SRE learning roadmap - 500+ resources, CN + EN\n")
    lines.append("\n**Body**:\n")
    lines.append("Covering Linux, Docker, K8s, CI/CD, Prometheus, Cloud Native.\n")
    lines.append("CN and EN versions. Updated regularly.\n")
    lines.append("https://github.com/vinson-lee01/ops-engineering-roadmap\n")
    return "\n".join(lines)

def generate_zhihu():
    lines = []
    lines.append("\n---\n\nZhihu:\n")
    lines.append("**Title**: 运维工程师学习路线（2026）\n\n")
    lines.append("**Body**:\n")
    lines.append("Linux / Docker / K8s / CI/CD / Prometheus 全栈资源。\n")
    lines.append("中英双语，持续更新。\n")
    lines.append("https://github.com/vinson-lee01/ops-engineering-roadmap\n")
    return "\n".join(lines)

def generate_csdn():
    lines = []
    lines.append("\n---\n\nCSDN:\n")
    lines.append("**Title**: 运维学习路线开源（500+ 资源，中英双语）\n\n")
    lines.append("**Body**:\n")
    lines.append("从 Linux 到 K8s，从 Docker 到 CI/CD。\n")
    lines.append("中文版 + English 版，各自独立。\n")
    lines.append("https://github.com/vinson-lee01/ops-engineering-roadmap\n")
    return "\n".join(lines)

def generate_linkedin():
    lines = []
    lines.append("\n---\n\nLinkedIn:\n")
    lines.append("Sharing my DevOps/SRE Learning Roadmap.\n\n")
    lines.append("500+ resources. CN + EN. Linux, Docker, K8s, CI/CD.\n")
    lines.append("#DevOps #SRE #CloudComputing #OpenSource\n\n")
    lines.append("https://github.com/vinson-lee01/ops-engineering-roadmap\n")
    return "\n".join(lines)

def main():
    cache = load_cache()
    highlights = load_trending_highlights()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(f"# Share Text - {TODAY}\n\n")

        f.write(generate_twitter(cache, highlights))
        f.write(generate_reddit(highlights))
        f.write(generate_zhihu())
        f.write(generate_csdn())
        f.write(generate_linkedin())

    print(f"done: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
