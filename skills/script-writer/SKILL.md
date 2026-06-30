---
name: script-writer
description: Escribe guiones para Reels, TikToks o videos cortos de Campuslands AI Academy con estructura fija de 30 segundos (0–3s hook, 3–15s desarrollo, 15–25s demo/ejemplo, 25–30s CTA). Usa esta skill siempre que el usuario pida "un guion", "un reel", "un video", "un script para TikTok", o cuando social-post-generator detecte que el formato pedido es video y no post estático.
---

# Script Writer

## Función
Convertir un tema, masterclass o ángulo de tendencia en un guion de video corto, con timing explícito y dirección de cámara/edición básica, listo para grabar.

## Cuándo se activa
- "Escribe un guion para Reel sobre [tema]"
- "Necesito un script de TikTok de [masterclass/programa]"
- "Convierte esta tendencia en un video"

## Inputs necesarios
1. Tema o tendencia base (puede venir de `trend-researcher`).
2. Avatar objetivo (`context/audience-profiles.md`).
3. Pilar de contenido.
4. Formato de entrega: ¿quién habla? (vocero, texto en pantalla, voz en off) — si no se especifica, ofrecer ambas opciones.

## Estructura obligatoria (30 segundos)
| Tiempo | Función | Qué debe pasar |
|---|---|---|
| 0–3s | Hook | Frase o imagen que detiene el scroll. Debe generar una pregunta o tensión inmediata. |
| 3–15s | Desarrollo | Explica el problema o la idea central. Lenguaje simple, una idea por frase. |
| 15–25s | Demo/Ejemplo | Muestra algo concreto: una herramienta, un resultado, un testimonio breve, una captura. |
| 25–30s | CTA | Acción clara: "Escríbenos al WhatsApp", "Link en bio", "Inscríbete antes del [fecha]". |

## Proceso
1. Define el hook primero — si el hook no funciona, el resto no importa. Prueba 2 opciones de hook si el tema lo permite.
2. Escribe el guion marcando: **[texto hablado/voz en off]**, *(texto en pantalla)*, [dirección de cámara/B-roll sugerido].
3. Ajusta el lenguaje al avatar: técnico y directo para El Profesional; motivacional y cercano para El Camper.
4. Cierra con CTA alineado al canal (TikTok/Reels → "link en bio" o "comenta IA y te escribimos").
5. Pasa por `brand-voice-enforcer`.

## Output esperado
```
GUION — [tema] | Pilar: [pilar] | Avatar: [avatar] | Duración: 30s

[0–3s] HOOK
[texto hablado] / *(texto en pantalla)* / [B-roll sugerido]

[3–15s] DESARROLLO
...

[15–25s] DEMO/EJEMPLO
...

[25–30s] CTA
...
```

## Restricciones
- Nunca exceder los 30s de estructura salvo que el usuario pida explícitamente un video largo (en ese caso, escalar proporcionalmente la misma lógica de bloques).
- Nunca prometer resultados de empleabilidad como garantía absoluta sin matizar (revisar claims permitidos en `voice-type.md`).
- Evitar jerga de IA sin explicarla en una frase simple — la audiencia Camper no siempre es técnica.

## Conexión con otras skills
`trend-researcher` (input de tema) · `testimonial-formatter` (si el demo es un caso real) · `ab-variant-creator` (variantes de hook) · `brand-voice-enforcer` (validación final).

