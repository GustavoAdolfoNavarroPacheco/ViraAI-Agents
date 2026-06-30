---
name: event-announcement
description: Planea el flujo completo de comunicación para un evento, masterclass o fecha límite de Campuslands AI Academy, incluyendo anuncio inicial e historias en D-7, D-3, D-1, día del evento y post-evento. Usa esta skill cuando el usuario mencione "evento", "masterclass", "lanzamiento", "fecha límite de inscripción" o cualquier hito con fecha específica que requiera comunicación escalonada.
---

# Event Announcement

## Función
Asegurar que cada evento tenga una secuencia de comunicación completa y escalonada, en vez de una sola pieza aislada, maximizando recordación y conversión antes de la fecha límite.

## Cuándo se activa
- "Vamos a anunciar la masterclass de [tema] el [fecha]"
- "Necesitamos comunicar el cierre de inscripciones"
- Cuando `content-calendar-planner` detecta un evento en el periodo planeado.

## Estructura del flujo
1. **Anuncio inicial** (apenas se confirma el evento): post o carrusel completo presentando qué es, para quién, cuándo y cómo inscribirse.
2. **D-7** (historia/post recordatorio): "quedan 7 días", reforzar beneficio principal.
3. **D-3** (historia): generar urgencia real (cupos, fecha límite), responder objeciones comunes.
4. **D-1** (historia): último llamado, tono más directo y emocional.
5. **Día del evento**: cobertura en vivo o resumen de inicio, según si es presencial/digital.
6. **Post-evento**: agradecimiento, resumen de aprendizajes o resultados, CTA para el próximo paso (siguiente cohorte, masterclass relacionada) — buen momento para alimentar `testimonial-formatter` si hay historias que recoger.

## Proceso
1. Recibe del usuario: nombre del evento, fecha, formato (presencial/digital/híbrido), avatar principal, beneficio central.
2. Genera cada pieza de la secuencia usando `social-post-generator` (anuncio), formato historia breve para D-7/D-3/D-1 (más corto que un post normal, pensado para Stories), y `script-writer` si se quiere cobertura en video.
3. Usa `cta-generator` para variar el cierre según la etapa del funnel (D-7 = descubrimiento, D-1 = decisión).
4. Verifica con `brand-voice-enforcer` cada pieza antes de entregar el paquete completo.

## Output esperado
```
FLUJO DE EVENTO — [nombre del evento] | Fecha: [fecha]

1. Anuncio inicial: [pieza completa]
2. D-7 (historia): [texto corto]
3. D-3 (historia): [texto corto]
4. D-1 (historia): [texto corto]
5. Día del evento: [pieza]
6. Post-evento: [pieza]
```

## Restricciones
- Nunca inventar cupos limitados o fechas si no están confirmadas por el equipo.
- Las historias (D-7/D-3/D-1) deben ser más cortas y directas que un post de feed normal.
- Todo el flujo debe quedar registrado en `context/memory-log.md` vía `memory-manager` para medir desempeño después.

## Conexión con otras skills
`social-post-generator`, `script-writer`, `cta-generator`, `testimonial-formatter` (post-evento), `brand-voice-enforcer`, `memory-manager`.

