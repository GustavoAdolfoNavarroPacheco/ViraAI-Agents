---
name: trend-researcher
description: Investiga de forma autónoma tendencias actuales de IA Generativa, Machine Learning y Computer Vision en redes sociales e internet, y las sintetiza en ángulos de contenido aprovechables para Campuslands AI Academy. Usa esta skill cuando el usuario pida "tendencias", "qué está pasando en IA", "ideas frescas", "qué se está hablando en redes sobre IA", o cuando otra skill (social-post-generator, script-writer, newsjacking) necesite un ángulo actual y no tenga uno claro.
---

# Trend Researcher

## Función
Encontrar qué se está discutiendo AHORA sobre IA (lanzamientos, virales, debates, herramientas nuevas) y traducirlo en 2–4 ángulos de contenido relevantes para los avatares de Campuslands.

## Cuándo se activa
- "Investiga tendencias de IA esta semana"
- "Dame ideas frescas para contenido"
- "¿Qué está pasando en el mundo de la IA que podamos aprovechar?"
- Como sub-paso automático antes de `content-calendar-planner` si el calendario necesita temas nuevos.

## Proceso
1. **Buscar en tiempo real** (requiere web search activo — ver `instructions.md` sección "Integración de búsqueda"):
   - Lanzamientos recientes de modelos/herramientas de IA (OpenAI, Anthropic, Google, Meta, etc.)
   - Tendencias virales en TikTok/Instagram relacionadas con IA, productividad o empleo tech
   - Noticias sobre empleabilidad tech en Colombia/LatAm
2. **Filtrar por relevancia**: descarta lo que no conecte con los avatares (El Camper busca empleabilidad; El Profesional busca actualización; Empresas buscan ROI de talento).
3. **Sintetizar cada tendencia en formato ángulo de contenido**:
   - Qué es la tendencia (1 línea, en tus propias palabras, nunca cita textual extensa).
   - Por qué le importa a cada avatar.
   - Pilar de contenido sugerido (Educativo/Inspiracional/Promocional/Comunidad).
   - Formato sugerido (post, carrusel, reel).
4. Si una tendencia es noticia reciente y aplicable a posicionamiento de marca → sugerir derivar a `newsjacking`.
5. Registrar las tendencias encontradas y su fecha en `context/memory-log.md` vía `memory-manager` para no repetirlas en sesiones futuras.

## Output esperado
```
## Tendencias detectadas — [fecha]

1. [Tendencia] — Fuente: [tipo de fuente, sin URLs largas si no se piden]
   Relevancia: [avatar(es)]
   Ángulo sugerido: [una línea]
   Pilar: [pilar] | Formato: [post/carrusel/reel]

2. ...
```

## Restricciones
- NUNCA reproducir texto extenso de artículos o posts encontrados (parafrasear siempre, respetar derechos de autor).
- NUNCA presentar una tendencia como confirmada si la fuente es dudosa o no verificable.
- Evitar tendencias que no tengan conexión clara y honesta con la propuesta de valor de Campuslands.
- Si no hay acceso a búsqueda en tiempo real, decirlo explícitamente y trabajar con conocimiento general, marcándolo como "no verificado en tiempo real".

## Conexión con otras skills
`newsjacking` (convertir noticia en contenido posicionado) · `content-calendar-planner` (alimentar el calendario) · `memory-manager` (guardar hallazgos) · `social-post-generator` / `script-writer` (ejecutar el ángulo).

