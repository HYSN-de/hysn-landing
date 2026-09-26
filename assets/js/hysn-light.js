/* HYSN light theme: small additions on top of Bizox main.js
   - clip-path image reveal on scroll
   - process line draw
   - subtle hero parallax (GSAP ScrollTrigger, already bundled in plugin.js) */
(function () {
  "use strict";
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if ("IntersectionObserver" in window && !reduce) {
    document.documentElement.classList.add("js-reveal");
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add("is-in");
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.18, rootMargin: "0px 0px -40px 0px" });
    document.querySelectorAll(".hy-reveal, .hy-steps").forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll(".hy-steps").forEach(function (el) { el.classList.add("is-in"); });
  }

  if (!reduce && window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
    gsap.to(".hy-hero-media", {
      yPercent: 8,
      ease: "none",
      scrollTrigger: { trigger: ".hy-hero", start: "top top", end: "bottom top", scrub: true }
    });
  }
})();

/* Standalone landing: close the mobile menu after tapping an anchor link */
(function () {
  document.querySelectorAll('.xb-menu-primary a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function () {
      document.querySelectorAll(".xb-header-menu").forEach(function (m) { m.classList.remove("active"); });
      document.querySelectorAll(".xb-nav-mobile").forEach(function (b) { b.classList.remove("active"); });
    });
  });
})();

/* Impressum / Datenschutz open in an on-page dialog (no extra pages) */
(function () {
  function open(id) {
    var d = document.getElementById(id);
    if (!d) return;
    document.querySelectorAll("dialog[open]").forEach(function (o) { o.close(); });
    if (d.showModal) d.showModal(); else d.setAttribute("open", "");
    document.documentElement.style.overflow = "hidden";
  }
  document.addEventListener("click", function (e) {
    var t = e.target.closest("[data-dialog]");
    if (t) { e.preventDefault(); open(t.getAttribute("data-dialog")); return; }
    if (e.target.closest(".hy-dialog-close")) { e.target.closest("dialog").close(); return; }
    if (e.target.tagName === "DIALOG") e.target.close(); /* click on backdrop */
  });
  document.querySelectorAll("dialog.hy-dialog").forEach(function (d) {
    d.addEventListener("close", function () { document.documentElement.style.overflow = ""; });
  });
  if (location.hash === "#impressum") open("dlg-impressum");
  if (location.hash === "#datenschutz") open("dlg-datenschutz");
})();

/* Before / after comparison slider: drag, click, keyboard, touch (vertical scroll still works) */
(function () {
  document.querySelectorAll(".hy-compare").forEach(function (box) {
    var range = box.querySelector(".hy-compare-range");
    var capB = document.querySelector(".hy-cap-before");
    var capA = document.querySelector(".hy-cap-after");
    var dragging = false, touched = false, hintRaf = null;

    function set(p) {
      p = Math.max(0, Math.min(100, p));
      box.style.setProperty("--pos", p + "%");
      range.value = Math.round(p);
      range.setAttribute("aria-valuetext", Math.round(100 - p) + " % Nachher sichtbar");
      if (capB && capA) { capB.classList.toggle("is-dim", p < 35); capA.classList.toggle("is-dim", p > 65); }
    }
    function fromEvent(e) {
      var r = box.getBoundingClientRect();
      return ((e.clientX - r.left) / r.width) * 100;
    }
    function touch() {
      if (!touched) { touched = true; box.classList.add("is-touched"); }
      if (hintRaf) { cancelAnimationFrame(hintRaf); hintRaf = null; }
    }

    box.addEventListener("pointerdown", function (e) {
      if (e.pointerType === "mouse" && e.button !== 0) return;
      touch(); dragging = true; box.classList.add("is-dragging");
      box.setPointerCapture && box.setPointerCapture(e.pointerId);
      set(fromEvent(e));
    });
    box.addEventListener("pointermove", function (e) { if (dragging) set(fromEvent(e)); });
    ["pointerup", "pointercancel", "lostpointercapture"].forEach(function (t) {
      box.addEventListener(t, function () { dragging = false; box.classList.remove("is-dragging"); });
    });
    range.addEventListener("input", function () { touch(); set(+range.value); });

    /* one gentle sweep the first time it scrolls into view, so people see it's interactive */
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!reduce && "IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (en) {
        if (!en[0].isIntersecting) return;
        io.disconnect();
        var keys = [[0, 50], [700, 22], [1500, 78], [2300, 50]], t0 = null;
        var ease = function (x) { return x < .5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2; };
        setTimeout(function () {
          function step(ts) {
            if (touched) return;
            if (!t0) t0 = ts;
            var t = ts - t0, i = 1;
            while (i < keys.length - 1 && t > keys[i][0]) i++;
            var a = keys[i - 1], b = keys[i];
            var k = Math.min(1, (t - a[0]) / (b[0] - a[0]));
            set(a[1] + (b[1] - a[1]) * ease(k));
            if (t < keys[keys.length - 1][0]) hintRaf = requestAnimationFrame(step);
          }
          hintRaf = requestAnimationFrame(step);
        }, 600);
      }, { threshold: 0.5 });
      io.observe(box);
    }
    set(50);
  });
})();
