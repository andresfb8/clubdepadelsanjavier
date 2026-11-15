# Guía de estilo — Club de Pádel San Javier

Sistema de diseño del sitio. Todo vive en `assets/css/site.css` (tokens, tipografía,
layout, navegación) y `assets/css/components.css` (componentes).

## Concepto

Deporte mediterráneo, limpio y premium. Base de papel arena, tinta verde-marino muy
oscura, lima de pelota solo para acción, y coral como único acento cálido. Sin neones,
sin degradados morados, sin tarjetas flotando en el vacío: los bloques se apoyan en
"bandejas" (doble bisel) y el aire hace el resto.

## Color

| Token | Valor | Uso |
| --- | --- | --- |
| `--paper` | `#F4F0E7` | Fondo base (papel arena) |
| `--paper-2` | `#FBF8F1` | Superficies y tarjetas |
| `--ink` | `#0A1E1B` | Texto principal y secciones oscuras |
| `--ink-2` | `#123330` | Superficie oscura elevada |
| `--sea` | `#0E4A42` | Verde pista, enlaces y datos |
| `--lime` | `#D8F14B` | CTA principal y acentos |
| `--lime-deep` | `#C6E02F` | Hover del CTA |
| `--coral` | `#FF6A4D` | Punto de atención, badges vivos |
| `--muted` | `rgba(10,30,27,.62)` | Texto secundario |
| `--line` | `rgba(10,30,27,.14)` | Hairline estándar |

Reglas: el lima **nunca** lleva texto claro; siempre tinta. El coral no se usa para
texto pequeño sobre arena (contraste insuficiente): solo puntos, badges y detalles.

## Tipografía

- **Display / titulares:** `Bricolage Grotesque` variable (`opsz 12–96`, `wdth 75–100`,
  `wght 200–800`). Titulares con `letter-spacing: -0.04em` y `line-height: 0.94`.
- **Texto / UI:** `Instrument Sans` 400–700.
- Escala fluida con `clamp()`:
  - hero: `clamp(3rem, 8.4vw, 7.4rem)`
  - h2: `clamp(2.1rem, 4.4vw, 3.9rem)`
  - h3: `clamp(1.35rem, 2vw, 1.85rem)`
  - cuerpo: `clamp(1rem, .96rem + .16vw, 1.075rem)`
- El contraste editorial del hero se consigue con **peso y ancho** (`font-weight: 300;
  font-stretch: 82%`), no con una segunda familia.

## Espacio y forma

- Contenedor `1320px`, gutter `clamp(20px, 5vw, 64px)`.
- Sección: `padding-block: clamp(72px, 10vw, 148px)`.
- Radios: `44px` (shell), `32px` (tarjeta), `24px` (media), `100px` (píldoras).
- Sombra suave difusa únicamente; nunca sombra negra dura.

## Componentes clave

- **Doble bisel (`.shell` + `.core`)**: bandeja exterior con hairline y padding de 10 px,
  contenido dentro con radio concéntrico. Aplica a imágenes, mapas y vídeo.
- **Botones (`.btn`)**: píldora, icono en círculo anidado a la derecha que se desplaza
  `2px/-2px` en hover; `active: scale(.985)`. Variantes: `--primary` (lima), `--ink`,
  `--ghost`, `--light`, `--outline-light`, `--sm`, `--lg`, `--block`.
- **Eyebrow**: píldora con punto coral, versalitas y `letter-spacing: .2em`.
- **Tarjetas**: `.card`, `.level`, `.reason`, `.price-card`, `.quote`, `.team-card`.
- **Raíl horizontal**: `.rail` con snap, flechas que se desactivan en los extremos.
- **Acordeón**: botón con icono `+` que rota 45°; panel con `grid-template-rows 0fr→1fr`.

## Movimiento

- Curvas propias: `--ease: cubic-bezier(.16,1,.3,1)` y `--ease-soft:
  cubic-bezier(.32,.72,0,1)`. Nada de `linear` salvo la marquesina.
- Reveals con `IntersectionObserver`: `translateY(26px) + blur(5px) + opacity` → 900 ms,
  con retardo escalonado (`--d`).
- Nav: píldora flotante que se comprime al hacer scroll; menú móvil a pantalla completa
  con enlaces escalonados y hamburguesa que se convierte en X.
- Vídeo: `preload="none"`, carga y reproduce solo al entrar en pantalla, pausa al salir.
- `prefers-reduced-motion`: todo el movimiento se desactiva y el contenido aparece.

## Iconografía

Set propio de 24 px con trazo `1.45`, esquinas redondeadas, definido como sprite en
`tools/build.py` (`ICONS`). Se usa con `<svg class="i"><use href="#i-nombre"/></svg>`.
Nada de librerías de iconos.

## Voz y microcopy

- Español de tú, directo, sin superlativos de folleto.
- CTA siempre orientados a acción real: «Reservar clase», «Apúntate al torneo del
  viernes», «Ver próximos viajes», «Área de alumnos».
- Se admiten guiños («El viernes se juega», «Tu pádel, en orden»), nunca bromas que
  oculten información.

## Accesibilidad

- Contraste mínimo AA en texto y en botones.
- Foco visible de 2 px (lima sobre fondo oscuro, tinta sobre claro).
- Objetivos táctiles ≥ 44 px; barra móvil fija con Reservar y Alumnos.
- Texto alternativo descriptivo en todas las imágenes; iconos decorativos con
  `aria-hidden`.

## Fotografía

- Luz natural, color coherente, gente real jugando.
- Retratos de equipo en blanco y negro, color al hover.
- Imágenes provisionales de Pexels; sustituir por material propio manteniendo encuadres
  4:5 (retrato), 3:2 (escena) y 16:10 (panorámica).
