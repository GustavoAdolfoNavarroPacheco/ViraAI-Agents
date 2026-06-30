---
name: persona-adapter
description: Reescribe automáticamente una pieza de copy base para los distintos avatares de audiencia de Campuslands AI Academy (El Camper, El Profesional/Educador, Empresas/Patrocinadores), ajustando lenguaje, motivadores y nivel técnico sin cambiar el mensaje central. Usa esta skill cuando el usuario pida "adapta esto para [otro avatar]", "necesito esta misma idea para empresas también", o "reescribe esto en un tono más profesional/más cercano".
---

# Persona Adapter

## Función
Tomar una pieza ya creada para un avatar y producir versiones equivalentes para los otros avatares, manteniendo el mensaje central pero ajustando tono, vocabulario y motivador.

## Cuándo se activa
- "Esto lo escribimos para El Camper, adáptalo también para Empresas"
- "Necesito una versión más profesional de este post"
- Como paso de eficiencia cuando una idea fuerte merece llegar a más de un avatar.

## Mapa de adaptación (basado en context/audience-profiles.md)
| Elemento | El Camper (18–28) | El Profesional/Educador (28–50) | Empresas/Patrocinadores |
|---|---|---|---|
| Motivador central | Empleabilidad, salir adelante sin migrar | Actualización de habilidades, vigencia profesional | ROI, talento calificado, impacto social medible (BIC) |
| Tono | Cercano, motivacional, directo | Profesional pero cálido, orientado a resultados | Formal, orientado a datos y beneficios concretos |
| Vocabulario técnico | Explicado en simple, evitar jerga sin contexto | Puede usar términos técnicos con naturalidad | Enfocado en términos de negocio (talento, productividad, certificación) |
| CTA típico | WhatsApp directo, "escríbenos" | "Conoce el programa", "agenda una llamada" | "Hablemos de una alianza", contacto empresas |

## Proceso
1. Identifica el mensaje central de la pieza original (qué idea NO debe cambiar).
2. Para el avatar destino, reescribe: hook, cuerpo y CTA según el mapa de adaptación.
3. Verifica que ningún dato (cifras, sedes, programas) cambie entre versiones — solo cambia el envoltorio, no los hechos.
4. Usa `cta-generator` para el cierre específico del nuevo avatar.
5. Pasa cada versión por `brand-voice-enforcer`.

## Output esperado
```
ADAPTACIÓN — Pieza original para [avatar origen] → [avatar destino]

[Versión adaptada completa: hook, cuerpo, CTA]

Cambios clave: [resumen de qué se ajustó y por qué]
```

## Restricciones
- Nunca alterar los hechos o cifras al adaptar — solo el tono y enfoque.
- No forzar una adaptación si el mensaje central genuinamente no aplica a otro avatar (ej. contenido muy específico de becas para jóvenes no siempre tiene sentido para Empresas) — decirlo en vez de forzar una mala adaptación.

## Conexión con otras skills
Trabaja sobre outputs de `social-post-generator`, `script-writer`, `carousel-builder` · usa `cta-generator` · valida con `brand-voice-enforcer`.

