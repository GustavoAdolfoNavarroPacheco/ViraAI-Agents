---
name: brand-voice-enforcer
description: Valida que cualquier pieza de contenido generada por VIRA AI (post, carrusel, guion, CTA, anuncio) cumpla la voz de marca, el tono y las restricciones de Campuslands AI Academy antes de ser entregada al usuario. Usa esta skill como paso final SIEMPRE después de generar contenido con cualquier otra skill, y también cuando el usuario pida explícitamente "revisa el tono", "valida esto" o "¿esto suena a Campuslands?".
---

# Brand Voice Enforcer

## Función
Actuar como el filtro de calidad de marca: revisa cada pieza de output contra `voice-type.md`, `instructions.md` y `campuslands.md`, y corrige o señala desviaciones antes de la entrega final.

## Cuándo se activa
- Automáticamente al final de cualquier skill que genere contenido orientado al usuario final (posts, carruseles, guiones, anuncios, CTAs).
- Manualmente: "revisa el tono de esto", "¿esto suena bien para Campuslands?", "valida esta pieza".

## Checklist de validación
1. **Tono**: ¿es inspirador, cercano y experto? ¿evita ser corporativo-frío o exageradamente informal?
2. **Idioma**: ¿está en español colombiano natural? ¿los términos técnicos en inglés son los estándar de la industria (no anglicismos innecesarios)?
3. **Visión central**: cuando el tema lo permite, ¿conecta con "formar sin migrar"?
4. **Veracidad**: ¿todas las cifras, nombres, sedes y datos coinciden exactamente con `campuslands.md`? ¿no hay testimonios o logros inventados?
5. **Claims permitidos**: ¿las promesas de empleabilidad o resultados están matizadas según lo que autoriza `voice-type.md` (sin garantías absolutas no verificables)?
6. **Ajuste a avatar**: ¿el lenguaje y los motivadores corresponden al avatar objetivo (`context/audience-profiles.md`)?
7. **Restricciones SIEMPRE/NUNCA** de `instructions.md`: ¿se respetan todas?
8. **Coherencia de canal**: ¿la longitud y formato son correctos para la red social o formato indicado?

## Proceso
1. Recibe la pieza generada y el contexto (pilar, avatar, canal).
2. Recorre el checklist punto por punto.
3. Si encuentra una desviación:
   - Si es menor (una palabra, un ajuste de tono) → corrige directamente y señala el cambio.
   - Si es mayor (dato inventado, claim no permitido, tono fuera de marca) → NO entregues la pieza corregida sin avisar; explica el problema y por qué se ajustó.
4. Entrega la versión final aprobada, con una nota breve de qué se validó (no es necesario listar los 8 puntos siempre, solo mencionar si hubo ajustes relevantes).

## Output esperado
```
✅ Validación de marca — [tipo de pieza]
[Ajustes realizados, si los hubo, en una línea]

[Pieza final aprobada]
```

## Restricciones
- Esta skill NUNCA debe inventar contenido nuevo — solo valida y corrige lo existente.
- Si una pieza tiene un problema de veracidad que no puede resolverse sin más información del usuario, debe señalarlo y pedir confirmación antes de entregar.
- No ser excesivamente rígida con piezas que ya cumplen — evitar fricción innecesaria cuando todo está bien.

## Conexión con otras skills
Es el paso final de: `social-post-generator`, `carousel-builder`, `script-writer`, `cta-generator`, `event-announcement`, `ab-variant-creator`, `testimonial-formatter`, `newsjacking`.

