/* ==========================================================================
   Club de Pádel San Javier — interactions
   Dependency free. Everything degrades gracefully without JS.
   ========================================================================== */
(function () {
  "use strict";

  const doc = document.documentElement;
  const body = document.body;
  const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const finePointer = window.matchMedia("(hover: hover) and (pointer: fine)").matches;

  /* ---------------------------------------------------------- nav state */
  const nav = document.getElementById("nav");
  let lastY = window.scrollY;
  let ticking = false;

  function onScroll() {
    const y = window.scrollY;
    if (y > 24) body.classList.add("is-scrolled");
    else body.classList.remove("is-scrolled");
    lastY = y;
    ticking = false;
  }

  window.addEventListener(
    "scroll",
    () => {
      if (!ticking) {
        window.requestAnimationFrame(onScroll);
        ticking = true;
      }
    },
    { passive: true }
  );
  onScroll();

  /* ------------------------------------------------------- dropdown menu */
  const dropBtn = document.getElementById("exp-btn");
  const dropPanel = document.getElementById("exp-panel");
  let closeTimer = null;

  function setDrop(open) {
    if (!dropBtn || !dropPanel) return;
    dropBtn.setAttribute("aria-expanded", String(open));
    dropPanel.setAttribute("data-open", String(open));
  }

  if (dropBtn && dropPanel) {
    const wrap = dropBtn.closest(".nav__drop");

    dropBtn.addEventListener("click", (e) => {
      e.preventDefault();
      setDrop(dropBtn.getAttribute("aria-expanded") !== "true");
    });

    wrap.addEventListener("mouseenter", () => {
      if (!finePointer) return;
      clearTimeout(closeTimer);
      setDrop(true);
    });
    wrap.addEventListener("mouseleave", () => {
      if (!finePointer) return;
      closeTimer = window.setTimeout(() => setDrop(false), 140);
    });

    document.addEventListener("click", (e) => {
      if (!wrap.contains(e.target)) setDrop(false);
    });
    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && dropBtn.getAttribute("aria-expanded") === "true") {
        setDrop(false);
        dropBtn.focus();
      }
    });
  }

  /* --------------------------------------------------------- mobile menu */
  const burger = document.getElementById("burger");
  const menu = document.getElementById("menu");
  let menuOpen = false;
  let lastFocused = null;

  function focusables(root) {
    return Array.from(
      root.querySelectorAll('a[href], button:not([disabled]), input, select, textarea, [tabindex]:not([tabindex="-1"])')
    ).filter((el) => el.offsetParent !== null);
  }

  function setMenu(open) {
    if (!menu || !burger) return;
    menuOpen = open;
    burger.setAttribute("aria-expanded", String(open));
    burger.setAttribute("aria-label", open ? "Cerrar menú" : "Abrir menú");
    menu.setAttribute("data-open", String(open));
    menu.setAttribute("aria-hidden", String(!open));
    body.classList.toggle("is-locked", open);
    doc.style.overflow = open ? "hidden" : "";

    if (open) {
      lastFocused = document.activeElement;
      const first = focusables(menu)[0];
      if (first) window.setTimeout(() => first.focus(), 220);
    } else if (lastFocused && typeof lastFocused.focus === "function") {
      lastFocused.focus();
    }
  }

  if (burger && menu) {
    burger.addEventListener("click", () => setMenu(!menuOpen));
    menu.querySelectorAll("a").forEach((a) =>
      a.addEventListener("click", () => setMenu(false))
    );
    document.addEventListener("keydown", (e) => {
      if (!menuOpen) return;
      if (e.key === "Escape") {
        setMenu(false);
        return;
      }
      if (e.key === "Tab") {
        const items = focusables(menu);
        if (!items.length) return;
        const first = items[0];
        const last = items[items.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    });

    window.addEventListener("resize", () => {
      if (window.innerWidth > 1100 && menuOpen) setMenu(false);
    });
  }

  /* ----------------------------------------------------- scroll reveals */
  const revealTargets = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window && !reduced) {
    const io = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );
    revealTargets.forEach((el) => io.observe(el));
  } else {
    revealTargets.forEach((el) => el.classList.add("is-in"));
  }

  /* ------------------------------------------------------- hero entrance */
  const heroCopy = document.querySelector(".hero__copy, .alumnos__card");
  if (heroCopy && !reduced) {
    const kids = Array.from(heroCopy.children);
    kids.forEach((el, i) => {
      el.style.transitionDelay = `${120 + i * 90}ms`;
      window.requestAnimationFrame(() => el.classList.add("is-in"));
    });
  }

  const heroMedia = document.querySelector(".hero__media");
  if (heroMedia) {
    const img = heroMedia.querySelector("img");
    const show = () => heroMedia.classList.add("is-loaded");
    if (img && !img.complete) {
      img.addEventListener("load", show, { once: true });
      img.addEventListener("error", show, { once: true });
      window.setTimeout(show, 1200);
    } else {
      show();
    }
  }

  /* --------------------------------------------------------- rail arrows */
  document.querySelectorAll("[data-rail]").forEach((rail) => {
    const track = rail.querySelector(".rail__track");
    const prev = rail.querySelector('[data-rail-prev]');
    const next = rail.querySelector('[data-rail-next]');
    if (!track) return;

    const step = () => {
      const item = track.querySelector(".rail__item");
      const gap = parseFloat(getComputedStyle(track).columnGap || "16") || 16;
      return item ? item.getBoundingClientRect().width + gap : 320;
    };

    const sync = () => {
      const max = track.scrollWidth - track.clientWidth - 2;
      if (prev) prev.disabled = track.scrollLeft <= 2;
      if (next) next.disabled = track.scrollLeft >= max;
    };

    prev && prev.addEventListener("click", () => track.scrollBy({ left: -step(), behavior: "smooth" }));
    next && next.addEventListener("click", () => track.scrollBy({ left: step(), behavior: "smooth" }));
    track.addEventListener("scroll", () => window.requestAnimationFrame(sync), { passive: true });
    window.addEventListener("resize", sync);
    sync();
  });

  /* ----------------------------------------------------------- accordion */
  document.querySelectorAll(".acc__btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const panel = document.getElementById(btn.getAttribute("aria-controls"));
      const open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!open));
      if (panel) panel.setAttribute("data-open", String(!open));
    });
  });

  /* -------------------------------------------------- magnetic buttons */
  if (finePointer && !reduced) {
    document.querySelectorAll(".magnetic").forEach((el) => {
      el.addEventListener("pointermove", (e) => {
        const r = el.getBoundingClientRect();
        const x = ((e.clientX - r.left) / r.width - 0.5) * 12;
        const y = ((e.clientY - r.top) / r.height - 0.5) * 8;
        el.style.setProperty("--mx", `${x.toFixed(2)}px`);
        el.style.setProperty("--my", `${y.toFixed(2)}px`);
      });
      el.addEventListener("pointerleave", () => {
        el.style.setProperty("--mx", "0px");
        el.style.setProperty("--my", "0px");
      });
    });
  }

  /* ------------------------------------------------------ background video */
  const video = document.querySelector("[data-lazy-video]");
  if (video) {
    const src = video.getAttribute("data-src");
    const load = () => {
      if (src && !video.querySelector("source")) {
        const s = document.createElement("source");
        s.src = src;
        s.type = "video/mp4";
        video.appendChild(s);
        video.load();
      }
      const play = video.play();
      if (play && play.catch) play.catch(() => {});
    };

    if ("IntersectionObserver" in window) {
      const vo = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              load();
              if (video.dataset.played !== "1") {
                video.dataset.played = "1";
                video.addEventListener("playing", () => video.classList.add("is-playing"), { once: true });
              }
            } else if (!video.paused) {
              video.pause();
            }
          });
        },
        { rootMargin: "160px" }
      );
      vo.observe(video);
    } else {
      load();
    }
  }

  /* --------------------------------------------------------- contact form */
  const form = document.getElementById("form-contacto");
  if (form) {
    const note = form.querySelector("[data-form-note]");
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const get = (k) => (data.get(k) || "").toString().trim();
      const lines = [
        "Hola, escribo desde la web del club.",
        `Nombre: ${get("nombre")}`,
        get("nivel") ? `Nivel: ${get("nivel")}` : "",
        get("mensaje") ? `Mensaje: ${get("mensaje")}` : "",
      ].filter(Boolean);
      const url = `https://wa.me/34722193369?text=${encodeURIComponent(lines.join("\n"))}`;
      window.open(url, "_blank", "noopener");
      if (note) {
        note.hidden = false;
        note.textContent = "Te hemos abierto WhatsApp con el mensaje preparado. Si no se abre, escríbenos al 722 193 369.";
      }
    });
  }

  /* --------------------------------------------------- smooth in-page nav */
  document.querySelectorAll('a[href^="#"]:not([href="#"])').forEach((a) => {
    a.addEventListener("click", (e) => {
      const id = a.getAttribute("href").slice(1);
      const target = document.getElementById(id);
      if (!target) return;
      e.preventDefault();
      target.scrollIntoView({ behavior: reduced ? "auto" : "smooth", block: "start" });
      window.history.replaceState(null, "", `#${id}`);
    });
  });
})();
