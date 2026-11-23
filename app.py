"""Portfolio backend: a small Flask app with a read-only REST API and the page shells.

Run (development):   python app.py        then open http://127.0.0.1:5000
All content comes from data.py. The browser renders the pages by calling the /api/* endpoints.
"""
from __future__ import annotations

import os
from datetime import date

from flask import Flask, abort, jsonify, render_template, request

import data as d

app = Flask(__name__, static_folder="static", template_folder="templates")
app.json.sort_keys = False

# ---------------------------------------------------------------------------
# Helpers that derive API fields from data.py
# ---------------------------------------------------------------------------


def norm(value) -> str:
    return str(value).strip().lower()


ALL_SKILLS = [skill for category in d.SKILLS for skill in category["skills"]]
PROJECT_BY_SLUG = {p["slug"]: p for p in d.PROJECTS}
TECH_LISTS = [p["stack"] for p in d.PROJECTS] + [e["technologies"] for e in d.EXPERIENCE]
KNOWN_FILTERS = {norm(f) for f in d.PROJECT_FILTERS}


def skill_terms(skill: dict) -> list[str]:
    return [norm(t) for t in [skill["name"], *skill["aliases"]]]


def is_linked(skill: dict) -> bool:
    terms = set(skill_terms(skill))
    return any(norm(item) in terms for items in TECH_LISTS for item in items)


def project_payload(project: dict) -> dict:
    tag = project["employer"] + (f" · {project['stream']}" if project["stream"] else "")
    return {**project, "tag": tag, "metric": list(project["metric"]) if project.get("metric") else None}


def experience_payload(experience: dict) -> dict:
    related = [
        {"slug": s, "name": PROJECT_BY_SLUG[s]["name"], "category": PROJECT_BY_SLUG[s]["category"]}
        for s in experience["projects"]
    ]
    return {**experience, "project_links": related}


def skills_payload() -> dict:
    categories = []
    lookup: dict[str, dict] = {}
    for category in d.SKILLS:
        skills = []
        for skill in category["skills"]:
            linked = is_linked(skill)
            terms = skill_terms(skill)
            skills.append({
                "name": skill["name"], "level": skill["level"],
                "level_label": d.LEVEL_LABELS[skill["level"]], "terms": terms, "linked": linked,
            })
            if linked:
                for term in terms:
                    lookup[term] = {"name": skill["name"], "terms": terms}
        categories.append({"name": category["name"], "icon": category["icon"], "skills": skills})
    return {"categories": categories, "lookup": lookup, "legend": d.LEVEL_LABELS, "marquee": d.MARQUEE}


def links_payload() -> dict:
    return {"linkedin": d.CONTACT["linkedin"], "github": d.CONTACT["github"]}


def ok(payload):
    response = jsonify(payload)
    response.headers["Cache-Control"] = "public, max-age=300"
    return response


# ---------------------------------------------------------------------------
# REST API (read-only)
# ---------------------------------------------------------------------------


@app.get("/api/profile")
def api_profile():
    return ok(d.PERSON)


@app.get("/api/links")
def api_links():
    return ok(links_payload())


@app.get("/api/meta")
def api_meta():
    return ok({"confidentiality_note": d.CONFIDENTIALITY_NOTE, "project_filters": d.PROJECT_FILTERS})


@app.get("/api/impact")
def api_impact():
    return ok(d.IMPACT)


@app.get("/api/experience")
def api_experience():
    return ok({"items": [experience_payload(e) for e in d.EXPERIENCE], "team_contributions": d.TEAM_CONTRIBUTIONS})


@app.get("/api/projects")
def api_projects():
    wanted = norm(request.args.get("filter", "all"))
    if wanted != "all" and wanted not in KNOWN_FILTERS:
        return jsonify(error=f"Unknown filter '{wanted}'", allowed=sorted(KNOWN_FILTERS)), 400
    items = [p for p in d.PROJECTS if wanted == "all" or wanted in {norm(f) for f in p["filters"]}]
    counts = {f: sum(1 for p in d.PROJECTS if f in p["filters"]) for f in d.PROJECT_FILTERS}
    return ok({"items": [project_payload(p) for p in items], "count": len(items), "total": len(d.PROJECTS),
               "filter_counts": {f: n for f, n in counts.items() if n}})


@app.get("/api/projects/<slug>")
def api_project(slug: str):
    project = PROJECT_BY_SLUG.get(slug)
    if project is None:
        return jsonify(error="Project not found"), 404
    index = d.PROJECTS.index(project)
    previous_p = d.PROJECTS[index - 1] if index > 0 else None
    next_p = d.PROJECTS[index + 1] if index < len(d.PROJECTS) - 1 else None
    link = lambda p: {"slug": p["slug"], "name": p["name"]} if p else None  # noqa: E731
    return ok({**project_payload(project), "previous": link(previous_p), "next": link(next_p)})


@app.get("/api/skills")
def api_skills():
    return ok(skills_payload())


@app.get("/api/certifications")
def api_certifications():
    return ok(d.CERTIFICATIONS)


@app.get("/api/recognition")
def api_recognition():
    return ok(d.RECOGNITION)


@app.get("/api/education")
def api_education():
    return ok({"education": d.EDUCATION, "internship": d.INTERNSHIP, "academic_projects": d.ACADEMIC_PROJECTS,
               "languages": d.PERSON["languages"]})


@app.get("/api/approach")
def api_approach():
    return ok([{"title": t, "description": text, "icon": icon} for t, text, icon in d.APPROACH])


@app.get("/api/beyond")
def api_beyond():
    return ok(d.BEYOND_WORK)


# ---------------------------------------------------------------------------
# Pages (HTML shells; content is rendered in the browser from the API)
# ---------------------------------------------------------------------------


def canonical(path: str) -> str:
    return f"{d.SITE_URL.rstrip('/')}{path}" if d.SITE_URL else ""


def site_urls(static: bool, depth: int = 0) -> dict:
    """Link targets for the templates: Flask routes when served, relative .html files when exported."""
    if static:
        root = "../" * depth
        return {"static_mode": True, "root": root, "home_url": f"{root}index.html", "resume_url": f"{root}resume.html"}
    return {"static_mode": False, "root": "/", "home_url": "/", "resume_url": "/resume"}


def person_jsonld() -> dict:
    p = d.PERSON
    data = {
        "@context": "https://schema.org", "@type": "Person", "name": p["name"], "jobTitle": p["title"],
        "description": p["description"],
        "address": {"@type": "PostalAddress", "addressLocality": "Bengaluru", "addressCountry": "IN"},
        "worksFor": {"@type": "Organization", "name": "KPMG Global Services"},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "Rajeev Institute of Technology"},
        "knowsAbout": p["focus_areas"],
    }
    same_as = [u for u in d.CONTACT.values() if u]
    if same_as:
        data["sameAs"] = same_as
    if d.SITE_URL:
        data["url"] = d.SITE_URL
    return data


def page_context(static: bool = False, depth: int = 0, **extra) -> dict:
    return {"person": d.PERSON, "links": links_payload(), "note": d.CONFIDENTIALITY_NOTE,
            "year": date.today().year, "keywords": ", ".join(d.PERSON["keywords"]),
            **site_urls(static, depth), **extra}


def home_context(static: bool = False) -> dict:
    website = {"@context": "https://schema.org", "@type": "WebSite", "name": f"{d.PERSON['name']} – Portfolio"}
    if d.SITE_URL:
        website["url"] = d.SITE_URL
    return page_context(static, title=f"{d.PERSON['name']} | {d.PERSON['title']} – Custom Application Developer",
                        description=d.PERSON["description"], canonical=canonical("/"),
                        jsonld=[person_jsonld(), website], page="home")


def resume_context(static: bool = False) -> dict:
    return page_context(static, title=f"{d.PERSON['name']} – Interactive Resume",
                        description=f"Interactive resume of {d.PERSON['name']}: {d.PERSON['description']}",
                        canonical=canonical("/resume.html" if static else "/resume"),
                        jsonld=[person_jsonld()], page="resume")


def project_context(slug: str, static: bool = False) -> dict:
    project = PROJECT_BY_SLUG[slug]
    creative_work = {
        "@context": "https://schema.org", "@type": "CreativeWork", "name": project["name"],
        "description": project["overview"], "creator": {"@type": "Person", "name": d.PERSON["name"]},
        "keywords": ", ".join(project["stack"]) if project["stack"] else project["category"],
    }
    path = f"/projects/{slug}.html" if static else f"/projects/{slug}"
    return page_context(static, 1 if static else 0, title=f"{project['name']} – Case study",
                        description=project["overview"], canonical=canonical(path), jsonld=[creative_work],
                        page="project", slug=slug)


def error_context(static: bool = False) -> dict:
    return page_context(static, title="Page not found", description="", canonical="", jsonld=[], page="error")


def robots_text(base: str) -> str:
    return f"User-agent: *\nAllow: /\nSitemap: {base}/sitemap.xml\n"


def sitemap_xml(base: str, static: bool = False) -> str:
    suffix = ".html" if static else ""
    paths = ["/", f"/resume{suffix}", *[f"/projects/{p['slug']}{suffix}" for p in d.PROJECTS]]
    urls = "".join(f"  <url><loc>{base}{path}</loc></url>\n" for path in paths)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n')


@app.get("/")
def home():
    return render_template("index.html", **home_context())


@app.get("/resume")
def resume():
    return render_template("resume.html", **resume_context())


@app.get("/projects/<slug>")
def project_page(slug: str):
    if slug not in PROJECT_BY_SLUG:
        abort(404)
    return render_template("project.html", **project_context(slug))


@app.get("/robots.txt")
def robots():
    base = (d.SITE_URL or request.url_root).rstrip("/")
    return robots_text(base), 200, {"Content-Type": "text/plain; charset=utf-8"}


@app.get("/sitemap.xml")
def sitemap():
    base = (d.SITE_URL or request.url_root).rstrip("/")
    return sitemap_xml(base), 200, {"Content-Type": "application/xml; charset=utf-8"}


# ---------------------------------------------------------------------------
# Errors and security headers
# ---------------------------------------------------------------------------


@app.errorhandler(404)
def not_found(_error):
    if request.path.startswith("/api/"):
        return jsonify(error="Not found"), 404
    return render_template("error.html", **error_context()), 404


@app.after_request
def add_headers(response):
    response.headers["Content-Security-Policy"] = (
        "default-src 'self'; script-src 'self'; style-src 'self'; style-src-attr 'unsafe-inline'; "
        "img-src 'self' data:; connect-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'"
    )
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "camera=(), microphone=(), geolocation=()"
    if response.mimetype == "text/html":
        response.headers["Cache-Control"] = "no-cache"
    return response


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.environ.get("PORT", "5000")), debug=os.environ.get("FLASK_DEBUG") == "1")
