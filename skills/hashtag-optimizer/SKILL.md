---
name: hashtag-optimizer
description: Selecciona el set óptimo de hashtags para una publicación de Campuslands AI Academy según la red social, el tema y el avatar objetivo, combinando hashtags oficiales de marca con hashtags de alcance y de nicho. Usa esta skill cuando el usuario pida "hashtags", "dame los tags para esto", o como paso final de cualquier pieza generada con social-post-generator o carousel-builder si no se incluyeron ya.
---

# Hashtag Optimizer

## Función
Generar un set balanceado de hashtags (marca + nicho + alcance) que maximice descubribilidad sin diluir la identidad de marca.

## Cuándo se activa
- "Dame los hashtags para este post"
- "Optimiza los tags de esta publicación"
- Automáticamente al final de `social-post-generator` o `carousel-builder` si el usuario no pidió hashtags pero el formato los requiere (Instagram, TikTok).

## Inputs necesarios
1. Tema/pilar de la pieza.
2. Red social (los hashtags relevantes en LinkedIn son mínimos o nulos; en Instagram/TikTok son centrales).
3. Avatar objetivo.

## Proceso
1. **Capa de marca** (siempre incluir, ver `ai-academy.md` para el listado oficial): hashtags propios de Campuslands/AI Academy.
2. **Capa de nicho** (3–5 tags): específicos del tema (#MachineLearning, #ComputerVision, #IAGenerativa) — ajustar según si el avatar es técnico o no.
3. **Capa de alcance** (2–4 tags): hashtags más generales y de volumen alto en la categoría tech/educación/empleo en Colombia (#TalentoTech, #EmpleoColombia, #AprendeIA), sin caer en tags genéricos irrelevantes (#viral, #fyp salvo que el formato sea TikTok y aplique).
4. Total recomendado: Instagram 8–15 hashtags; TikTok 3–6; LinkedIn 3–5 (más editorial, menos hashtag-driven); Facebook 0–3 (poco relevante en esa red).
5. Evitar hashtags banneados, irrelevantes o de marcas competidoras.

## Output esperado
```
Hashtags sugeridos ([red social]):
Marca: #... #...
Nicho: #... #... #...
Alcance: #... #...
```

## Restricciones
- Nunca usar hashtags de competidores directos ni de marcas no relacionadas para "robar" alcance.
- No saturar con hashtags genéricos sin relación temática real.
- Respetar el límite de la plataforma (Instagram permite hasta 30, pero la práctica recomendada es priorizar calidad sobre cantidad).

## Conexión con otras skills
Se invoca como cierre de `social-post-generator`, `carousel-builder`, `event-announcement`.
