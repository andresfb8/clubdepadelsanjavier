"""Static site builder for Club de Pádel San Javier.

Reads page bodies from src/pages/<name>.html and wraps them in the shared
layout (head, island nav, mobile overlay, footer, floating contact widgets).

    python tools/build.py

Output: <page>.html at the repository root.
"""
from __future__ import annotations

import hashlib
import html
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = ROOT / "src" / "pages"

SITE = "Club de Pádel San Javier"
SITE_URL = "https://clubdepadelsanjavier.netlify.app"
PHONE = "+34 722 193 369"
PHONE_RAW = "34722193369"
ADDRESS = "Polideportivo Municipal, Av. de la Unión, 30730 San Javier, Murcia"
MAPS = "https://www.google.com/maps/search/?api=1&query=Polideportivo+Municipal+San+Javier+Murcia"
INSTAGRAM = "https://www.instagram.com/clubpadelsanjavier/"
YEAR = "2026"


def wa(text: str) -> str:
    return f"https://wa.me/{PHONE_RAW}?text={quote(text)}"


def asset(path: str) -> str:
    """Cache-busting URL: appends a short content hash so a CSS/JS change is
    picked up by browsers without a manual hard refresh."""
    file = ROOT / path
    digest = hashlib.md5(file.read_bytes()).hexdigest()[:8] if file.exists() else "0"
    return f"{path}?v={digest}"


LOCAL_JSONLD = json.dumps(
    {
        "@context": "https://schema.org",
        "@type": ["SportsActivityLocation", "SportsClub"],
        "name": SITE,
        "description": (
            "Academia de pádel en San Javier, Mar Menor. Clases para todos los niveles, "
            "mini torneos los viernes y viajes de pádel."
        ),
        "telephone": f"+{PHONE_RAW}",
        "email": "info@clubpadelsanjavier.es",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "Av. de la Unión, Polideportivo Municipal",
            "addressLocality": "San Javier",
            "postalCode": "30730",
            "addressRegion": "Murcia",
            "addressCountry": "ES",
        },
        "geo": {"@type": "GeoCoordinates", "latitude": 37.8067, "longitude": -0.8353},
        "openingHoursSpecification": [
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "09:00",
                "closes": "22:00",
            },
            {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": "Saturday",
                "opens": "09:00",
                "closes": "14:00",
            },
        ],
        "sameAs": [INSTAGRAM],
        "priceRange": "€€",
        "areaServed": ["San Javier", "Mar Menor", "Murcia"],
    },
    ensure_ascii=False,
)


TOKENS = {
    "%%WA%%": wa("Hola, vengo de la web del club y quiero información."),
    "%%WA_CLASE%%": wa("Hola, quiero reservar una clase de prueba en el club de pádel de San Javier."),
    "%%WA_PARTICULAR%%": wa("Hola, quiero reservar una clase particular."),
    "%%WA_INSCRIPCION%%": wa("Hola, quiero inscribirme en la academia de pádel."),
    "%%WA_TORNEO%%": wa("Hola, quiero apuntarme al mini torneo del viernes."),
    "%%WA_VIAJE%%": wa("Hola, quiero información para venir a jugar unos días a San Javier (pádel + estancia)."),
    "%%WA_MENORES%%": wa("Hola, quiero información sobre la escuela de menores."),
    "%%WA_CAMP%%": wa("Hola, quiero información sobre el padel camp (entrenamiento + estancia)."),
    "%%WA_ALUMNO%%": wa("Hola, soy alumno del club y necesito ayuda con el área de alumnos."),
    "%%WA_INFO%%": wa("Hola, vengo de la web del club y quiero información."),
    "%%TEL%%": PHONE,
    "%%TEL_HREF%%": f"tel:+{PHONE_RAW}",
    "%%ADDRESS%%": ADDRESS,
    "%%MAPS%%": MAPS,
    "%%IG%%": INSTAGRAM,
    "%%YEAR%%": YEAR,
}

# --------------------------------------------------------------------------- icons
ICONS = {
    "arrow": '<path d="M7 17 17 7"/><path d="M9 7h8v8"/>',
    "arrow-right": '<path d="M4 12h15"/><path d="m13 6 6 6-6 6"/>',
    "chevron-down": '<path d="m6 9 6 6 6-6"/>',
    "chevron-left": '<path d="m14 6-6 6 6 6"/>',
    "chevron-right": '<path d="m10 6 6 6-6 6"/>',
    "pin": '<path d="M12 21s7-6.3 7-11a7 7 0 1 0-14 0c0 4.7 7 11 7 11Z"/><circle cx="12" cy="10" r="2.6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7.5V12l3.2 2"/>',
    "phone": '<path d="M6.2 3.5h3l1.6 4-2 1.4a11 11 0 0 0 5.3 5.3l1.4-2 4 1.6v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.2 5.7a2 2 0 0 1 2-2.2Z"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><path d="M3 20c0-3.3 2.7-5.6 6-5.6s6 2.3 6 5.6"/><path d="M16 5.2a3.2 3.2 0 0 1 0 6"/><path d="M17.5 14.8c2.1.6 3.5 2.3 3.5 4.6"/>',
    "trophy": '<path d="M7 4h10v4a5 5 0 0 1-10 0V4Z"/><path d="M7 5.5H4.5V7A3.5 3.5 0 0 0 8 10.5"/><path d="M17 5.5h2.5V7A3.5 3.5 0 0 1 16 10.5"/><path d="M12 13v4"/><path d="M8.5 20h7"/>',
    "plane": '<path d="M3.5 13.5 20 4.5l-3 15-5-4.2-2.6 3.4-.5-4.6 8.2-6.1"/>',
    "racket": '<g transform="rotate(-38 12 12)"><rect x="7.4" y="2.6" width="9.2" height="13" rx="4.6"/><path d="M12 8.2h.01M10 11.6h.01M14 11.6h.01M12 15h.01"/><path d="M12 15.6V21"/></g>',
    "calendar": '<rect x="3.5" y="5" width="17" height="15.5" rx="3"/><path d="M3.5 10h17M8 3v4M16 3v4"/>',
    "check": '<path d="m4.5 12.5 5 5L20 6.5"/>',
    "plus": '<path d="M12 5.5v13"/><path d="M5.5 12h13"/>',
    "star": '<path d="m12 3.2 2.6 5.6 6.1.8-4.5 4.2 1.2 6-5.4-3-5.4 3 1.2-6L3.3 9.6l6.1-.8L12 3.2Z"/>',
    "play": '<path d="M8 5.5v13l10.5-6.5L8 5.5Z"/>',
    "lock": '<rect x="4.5" y="10" width="15" height="10.5" rx="3"/><path d="M8.2 10V7.5a3.8 3.8 0 0 1 7.6 0V10"/>',
    "mail": '<rect x="3" y="5.5" width="18" height="13" rx="3"/><path d="m4.5 8 6.4 4.6a2 2 0 0 0 2.2 0L19.5 8"/>',
    "spark": '<path d="M12 3.5c.7 4.6 2.4 6.3 7 7-4.6.7-6.3 2.4-7 7-.7-4.6-2.4-6.3-7-7 4.6-.7 6.3-2.4 7-7Z"/>',
    "ball": '<circle cx="12" cy="12" r="8.5"/><path d="M5.2 7.5c3.6.6 6.4 3.2 7.2 6.7.5 2.2.2 4.3-.8 6"/><path d="M18.5 6.5c-3.6.6-6.4 3.2-7.2 6.7"/>',
    "waves": '<path d="M3 9c2-1.6 3.8-1.6 5.8 0S12.6 10.6 14.6 9s3.8-1.6 5.8 0"/><path d="M3 15c2-1.6 3.8-1.6 5.8 0s3.8 1.6 5.8 0 3.8-1.6 5.8 0"/>',
    "instagram": '<rect x="3.5" y="3.5" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17 7h.01"/>',
    "whatsapp": '<path d="M12.04 2.5a9.4 9.4 0 0 0-8 14.3L2.5 21.5l4.8-1.5a9.4 9.4 0 1 0 4.7-17.5Zm0 1.8a7.6 7.6 0 0 1 0 15.2 7.6 7.6 0 0 1-3.9-1.1l-.4-.2-2.7.8.8-2.6-.2-.4A7.6 7.6 0 0 1 12 4.3Zm-3 3.4c-.2 0-.5.1-.7.3-.3.3-.7.8-.7 1.6s.6 1.6.7 1.7c.1.2 1.2 2 3 2.8 1.5.6 1.8.5 2.1.5.4 0 1.2-.5 1.4-1s.2-.9.2-1c0-.1-.2-.2-.4-.3l-1.3-.6c-.2-.1-.3-.1-.5.1l-.7.8c-.1.2-.3.2-.5.1a6 6 0 0 1-1.8-1.1 6.6 6.6 0 0 1-1.2-1.5c-.1-.2 0-.3.1-.4l.3-.4c.1-.2.1-.3 0-.5l-.5-1.3c-.2-.4-.4-.4-.5-.4h-.5Z"/>',
    "swipe": '<path d="M4 12h13"/><path d="m13 8 4 4-4 4"/><path d="M20 5v14"/>',
    "shield": '<path d="M12 3 5 5.6v5.6c0 4.3 2.8 8.2 7 9.2 4.2-1 7-4.9 7-9.2V5.6L12 3Z"/><path d="m9 11.8 2.2 2.2 4-4.4"/>',
    "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.2 5.2l1.4 1.4M17.4 17.4l1.4 1.4M18.8 5.2l-1.4 1.4M6.6 17.4l-1.4 1.4"/>',
    "target": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.6"/><circle cx="12" cy="12" r="1"/>',
    "route": '<circle cx="6" cy="18.5" r="2.5"/><circle cx="18" cy="5.5" r="2.5"/><path d="M8.5 18.5h6a3.5 3.5 0 0 0 0-7h-4a3.5 3.5 0 0 1 0-7h5"/>',
}


def icon(name: str, cls: str = "", fill: bool = False) -> str:
    extra = " i--fill" if fill else ""
    return (
        f'<svg class="i {cls}{extra}" aria-hidden="true" focusable="false">'
        f'<use href="#i-{name}"/></svg>'
    )


def sprite() -> str:
    items = "".join(
        f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items()
    )
    return f'<svg class="sprite" aria-hidden="true" focusable="false" width="0" height="0">{items}</svg>'


# --------------------------------------------------------------------------- nav
NAV_MAIN = [
    ("drop:clases", "Clases", "clases"),
    ("drop:exp", "Experiencias", "exp"),
    ("entrenadores.html", "Entrenadores", "entrenadores"),
    ("horarios.html", "Horarios", "horarios"),
    ("academia.html", "Academia", "academia"),
    ("contacto.html", "Contacto", "contacto"),
]

DROPDOWNS = {
    "clases": {
        "active": {"clases"},
        "items": [
            ("clases.html#adultos", "Clases de adultos", "Iniciación, intermedio y competición", "users"),
            ("clases.html#menores", "Escuela de menores", "Desde 6 años, después del cole", "ball"),
            ("clases.html#precios", "Precios y formatos", "Escuela, particulares y bonos", "target"),
        ],
    },
    "exp": {
        "active": {"torneos", "viajes"},
        "items": [
            ("torneos.html", "Mini torneos del viernes", "Cada viernes, plazas limitadas", "trophy"),
            ("viajes.html", "Ven a San Javier", "Pádel + Mar Menor, con estancia", "waves"),
        ],
    },
}


def brand(href: str = "index.html") -> str:
    return f"""<a class="brand" href="{href}" aria-label="{SITE} — inicio">
      <span class="brand__mark">
        <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true">
          <circle cx="12" cy="12" r="8.4" fill="none" stroke="#0f172a" stroke-width="1.5"/>
          <path d="M5.6 8.4c3.2.6 5.6 3 6.3 6.1.4 1.9.2 3.7-.6 5.2" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
          <path d="M18.4 7.6c-3.2.6-5.6 3-6.3 6.1" fill="none" stroke="#0f172a" stroke-width="1.5" stroke-linecap="round"/>
          <circle cx="12" cy="12" r="1.6" fill="#0f172a"/>
        </svg>
      </span>
      <span class="brand__text"><strong>Club de Pádel</strong><span>San Javier · Mar Menor</span></span>
    </a>"""


def nav_dropdown(key: str, label: str, active: str) -> str:
    spec = DROPDOWNS[key]
    current = ' aria-current="page"' if active in spec["active"] else ""
    items = "".join(
        f"""<a class="nav__panel-link" href="{href}">
              <span class="nav__panel-icon">{icon(ic)}</span>
              <span><strong>{title}</strong><span>{desc}</span></span>
            </a>"""
        for href, title, desc, ic in spec["items"]
    )
    return f"""<div class="nav__drop" data-drop>
          <button class="nav__drop-btn" type="button" id="{key}-btn" aria-expanded="false" aria-controls="{key}-panel"{current}>
            {label} {icon("chevron-down")}
          </button>
          <div class="nav__panel" id="{key}-panel" data-open="false">
            {items}
          </div>
        </div>"""


def nav(active: str) -> str:
    links = []
    for href, label, key in NAV_MAIN:
        if href.startswith("drop:"):
            links.append(nav_dropdown(href.split(":", 1)[1], label, active))
        else:
            current = ' aria-current="page"' if active == key else ""
            links.append(f'<a class="nav__link" href="{href}"{current}>{label}</a>')

    return f"""<header class="nav" id="nav">
    <div class="nav__inner">
      {brand()}
      <nav class="nav__links" aria-label="Navegación principal">
        {''.join(links)}
      </nav>
      <div class="nav__actions">
        <a class="btn btn--ghost btn--sm" href="area-alumnos.html">Área de alumnos</a>
        <a class="btn btn--primary btn--sm" href="%%WA_CLASE%%" target="_blank" rel="noopener">
          Reservar
          <span class="btn__icon">{icon("arrow")}</span>
        </a>
        <button class="burger" type="button" id="burger" aria-expanded="false" aria-controls="menu" aria-label="Abrir menú">
          <span></span><span></span><span></span>
        </button>
      </div>
    </div>
  </header>"""


def nav_minimal() -> str:
    return f"""<header class="nav nav--minimal" id="nav">
    <div class="nav__inner">
      {brand()}
      <a class="btn btn--outline-light btn--sm" href="index.html">
        Volver a la web
        <span class="btn__icon">{icon("arrow")}</span>
      </a>
    </div>
  </header>"""


def menu(active: str) -> str:
    items = [
        ("clases.html", "Clases", "clases"),
        ("clases.html#menores", "Escuela de menores", "menores"),
        ("torneos.html", "Mini torneos", "torneos"),
        ("viajes.html", "Ven a San Javier", "viajes"),
        ("entrenadores.html", "Entrenadores", "entrenadores"),
        ("horarios.html", "Horarios y precios", "horarios"),
        ("academia.html", "Academia", "academia"),
        ("contacto.html", "Contacto", "contacto"),
    ]
    links = "".join(
        f'<li class="menu__item"><a class="menu__link" href="{href}" style="--i:{i}"'
        f'{" aria-current=\"page\"" if active == key else ""}>{label}<small>{i + 1:02d}</small></a></li>'
        for i, (href, label, key) in enumerate(items)
    )
    return f"""<div class="menu" id="menu" data-open="false" aria-hidden="true">
    <nav aria-label="Menú móvil">
      <ul class="menu__list">{links}</ul>
    </nav>
    <div class="menu__foot">
      <a href="area-alumnos.html">{icon("lock")} Área de alumnos</a>
      <a href="%%WA_CLASE%%" target="_blank" rel="noopener">{icon("whatsapp", fill=True)} WhatsApp · %%TEL%%</a>
      <a href="%%IG%%" target="_blank" rel="noopener">{icon("instagram")} @clubpadelsanjavier</a>
    </div>
  </div>"""


# ------------------------------------------------------------------------ footer
def footer(bare: bool = False) -> str:
    if bare:
        return f"""<footer class="footer footer--bare">
    <div class="wrap">
      <div class="footer__bottom" style="border:0">
        <p>© %%YEAR%% {SITE} · San Javier, Murcia</p>
        <div class="footer__legal"><a href="index.html">Volver a la web</a><a href="contacto.html">Contacto</a></div>
      </div>
    </div>
  </footer>"""

    return f"""<footer class="footer">
    <div class="wrap">
      <div class="footer__top">
        <div class="footer__brand">
          {brand()}
          <p>Academia de pádel en San Javier, Mar Menor. Clases para todos los niveles, escuela de menores, mini torneos los viernes y pádel + estancia para quien viene a jugar.</p>
          <div class="footer__cta">
            <a class="btn btn--primary btn--sm" href="%%WA_CLASE%%" target="_blank" rel="noopener">Reserva tu clase<span class="btn__icon">{icon("arrow")}</span></a>
            <a class="btn btn--outline-light btn--sm" href="area-alumnos.html">{icon("lock")} Área de alumnos</a>
          </div>
        </div>
        <div class="footer__col">
          <h3>Academia</h3>
          <div class="footer__links">
            <a href="clases.html">Clases de adultos</a>
            <a href="clases.html#menores">Escuela de menores</a>
            <a href="academia.html">La academia</a>
            <a href="entrenadores.html">Entrenadores</a>
            <a href="horarios.html">Horarios y precios</a>
            <a href="area-alumnos.html">Área de alumnos</a>
          </div>
        </div>
        <div class="footer__col">
          <h3>Experiencias</h3>
          <div class="footer__links">
            <a href="torneos.html">Mini torneos de los viernes</a>
            <a href="viajes.html">Ven a San Javier</a>
            <a href="%%IG%%" target="_blank" rel="noopener">Comunidad en Instagram</a>
            <a href="contacto.html">Contacto y ubicación</a>
          </div>
        </div>
        <div class="footer__col">
          <h3>Ven al club</h3>
          <div class="footer__links">
            <address>%%ADDRESS%%</address>
            <a href="%%TEL_HREF%%">%%TEL%%</a>
            <a href="%%MAPS%%" target="_blank" rel="noopener">Cómo llegar</a>
            <a href="%%WA%%" target="_blank" rel="noopener">WhatsApp</a>
          </div>
        </div>
      </div>
      <div class="footer__wordmark" aria-hidden="true">SAN JAVIER</div>
      <div class="footer__bottom">
        <p>© %%YEAR%% {SITE}. Todos los derechos reservados.</p>
        <div class="footer__legal">
          <a href="legal.html">Aviso legal</a>
          <a href="legal.html#privacidad">Privacidad</a>
          <a href="legal.html#cookies">Cookies</a>
          <a href="horarios.html">Horarios</a>
        </div>
      </div>
    </div>
  </footer>"""


def floating() -> str:
    return f"""<a class="wa-fab" href="%%WA_CLASE%%" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp">
    {icon("whatsapp", fill=True)}
    <span>WhatsApp</span>
  </a>

  <div class="mobile-bar">
    <a class="btn btn--primary" href="%%WA_CLASE%%" target="_blank" rel="noopener">Reservar clase<span class="btn__icon">{icon("arrow")}</span></a>
    <a class="btn btn--ghost" href="area-alumnos.html">{icon("lock")} Alumnos</a>
  </div>"""


# -------------------------------------------------------------------------- head
def head(
    title: str,
    description: str,
    body_class: str = "",
    jsonld: str = "",
    canonical: str = "",
    noindex: bool = False,
) -> str:
    schema = f'\n  <script type="application/ld+json">{jsonld}</script>' if jsonld else ""
    link = f'\n  <link rel="canonical" href="{canonical}">' if canonical else ""
    ogurl = f'\n  <meta property="og:url" content="{canonical}">' if canonical else ""
    robots = '\n  <meta name="robots" content="noindex, follow">' if noindex else ""
    return f"""<!DOCTYPE html>
<html lang="es" class="no-js">
<head>
  <meta charset="utf-8">
  <script>document.documentElement.classList.replace('no-js', 'js');</script>
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(description)}">{robots}
  <meta name="theme-color" content="#0f172a">
  <link rel="icon" href="{asset('assets/favicon.svg')}" type="image/svg+xml">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE}">
  <meta property="og:locale" content="es_ES">
  <meta property="og:title" content="{html.escape(title)}">
  <meta property="og:description" content="{html.escape(description)}">
  <meta property="og:image" content="assets/img/og.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wdth,wght@12..96,75..100,200..800&family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{asset('assets/css/site.css')}">
  <link rel="stylesheet" href="{asset('assets/css/components.css')}">
  <link rel="stylesheet" href="{asset('assets/css/pages.css')}">{link}{ogurl}{schema}
</head>
<body class="{body_class}">"""


def scripts() -> str:
    return f"""  <script src="{asset('assets/js/site.js')}" defer></script>
</body>
</html>"""


# --------------------------------------------------------------------- registry
PAGES = [
    {
        "file": "index.html",
        "nav": "inicio",
        "title": "Academia de pádel en San Javier · Club de Pádel San Javier",
        "desc": "Clases de pádel en San Javier, Mar Menor. Clases particulares, academia, mini torneos los viernes y viajes de pádel. Reserva tu clase de prueba.",
        "jsonld": LOCAL_JSONLD,
    },
    {
        "file": "clases.html",
        "nav": "clases",
        "title": "Clases de pádel en San Javier · Academia y particulares",
        "desc": "Clases y niveles de pádel en San Javier: iniciación, intermedio, competición y clases particulares. Grupos reducidos con entrenadores titulados.",
    },
    {
        "file": "torneos.html",
        "nav": "torneos",
        "title": "Mini torneos de pádel los viernes · San Javier",
        "desc": "Mini torneos de pádel cada viernes en San Javier. Formato, niveles, plazas limitadas y calendario de próximas fechas en el Mar Menor.",
    },
    {
        "file": "viajes.html",
        "nav": "viajes",
        "title": "Ven a jugar a San Javier · Pádel y Mar Menor",
        "desc": "Escapadas de pádel en San Javier: entrenamiento, alojamiento y Mar Menor. Planes de fin de semana a una semana para jugadores de todos los niveles.",
    },
    {
        "file": "academia.html",
        "nav": "academia",
        "title": "La academia de pádel de San Javier · Metodología",
        "desc": "Quiénes somos, cómo entrenamos y dónde. Academia de pádel en San Javier, Mar Menor, con grupos por nivel e instalaciones municipales.",
    },
    {
        "file": "entrenadores.html",
        "nav": "entrenadores",
        "title": "Entrenadores de pádel · San Javier",
        "desc": "El equipo de entrenadores del Club de Pádel San Javier: titulación, especialidad y coordinación de la escuela de adultos y menores.",
    },
    {
        "file": "horarios.html",
        "nav": "horarios",
        "title": "Horarios y precios · Clases de pádel en San Javier",
        "desc": "Horarios de la academia y precios de clases de pádel en San Javier: escuelas de adultos y menores, clases particulares y bonos.",
    },
    {
        "file": "contacto.html",
        "nav": "contacto",
        "title": "Contacto · Club de Pádel San Javier",
        "desc": "Contacta con la academia de pádel de San Javier: dirección en el Polideportivo Municipal, WhatsApp, horarios y cómo llegar.",
        "jsonld": LOCAL_JSONLD,
    },
    {
        "file": "estilo.html",
        "nav": "estilo",
        "title": "Guía visual · Sistema de diseño del Club de Pádel San Javier",
        "desc": "Biblioteca de componentes del sitio: color, tipografía, botones, tarjetas, formularios y movimiento.",
        "body_class": "page-guia",
        "noindex": True,
    },
    {
        "file": "legal.html",
        "nav": "legal",
        "title": "Aviso legal y privacidad · Club de Pádel San Javier",
        "desc": "Aviso legal, política de privacidad y cookies del Club de Pádel San Javier.",
        "body_class": "page-legal",
    },
    {
        "file": "area-alumnos.html",
        "nav": "alumnos",
        "title": "Área de alumnos · Club de Pádel San Javier",
        "desc": "Accede a tu área de alumno del Club de Pádel San Javier: reservas, seguimiento y comunicación con el equipo.",
        "bare": True,
        "body_class": "page-alumnos",
    },
]


def build_page(spec: dict) -> str:
    file = spec["file"]
    stem = file.replace(".html", "")
    body_path = PAGES_DIR / f"{stem}.html"
    if not body_path.exists():
        raise SystemExit(f"Missing page body: {body_path}")
    body = body_path.read_text(encoding="utf-8")

    bare = spec.get("bare", False)
    canonical = f"{SITE_URL}/" if file == "index.html" else f"{SITE_URL}/{file}"
    chunks = [
        head(
            spec["title"],
            spec["desc"],
            spec.get("body_class", ""),
            spec.get("jsonld", ""),
            canonical,
            spec.get("noindex", False),
        )
    ]
    chunks.append(sprite())
    chunks.append('<a class="skip" href="#main">Saltar al contenido</a>')
    chunks.append('<div class="grain" aria-hidden="true"></div>')
    if bare:
        chunks.append(nav_minimal())
    else:
        chunks.append(nav(spec["nav"]))
        chunks.append(menu(spec["nav"]))
    chunks.append(f'<main id="main">{body}</main>')
    chunks.append(footer(bare))
    if not bare:
        chunks.append(floating())
    chunks.append(scripts())

    out = "\n".join(chunks)
    for token, value in TOKENS.items():
        out = out.replace(token, value)
    (ROOT / file).write_text(out, encoding="utf-8")
    return file


def build_extras() -> None:
    """sitemap.xml + robots.txt pointing at SITE_URL."""
    urls = []
    for spec in PAGES:
        if spec["nav"] in {"alumnos", "legal", "estilo"}:
            continue
        loc = f"{SITE_URL}/" if spec["file"] == "index.html" else f"{SITE_URL}/{spec['file']}"
        priority = "1.0" if spec["file"] == "index.html" else "0.8"
        urls.append(
            f"  <url>\n    <loc>{loc}</loc>\n    <changefreq>monthly</changefreq>\n"
            f"    <priority>{priority}</priority>\n  </url>"
        )
    sitemap = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(urls)
        + "\n</urlset>\n"
    )
    (ROOT / "sitemap.xml").write_text(sitemap, encoding="utf-8")
    robots = f"User-agent: *\nAllow: /\nDisallow: /area-alumnos.html\nDisallow: /estilo.html\n\nSitemap: {SITE_URL}/sitemap.xml\n"
    (ROOT / "robots.txt").write_text(robots, encoding="utf-8")


def main() -> None:
    import sys

    only = [a for a in sys.argv[1:] if not a.startswith("-")]
    specs = [s for s in PAGES if not only or s["file"] in only]
    built = [build_page(spec) for spec in specs]
    if not only:
        build_extras()
    print(f"Built {len(built)} pages: {', '.join(built)}")


if __name__ == "__main__":
    main()
