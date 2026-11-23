// Shared helpers for the browser-side rendering code.

export const state = {
  /** normalised technology name -> { name, terms[] }, supplied by /api/skills */
  lookup: {},
};

export const esc = (value) =>
  String(value ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

export const norm = (value) => String(value).trim().toLowerCase();

export const fmt = (n) => Number(n).toLocaleString("en-US");

export const dataTech = (items) => (items || []).map(norm).join("|");

export const displayUrl = (url) => url.replace(/^[a-z]+:\/\//i, "").replace(/\/$/, "");

export function initials(text) {
  const words = text.replace("–", " ").split(/\s+/).filter((w) => /^[A-Za-z0-9]/.test(w));
  return words.length >= 2 ? (words[0][0] + words[1][0]).toUpperCase() : text.slice(0, 2).toUpperCase();
}

export async function getJSON(url) {
  const response = await fetch(url, { headers: { Accept: "application/json" } });
  if (!response.ok) throw new Error(`${url} responded with ${response.status}`);
  return response.json();
}

// The same code runs under Flask (/api/...) and as an exported static site (api/....json).
const { root = "/", static: staticFlag } = document.body.dataset;
const isStatic = staticFlag === "true";

export const routes = {
  home: (hash = "") => `${isStatic ? `${root}index.html` : "/"}${hash ? `#${hash}` : ""}`,
  resume: () => (isStatic ? `${root}resume.html` : "/resume"),
  project: (slug) => (isStatic ? `${root}projects/${slug}.html` : `/projects/${slug}`),
};

export const api = (name) => getJSON(isStatic ? `${root}api/${name}.json` : `/api/${name}`);

export const prefersReducedMotion = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;

const plural = (n) => `${n} ${n === 1 ? "year" : "years"}`;

/** Friendly length of a career that began in `start` ("YYYY-MM"), measured to `now`: "nearly 5 years", "5 years", "5+ years", "5.5 years". */
export function experienceLabel(start, now = new Date()) {
  const [startYear, startMonth] = start.split("-").map(Number);
  const months = (now.getFullYear() - startYear) * 12 + (now.getMonth() + 1 - startMonth);
  if (months < 12) return "less than a year";
  const years = Math.floor(months / 12);
  const rest = months % 12;
  if (rest === 0) return plural(years);
  if (rest >= 10) return `nearly ${plural(years + 1)}`;
  if (rest <= 2) return `${years}+ years`;
  return `${(Math.round((months / 12) * 10) / 10).toFixed(1)} years`;
}

/** Replaces {{experience}} (lower case) and {{Experience}} (capitalised) in every string of `value`. */
export function fillExperience(value, label) {
  if (typeof value === "string") {
    const capital = label.charAt(0).toUpperCase() + label.slice(1);
    return value.replaceAll("{{Experience}}", capital).replaceAll("{{experience}}", label);
  }
  if (Array.isArray(value)) return value.map((item) => fillExperience(item, label));
  if (value && typeof value === "object") {
    return Object.fromEntries(Object.entries(value).map(([key, item]) => [key, fillExperience(item, label)]));
  }
  return value;
}

/** Profile data with the experience wording worked out for today's date. */
export const withExperience = (profile) => fillExperience(profile, experienceLabel(profile.career_start));
