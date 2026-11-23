// Builds the printable, ATS-friendly resume from the same API data as the portfolio.
import { dataTech, displayUrl, esc, fmt } from "./util.js";
import { skillItem } from "./sections.js";

const each = (items, fn) => (items || []).map(fn).join("");

function projectBlock(p) {
  const contributions = p.contributions.length
    ? `<ul class="bullets small">${each(p.contributions, (c) => `<li>${esc(c)}</li>`)}</ul>`
    : "";
  const capabilities = p.capabilities && p.capabilities.length
    ? `<p class="small"><em>Capabilities:</em> ${esc(p.capabilities.join(", "))}</p>`
    : "";
  const stack = p.stack.length ? `<p class="small"><em>Technology:</em> ${esc(p.stack.join(", "))}</p>` : "";
  return `
<li class="r-project" data-tech="${esc(dataTech(p.stack))}">
  <p><strong>${esc(p.name)}</strong> <span class="compact-only">– ${esc(p.outcome)}</span></p>
  <div class="detail-only"><p class="small"><em>${esc(p.role)}</em> ${esc(p.overview)}</p>${contributions}${capabilities}${stack}
    <p class="small"><em>Outcome:</em> ${esc(p.outcome)}</p></div>
</li>`;
}

function jobBlock(e, projectsBySlug) {
  const stages = e.stages.length
    ? `<ul class="bullets small detail-only">${each(e.stages, ([t, per, txt]) => `<li><strong>${esc(t)}</strong>, ${esc(per)}: ${esc(txt)}</li>`)}</ul>`
    : "";
  const lanes = e.lanes.length
    ? `<ul class="bullets small detail-only">${each(e.lanes, ([n, t]) => `<li><strong>${esc(n)}:</strong> ${esc(t)}</li>`)}</ul>`
    : "";
  return `
<article class="r-job" data-tech="${esc(dataTech(e.technologies))}">
  <div class="r-row"><h3>${esc(e.organization)}${e.unit ? `, ${esc(e.unit)}` : ""}</h3>
    <p class="mono small">${esc(e.start)} – ${esc(e.end)}</p></div>
  <p class="r-role">${esc(e.role)}${e.previous_role ? ` (previously ${esc(e.previous_role)})` : ""} · ${esc(e.location)}</p>
  <p>${esc(e.summary)}</p>${stages}${lanes}
  <ul class="bullets">${each(e.outcomes, (o) => `<li>${esc(o)}</li>`)}</ul>
  <div class="detail-only"><h4>Responsibilities</h4><ul class="bullets small">${each(e.responsibilities, (r) => `<li>${esc(r)}</li>`)}</ul></div>
  <h4>Projects</h4><ul class="r-projects">${each(e.projects, (slug) => projectBlock(projectsBySlug[slug]))}</ul>
</article>`;
}

export function resume({ profile, links, impact, experience, projects, skills, certifications, recognition, education, meta }) {
  const projectsBySlug = Object.fromEntries(projects.items.map((p) => [p.slug, p]));
  const contact = [profile.location];
  if (links.linkedin) contact.push(`<a href="${esc(links.linkedin)}" target="_blank" rel="noopener noreferrer">${esc(displayUrl(links.linkedin))}</a>`);
  if (links.github) contact.push(`<a href="${esc(links.github)}" target="_blank" rel="noopener noreferrer">${esc(displayUrl(links.github))}</a>`);
  const contactLine = contact.map((c, i) => (i === 0 ? esc(c) : c)).join(" · ");

  const impactItems = each(impact, (m) => {
    const value = m.from !== null && m.from !== undefined ? `${fmt(m.from)}–${fmt(m.to)}` : fmt(m.to);
    return `<li><strong>${esc(m.qualifier)} ${value}${esc(m.suffix)}</strong> – ${esc(m.label.toLowerCase())}: ${esc(m.context)}</li>`;
  });
  const skillRows = each(
    skills.categories,
    (c) => `<div class="r-skillrow"><h4>${esc(c.name)}</h4><ul class="skill-inline">${each(c.skills, skillItem)}</ul></div>`,
  );
  const certs = each(certifications, (c) => `<li>${esc(c.name)}${c.issuer ? ` – ${esc(c.issuer)}` : ""}</li>`);
  const recos = each(
    recognition,
    (r) => `<li><strong>${esc(r.name)}</strong>${r.issuer ? ` – ${esc(r.issuer)}` : ""}${r.date ? `, ${esc(r.date)}` : ""}. ${esc(r.summary)}</li>`,
  );
  const edu = each(
    education.education,
    (e) => `<li><strong>${esc(e.degree)}</strong>, ${esc(e.institution)}, ${esc(e.location)} (${esc(e.period)})</li>`,
  );
  const i = education.internship;
  const early = each(
    education.academic_projects,
    (a) => `<li><strong>${esc(a.title)}</strong> – ${esc(a.stack.join(", "))}${a.result ? `. ${esc(a.result)}` : ""}</li>`,
  );

  return `
<article class="resume-sheet">
  <header class="r-head">
    <h1>${esc(profile.name)}</h1>
    <p class="r-title">${esc(profile.headline)}</p>
    <p class="small">${contactLine}</p>
  </header>
  <section aria-labelledby="r-sum"><h2 id="r-sum">Summary</h2><p>${esc(profile.resume_summary)}</p></section>
  <section aria-labelledby="r-imp"><h2 id="r-imp">Key impact</h2><ul class="bullets">${impactItems}</ul></section>
  <section aria-labelledby="r-exp"><h2 id="r-exp">Professional experience</h2>${each(experience.items, (e) => jobBlock(e, projectsBySlug))}</section>
  <section aria-labelledby="r-skills"><h2 id="r-skills">Technical skills</h2>
    <p class="small muted no-print">&#9679; applied professionally &nbsp; &#9680; applied in projects &nbsp; &#9675; working knowledge</p>${skillRows}</section>
  <section aria-labelledby="r-cert"><h2 id="r-cert">Certifications and learning</h2><ul class="bullets small">${certs}</ul></section>
  <section aria-labelledby="r-reco"><h2 id="r-reco">Awards and recognition</h2><ul class="bullets small">${recos}</ul></section>
  <section aria-labelledby="r-edu"><h2 id="r-edu">Education</h2><ul class="bullets small">${edu}</ul></section>
  <section class="detail-only" aria-labelledby="r-int"><h2 id="r-int">Internship</h2>
    <p class="small"><strong>${esc(i.organization)} – ${esc(i.role)}</strong>, ${esc(i.location)} (${esc(i.period)}). Project: ${esc(i.project)}. ${esc(i.summary)}</p></section>
  <section class="detail-only" aria-labelledby="r-early"><h2 id="r-early">Academic and personal projects</h2><ul class="bullets small">${early}</ul></section>
  <section aria-labelledby="r-lang"><h2 id="r-lang">Languages</h2><p class="small">${esc(education.languages.join(", "))}</p></section>
  <p class="small muted">${esc(meta.confidentiality_note)}</p>
</article>`;
}
