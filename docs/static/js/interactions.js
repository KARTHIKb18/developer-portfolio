// Behaviour that is independent of the data: theme, menu, motion, view mode and the skill filter.
import { fmt, prefersReducedMotion } from "./util.js";

const $ = (selector, root = document) => root.querySelector(selector);
const $$ = (selector, root = document) => Array.from(root.querySelectorAll(selector));
const announce = (text) => {
  const el = $("#live-status");
  if (el) el.textContent = text;
};

/* ---------- Theme ---------- */
export function initTheme() {
  $("#theme-toggle")?.addEventListener("click", () => {
    const dark = document.documentElement.classList.toggle("dark");
    try {
      localStorage.setItem("theme", dark ? "dark" : "light");
    } catch {
      /* storage unavailable */
    }
  });
}

/* ---------- Mobile menu (Escape closes, Tab stays inside, focus returns) ---------- */
export function initMenu() {
  const button = $("#menu-toggle");
  const panel = $("#mobile-menu");
  if (!button || !panel) return;

  const setOpen = (open) => {
    panel.hidden = !open;
    button.setAttribute("aria-expanded", String(open));
    button.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    document.body.style.overflow = open ? "hidden" : "";
  };

  button.addEventListener("click", () => setOpen(panel.hidden));
  panel.addEventListener("click", (event) => {
    if (event.target.closest("[data-close-menu]")) setOpen(false);
  });
  document.addEventListener("keydown", (event) => {
    if (panel.hidden) return;
    if (event.key === "Escape") {
      setOpen(false);
      button.focus();
    } else if (event.key === "Tab") {
      const items = [button, ...$$("a[href]", panel)];
      const first = items[0];
      const last = items[items.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
  });
  window.matchMedia("(min-width: 1024px)").addEventListener("change", (e) => e.matches && setOpen(false));
}

/* ---------- Pointer spotlight on cards (decorative) ---------- */
export function initSpotlight() {
  document.addEventListener("pointermove", (event) => {
    const card = event.target.closest?.(".spotlight");
    if (!card) return;
    const rect = card.getBoundingClientRect();
    card.style.setProperty("--mx", `${event.clientX - rect.left}px`);
    card.style.setProperty("--my", `${event.clientY - rect.top}px`);
  });
}

/* ---------- Print ---------- */
export function initPrint() {
  $("#print-btn")?.addEventListener("click", () => window.print());
}

/* ---------- Compact / Detailed view ---------- */
export function currentView() {
  return document.documentElement.getAttribute("data-view") === "detailed" ? "detailed" : "compact";
}

export function applyView(mode, persist = true) {
  document.documentElement.setAttribute("data-view", mode);
  if (persist) {
    try {
      localStorage.setItem("view-mode", mode);
    } catch {
      /* storage unavailable */
    }
    announce(`${mode === "detailed" ? "Detailed" : "Compact"} view selected.`);
  }
  $$("[data-view-btn]").forEach((b) => b.setAttribute("aria-pressed", String(b.dataset.viewBtn === mode)));
  $$("details[data-exp-details]").forEach((d) => {
    d.open = mode === "detailed";
  });
}

export function initViewMode() {
  document.addEventListener("click", (event) => {
    const button = event.target.closest("[data-view-btn]");
    if (button) applyView(button.dataset.viewBtn);
  });
}

/* ---------- Skill filter: highlight roles and projects that use a skill ---------- */
let active = null;

export function applySkillFilter() {
  const targets = $$("[data-tech]");
  targets.forEach((el) => {
    el.classList.remove("is-match", "is-dim");
    if (!active) return;
    const hit = el.dataset.tech.split("|").some((t) => active.terms.has(t));
    el.classList.add(hit ? "is-match" : "is-dim");
  });
  // A role is relevant when one of its projects matches.
  targets.forEach((el) => {
    if (el.classList.contains("is-dim") && el.querySelector(".is-match")) {
      el.classList.remove("is-dim");
      el.classList.add("is-match");
    }
  });

  $$("[data-skill-btn]").forEach((b) => b.setAttribute("aria-pressed", String(Boolean(active) && b.dataset.label === active.name)));

  const bar = $("#skill-bar");
  if (!bar) return;
  bar.hidden = !active;
  if (active) {
    const roles = $$(".exp-item.is-match, .r-job.is-match").length;
    const projects = $$(".proj-row.is-match, .r-project.is-match").length;
    $("#skill-bar-name").textContent = active.name;
    $("#skill-bar-count").textContent = `· ${roles} ${roles === 1 ? "role" : "roles"}, ${projects} ${projects === 1 ? "project" : "projects"}`;
  }
}

export function initSkillFilter() {
  const set = (value) => {
    active = value;
    applySkillFilter();
    announce(value ? `Highlighting roles and projects that use ${value.name}.` : "Skill filter cleared.");
  };
  document.addEventListener("click", (event) => {
    const button = event.target.closest("[data-skill-btn]");
    if (!button) return;
    const same = active && active.name === button.dataset.label;
    set(same ? null : { name: button.dataset.label, terms: new Set(button.dataset.terms.split("|")) });
  });
  $("#skill-bar-clear")?.addEventListener("click", () => set(null));
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && active && $("#mobile-menu")?.hidden !== false) set(null);
  });
}

/* ---------- Things that need the rendered content ---------- */
export function observeReveal(root = document) {
  const items = $$(".reveal:not(.in)", root);
  if (!("IntersectionObserver" in window) || prefersReducedMotion()) {
    items.forEach((el) => el.classList.add("in"));
    return;
  }
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("in");
        io.unobserve(entry.target);
      });
    },
    { rootMargin: "0px 0px -60px 0px" },
  );
  items.forEach((el) => io.observe(el));
}

export function initCountUp(root = document) {
  if (prefersReducedMotion() || !("IntersectionObserver" in window)) return;
  $$(".count", root).forEach((el) => {
    const to = Number(el.dataset.countTo);
    const from = el.dataset.countFrom ? Number(el.dataset.countFrom) : null;
    const live = $("[data-count-live]", el);
    const io = new IntersectionObserver(
      ([entry]) => {
        if (!entry.isIntersecting) return;
        io.disconnect();
        const start = performance.now();
        const step = (now) => {
          const t = Math.min(1, (now - start) / 1400);
          const eased = 1 - Math.pow(1 - t, 3);
          live.textContent = from !== null ? `${fmt(Math.round(from * eased))}–${fmt(Math.round(to * eased))}` : fmt(Math.round(to * eased));
          if (t < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
      },
      { threshold: 0.4 },
    );
    io.observe(el);
  });
}

export function initRotator(root = document) {
  const el = $(".focus-text", root);
  if (!el || prefersReducedMotion()) return;
  const phrases = JSON.parse(el.dataset.phrases || "[]");
  if (phrases.length < 2) return;
  let i = 0;
  window.setInterval(() => {
    if (document.hidden) return;
    i = (i + 1) % phrases.length;
    el.textContent = phrases[i];
    el.classList.remove("swap");
    void el.offsetWidth;
    el.classList.add("swap");
  }, 2600);
}

export function initTimeline(root = document) {
  const timeline = $("[data-timeline]", root);
  if (!timeline) return;
  if (prefersReducedMotion()) return;
  let ticking = false;
  const update = () => {
    const rect = timeline.getBoundingClientRect();
    const progress = Math.min(1, Math.max(0, (window.innerHeight * 0.7 - rect.top) / rect.height));
    timeline.style.setProperty("--progress", progress.toFixed(3));
    ticking = false;
  };
  window.addEventListener("scroll", () => {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(update);
    }
  }, { passive: true });
  update();
}

export function initActiveNav() {
  const links = $$(".nav-link[data-nav]");
  if (!links.length || !("IntersectionObserver" in window)) return;
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        links.forEach((link) => {
          const on = link.dataset.nav === entry.target.id;
          link.classList.toggle("is-active", on);
          if (on) link.setAttribute("aria-current", "location");
          else link.removeAttribute("aria-current");
        });
      });
    },
    { rootMargin: "-45% 0px -50% 0px" },
  );
  links.forEach((link) => {
    const target = document.getElementById(link.dataset.nav);
    if (target) io.observe(target);
  });
}

/* ---------- Reading progress bar ---------- */
export function initProgress() {
  const bar = $("#progress");
  if (!bar) return;
  let ticking = false;
  const update = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.setProperty("--p", max > 0 ? (window.scrollY / max).toFixed(4) : "0");
    ticking = false;
  };
  window.addEventListener("scroll", () => {
    if (!ticking) {
      ticking = true;
      requestAnimationFrame(update);
    }
  }, { passive: true });
  update();
}

/* ---------- Round "View" label that follows the pointer over project rows (mouse only) ---------- */
export function initCursorLabel() {
  if (prefersReducedMotion() || !window.matchMedia("(hover: hover) and (pointer: fine)").matches) return;
  const label = document.createElement("div");
  label.className = "cursor-label";
  label.setAttribute("aria-hidden", "true");
  document.body.appendChild(label);
  document.addEventListener("pointermove", (event) => {
    const target = event.target.closest?.("[data-cursor]");
    if (!target) {
      label.classList.remove("on");
      return;
    }
    label.textContent = target.dataset.cursor;
    label.style.transform = `translate3d(${event.clientX + 14}px, ${event.clientY + 14}px, 0)`;
    label.classList.add("on");
  });
  document.addEventListener("pointerleave", () => label.classList.remove("on"));
}
