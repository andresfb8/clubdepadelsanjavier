# Rediseño "más serio" + enfoque extranjero — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Apply the redesign agreed in `docs/superpowers/specs/2026-08-03-serious-redesign-design.md` to `index.html`: muted palette, calmer hero typography, emoji removal, auto language detection, a new "Padel Camps" lead-gen section, a short-stay line on the Particulares card, and section reordering.

**Architecture:** Everything lives in the single existing `index.html` file (Tailwind config block, inline `<style>`, HTML markup, and the vanilla-JS `translations`/render logic at the bottom). No new files, no build step, no backend involved. Each task is a self-contained edit to a specific region of that file.

**Tech Stack:** Tailwind CSS (CDN, config inline), vanilla JS, no test runner in this project — verification is done by re-reading the edited HTML region and, for the final task, opening the page in a browser.

**Note on commits:** per this project's working convention, changes are left uncommitted for the user to review and commit when ready — no `git commit` steps are included in this plan.

---

### Task 1: Mute the lime accent color

**Files:**
- Modify: `index.html:27-46` (Tailwind config block)

- [ ] **Step 1: Change the `brand.lime` token**

In the `tailwind.config` script block, change:

```js
lime: '#E0ED1D',
```

to:

```js
lime: '#A9C93A',
```

- [ ] **Step 2: Verify**

Read `index.html:27-46` and confirm the value is now `#A9C93A`. Every existing `brand-lime` class in the page (buttons, borders, bullets) will pick up the new muted tone automatically — no other class names change in this task.

---

### Task 2: Calm down the hero CTA and typography

**Files:**
- Modify: `index.html:150-164` (hero H1, subtitle, CTA buttons)

- [ ] **Step 1: Reduce the H1 size and drop shadow**

Change:

```html
<h1 class="font-display font-bold text-5xl md:text-7xl lg:text-8xl leading-none mb-6 drop-shadow-lg" data-translate-key="hero-title">
```

to:

```html
<h1 class="font-display font-bold text-4xl md:text-6xl lg:text-7xl leading-none mb-6" data-translate-key="hero-title">
```

- [ ] **Step 2: Tone down the subtitle shadow**

Change:

```html
<p class="font-light text-lg md:text-2xl mb-10 max-w-3xl mx-auto drop-shadow-md leading-relaxed" data-translate-key="hero-subtitle">
```

to:

```html
<p class="font-light text-lg md:text-2xl mb-10 max-w-3xl mx-auto leading-relaxed" data-translate-key="hero-subtitle">
```

- [ ] **Step 3: Replace the glowing lime CTA with a solid white button**

Change:

```html
<a href="#escuelas" class="px-8 py-4 bg-brand-lime text-brand-blue font-display font-bold text-lg rounded shadow-[0_0_20px_rgba(224,237,29,0.4)] hover:shadow-[0_0_30px_rgba(224,237,29,0.6)] hover:bg-white transition-all uppercase tracking-wide" data-translate-key="hero-btn-aprender">
    ¡Quiero Aprender!
</a>
```

to:

```html
<a href="#escuelas" class="px-8 py-4 bg-white text-brand-blue font-display font-bold text-lg rounded shadow-lg hover:bg-brand-lime transition-all uppercase tracking-wide" data-translate-key="hero-btn-aprender">
    ¡Quiero Aprender!
</a>
```

- [ ] **Step 4: Verify**

Read `index.html:149-165` and confirm: H1 uses `text-4xl md:text-6xl lg:text-7xl` with no `drop-shadow-lg`, subtitle has no `drop-shadow-md`, and the first CTA button uses `bg-white ... hover:bg-brand-lime` instead of the old lime/glow classes.

---

### Task 3: Replace emoji icons in the "Propuesta de valor" section with SVG icons

**Files:**
- Modify: `index.html:178-198` (three value cards)

- [ ] **Step 1: Replace the graduation cap emoji**

Change:

```html
<span class="text-4xl text-brand-blue group-hover:text-brand-lime transition-colors">🎓</span>
```

to:

```html
<svg class="w-9 h-9 text-brand-blue group-hover:text-brand-lime transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 14l9-5-9-5-9 5 9 5zm0 0l6.16-3.42A12.02 12.02 0 0122 12c0 2.21-4.03 4-9 4s-9-1.79-9-4c0-.94.32-1.8.84-2.42L12 14zm0 0v7"></path></svg>
```

- [ ] **Step 2: Replace the trophy emoji**

Change:

```html
<span class="text-4xl text-brand-blue group-hover:text-brand-lime transition-colors">🏆</span>
```

to:

```html
<svg class="w-9 h-9 text-brand-blue group-hover:text-brand-lime transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M8 21h8m-4-4v4M6 4h12v3a6 6 0 01-12 0V4zM6 4H4a2 2 0 002 4M18 4h2a2 2 0 01-2 4"></path></svg>
```

- [ ] **Step 3: Replace the beer/glasses emoji**

Change:

```html
<span class="text-4xl text-brand-blue group-hover:text-brand-lime transition-colors">🍻</span>
```

to:

```html
<svg class="w-9 h-9 text-brand-blue group-hover:text-brand-lime transition-colors" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M17 3H7a1 1 0 00-1 1v6a6 6 0 0012 0V4a1 1 0 00-1-1zM6 9H4a2 2 0 000 4h2M9 21h6"></path></svg>
```

- [ ] **Step 4: Verify**

Read `index.html:178-198` and confirm all three `<span>...emoji...</span>` icons are gone, replaced by `<svg>` elements with `w-9 h-9 text-brand-blue group-hover:text-brand-lime` classes. Card text (`val-title-*`, `val-text-*`) is untouched.

---

### Task 4: Drop emojis from coach specialties

**Files:**
- Modify: `index.html:754-798` (the `coaches` array)

- [ ] **Step 1: Strip the emoji from every `specialties` entry**

Change each of the 6 `specialties` lines, e.g.:

```js
specialties: {'es': "La Víbora Letal 🐍", 'en': "The Lethal Víbora 🐍"},
```

to:

```js
specialties: {'es': "La Víbora Letal", 'en': "The Lethal Víbora"},
```

Apply the same trailing-emoji removal to the other five coaches (Alberto 🎈, Carlos 🛡️, Jorge 📉, Pedro 🚀, Antonio 🌀) — keep the text, drop the emoji and the trailing space before it.

- [ ] **Step 2: Verify**

Read `index.html:754-798` and confirm none of the six `specialties` values contain an emoji character; `roles` values are untouched.

---

### Task 5: Remove the decorative blobs from the "Filosofía" section

**Files:**
- Modify: `index.html:204-207`

- [ ] **Step 1: Remove the two blurred blob divs**

Change:

```html
<section id="filosofia" class="py-24 bg-brand-blue text-white relative overflow-hidden">
    <div class="absolute top-0 right-0 w-64 h-64 bg-brand-lime rounded-full blur-[100px] opacity-20"></div>
    <div class="absolute bottom-0 left-0 w-96 h-96 bg-cyan-400 rounded-full blur-[120px] opacity-20"></div>

    <div class="container mx-auto px-4 relative z-10">
```

to:

```html
<section id="filosofia" class="py-24 bg-brand-blue text-white relative overflow-hidden">
    <div class="container mx-auto px-4 relative z-10">
```

- [ ] **Step 2: Verify**

Read `index.html:203-212` and confirm there is no `blur-[` anywhere in the section and the section still opens with `<section id="filosofia" ...>` immediately followed by the container div.

---

### Task 6: Auto-detect browser language on first visit

**Files:**
- Modify: `index.html:955-960` (`DOMContentLoaded` handler)

- [ ] **Step 1: Add a language-detection helper and use it as the fallback**

Change:

```js
        // --- INICIALIZACIÓN ---
        document.addEventListener('DOMContentLoaded', () => {
            // Comprobar si hay una preferencia guardada, sino usar 'es'
            const storedLang = localStorage.getItem('langPref') || 'es';
            applyTranslation(storedLang); // Aplica la traducción al cargar la página y renderiza las tarjetas.
        });
```

to:

```js
        // --- INICIALIZACIÓN ---
        function detectBrowserLang() {
            const navLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
            return navLang.startsWith('es') ? 'es' : 'en';
        }

        document.addEventListener('DOMContentLoaded', () => {
            // Prioridad: preferencia guardada por el usuario > idioma del navegador > español
            const storedLang = localStorage.getItem('langPref');
            const initialLang = storedLang || detectBrowserLang();
            applyTranslation(initialLang); // Aplica la traducción al cargar la página y renderiza las tarjetas.
        });
```

- [ ] **Step 2: Verify**

Read `index.html:955-970` and confirm `detectBrowserLang` is defined before the `DOMContentLoaded` listener, and that `applyTranslation` is called with `storedLang || detectBrowserLang()` rather than the old `storedLang || 'es'`.

Manual check (do this once the file is opened in a browser in the final task): open the page with DevTools console open, run `localStorage.clear()`, reload — the page should load in English if your browser's language isn't Spanish, and in Spanish if it is.

---

### Task 7: Add the short-stay line to the "Particulares" card

**Files:**
- Modify: `index.html:317` (card text) and the two `translations` blocks (`es`/`en`)

- [ ] **Step 1: Add a new translation key in the Spanish block**

In the `'es'` object inside `translations`, right after `'esc-particulares-text'`, add:

```js
                'esc-particulares-text': 'Si quieres corregir manías, aprender la técnica perfecta o simplemente prefieres atención 100% exclusiva.',
                'esc-particulares-short-stay': 'Ideal si estás de paso pocos días.',
```

- [ ] **Step 2: Add the matching key in the English block**

In the `'en'` object, right after the English `'esc-particulares-text'`, add:

```js
                'esc-particulares-text': 'If you want to correct bad habits, learn perfect technique, or simply prefer 100% exclusive attention.',
                'esc-particulares-short-stay': 'Perfect for short stays.',
```

- [ ] **Step 3: Render the new line in the card markup**

Change:

```html
                            <p class="text-gray-600 mb-6 text-sm" data-translate-key="esc-particulares-text">Si quieres corregir manías, aprender la técnica perfecta o simplemente prefieres atención 100% exclusiva.</p>
                            <ul class="mb-8 space-y-2 text-sm text-gray-500">
                                <li class="flex items-center gap-2"><span class="text-brand-lime">✔</span> <span data-translate-key="esc-particulares-feat-1">+5€ por persona extra</span></li>
```

to:

```html
                            <p class="text-gray-600 mb-2 text-sm" data-translate-key="esc-particulares-text">Si quieres corregir manías, aprender la técnica perfecta o simplemente prefieres atención 100% exclusiva.</p>
                            <p class="text-gray-500 mb-6 text-xs italic" data-translate-key="esc-particulares-short-stay">Ideal si estás de paso pocos días.</p>
                            <ul class="mb-8 space-y-2 text-sm text-gray-500">
                                <li class="flex items-center gap-2"><span class="text-brand-lime">✔</span> <span data-translate-key="esc-particulares-feat-1">+5€ por persona extra</span></li>
```

- [ ] **Step 4: Verify**

Read the Particulares card markup and confirm the new `<p data-translate-key="esc-particulares-short-stay">` line renders between the description and the feature list, and that both `translations.es` and `translations.en` contain the `esc-particulares-short-stay` key.

---

### Task 8: Build the new "Padel Camps" section

**Files:**
- Modify: `index.html` — insert new `<section>` right after the closing `</section>` of `#escuelas` (currently `index.html:328`), before the `#equipo` section (currently `index.html:330`)
- Modify: the two `translations` blocks (`es`/`en`)

- [ ] **Step 1: Add the Spanish translation keys**

In the `'es'` object, after the `esc-particulares-btn` key, add:

```js
                'esc-particulares-btn': 'Reservar Hora',

                // PADEL CAMPS
                'camps-badge': 'Bajo consulta',
                'camps-tag': 'Para Visitantes',
                'camps-title': 'PADEL CAMPS: ENTRENA Y VIVE SAN JAVIER',
                'camps-text': '¿Vienes de fuera y quieres una experiencia de pádel completa? Combina entrenamiento intensivo con nuestros coachs y alojamiento recomendado en la zona, adaptado a los días que estés con nosotros.',
                'camps-btn': 'Quiero más información',
```

- [ ] **Step 2: Add the English translation keys**

In the `'en'` object, after the English `esc-particulares-btn` key, add:

```js
                'esc-particulares-btn': 'Book a Time',

                // PADEL CAMPS
                'camps-badge': 'On request',
                'camps-tag': 'For Visitors',
                'camps-title': 'PADEL CAMPS: TRAIN AND EXPERIENCE SAN JAVIER',
                'camps-text': "Coming from abroad and want a complete padel experience? Combine intensive training with our coaches and recommended local accommodation, tailored to however many days you're staying.",
                'camps-btn': 'I want more info',
```

- [ ] **Step 3: Insert the new section markup**

Right after the closing `</section>` of the Escuelas section (`index.html:328`) and before the `<!-- SECCIÓN DE COACHS (CARRUSEL MEJORADO) -->` comment (`index.html:330`), insert:

```html
        <!-- PADEL CAMPS (Entrenamiento + Estancia, para visitantes) -->
        <section id="padel-camps" class="py-20 bg-white">
            <div class="container mx-auto px-4">
                <div class="max-w-4xl mx-auto bg-brand-dark rounded-3xl p-10 md:p-14 text-center text-white relative overflow-hidden">
                    <span class="absolute top-6 right-6 bg-brand-lime/20 text-brand-lime text-xs font-bold uppercase tracking-widest px-4 py-1 rounded-full border border-brand-lime/40" data-translate-key="camps-badge">Bajo consulta</span>
                    <span class="text-brand-lime font-bold tracking-widest uppercase mb-2 block text-sm" data-translate-key="camps-tag">Para Visitantes</span>
                    <h2 class="font-display font-bold text-3xl md:text-4xl mb-6" data-translate-key="camps-title">PADEL CAMPS: ENTRENA Y VIVE SAN JAVIER</h2>
                    <p class="text-gray-300 max-w-2xl mx-auto mb-8 leading-relaxed" data-translate-key="camps-text">¿Vienes de fuera y quieres una experiencia de pádel completa? Combina entrenamiento intensivo con nuestros coachs y alojamiento recomendado en la zona, adaptado a los días que estés con nosotros.</p>
                    <a href="https://wa.me/34722193369?text=Hola%2C%20vengo%20de%20la%20web%20y%20me%20interesa%20el%20Padel%20Camp%20(entrenamiento%20%2B%20alojamiento)" target="_blank" class="inline-block px-8 py-4 bg-white text-brand-dark font-display font-bold rounded hover:bg-brand-lime transition-all uppercase tracking-wide" data-translate-key="camps-btn">Quiero más información</a>
                </div>
            </div>
        </section>
```

- [ ] **Step 4: Verify**

Read the region of `index.html` between the end of `#escuelas` and the start of `#equipo` and confirm the new `#padel-camps` section is there, that its four `data-translate-key` attributes (`camps-badge`, `camps-tag`, `camps-title`, `camps-text`, `camps-btn`) all have a matching key in both `translations.es` and `translations.en`, and that the WhatsApp link uses the same phone number (`34722193369`) as the rest of the site.

---

### Task 9: Move "Reseñas de Google" to right after "Valores"

**Files:**
- Modify: `index.html` — relocate the `<section id="resenas">` block

- [ ] **Step 1: Cut the Reseñas section from its current position**

The `<section id="resenas" ...> ... </section>` block currently sits between the closing `</section>` of `#competicion` and the opening `<!-- SOCIAL WALL -->` comment of `#social`. Remove that entire block (from `<!-- OPINIONES REALES (GOOGLE REVIEWS) -->` through its closing `</section>`) from that location.

- [ ] **Step 2: Paste it right after the "Valores" section**

Insert the same block (unchanged) immediately after the closing `</section>` of `#valores` (the "Propuesta de valor" section) and before the `<!-- NUESTRA FILOSOFÍA -->` comment that opens `#filosofia`.

- [ ] **Step 3: Verify final section order**

Read through `index.html`'s `<main>` and confirm the top-level `<section>` order is now: `#valores` (implicit id via comment) → `#resenas` → `#filosofia` → `#escuelas` → `#padel-camps` → `#equipo` → `#competicion` → `#social`. Confirm no section was duplicated and no section was lost — there should be exactly one `<section id="resenas">` and one `<section id="padel-camps">` in the whole file.

---

### Task 10: Full-file review and manual browser check

**Files:**
- Read-only check: `index.html` in full

- [ ] **Step 1: Structural sanity check**

Read the full `index.html` top to bottom and confirm:
- No leftover emoji in the Valores icons or coach specialties.
- No `blur-[` left in the Filosofía section.
- `brand.lime` in the Tailwind config is `#A9C93A`.
- Every `data-translate-key` used in the HTML (including the 5 new `camps-*` keys and `esc-particulares-short-stay`) has a matching entry in **both** `translations.es` and `translations.en` — a missing key means that element will render blank text when translated.
- The `<main>` section order matches Task 9's final list.

- [ ] **Step 2: Open in a browser and eyeball it**

Open `index.html` directly in a browser (double-click the file, or `start index.html` on Windows) and check:
- Hero looks calmer (smaller title, white CTA button, no lime glow).
- Value icons are line-art SVGs, not emoji.
- Reviews now appear right after the 3 value cards, before "Filosofía".
- "Padel Camps" section appears between "Escuelas" and "Equipo", with the "Bajo consulta" badge visible.
- Particulares card shows the new short-stay line.
- Switch language with the top-right selector and confirm the Padel Camps section and the short-stay line translate correctly to English.

- [ ] **Step 3: Report back**

Summarize what was checked and flag anything that looks off before considering this plan done — do not mark this task complete on the basis of the structural check alone; the visual check in Step 2 is required.

