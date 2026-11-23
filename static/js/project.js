// Renders one project as a case study from /api/projects/<slug>.
import { esc, routes } from "./util.js";

const each = (items, fn) => (items || []).map(fn).join("");
const bullets = (items) => `<ul class="bullets">${each(items, (i) => `<li>${esc(i)}</li>`)}</ul>`;

export function caseStudy(p, note) {
  const blocks = [["Overview", `<p>${esc(p.overview)}</p>`]];
  if (p.challenge) blocks.push(["Business challenge", `<p>${esc(p.challenge)}</p>`]);
  blocks.push(["My role", `<p>${esc(p.role)}</p>`]);
  if (p.contributions.length) blocks.push(["Key responsibilities", bullets(p.contributions)]);
  if (p.solution) blocks.push(["Solution", `<p>${esc(p.solution)}</p>`]);
  if (p.capabilities && p.capabilities.length) blocks.push(["Key capabilities", bullets(p.capabilities)]);
  if (p.stack.length) {
    blocks.push(["Technology stack", `<ul class="chips">${each(p.stack, (t) => `<li><span class="chip">${esc(t)}</span></li>`)}</ul>`]);
  }
  const metric = p.metric
    ? `<p class="metric-pill big"><strong class="grad">${esc(p.metric[0])}</strong> <span class="muted">${esc(p.metric[1])}</span></p>`
    : "";
  blocks.push(["Outcome", `${metric}<p>${esc(p.outcome)}</p>`]);

  const sections = blocks
    .map(([title, body], i) => `<section class="cs-block reveal" aria-labelledby="cs-${i}"><h2 id="cs-${i}">${esc(title)}</h2>${body}</section>`)
    .join("");
  const prev = p.previous ? `<a class="btn btn-ghost" href="${routes.project(p.previous.slug)}">&larr; ${esc(p.previous.name)}</a>` : "<span></span>";
  const next = p.next ? `<a class="btn btn-ghost" href="${routes.project(p.next.slug)}">${esc(p.next.name)} &rarr;</a>` : "<span></span>";

  return `
<article class="container cs">
  <p><a class="text-link" href="${routes.home("projects")}">&larr; All projects</a></p>
  <header class="cs-head">
    <p class="eyebrow">${esc(p.category)}</p>
    <h1>${esc(p.name)}</h1>
    <p><span class="badge">${esc(p.tag)}</span></p>
  </header>
  ${sections}
  <p class="note">${esc(note)}</p>
  <nav class="pager" aria-label="More projects">${prev}${next}</nav>
</article>`;
}
