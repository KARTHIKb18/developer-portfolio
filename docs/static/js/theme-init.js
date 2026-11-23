// Runs before first paint so the saved theme and view mode apply without a flash.
document.documentElement.classList.add("js");
(function () {
  try {
    var theme = localStorage.getItem("theme");
    var dark = theme ? theme === "dark" : window.matchMedia("(prefers-color-scheme: dark)").matches;
    if (dark) document.documentElement.classList.add("dark");
    var view = localStorage.getItem("view-mode");
    if (view === "compact" || view === "detailed") document.documentElement.setAttribute("data-view", view);
  } catch (e) {
    /* storage unavailable */
  }
})();
