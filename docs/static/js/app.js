// Entry point: calls the Flask REST API, renders the page, then wires up the interactions.
import {
  applySkillFilter, applyView, currentView, initActiveNav, initCountUp, initCursorLabel, initMenu, initPrint,
  initProgress, initRotator, initSkillFilter, initSpotlight, initTheme, initTimeline, initViewMode, observeReveal,
} from "./interactions.js";
import { caseStudy } from "./project.js";
import { resume } from "./resume.js";
import * as sections from "./sections.js";
import { api, esc, norm, state } from "./util.js";

const root = document.getElementById("app");
const page = document.body.dataset.page;

initTheme();
initMenu();
initSpotlight();
initViewMode();
initSkillFilter();
initPrint();
initProgress();
initCursorLabel();

function afterRender() {
  observeReveal(root);
  initCountUp(root);
  initRotator(root);
  initTimeline(root);
  initActiveNav();
  applyView(currentView(), false);
  applySkillFilter();
  if (location.hash.length > 1) {
    document.getElementById(decodeURIComponent(location.hash.slice(1)))?.scrollIntoView();
  }
}

async function renderHome() {
  const [profile, links, impact, experience, projects, skills, certifications, recognition, education, approach, meta] =
    await Promise.all([
      "profile", "links", "impact", "experience", "projects", "skills",
      "certifications", "recognition", "education", "approach", "meta",
    ].map((name) => api(name)));
  state.lookup = skills.lookup;
  root.innerHTML = [
    sections.hero(profile, links, skills.marquee),
    sections.about(profile),
    sections.impact(impact),
    sections.experience(experience),
    sections.projects(projects, meta.confidentiality_note),
    sections.skills(skills),
    sections.certifications(certifications),
    sections.recognition(recognition),
    sections.education(education),
    sections.earlyWork(education),
    sections.approach(approach),
    sections.contact(links),
  ].join("");
  bindProjectFilter(projects);
}

// Filtering happens in the browser, so it also works on a static host.
function bindProjectFilter(projects) {
  const group = root.querySelector(".filters");
  const grid = document.getElementById("project-grid");
  const status = document.getElementById("filter-status");
  if (!group || !grid) return;
  group.addEventListener("click", (event) => {
    const button = event.target.closest("[data-filter]");
    if (!button) return;
    const filter = button.dataset.filter;
    const items = filter === "all" ? projects.items : projects.items.filter((p) => p.filters.some((f) => norm(f) === filter));
    grid.innerHTML = items.map(sections.projectCard).join("");
    group.querySelectorAll("[data-filter]").forEach((b) => b.setAttribute("aria-pressed", String(b === button)));
    status.textContent = `Showing ${items.length} of ${projects.total} projects.`;
    applySkillFilter();
  });
}

async function renderResume() {
  const [profile, links, impact, experience, projects, skills, certifications, recognition, education, meta] =
    await Promise.all([
      "profile", "links", "impact", "experience", "projects", "skills",
      "certifications", "recognition", "education", "meta",
    ].map((name) => api(name)));
  state.lookup = skills.lookup;
  root.innerHTML = resume({ profile, links, impact, experience, projects, skills, certifications, recognition, education, meta });
}

async function renderProject() {
  const [project, meta] = await Promise.all([api(`projects/${root.dataset.slug}`), api("meta")]);
  root.innerHTML = caseStudy(project, meta.confidentiality_note);
}

async function load() {
  try {
    if (page === "home") await renderHome();
    else if (page === "resume") await renderResume();
    else if (page === "project") await renderProject();
    else return;
    afterRender();
  } catch (error) {
    console.error(error);
    root.innerHTML = `<div class="container error-box" role="alert"><p>Content could not be loaded: ${esc(error.message)}</p><p><button type="button" class="btn btn-primary" id="retry">Try again</button></p></div>`;
    document.getElementById("retry")?.addEventListener("click", load);
  } finally {
    root.removeAttribute("aria-busy");
  }
}

if (root) load();
