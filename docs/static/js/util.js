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
