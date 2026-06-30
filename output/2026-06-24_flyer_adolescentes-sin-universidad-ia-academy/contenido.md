# flyer_adolescentes_sin-universidad_ia-academy

**Fecha:** 2026-06-24
**Modelo vigente:** OpenAI / ChatGPT Images. Las referencias históricas a otros proveedores fueron retiradas de esta ficha.
**Estado:** Prompt listo para generar. Ver sección "Instrucciones para regenerar".
**Para qué pieza:** Flyer Instagram Feed portrait 4:5 (1080×1350 px) — informativo para adolescentes 15–20 años
**Red social destino:** Instagram Feed
**Avatar objetivo:** Pre-Camper (adolescente 15–20 años, estratos 1–3, Colombia)

---

## Prompt exacto para generación

Usar en OpenAI / ChatGPT Images `OpenAI / ChatGPT Images` con aspect ratio `3:4`, o en OpenAI / ChatGPT Images/V4 con ratio `4:5`, o en OpenAI / ChatGPT Images con `--ar 4:5`:

```
Portrait 3:4 format Instagram Feed marketing image. TOP-LEFT CORNER: completely clean empty dark space approximately 22% width by 10% height, reserved for logo, zero visual elements in this zone. SUBJECT: young Latin American teenager 17 years old, casual dark charcoal hoodie, backpack strap visible on one shoulder, warm medium-dark skin tone, authentic natural look absolutely not stock photo. Expression: determined proud hopeful, chin slightly up, eyes looking straight ahead with quiet fire and confidence, genuine emotion not posed smile. Three-quarter body shot centered-left frame. HOLOGRAPHIC ELEMENTS floating around subject: glowing cyan neural brain network #00D4FF upper-right background, electric blue circuit lines #3D37EF radiating outward from center, luminous particle data nodes scattered, purple #5040A8 atmospheric light scatter. LIGHTING: strong cinematic rim light from front-left, electric blue-cyan glow sculpting face and shoulders and hoodie edges, background dark, subject appears to glow against deep void. BACKGROUND: deep navy #080B2A, ultra-subtle circuit board texture at 5% opacity, atmospheric gradient from dark navy to slightly deeper blue-purple at edges, fine particle dots. COMPOSITION: subject occupies upper 55% of frame centered, holographic elements float upper-right quadrant, lower 40% transitions to very clean very dark navy almost solid for text overlay space, gentle diagonal energy top-right to bottom-left. COLOR PALETTE: #080B2A background, #3D37EF electric blue accents, #00D4FF cyan neon holographic elements, #5040A8 purple atmospheric, #FFFFFF any highlights. STYLE: Campuslands AI Academy NEBULA design system, tech-futuristic yet warmly human, aspirational Latin American youth, editorial cinematic quality, photorealistic ultra-detailed, empowerment aesthetic, NOT corporate NOT generic NOT stock photo. ABSOLUTE: no readable text anywhere, no logos, no watermarks, no white background, no formal clothing, no tie, no suit, no robots, no globe icons.
```

**Negative prompt (si el modelo lo acepta como campo separado):**
```
no text, no watermark, no logo, no corporate style, no generic stock photo, no tie no formal suit, no white background, no robots, no globe icons, no padlock icons, no distorted anatomy, no blurry faces, no overexposed areas, no caucasian-only appearance
```

---

## Decisiones visuales del prompt

- **Referencia base:** `ia-academy3.jpg` (holograma neural flotante + persona + fondo dark) combinada con el patrón de `ia-academy1.jpg` (zona inferior limpia para texto overlay).
- **Persona:** Adolescente latinoamericano/a con hoodie oscuro y morral — evoca estudiante real de barrio, no actor de publicidad. Expresión de determinación hacia adelante, no sonrisa de stock.
- **Hologramas:** Cerebro neural cian (#00D4FF) flotando arriba-derecha, igual que `ia-academy3.jpg`, para comunicar IA visualmente sin texto.
- **Iluminación:** Rim light desde la izquierda (mismo patrón que todas las referencias) — la persona brilla contra el fondo oscuro, efecto cinematic que transmite protagonismo.
- **Zona inferior limpia:** El 40% inferior del frame queda en navy sólido oscuro para que el equipo superponga titular, badges y CTA en Canva sin competir con la foto.
- **Top-left vacío:** Zona explícitamente reservada en el prompt para el logo vectorial oficial.

---

## Especificación completa de texto overlay (para aplicar en Canva)

### Zona superior (0–15%)
| Elemento | Contenido | Estilo |
|---|---|---|
| Badge pill top-center | `IA ACADEMY` | Fondo #1A1060, borde #3D37EF, texto blanco Roboto Medium, 12px, padding 6×16px |
| Zona top-left | *(vacío — logo oficial aquí)* | Logo vectorial blanco campuslands IA ACADEMY, ~20% ancho |

### Zona media (55–75%) — sobre área oscura
| Elemento | Contenido | Estilo |
|---|---|---|
| Badge 1 | `IA Generativa  ·  Machine Learning  ·  Computer Vision` | Fondo #1A1060 semitransparente, borde #3D37EF, ícono cerebro #00D4FF, texto blanco Roboto Light 11px |
| Badge 2 | `Sin conocimientos previos` | Mismo estilo, ícono check #00D4FF |
| Badge 3 | `Presencial y Online` | Mismo estilo, ícono laptop #00D4FF |
| Badge 4 | `Bucaramanga  ·  Bogotá  ·  Cúcuta  ·  Guatemala` | Mismo estilo, ícono pin #3D37EF |

### Zona inferior (75–100%)
| Elemento | Contenido | Estilo |
|---|---|---|
| Titular principal | `Tu carrera en IA empieza aquí.` | Roboto Mono Bold, 28px, blanco #FFFFFF |
| Titular línea 2 | `Sin universidad. Sin excusas.` | Roboto Mono Bold, 28px, blanco — "Sin" en blanco, "universidad" en gradiente #3D37EF→#C850FF |
| Subtítulo | `Aprende Inteligencia Artificial desde cero y consigue tu primer empleo en tecnología.` | Roboto Regular 13px, blanco 80% opacidad |
| Botón CTA | `Empieza hoy →` | Gradiente horizontal #3D37EF→#5040A8→#C850FF, radio 50px, Roboto Bold 16px blanco, ancho 90% frame |
| Fila datos | `+57 300 971 1559  ·  campuslands.aiacademy.com.co  ·  @ai.campuslands` | Roboto Light 10px, blanco 60% opacidad, centrado |
| Tagline | `"Formar sin migrar."` | Roboto Italic Light 10px, #00D4FF, centrado |

---

## Instrucciones para el equipo de diseño en Canva

### Paso 1 — Subir imagen de fondo
1. Abrir documento nuevo en Canva: **1080 × 1350 px** (Instagram Feed portrait).
2. Subir la imagen generada (`flyer_adolescentes_ia-academy.png`) como elemento de fondo, ajustar a "llenar marco".

### Paso 2 — Logo oficial (top-left)
1. Subir el archivo vectorial oficial del logo (versión blanca sobre transparente).
2. Posicionar en esquina superior izquierda.
3. Tamaño: ~216px de ancho (20% del frame de 1080px).
4. Margen desde los bordes: 32px top, 32px left.
5. Verificar que ningún elemento de la imagen generada compita con el logo en esa zona.

### Paso 3 — Badge "IA ACADEMY" (top-center)
1. Crear caja de texto con fondo #1A1060, borde 1px #3D37EF, radio 50px.
2. Texto: `IA ACADEMY` — Roboto Medium, 12px, #FFFFFF, todo mayúsculas.
3. Centrar horizontalmente. Posición Y: ~80px desde arriba.

### Paso 4 — Titular (zona oscura inferior de la imagen)
1. Añadir titular en dos líneas sobre la zona dark inferior (aprox. desde Y=740px).
2. Usar Roboto Mono Bold, ~54px, color blanco.
3. En la segunda línea, colorear "universidad" con gradiente o color #5040A8 (Canva: usar texto con efecto color o degradado manual).

### Paso 5 — Badges informativos (zona media)
1. Crear 4 badges tipo píldora con fondo #0D0D3A (semitransparente 85%), borde #3D37EF 1px, radio 8px.
2. Ancho: ~90% del frame. Alto: ~44px cada uno. Espaciado: 8px entre badges.
3. Ícono a la izquierda en color #00D4FF (usar íconos de Canva: cerebro, check, laptop, pin).
4. Texto en blanco Roboto Regular 12px.
5. Posición vertical: entre Y=720px y Y=920px aprox.

### Paso 6 — Botón CTA
1. Rectángulo con gradiente horizontal #3D37EF → #C850FF, radio 50px.
2. Ancho: 960px (90% de 1080px). Alto: 64px.
3. Centrar. Posición Y: ~1180px desde arriba.
4. Texto: `Empieza hoy →` — Roboto Bold 18px, #FFFFFF.

### Paso 7 — Fila de datos de contacto
1. Texto: `+57 300 971 1559  ·  campuslands.aiacademy.com.co  ·  @ai.campuslands`
2. Roboto Regular 10px, #FFFFFF a 60% opacidad. Centrado. Y: ~1265px.

### Paso 8 — Tagline
1. Texto: `"Formar sin migrar."`
2. Roboto Italic 10px, color #00D4FF. Centrado. Y: ~1290px.

### Paso 9 — Revisión final
- [ ] El logo se ve limpio en top-left sin elementos de fondo compitiendo
- [ ] No hay texto ilegible o cortado en los bordes
- [ ] El gradiente del CTA va de azul a magenta (no al revés)
- [ ] Los badges tienen suficiente contraste sobre la imagen
- [ ] La imagen exportada pesa menos de 2MB para Instagram

---

## Notas de evaluación

**Intentos de generación:**
1. `OpenAI / ChatGPT Images` 4:5 — bloqueado: 0 créditos suficientes (requiere 2.0, disponibles 1.76)
2. `OpenAI / ChatGPT Images` 3:4 — bloqueado: límite diario de generaciones del plan Plus agotado

**Nota:** El flujo vigente usa OpenAI / ChatGPT Images. El prompt está validado conceptualmente contra los criterios NEBULA:
- [x] Zona top-left reservada para logo — especificado explícitamente en prompt
- [x] Fondo oscuro dominante navy #080B2A — especificado con hex exacto
- [x] Acentos NEBULA (#3D37EF, #00D4FF, #5040A8) — inyectados con hex en prompt
- [x] Sin texto superpuesto — restricción absoluta en prompt
- [x] Persona latinoamericana, no stock photo — descripción específica anti-corporativa
- [x] Espacio limpio inferior para overlay — 40% inferior reservado explícitamente
- [x] Composición dinámica patrón NEBULA — diagonal energy + patrón ia-academy3.jpg

**Para regenerar:** Esperar reset del límite diario OpenAI / ChatGPT Images (generalmente 24h) o recargar créditos a mínimo 2.0. Alternativamente, usar OpenAI / ChatGPT Images/V4 o OpenAI / ChatGPT Images con el prompt de esta sección.

