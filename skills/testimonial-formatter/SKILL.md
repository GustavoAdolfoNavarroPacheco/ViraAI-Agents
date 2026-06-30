---
name: testimonial-formatter
description: Estructura historias reales de Campers (estudiantes/egresados de Campuslands) en una plantilla de apertura, desarrollo, resultado y CTA, lista para convertirse en post, carrusel o video. Usa esta skill cuando el usuario comparta o describa la historia de un Camper real, un caso de éxito, o pida "formatea este testimonio".
---

# Testimonial Formatter

## Función
Convertir una historia real (compartida por el equipo de Campuslands) en una pieza narrativa estructurada y emocionalmente efectiva, sin alterar ni exagerar los hechos.

## Cuándo se activa
- "Tenemos la historia de [nombre/Camper], ayúdame a estructurarla"
- "Formatea este testimonio para redes"
- Como insumo post-evento desde `event-announcement`.

## Inputs necesarios (deben venir del usuario/equipo — NUNCA inventar)
1. Quién es la persona (nombre o anónimo si se pide privacidad) y su situación de partida.
2. Qué programa cursó y qué la motivó a empezar.
3. Qué resultado obtuvo (empleo, cambio de carrera, proyecto, etc.) — solo si está confirmado por el equipo.
4. Cita o frase textual de la persona, si existe (mantenerla fiel, no parafrasear lo que la persona realmente dijo si se entrega como cita directa).

## Estructura de la plantilla
1. **Apertura**: contexto inicial — quién era, qué situación vivía antes de Campuslands (genera identificación con El Camper).
2. **Desarrollo**: qué decisión tomó, qué vivió en el programa, qué dificultad superó.
3. **Resultado**: qué logró, de forma concreta y verificable (no genérica tipo "le cambió la vida" sin un hecho específico detrás).
4. **CTA**: invitación a quien se identifique con la historia a dar el siguiente paso (usar `cta-generator`).

## Proceso
1. Solicita los hechos reales si no están completos — NUNCA rellenar huecos con suposiciones o datos inventados.
2. Redacta siguiendo la estructura, en primera o tercera persona según se entregue el material.
3. Mantén el tono humano y honesto, evita sonar a comercial forzado.
4. Pasa por `brand-voice-enforcer`, prestando especial atención a que no se infle el resultado real.

## Output esperado
```
TESTIMONIO — [nombre o "Camper anónimo"]

Apertura: ...
Desarrollo: ...
Resultado: ...
CTA: ...
```

## Restricciones
- NUNCA inventar nombres, resultados o citas de Campers que no hayan sido confirmados por el equipo.
- Si la persona pidió anonimato, respetarlo estrictamente.
- No exagerar resultados ("consiguió trabajo en una semana" solo si es literalmente cierto).

## Conexión con otras skills
Insumo para `social-post-generator`, `script-writer`, `carousel-builder` · usado en el cierre de `event-announcement` · valida con `brand-voice-enforcer`.
