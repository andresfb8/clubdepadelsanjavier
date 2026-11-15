# Contenido pendiente de confirmar

Todo lo que está publicado como dato provisional y debe validar el club antes de salir a
producción. Los textos legales y de privacidad requieren revisión profesional.

## Precios

| Dato | Valor publicado | Dónde |
| --- | --- | --- |
| Escuela de adultos 1 día | 30 €/mes | `horarios.html`, `clases.html`, home |
| Escuela de adultos 2 días | 45 €/mes | `horarios.html` |
| Escuela de menores | 20 €/mes · 370 €/temporada | `horarios.html`, `academia.html` |
| Clase particular 1 persona | desde 30 €/h | `clases.html`, home |
| Clase particular 2 personas | desde 35 €/h | `clases.html` |
| Bono 4 clases | 112 € / 132 € | `horarios.html` |
| Bono 8 clases | 208 € / 248 € | `horarios.html` |
| Inscripción mini torneo | 10 €/jugador | `torneos.html`, home |

> Los importes de adultos, menores y particulares vienen del sitio anterior; los bonos y
> el precio del torneo son estimaciones de maqueta y hay que confirmarlos.

## Torneos

- Fechas publicadas: **20 y 27 de noviembre**, **4 de diciembre** (abierto) y
  **11 de diciembre** (completo, «Torneo de Navidad»).
- Horario 20:00–23:00, formato americano de 4 rondas, 16 plazas, 6 libres.
- Ranking del mes: los cinco nombres y puntos son **de ejemplo**; hay que conectarlo a
  resultados reales o retirarlo.

## Viajes

- **Valencia**: 27–29 nov 2026, 165 €/persona, 16 plazas, nivel medio, 4 partidos.
- **Sierra Nevada**: 12–14 dic 2026, 195 €/persona, 12 plazas, nivel medio, 3 partidos.
- **Mallorca**: 5–8 mar 2027, 320 €/persona, 18 plazas, todos los niveles, 6 partidos.
- Faltan por definir: transporte, alojamientos concretos, política de cancelación real y
  qué incluye exactamente cada precio.

## Horarios

- Cuadro semanal de `horarios.html` (17:00–21:00, lunes a sábado) y horario de oficina
  (L–V 16:00–21:00, S 10:00–13:00): ambos son orientativos.
- Estado «Actualizado · nov 2026»: cambiar cuando se confirme el cuadro definitivo.

## Instalaciones y contacto

- Dirección publicada: *Polideportivo Municipal, Av. de la Unión, 30730 San Javier,
  Murcia*, con segunda sede en *Polígono Industrial El Pino*.
- Coordenadas del JSON-LD (`37.8067, -0.8353`): aproximadas, conviene ajustarlas al punto
  exacto de las pistas.
- Correo `info@clubpadelsanjavier.es` en el schema: **no verificado**, sustituir o quitar.
- `SITE_URL` en `tools/build.py` apunta a `https://clubdepadelsanjavier.netlify.app`.
  Cambiar por el dominio final (afecta a canonical, `og:url`, `sitemap.xml`, `robots.txt`).
- Enlaces de «Ver reseñas en Google» y «Fotos del último torneo»: revisar que apunten a la
  ficha y al perfil correctos.

## Área de alumnos

- La pantalla de acceso es una maqueta: no hay backend ni validación. Hay que conectar el
  sistema de reservas del club (o el proveedor que se elija) y decidir si el login se abre
  en el mismo dominio o en uno externo.

## Legal

- `legal.html` es una base de trabajo: faltan razón social, NIF, datos registrales y
  revisión de la política de cookies (Google Analytics, mapas de Google, Instagram,
  WhatsApp).
- Si se activa Google Analytics, añadir el banner de consentimiento correspondiente.
  Ahora mismo la etiqueta de analítica **no** está incluida en el nuevo sitio; la versión
  anterior sí la tenía (`G-X9BEJ5WG8E`).

## Medios

- Todas las fotos de acción, pistas y destinos son de **Pexels** (provisionales).
- Los retratos de los entrenadores son fotos reales del club, ya optimizadas. Falta la de
  **Jorge**: la que había en el repositorio era un avatar genérico, así que se ha omitido
  del equipo hasta tener una real.
- Sustituir el vídeo de archivo por un clip propio de las pistas cuando exista.
