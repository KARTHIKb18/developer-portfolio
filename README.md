# Karthik B – Portfolio and Interactive Resume

A personal portfolio and interactive resume built with **Python (Flask)** for the backend and plain **HTML, CSS and JavaScript** for the frontend. No database, no build step, no Node.js.

## How it works

```
data.py            all content (edit this to update the site)
app.py             Flask app: read-only REST API + page routes + security headers
export_static.py   renders the whole site to ./docs for free static hosting (GitHub Pages)
templates/         HTML shells (Jinja): head/SEO tags, navigation, footer
static/css/        site.css (light and dark themes, responsive, print layout)
static/js/         ES modules: call the API, render sections, interactions
static/fonts/      self-hosted fonts (Bricolage Grotesque, Geist, Geist Mono, Mr Dafoe; SIL Open Font License)
content/my_data.md original source text the content was written from
```

The browser loads a page shell from Flask, then JavaScript calls the REST API and renders the sections.

### REST API (all `GET`, JSON)

| Endpoint | Returns |
|---|---|
| `/api/profile` | name, title, summary, focus areas, languages |
| `/api/links` | public links (LinkedIn, GitHub) |
| `/api/impact` | headline metrics |
| `/api/experience` | roles, responsibilities, outcomes |
| `/api/projects?filter=<name>` | projects; filters: python, ai, automation, relativityone, azure, data processing, testing |
| `/api/projects/<slug>` | one case study with previous/next links |
| `/api/skills` | skill groups with evidence levels |
| `/api/certifications`, `/api/recognition`, `/api/education`, `/api/approach`, `/api/meta` | the remaining sections |

### Pages

- `/` – portfolio
- `/resume` – interactive resume (Compact or Detailed, **Save as PDF** button)
- `/projects/<slug>` – one case study per project

## Run locally

Requires Python 3.10+ and Flask.

```powershell
pip install -r requirements.txt   # only if Flask is not installed yet
python app.py
```

Open http://127.0.0.1:5000. Set `PORT` to change the port. Set `FLASK_DEBUG=1` for auto-reload while editing (development only).

## Update the content

1. Edit `data.py` (projects, skills, experience, links, and so on).
2. Restart `python app.py` and refresh the browser.

Public links are in the `CONTACT` block at the top of `data.py`. Leave a value as `""` to hide that button.

```python
CONTACT = {
    "linkedin": "https://www.linkedin.com/in/karthik-18k/",
    "github": "",          # add your GitHub URL here
}
```

No email address is published anywhere on the site, by design.

Other optional fields in `data.py`:

- `SITE_URL` – set to your public address after deployment so canonical links, the sitemap and social cards are correct.
- Certifications – add `issuer`, `date`, `credential_id` or `verify_url` to an entry and it appears automatically. A "Verify credential" link only shows when `verify_url` is set.

## Interactive resume

- **Compact / Detailed** – switches between a short recruiter summary and the full resume. The choice is remembered in the browser.
- **Save as PDF** – opens the print dialog; choose "Save as PDF". The page has a dedicated A4 print layout.
- **Skill highlight** – select any skill chip to highlight related roles and projects; press Escape or use Clear to reset.

## Deploy

### Free hosting on GitHub Pages (static)

GitHub Pages only serves static files, so export the site first. The exported copy works without Flask: the same pages, with the API responses saved as JSON files.

1. Set `SITE_URL` in `data.py` to your Pages address, for example `https://<username>.github.io/<repository>`.
2. Run `python export_static.py`. It writes the finished site into the `docs` folder.
3. Commit and push the repository, including `docs/`.
4. On GitHub open **Settings > Pages**, choose **Deploy from a branch**, select your main branch and the **/docs** folder, then save.
5. After a minute the site is live at the address from step 1.

Re-run `python export_static.py` and push again whenever you change `data.py` or the frontend.

To preview the exported site locally: `python -m http.server -d docs 8000`, then open http://localhost:8000. Opening the files directly from disk does not work, because browsers block loading the JSON files that way.

### Any Python host (Flask)

The app is also a standard WSGI application (`app:app`), so it runs on any Python host (Render, Railway, PythonAnywhere, Azure App Service, and so on).

1. Push the folder to a Git repository.
2. Create a web service using `requirements.txt` and a production server, for example `gunicorn app:app` on Linux hosts. The built-in `python app.py` server is for development only.
3. Set `SITE_URL` in `data.py` to the public address.

## Accessibility and performance notes

- Semantic landmarks, skip link, visible focus states, keyboard-operable menu with Escape support, live-region announcements for filters.
- Respects `prefers-reduced-motion` and the operating-system theme on first visit.
- No third-party scripts or external requests: the fonts are self-hosted.
- Content Security Policy forbids inline scripts; all rendered text is HTML-escaped.
- Content is rendered by JavaScript from the API, so a visitor with JavaScript disabled sees only a short fallback message. Search engines that run JavaScript index the full content.
