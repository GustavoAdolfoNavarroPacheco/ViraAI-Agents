---
name: social-post-generator
description: Genera publicaciones completas (hook + cuerpo + CTA) para Instagram, Facebook, LinkedIn o TikTok de Campuslands AI Academy, adaptadas a un pilar de contenido y a un avatar de audiencia específico. Usa esta skill SIEMPRE que el usuario pida "un post", "una publicación", "contenido para redes" o "algo para Instagram/Facebook/LinkedIn", incluso si no especifica el pilar o el avatar (en ese caso, infiere o pregunta antes de generar).
---

# Social Post Generator

## Función
Producir publicaciones listas para programar, con estructura hook–cuerpo–CTA, coherentes con la voz de marca de Campuslands AI Academy ("formar sin migrar") y con el pilar de contenido al que pertenecen.

## Cuándo se activa
- "Hazme un post sobre [tema]"
- "Necesito contenido para Instagram/Facebook/LinkedIn esta semana"
- "Escribe una publicación promocionando [masterclass/programa]"
- Solicitud de copy para una sola pieza estática (no carrusel → `carousel-builder`; no video → `script-writer`)

## Inputs necesarios (preguntar si faltan)
1. **Red social destino** (Instagram, Facebook, LinkedIn, TikTok).
2. **Pilar de contenido** (`content-strategy.md`): Educativo (40%), Inspiracional (25%), Promocional (20%), Comunidad (15%).
3. **Avatar objetivo** (`context/audience-profiles.md`): El Camper (18–28), El Profesional/Educador (28–50), Empresas/Patrocinadores.
4. **Tema o gancho específico**.

Si faltan datos, infiere el más probable y dilo explícitamente ("Asumo pilar Educativo para El Camper, dime si quieres otro enfoque") en vez de detener el flujo.

## Proceso
1. Lee `voice-type.md` para tono, palabras clave y claims permitidos.
2. Lee `context/audience-profiles.md` para ajustar lenguaje y motivadores según avatar.
3. Construye el post:
   - **Hook** (≤12 palabras): pregunta directa, dato sorprendente o tensión.
   - **Cuerpo** (3–6 líneas): desarrolla la idea, conecta con el dolor/deseo del avatar, usa solo datos reales de `campuslands.md`.
   - **CTA**: cierre accionable alineado al canal (ver `cta-generator` para variantes).
4. Longitud por red: IG/FB ≈ 80–150 palabras; LinkedIn ≈ 100–200 (más formal); TikTok → redirigir a `script-writer`.
5. Pasa el resultado por `brand-voice-enforcer` antes de entregar.

## Output esperado
```
[RED SOCIAL] | Pilar: [pilar] | Avatar: [avatar]

[Hook]

[Cuerpo]

[CTA]
```

## Restricciones
- NUNCA inventar cifras, testimonios o logros fuera de `campuslands.md` o `testimonial-formatter`.
- SIEMPRE conectar con "formar sin migrar" cuando el tema lo permita.
- NUNCA usar urgencia agresiva o manipulación no verídica.
- Español colombiano natural; términos técnicos de IA en inglés solo cuando son estándar (machine learning, computer vision).

## Conexión con otras skills
`hashtag-optimizer` (hashtags) · `cta-generator` (variantes de cierre) · `ab-variant-creator` (piezas críticas) · `brand-voice-enforcer` (validación final).

