"""Export the site as plain static files (HTML, CSS, JS and JSON) for free hosting on GitHub Pages.

Usage:
    python export_static.py       writes the finished site into ./docs

The Flask app (app.py) is still used for local development and as the REST API; this script
renders the same pages and the same API responses to files so no server is needed.
"""
from __future__ import annotations

import shutil
from pathlib import Path

from flask import render_template

import app as site
import data as d

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "docs"

API_NAMES = [
    "profile", "links", "meta", "impact", "experience", "projects", "skills",
    "certifications", "recognition", "education", "approach", "beyond",
]


def write(path: Path, content: str | bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, bytes):
        path.write_bytes(content)
    else:
        path.write_text(content, encoding="utf-8", newline="\n")


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    shutil.copytree(ROOT / "static", OUT / "static")

    client = site.app.test_client()
    for name in [*API_NAMES, *[f"projects/{p['slug']}" for p in d.PROJECTS]]:
        response = client.get(f"/api/{name}")
        if response.status_code != 200:
            raise RuntimeError(f"/api/{name} returned {response.status_code}")
        write(OUT / "api" / f"{name}.json", response.get_data())

    with site.app.test_request_context():
        write(OUT / "index.html", render_template("index.html", **site.home_context(static=True)))
        write(OUT / "resume.html", render_template("resume.html", **site.resume_context(static=True)))
        for project in d.PROJECTS:
            write(OUT / "projects" / f"{project['slug']}.html",
                  render_template("project.html", **site.project_context(project["slug"], static=True)))
        write(OUT / "404.html", render_template("error.html", **site.error_context(static=True)))

    if d.SITE_URL:
        base = d.SITE_URL.rstrip("/")
        write(OUT / "sitemap.xml", site.sitemap_xml(base, static=True))
        write(OUT / "robots.txt", site.robots_text(base))
    else:
        write(OUT / "robots.txt", "User-agent: *\nAllow: /\n")

    write(OUT / ".nojekyll", "")  # stops GitHub Pages from processing the files with Jekyll
    count = sum(1 for f in OUT.rglob("*") if f.is_file())
    print(f"Exported {count} files to {OUT}")


if __name__ == "__main__":
    main()
