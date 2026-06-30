---
name: carousel-builder
description: Construye carruseles de Instagram/LinkedIn slide por slide, definiendo texto, ícono/imagen sugerida y CTA para cada slide de Campuslands AI Academy. Usa esta skill cuando el usuario pida "un carrusel", "varias slides", "un post con varias imágenes" o contenido educativo que requiera explicarse en pasos.
---

# Carousel Builder

## Función
Diseñar carruseles educativos o inspiracionales con una estructura clara slide por slide, ideal para contenido que requiere desglose paso a paso (ej. "5 herramientas de IA para tu primer empleo tech").

## Cuándo se activa
- "Hazme un carrusel sobre [tema]"
- "Necesito explicar [proceso/lista] en varias slides"
- Cuando `content-calendar-planner` asigna formato "carrusel" a una celda

## Inputs necesarios
1. Tema y cantidad aproximada de puntos a cubrir (define el número de slides; recomendado 5–8 slides, incluyendo portada y cierre).
2. Pilar de contenido y avatar objetivo.
3. Plantilla visual si ya existe una de `ai-academy.md` (hay 4 plantillas de contenido definidas).

## Proceso
1. **Slide 1 (Portada)**: título gancho + subtítulo, debe funcionar igual que un hook de post.
2. **Slides 2 a N-1 (Desarrollo)**: una idea por slide, texto breve (máx. 25–30 palabras por slide), sugerencia de ícono o imagen de apoyo.
3. **Slide N (Cierre)**: resumen breve + CTA claro.
4. Mantén consistencia de tono entre slides — no cambiar de registro a mitad de carrusel.
5. Si el tema lo amerita, usa numeración visible ("1/6", "2/6"...) para guiar el swipe.
6. Pasa por `brand-voice-enforcer`.

## Output esperado
```
CARRUSEL — [tema] | Pilar: [pilar] | Avatar: [avatar] | N slides

Slide 1 (Portada): [texto] | Visual sugerido: [...]
Slide 2: [texto] | Visual sugerido: [...]
...
Slide N (Cierre + CTA): [texto] | Visual sugerido: [...]
```

## Restricciones
- Máximo 8 slides recomendado (más de eso reduce el completion rate); si el usuario pide más, advertir brevemente.
- Cada slide debe poder entenderse de forma independiente (alguien puede ver solo una slide en el feed).
- Mismas restricciones de veracidad y tono que `social-post-generator`.

## Conexión con otras skills
`hashtag-optimizer` · `cta-generator` (slide de cierre) · `ab-variant-creator` (variantes de portada) · `brand-voice-enforcer`.
