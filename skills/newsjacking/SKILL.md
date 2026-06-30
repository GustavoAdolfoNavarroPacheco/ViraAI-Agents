---
name: newsjacking
description: Convierte noticias recientes y relevantes del mundo de la IA en contenido oportuno y posicionado para Campuslands AI Academy, conectando la noticia con la propuesta de valor de la marca. Usa esta skill cuando el usuario pida "aprovechemos esta noticia", "newsjacking", o cuando trend-researcher detecte una noticia con alto potencial de posicionamiento de marca.
---

# Newsjacking

## Función
Reaccionar rápido y con criterio a noticias de actualidad en IA, posicionando a Campuslands como una voz informada y relevante, sin caer en clickbait vacío o desinformación.

## Cuándo se activa
- "Salió esta noticia de [tema], aprovechémosla"
- Sugerencia automática de `trend-researcher` cuando detecta una noticia de alto impacto.

## Criterios para decidir SI vale la pena hacer newsjacking
1. **Relevancia genuina**: ¿la noticia conecta de forma honesta con IA Generativa, Machine Learning, Computer Vision o empleabilidad tech?
2. **Vigencia**: ¿sigue siendo actual (idealmente menos de 48–72h)?
3. **Riesgo**: ¿es un tema sensible, polémico o no verificado? Si sí, evaluar con más cautela o evitar.
4. Si la noticia no cumple estos criterios, recomendar NO hacer newsjacking y sugerir un ángulo alternativo de `trend-researcher`.

## Proceso
1. Resume la noticia en 1–2 líneas, en palabras propias (nunca citar extensamente el artículo original — respetar derechos de autor).
2. Conecta la noticia con la visión de Campuslands: ¿qué significa esto para alguien que quiere trabajar en tech sin migrar? ¿qué dice sobre la importancia de actualizarse en IA?
3. Define el ángulo: educativo (explicar qué significa la noticia), inspiracional (qué oportunidad abre), o promocional (cómo un programa de Campuslands prepara para esto).
4. Genera la pieza vía `social-post-generator` o `script-writer` según el formato, citando la fuente de forma general (sin URLs largas innecesarias) y sin atribuir afirmaciones falsas a la fuente.

## Output esperado
```
NEWSJACKING — [noticia resumida] | Vigencia: [fecha]

Conexión con Campuslands: [1-2 líneas]
Ángulo elegido: [educativo/inspiracional/promocional]

[Pieza generada]
```

## Restricciones
- Nunca reproducir párrafos extensos de la noticia original; resumir en palabras propias.
- Nunca aprovechar noticias trágicas, polémicas o sensibles de forma oportunista o de mal gusto.
- Si la fuente no es confiable o no se puede verificar, no usarla.
- Velocidad de reacción nunca debe sacrificar la veracidad ni el tono de marca.

## Conexión con otras skills
Recibe input de `trend-researcher` · ejecuta vía `social-post-generator`/`script-writer` · valida con `brand-voice-enforcer`.
