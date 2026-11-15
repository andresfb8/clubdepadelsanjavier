# Contenido pendiente de confirmar

Todo lo que está publicado como dato provisional y debe validar el club antes de salir a
producción. Los textos legales y de privacidad requieren revisión profesional.

## Precios

| Dato | Valor publicado | Dónde |
| --- | --- | --- |
| Escuela de adultos 1 día | 30 €/mes | `horarios.html`, `clases.html`, home |
| Escuela de adultos 2 días | 45 €/mes | `horarios.html` |
| Escuela de menores | 20 €/mes · 370 €/temporada | `horarios.html`, `clases.html`, `academia.html`, home |
| Clase particular 1 persona | desde 30 €/h | `clases.html`, home |
| Clase particular 2 personas | desde 35 €/h | `clases.html` |
| Bono 4 clases | 112 € / 132 € | `horarios.html` |
| Bono 8 clases | 208 € / 248 € | `horarios.html` |
| Inscripción mini torneo | 10 €/jugador | `torneos.html`, home |

> Los importes de adultos, menores y particulares vienen del sitio anterior; los bonos y
> el precio del torneo son estimaciones de maqueta y hay que confirmarlos.

## Escuela de menores

- Edades publicadas: **6 a 14 años**, grupos 6–9 y 10–14 (ajustar a los grupos reales).
- Días: de lunes a viernes por la tarde, 1 o 2 días por semana.
- Cuota: 20 €/mes o 370 €/temporada (heredado del sitio anterior).
- Falta confirmar si hay matrícula, descuentos por hermanos y calendario por trimestres.
- La foto de la sección es `img/menores.jpg` (real del club), recortada a 3:2.

## Ven a San Javier (pádel + estancia)

La página `viajes.html` ya no plantea salidas del club: está enfocada a **recibir
jugadores** que vienen unos días a San Javier. Faltan por cerrar:

- **Precios** por persona (publicados como orientativos): escapada corta 165 €,
  semana 390 €, finde largo 240 €. Incluyen pistas, entrenador y alojamiento.
- **Alojamientos**: no hay acuerdos cerrados todavía. Definir 2–3 opciones por
  presupuesto (hotel, apartamento, casa) y sus condiciones.
- **Fechas**: no se publican fechas fijas, se trabaja bajo petición. Confirmar si habrá
  salidas cerradas en temporada alta.
- **Transporte**: se indica que se organiza aparte; el texto menciona el aeropuerto de
  Murcia (Corvera) a 25 minutos. Verificar tiempos reales.
- **Idiomas**: la sección en inglés asume entrenamiento bilingüe. Confirmar qué
  entrenadores pueden dar clase en inglés.
- **Qué incluye/no incluye**: revisar la política real de cancelación y el pago del 30 %.

## Torneos

- Fechas publicadas: **20 y 27 de noviembre**, **4 de diciembre** (abierto) y
  **11 de diciembre** (completo, «Torneo de Navidad»).
- Horario 20:00–23:00, formato americano de 4 rondas, 16 plazas, 6 libres.
- Ranking del mes: los cinco nombres y puntos son **de ejemplo**; hay que conectarlo a
  resultados reales o retirarlo.

## Horarios

- Cuadro semanal de `horarios.html` (17:00–21:00, lunes a sábado) y horario de oficina
  (L–V 16:00–21:00, S 10:00–13:00): ambos son orientativos.
- La fila de menores (17:00 lunes a viernes) debe cuadrar con los grupos reales.
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
  sistema de reservas del club (o el proveedor que se elija).

## Legal

- `legal.html` es una base de trabajo: faltan razón social, NIF, datos registrales y
  revisión de la política de cookies (Google Analytics, mapas de Google, Instagram,
  WhatsApp).
- Si se activa Google Analytics, añadir el banner de consentimiento correspondiente.
  Ahora mismo la etiqueta de analítica **no** está incluida en el nuevo sitio; la versión
  anterior sí la tenía (`G-X9BEJ5WG8E`).

## Medios y marca

- Paleta aplicada con los colores del club: azul `#1D4CAF` y lima `#A9C93A` (los del
  `tailwind.config` del sitio anterior). Confirmar que son los colores oficiales de marca.
- Todas las fotos de acción, pistas y entorno son de **Pexels** (provisionales).
- Los retratos de los entrenadores son fotos reales del club, ya optimizadas. Falta la de
  **Jorge**: la que había en el repositorio era un avatar genérico, así que se ha omitido
  del equipo hasta tener una real.
- Sustituir el vídeo de archivo por un clip propio de las pistas cuando exista.
