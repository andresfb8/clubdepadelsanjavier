# Rediseño "más serio" + enfoque en público extranjero

## Contexto

La web (`index.html`, single-page Tailwind + JS vanilla, sin backend) tiene actualmente un
tono muy desenfadado (emojis grandes, lima flúor como color dominante, blobs difuminados,
tipografía de héroe muy grande) y arranca siempre en español pese a que la mayoría de
visitas son de público extranjero. El objetivo es transmitir más seriedad/profesionalidad
sin perder calidez, y priorizar la experiencia del visitante no español, incluyendo una
nueva vía de negocio (packs de entrenamiento + estancia) aún sin validar operativamente.

Todo el trabajo se hace dentro de `index.html` (HTML + Tailwind config inline + JS de
traducción/render ya existente). No se introducen nuevos archivos ni dependencias.

## 1. Paleta de color

- Se mantienen `brand.blue` (`#1D4CAF`) y `brand.dark` (`#0F172A`) tal cual.
- `brand.lime` (`#E0ED1D`) se sustituye en `tailwind.config` por un verde oliva/musgo
  apagado (`#A9C93A` aprox.) — mismo token, nuevo valor, así no hace falta tocar cada
  clase `brand-lime` del markup.
- El lima deja de usarse como fondo de bloques grandes (botones CTA principales, badges
  grandes). Se reserva para: subrayados, bordes, hover states, y acentos puntuales
  (bullets `✔`, borde de la tarjeta "Particulares").
- Nuevo estilo de botón CTA primario: fondo blanco o azul oscuro con texto, en lugar de
  bloque lima brillante con glow. Aplica al botón del héroe y a los CTA de "Escuelas".

## 2. Tipografía y jerarquía del héroe

- Se mantiene el pairing de fuentes actual (League Spartan display + Montserrat body).
- El H1 del héroe baja de `text-5xl md:text-7xl lg:text-8xl` a `text-4xl md:text-6xl
  lg:text-7xl`.
- Se elimina o suaviza el `drop-shadow-lg` pronunciado del H1 y el subtítulo.

## 3. Contenido / tono

- Los 3 iconos de "Propuesta de valor" (🎓🏆🍻) se sustituyen por iconos SVG lineales en
  `brand-blue` (mismo texto, mismo layout de card).
- Los apodos de golpe de los coachs (`specialties`) mantienen el texto (p. ej. "La Víbora
  Letal") pero sin el emoji al lado — se elimina el emoji de cada entrada en el array
  `coaches` y del label del icono "Golpe Maestro" si lleva alguno.
- Se eliminan los círculos difuminados (`blur-[100px]`, `blur-[120px]`) de fondo en la
  sección "Filosofía". El fondo pasa a azul liso (`bg-brand-blue`) sin decoración extra.

## 4. Detección automática de idioma

- Al cargar la página (`DOMContentLoaded`), si no hay `langPref` guardado en
  `localStorage`, se comprueba `navigator.language`:
  - Si empieza por `es` → arranca en español (comportamiento actual).
  - En cualquier otro caso → arranca en inglés.
- Si ya existe `langPref` en `localStorage` (el usuario cambió de idioma manualmente en
  una visita anterior), esa preferencia manda siempre sobre la detección automática.
- El selector de idioma sigue funcionando exactamente igual para cambiar manualmente.

## 5. Nueva sección "Padel Camps"

- Sección nueva, ubicada **justo después de "Escuelas"** (antes de "Equipo"), con el
  mismo lenguaje visual serio que el resto (misma tipografía, misma paleta, sin blobs).
- Enfocada en el visitante extranjero que viene pocos días y quiere una experiencia
  completa: entrenamiento intensivo + alojamiento recomendado en la zona.
- **No incluye precios ni detalles de alojamiento concretos** — el club no tiene aún
  acuerdo operativo con ningún hotel/apartamento. Es una sección de captación de interés
  para validar demanda antes de comprometerse operativamente.
- Badge visible tipo "Bajo consulta" / EN "On request" para dejar claro que no es un
  producto cerrado y evitar expectativas de reserva inmediata.
- CTA: "Quiero más información" → mismo enlace de WhatsApp que el resto del sitio (con
  mensaje predefinido distinto, mencionando "Padel Camp").
- Requiere: nuevo bloque de traducciones ES/EN (tag, título, texto, CTA, badge) siguiendo
  el mismo patrón `data-translate-key` que el resto de la página.

## 6. Ajuste de copy en la tarjeta "Particulares"

- Se añade una línea breve bajo el texto actual de la tarjeta, dirigida al visitante de
  paso: ES "Ideal si estás de paso pocos días" / EN "Perfect for short stays". No cambia
  precio ni estructura de la tarjeta, solo esta línea adicional en ambos idiomas.

## 7. Reordenación de secciones

Orden actual: Hero → Valores → Filosofía → Escuelas → Equipo → Competición → Reseñas →
Social → Footer.

Nuevo orden:

1. Hero
2. Valores
3. **Reseñas de Google** (movida aquí — prueba social temprana para visitantes que no
   conocen el club)
4. Filosofía
5. Escuelas
6. **Padel Camps** (nueva, justo después de Escuelas)
7. Equipo
8. Competición
9. Social (Instagram)
10. Footer

Solo cambia la posición de los bloques `<section>` en el HTML; ningún bloque cambia de
contenido salvo lo descrito en las secciones 5 y 6 de este documento.

## Fuera de alcance

- No se toca `reviews.php` ni la integración de EmbedSocial (ya resueltas en trabajo
  previo).
- No se implementa el sistema de reservas/pagos para "Padel Camps" — solo captación de
  interés vía WhatsApp.
- No se cambia la estructura de precios de Escuelas/Particulares/Menores (ya actualizada
  previamente).
