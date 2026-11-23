// Builds the home-page HTML from the JSON returned by the API (editorial layout).
import { icon } from "./icons.js";
import { dataTech, esc, fmt, norm, routes, state } from "./util.js";

const each = (items, fn) => (items || []).map(fn).join("");
const num = (n) => String(n).padStart(2, "0");

export function chip(label) {
  const hit = state.lookup[norm(label)];
  if (!hit) return `<span class="chip">${esc(label)}</span>`;
  return `<button type="button" class="chip chip-btn" data-skill-btn data-terms="${esc(hit.terms.join("|"))}" data-label="${esc(hit.name)}" aria-pressed="false">${esc(label)}</button>`;
}

export function externalLink(href, label, iconName, cls = "btn btn-ghost") {
  return `<a class="${cls}" href="${esc(href)}" target="_blank" rel="noopener noreferrer">${icon(iconName)}${esc(label)}<span class="sr-only"> (opens in a new tab)</span></a>`;
}

export function socialButtons(links, primary = false) {
  const parts = [];
  if (links.linkedin) parts.push(externalLink(links.linkedin, "LinkedIn", "linkedin", primary ? "btn btn-primary" : "btn btn-ghost"));
  if (links.github) parts.push(externalLink(links.github, "GitHub", "github", parts.length || !primary ? "btn btn-ghost" : "btn btn-primary"));
  return parts.join("");
}

function section(id, n, label, title, inner, lead = "", cls = "") {
  return `
<section id="${id}" class="section ${cls}" aria-labelledby="${id}-title">
  <div class="container">
    <div class="sec-head reveal">
      <p class="sec-num">${num(n)} / ${esc(label)}</p>
      <h2 id="${id}-title" class="sec-title">${esc(title)}</h2>
      ${lead ? `<p class="sec-lead">${esc(lead)}</p>` : ""}
    </div>
    ${inner}
  </div>
</section>`;
}

export function hero(p, links, marquee) {
  const phrases = p.hero_phrases;
  const letters = [...p.name.toUpperCase()]
    .map((ch) => `<span class="wm-letter">${ch === " " ? "&nbsp;" : esc(ch)}</span>`)
    .join("");
  const lead = esc(p.tagline).replace("real operational challenges", "<mark>real operational challenges</mark>");
  const strip = each(p.stats, ([k, v]) => `<div><dt>${esc(k)}/</dt><dd>${esc(v)}</dd></div>`);
  const band = each(marquee, (t) => `<li>${esc(t)}</li>`);
  const bandCopy = each(marquee, (t) => `<li aria-hidden="true">${esc(t)}</li>`);
  const linkedin = links.linkedin ? externalLink(links.linkedin, "LinkedIn", "linkedin") : "";
  return `
<section id="home" class="hero" aria-labelledby="hero-title">
  <div class="container hero-top">
    <dl class="meta-strip rise">${strip}</dl>
    <h1 id="hero-title" class="wordmark rise" style="--d:.1s">
      <span class="sr-only">${esc(p.name)}, ${esc(p.role_line)}</span>
      <span aria-hidden="true">${letters}</span>
      <span class="wm-script" aria-hidden="true">${esc(p.role_line)}</span>
    </h1>
    <div class="hero-lower">
      <div>
        <p class="hero-lead rise" style="--d:.25s">${lead}</p>
        <p class="focus-line rise" style="--d:.35s">
          <span class="sr-only">Focus areas: ${esc(phrases.join(", "))}.</span>
          <span class="prompt" aria-hidden="true">&gt;</span>
          <span class="focus-text" aria-hidden="true" data-phrases="${esc(JSON.stringify(phrases))}">${esc(phrases[0])}</span>
          <span class="caret" aria-hidden="true"></span>
        </p>
      </div>
      <div class="rise" style="--d:.45s">
        <div class="hero-cta">
          <a class="btn btn-primary" href="#projects">View projects${icon("arrow-right")}</a>
          <a class="btn btn-ghost" href="#experience">Experience</a>
          ${linkedin}
          <a class="text-link" href="${routes.resume()}">${icon("file-text")}Interactive resume</a>
        </div>
        <p class="muted hero-blurb">${esc(p.hero_blurb)}</p>
      </div>
    </div>
  </div>
  <div class="stack-band" aria-label="Core technologies"><ul class="marquee-track">${band}${bandCopy}</ul></div>
</section>`;
}

export function about(p) {
  const inner = `
<div class="about-grid">
  <div class="prose reveal">${each(p.about, (t) => `<p>${esc(t)}</p>`)}</div>
  <aside class="reveal" aria-labelledby="focus-title">
    <h3 id="focus-title" class="subhead" style="margin-top:0">Technical focus areas</h3>
    <ul class="focus-list">${each(p.focus_areas, (t) => `<li>${esc(t)}</li>`)}</ul>
  </aside>
</div>`;
  return section("about", 1, "About", "Let me introduce myself", inner);
}

export function impact(items) {
  const cards = each(items, (m) => {
    const hasRange = m.from !== null && m.from !== undefined;
    const final = hasRange ? `${fmt(m.from)}–${fmt(m.to)}` : fmt(m.to);
    const attrs = `data-count-to="${m.to}"${hasRange ? ` data-count-from="${m.from}"` : ""}`;
    const pct = m.suffix === "%";
    return `
<li class="impact-item reveal">
  <p class="label impact-qual">${esc(m.qualifier)}</p>
  <p class="impact-num"><span class="count" ${attrs}><span class="sr-only">${final}</span><span aria-hidden="true" data-count-live>${final}</span></span>${pct ? "<span>%</span>" : `<span class="impact-unit">${esc(m.suffix.trim())}</span>`}</p>
  <h3>${esc(m.label)}</h3>
  <p class="muted">${esc(m.context)}</p>
  <a class="link-arrow" href="${routes.project(m.project)}">Case study${icon("arrow-up-right")}</a>
</li>`;
  });
  return section("impact", 2, "Impact", "Measurable outcomes", `<ul class="impact-grid">${cards}</ul>`,
    "Outcome-based proof points from professional projects.");
}

function experienceItem(e) {
  const stages = e.stages.length
    ? `<ol class="steps" aria-label="Career progression">${each(
        e.stages,
        ([title, period, text], i) => `<li><p class="label">Step ${i + 1} · ${esc(period)}</p><div><p class="strong">${esc(title)}</p><p class="muted small">${esc(text)}</p></div></li>`,
      )}</ol>`
    : "";
  const lanes = e.lanes.length
    ? `<ul class="steps" aria-label="Work streams">${each(
        e.lanes,
        ([name, text]) => `<li><p class="label strong">${esc(name)}</p><p class="muted small">${esc(text)}</p></li>`,
      )}</ul>`
    : "";
  return `
<li class="exp-item reveal" data-tech="${esc(dataTech(e.technologies))}">
  <div class="exp-when">
    <span class="badge${e.current ? " badge-current" : ""}">${e.current ? "Current" : "Previous"}</span>
    <span>${esc(e.start)} – ${esc(e.end)}</span>
  </div>
  <div class="exp-main">
    <h3 class="exp-org">${esc(e.organization)}</h3>
    ${e.unit ? `<p class="muted">${esc(e.unit)}</p>` : ""}
    <p class="exp-role">${esc(e.role)}</p>
    ${e.previous_role ? `<p class="muted small">Previously: ${esc(e.previous_role)}</p>` : ""}
    <p class="muted small loc">${icon("pin")}${esc(e.location)}</p>
    <p class="exp-summary">${esc(e.summary)}</p>
    ${stages}${lanes}
    <ul class="outcomes" aria-label="Measurable outcomes">${each(e.outcomes, (o) => `<li>${icon("check")}<span>${esc(o)}</span></li>`)}</ul>
    <details class="exp-details" data-exp-details>
      <summary>${icon("chevron")}<span>Responsibilities, projects and technology</span></summary>
      <div class="exp-body">
        <h4 class="subhead">Responsibilities</h4><ul class="bullets two-col">${each(e.responsibilities, (r) => `<li>${esc(r)}</li>`)}</ul>
        <h4 class="subhead">Projects</h4><ul class="mini-links">${each(
          e.project_links,
          (p) => `<li><a href="${routes.project(p.slug)}"><span class="strong">${esc(p.name)}</span><span class="muted small">${esc(p.category)}</span></a></li>`,
        )}</ul>
        <h4 class="subhead">Technology</h4><ul class="chips">${each(e.technologies, (t) => `<li>${chip(t)}</li>`)}</ul>
        <p class="muted small">Select a technology to highlight related roles and projects across the page.</p>
      </div>
    </details>
  </div>
</li>`;
}

export function experience(data) {
  const inner = `
<div class="view-toggle reveal" role="group" aria-label="Recruiter view">
  <span class="label">Recruiter view</span>
  <button type="button" class="seg" data-view-btn="compact" aria-pressed="true">Compact</button>
  <button type="button" class="seg" data-view-btn="detailed" aria-pressed="false">Detailed</button>
</div>
<ol class="exp-list">${each(data.items, experienceItem)}</ol>
<div class="team reveal"><h3 class="subhead">Engineering and team contributions</h3>
  <ul class="chips">${each(data.team_contributions, (t) => `<li><span class="chip">${esc(t)}</span></li>`)}</ul></div>`;
  return section("experience", 3, "Experience", "Career journey", inner, "Current and previous employment, shown newest first.");
}

export function projectCard(p, i = 0) {
  const metric = p.metric ? `<span class="proj-metric">${esc(p.metric[0])}<small>${esc(p.metric[1])}</small></span>` : `<span class="proj-metric"></span>`;
  const tags = p.stack.length ? `<span class="proj-tags">${esc(p.stack.slice(0, 5).join(" / "))}${p.stack.length > 5 ? ` / +${p.stack.length - 5}` : ""}</span>` : "";
  return `
<li class="proj-row" data-tech="${esc(dataTech(p.stack))}">
  <a class="proj-link" href="${routes.project(p.slug)}" data-cursor="View">
    <span class="proj-num">${num(i + 1)}</span>
    <span class="proj-main"><span class="proj-name">${esc(p.name)}</span><span class="proj-meta">${esc(p.tag)} · ${esc(p.category)}</span></span>
    <span class="proj-desc">${esc(p.overview)}${tags}</span>
    ${metric}
    <span class="proj-arrow">${icon("arrow-up-right")}</span>
  </a>
</li>`;
}

export function projects(data, note) {
  const buttons =
    `<button type="button" class="seg" data-filter="all" aria-pressed="true">All <span class="count-badge">${data.total}</span></button>` +
    Object.entries(data.filter_counts)
      .map(([name, n]) => `<button type="button" class="seg" data-filter="${esc(norm(name))}" aria-pressed="false">${esc(name)} <span class="count-badge">${n}</span></button>`)
      .join("");
  const inner = `
<div class="filters reveal" role="group" aria-label="Filter projects by focus area">${buttons}</div>
<p class="sr-only" role="status" aria-live="polite" id="filter-status"></p>
<ul class="proj-list" id="project-grid">${each(data.items, projectCard)}</ul>
<p class="note reveal">${esc(note)}</p>`;
  return section("projects", 4, "Projects", "Selected work", inner,
    "Each project opens as a short case study: the challenge, my role, the approach, and the outcome.");
}

const LEVEL_MARK = { professional: "●", projects: "◐", working: "○" };

export function skillItem(skill) {
  const inner = `<span class="mark" aria-hidden="true">${LEVEL_MARK[skill.level]}</span>${esc(skill.name)}<span class="sr-only">, ${esc(skill.level_label.toLowerCase())}</span>`;
  if (skill.linked) {
    return `<li><button type="button" class="skill lvl-${skill.level}" data-skill-btn data-terms="${esc(skill.terms.join("|"))}" data-label="${esc(skill.name)}" aria-pressed="false">${inner}</button></li>`;
  }
  return `<li><span class="skill lvl-${skill.level}">${inner}</span></li>`;
}

export function skills(data) {
  const legend = Object.entries(data.legend)
    .map(([key, label]) => `<li><span class="mark" aria-hidden="true">${LEVEL_MARK[key]}</span>${esc(label)}</li>`)
    .join("");
  const rows = each(
    data.categories,
    (c) => `<div class="reveal"><h3 class="skill-label">${esc(c.name)}</h3><ul class="skill-list">${each(c.skills, skillItem)}</ul></div>`,
  );
  const inner = `
<ul class="legend" aria-label="Evidence legend">${legend}</ul>
<p class="muted small">Select a skill to highlight the roles and projects where it was applied.</p>
<div class="skill-rows">${rows}</div>`;
  return section("skills", 5, "Skills", "What I work with", inner,
    "Grouped by area and labelled by how each skill was used, not rated with percentages.");
}

function certRow(c) {
  const meta = [c.issuer, c.date, c.credential_id ? `ID ${c.credential_id}` : ""].filter(Boolean).map(esc).join(" · ");
  const verify = c.verify_url ? externalLink(c.verify_url, "Verify credential", "arrow-up-right", "link-arrow") : "";
  return `
<li class="reveal"><p class="row-meta">${meta || "Professional badge"}</p>
  <div><h4>${esc(c.name)}</h4>${c.description ? `<p class="muted small" style="margin-top:.35rem">${esc(c.description)}</p>` : ""}${verify}</div></li>`;
}

export function certifications(items) {
  const inner = `
<h3 class="subhead" style="margin-top:0">Professional badges</h3>
<ul class="rows">${each(items.filter((c) => c.type === "badge"), certRow)}</ul>
<h3 class="subhead">Workshops and learning programs</h3>
<ul class="rows">${each(items.filter((c) => c.type === "workshop"), certRow)}</ul>`;
  return section("certifications", 6, "Certifications", "Continuous learning", inner);
}

export function recognition(items) {
  const rows = each(items, (r) => {
    const meta = [r.issuer, r.date].filter(Boolean).map(esc).join(" · ");
    return `
<li class="reveal"><div><p class="row-meta">${esc(r.kind)}</p>${meta ? `<p class="row-meta">${meta}</p>` : ""}</div>
  <div><h3>${esc(r.name)}</h3><p class="muted" style="margin-top:.4rem">${esc(r.summary)}</p></div></li>`;
  });
  return section("recognition", 7, "Recognition", "Awards and appreciation", `<ul class="rows">${rows}</ul>`);
}

export function education(data) {
  const rows = each(
    data.education,
    (e) => `
<li class="reveal"><p class="row-meta">${esc(e.period)}</p>
  <div><h3>${esc(e.degree)}</h3><p style="margin-top:.35rem">${esc(e.institution)}, ${esc(e.location)}</p>
  ${e.areas.length ? `<ul class="chips" style="margin-top:1rem">${each(e.areas, (a) => `<li><span class="chip">${esc(a)}</span></li>`)}</ul>` : ""}</div></li>`,
  );
  const inner = `<ul class="rows">${rows}</ul>
<h3 class="subhead">Languages</h3><ul class="chips">${each(data.languages, (l) => `<li><span class="chip">${esc(l)}</span></li>`)}</ul>`;
  return section("education", 8, "Education", "Academic background", inner);
}

export function earlyWork(data) {
  const i = data.internship;
  const intern = `
<ul class="rows"><li class="reveal"><p class="row-meta">Internship · ${esc(i.period)}</p>
  <div><h3>${esc(i.organization)} – ${esc(i.role)}</h3><p class="muted small loc">${icon("pin")}${esc(i.location)}</p>
  <p style="margin-top:.8rem"><strong>Project: ${esc(i.project)}.</strong> ${esc(i.summary)}</p>
  <ul class="chips" style="margin:1rem 0">${each(i.stack, (t) => `<li><span class="chip">${esc(t)}</span></li>`)}</ul>
  <h4 class="subhead" style="margin:1rem 0 .6rem">Key learning</h4><ul class="bullets small">${each(i.learnings, (t) => `<li>${esc(t)}</li>`)}</ul></div></li></ul>`;
  const rows = each(
    data.academic_projects,
    (a) => `
<li class="reveal"><p class="row-meta">Early project</p>
  <div><h4>${esc(a.title)}</h4><p class="muted small" style="margin-top:.35rem">${esc(a.summary)}</p>
  ${a.capabilities.length ? `<ul class="bullets small" style="margin-top:.8rem">${each(a.capabilities, (c) => `<li>${esc(c)}</li>`)}</ul>` : ""}
  ${a.result ? `<p class="strong accent-text" style="margin-top:.8rem">${esc(a.result)}</p>` : ""}
  <p class="proj-tags">${esc(a.stack.join(" / "))}</p></div></li>`,
  );
  const inner = `${intern}
<h3 class="subhead">Academic and personal projects</h3>
<p class="muted small" style="margin-bottom:1rem">Early projects that show how my technical interests developed before my professional career.</p>
<ul class="rows">${rows}</ul>`;
  return section("early-work", 9, "Early work", "Internship and early projects", inner);
}

export function approach(steps) {
  const items = each(
    steps,
    (s, n) => `<li class="reveal"><p class="label">${num(n + 1)}</p><h3>${esc(s.title)}</h3><p class="muted">${esc(s.description)}</p></li>`,
  );
  return section("approach", 10, "Approach", "How I work", `<ol class="approach-grid">${items}</ol>`);
}

export function beyondWork(data) {
  const cards = each(
    data.interests,
    (item) => `
<li class="reveal"><span class="icon-box">${icon(item.icon)}</span><h3>${esc(item.title)}</h3>
  <p class="muted">${esc(item.text)}</p>${item.favourite ? `<p class="label accent-text">${esc(item.favourite)}</p>` : ""}</li>`,
  );
  const inner = `
<ul class="life-grid">${cards}</ul>
<div class="reveal">
  <h3 class="subhead">${esc(data.people_title)}</h3>
  <p class="muted" style="margin-bottom:1rem">${esc(data.people_lead)}</p>
  <ul class="focus-list two-col">${each(data.people, (t) => `<li>${esc(t)}</li>`)}</ul>
</div>`;
  return section("beyond-work", 11, "Beyond work", data.title, inner, data.lead);
}

export function contact(links) {
  return `
<section id="contact" class="section contact-slab" aria-labelledby="contact-title">
  <div class="container">
    <p class="sec-num reveal">12 / Contact</p>
    <h2 id="contact-title" class="contact-title reveal" style="margin-top:1rem">Let&rsquo;s <span>talk.</span></h2>
    <p class="contact-copy reveal">The fastest way to reach me is through my professional profiles. My interactive resume is also available to view or save as PDF.</p>
    <div class="hero-cta reveal">${socialButtons(links, true)}<a class="btn btn-ghost" href="${routes.resume()}">${icon("file-text")}Interactive resume</a></div>
  </div>
</section>`;
}
