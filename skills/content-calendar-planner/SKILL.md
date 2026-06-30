---
name: content-calendar-planner
description: Crea calendarios editoriales mensuales o semanales para Campuslands AI Academy, distribuyendo publicaciones por pilares de contenido, días de la semana y avatares de audiencia. Usa esta skill cuando el usuario pida "calendario de contenido", "planeación del mes", "qué publicamos esta semana", o cuando se necesite organizar varias piezas de contenido a la vez en lugar de generar una sola pieza suelta.
---

# Content Calendar Planner

## Función
Organizar la producción de contenido en el tiempo, asegurando que se respete la distribución de pilares (Educativo 40% / Inspiracional 25% / Promocional 20% / Comunidad 15%) y que haya variedad de avatares y formatos.

## Cuándo se activa
- "Hazme el calendario de [mes]"
- "¿Qué publicamos esta semana?"
- "Organiza el contenido del próximo lanzamiento"

## Inputs necesarios
1. Periodo a planear (semana o mes) y número de publicaciones por semana (ver `content-strategy.md` para frecuencia estándar; si no está definida, preguntar).
2. Eventos o fechas clave del periodo (masterclasses, fechas de inscripción, becas) — si hay un evento, derivar esas piezas a `event-announcement`.
3. Temas o tendencias disponibles (puede invocar `trend-researcher` si el calendario necesita ideas nuevas).

## Proceso
1. Calcula cuántas piezas corresponden a cada pilar según el % objetivo y el total de piezas del periodo (redondear de forma razonable).
2. Asigna piezas a días de la semana siguiendo buenas prácticas: contenido Educativo a inicio/mitad de semana, Inspiracional fines de semana o lunes, Promocional cerca de fechas límite, Comunidad cuando hay testimonios o eventos.
3. Para cada pieza, define: fecha, pilar, avatar, formato (post/carrusel/reel), tema/título tentativo. NO escribas el copy completo aquí — eso lo hacen `social-post-generator`, `carousel-builder` o `script-writer` después.
4. Verifica que ningún avatar quede sin contenido en el periodo y que no se repita el mismo ángulo dos veces.
5. Si hay un evento en el periodo, inserta automáticamente los puntos de contacto D-7/D-3/D-1/día-evento/post-evento (coordinrar con `event-announcement`).

## Output esperado
```
CALENDARIO — [mes/semana]

| Fecha | Pilar | Avatar | Formato | Tema/Título tentativo |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

Resumen de distribución: Educativo X% | Inspiracional X% | Promocional X% | Comunidad X%
```

## Restricciones
- Nunca desviarse más de ±5 puntos porcentuales de la distribución objetivo de pilares sin explicarlo.
- No generar copy completo dentro de esta skill — solo planeación, para mantener separación de responsabilidades.
- Si el usuario pide un calendario sin haber definido frecuencia, usar como default razonable lo que indique `content-strategy.md`, y aclarar el supuesto.

## Conexión con otras skills
`trend-researcher` (ideas) · `event-announcement` (fechas clave) · `social-post-generator` / `carousel-builder` / `script-writer` (ejecución de cada celda) · `memory-manager` (registrar el calendario aprobado).
