# Guía de estilo — Club de Pádel San Javier

Sistema de diseño del sitio, alineado con los colores del club y con una base clara de
aire deportivo. Todo vive en `assets/css/site.css` (tokens, tipografía, layout,
navegación) y `assets/css/components.css` (componentes).

## Concepto

Deporte moderno, limpio y con energía. Fondo claro y frío (blanco y gris azulado), tinta
azul noche y **azul club** `#1D4CAF` como color de identidad y de acción. La interfaz es
azul, blanca y tinta; el **lima** `#A9C93A` queda como sello de marca (logo, sellos y
badges), nunca en botones ni enlaces.

## Color

| Token | Valor | Uso |
| --- | --- | --- |
| `--paper` | `#F4F6FA` | Fondo base (gris azulado muy claro) |
| `--paper-2` | `#FFFFFF` | Tarjetas y superficies |
| `--ink` | `#0F172A` | Texto principal y secciones oscuras |
| `--ink-2` | `#16213C` | Superficie oscura elevada |
| `--blue` | `#1D4CAF` | **Azul club**: CTA principal, enlaces, focos y estados |
| `--blue-deep` | `#143B8A` | Hover del azul y datos |
| `--lime` | `#A9C93A` | **Lima club**: solo relleno de badges, marca y sello |
| `--lime-deep` | `#94B22C` | Hover del lima (uso residual) |
| `--sand` | `#E4E9F2` | Placeholder de imagen, superficies neutras |
| `--muted` | `rgba(15,23,42,.62)` | Texto secundario |
| `--line` | `rgba(15,23,42,.14)` | Hairline estándar |

### Reglas de uso

- **Un CTA principal por pantalla.** Es azul sobre fondo claro y **blanco con texto
  tinta** sobre fondo oscuro (tour, CTA band, footer, área de alumnos, tarjetas
  destacadas). Nunca lima.
- El lima no se usa en botones, enlaces, iconos de interfaz ni estados de foco: solo en
  el relleno de badges, la marca del nav y el sello del hero.
- El azul cubre también enlaces, iconos de check, focos y el punto de las etiquetas.

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
  font-stretch: 82%`) y con **azul club** en la segunda línea, no con otra familia.

## Espacio y forma

- Contenedor `1320px`, gutter `clamp(20px, 5vw, 64px)`.
- Sección: `padding-block: clamp(72px, 10vw, 148px)`.
- Radios: `44px` (shell), `32px` (tarjeta), `24px` (media), `100px` (píldoras).
- Sombra suave difusa únicamente; nunca sombra negra dura.

## Componentes clave

- **Doble bisel (`.shell` + `.core`)**: bandeja exterior con hairline y padding de 10 px,
  contenido dentro con radio concéntrico. Aplica a imágenes, mapas y vídeo.
- **Botones (`.btn`)**: píldora, icono en círculo anidado a la derecha que se desplaza
  `2px/-2px` en hover; `active: scale(.985)`. Variantes: `--primary` (azul en claro,
  blanco en oscuro), `--ink`, `--ghost`, `--light`, `--outline-light`, `--sm`, `--lg`.
- **Eyebrow**: píldora con punto azul, versalitas y `letter-spacing: .2em`.
- **Tarjetas**: `.card`, `.level`, `.reason`, `.price-card`, `.quote`, `.team-card`.
- **Raíl horizontal**: `.rail` con snap, flechas que se desactivan en los extremos.
- **Acordeón**: botón con icono `+` que rota 45° y se tiñe de azul; panel con
  `grid-template-rows 0fr→1fr`.
- **Menús desplegables**: `Clases` y `Experiencias` comparten el mismo componente
  (`.nav__drop` + `.nav__panel`), con apertura por teclado, hover y Esc.

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
- CTA orientados a acción real: «Reservar clase», «Apúntate al torneo del viernes»,
  «Ven a San Javier», «Área de alumnos».
- Se admiten guiños («El viernes se juega», «También hay cantera»), nunca bromas que
  oculten información.

## Accesibilidad

- Contraste mínimo AA en texto y botones; blanco sobre azul (7,4:1) y tinta sobre blanco.
- Foco visible de 2 px (azul sobre claro, blanco sobre oscuro).
- Objetivos táctiles ≥ 44 px; barra móvil fija con Reservar y Alumnos.
- Texto alternativo descriptivo en todas las imágenes; iconos decorativos con
  `aria-hidden`.

## Fotografía

- Luz natural, color coherente, gente real jugando.
- Retratos de equipo en blanco y negro, color al hover.
- Imágenes provisionales de Pexels; sustituir por material propio manteniendo encuadres
  4:5 (retrato), 3:2 (escena) y 16:10 (panorámica).
