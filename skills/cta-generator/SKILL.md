---
name: cta-generator
description: Genera llamados a la acción (CTA) específicos por canal (WhatsApp, Instagram, web) y por avatar de audiencia para Campuslands AI Academy. Usa esta skill cuando el usuario pida "un CTA", "varios cierres", "cómo cierro este post", o cuando otra skill necesite 2-3 opciones de cierre para una pieza.
---

# CTA Generator

## Función
Producir cierres de acción claros, no genéricos, adaptados al canal de conversión y al nivel de urgencia/confianza del avatar.

## Cuándo se activa
- "Dame un CTA para esto"
- "Necesito 3 opciones de cierre"
- Como sub-paso de `social-post-generator`, `script-writer`, `carousel-builder`, `event-announcement`.

## Inputs necesarios
1. Canal de conversión: WhatsApp (general/empresas/visitas — ver números en `campuslands.md`), Instagram (link en bio/DM), Web (formulario/inscripción).
2. Avatar objetivo (afecta el nivel de formalidad y el motivador: empleabilidad para El Camper, actualización profesional para El Profesional, ROI para Empresas).
3. Etapa del funnel: descubrimiento (CTA suave: "conoce más"), consideración (CTA medio: "agenda una visita"), decisión (CTA fuerte: "inscríbete ahora").

## Proceso
1. Identifica el canal y selecciona el contacto correcto de `campuslands.md`:
   - General: WhatsApp +57 300 971 1559
   - Empresas: WhatsApp +57 316 052 2555
   - Visitas: WhatsApp +57 317 770 9345
2. Redacta el CTA en verbo de acción + beneficio claro + fricción mínima ("Escríbenos al WhatsApp y agenda tu visita a Zona Franca Santander", no "contáctanos para más información").
3. Si se piden variantes, genera 2–3 con distinto nivel de urgencia o enfoque (beneficio vs. urgencia vs. comunidad), sin recurrir a manipulación falsa.
4. Ajusta el verbo y tono al avatar (más directo/motivacional para Camper; más profesional para Empresas/Profesional).

## Output esperado
```
CTA — Canal: [canal] | Avatar: [avatar] | Etapa: [funnel]
1. [opción 1]
2. [opción 2] (si se pidieron variantes)
3. [opción 3] (si se pidieron variantes)
```

## Restricciones
- Nunca usar un número de WhatsApp incorrecto o inventado — siempre verificar contra `campuslands.md`.
- Nunca generar CTAs con falsa urgencia ("solo quedan 2 cupos") si no es un dato verificado.
- Mantener un CTA por pieza como recomendación final salvo que se pidan variantes explícitamente.

## Conexión con otras skills
Usado por `social-post-generator`, `script-writer`, `carousel-builder`, `event-announcement` · complementado por `ab-variant-creator` para pruebas A/B/C.
