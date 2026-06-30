---
name: ab-variant-creator
description: Genera automáticamente 3 variantes A/B/C de cualquier pieza de contenido crítica (hook, post completo, CTA, anuncio) de Campuslands AI Academy, cambiando un solo elemento por variante para permitir pruebas controladas. Usa esta skill cuando el usuario pida "variantes", "A/B test", "dame opciones para probar", o para piezas de campaña paga / lanzamientos importantes.
---

# A/B Variant Creator

## Función
Producir variantes comparables de una misma pieza, aislando una sola variable por vez, para que el equipo de marketing pueda medir qué funciona mejor.

## Cuándo se activa
- "Dame 3 variantes de este post para probar"
- "Necesito opciones A/B para el anuncio de la masterclass"
- Recomendado automáticamente para piezas marcadas como "críticas" (campañas pagas, lanzamientos, cierres de inscripción) por `event-announcement` o `content-calendar-planner`.

## Principio rector
**Una variable por variante.** No generar 3 posts completamente distintos entre sí — eso no permite aprender qué causó la diferencia. Ejemplos de variables a aislar:
- Variante de **hook** (mismo cuerpo y CTA, distinto gancho inicial: pregunta vs. dato vs. afirmación polémica).
- Variante de **enfoque emocional** (aspiracional vs. urgencia vs. pertenencia/comunidad).
- Variante de **CTA** (mismo contenido, distinto cierre: WhatsApp directo vs. link en bio vs. comenta para que te escribamos).
- Variante de **avatar/ángulo** (mismo tema, hablado para El Camper vs. para El Profesional).

## Proceso
1. Identifica con el usuario (o infiere) cuál es la variable más relevante a probar para esa pieza.
2. Genera la pieza base completa (vía `social-post-generator`, `script-writer` o `cta-generator` según el tipo).
3. Crea variante A (control), B y C, cambiando SOLO la variable elegida.
4. Etiqueta claramente cada variante con qué cambia respecto a la base.
5. Sugiere brevemente qué métrica usar para comparar (CTR, comentarios, mensajes a WhatsApp) — sin inventar datos de resultados.
6. Pasa las 3 por `brand-voice-enforcer`.

## Output esperado
```
A/B/C — [pieza] | Variable probada: [hook/enfoque/CTA/avatar]

VARIANTE A (control): [pieza completa]
VARIANTE B (cambia: [elemento]): [pieza completa]
VARIANTE C (cambia: [elemento]): [pieza completa]

Métrica sugerida para comparar: [...]
```

## Restricciones
- Nunca variar más de un elemento por variante — rompe la validez de la prueba.
- No generar más de 3 variantes salvo solicitud explícita (más allá de eso, diluye el aprendizaje y la atención del equipo).
- Registrar en `context/memory-log.md` (vía `memory-manager`) qué se probó, para que `performance-analyst` pueda usarlo después.

## Conexión con otras skills
Se apoya en `social-post-generator`, `script-writer`, `cta-generator` para construir las variantes · alimenta a `memory-manager` y `performance-analyst`.

