---
name: image-generator
description: Genera imagenes reales para marketing de Campuslands AI Academy usando OpenAI / ChatGPT Images. Construye prompts en ingles, ejecuta la generacion con la API de OpenAI disponible, evalua contra el sistema visual NEBULA y guarda el asset con ficha completa en una carpeta propia dentro de output/.
---

# Image Generator - OpenAI / ChatGPT Images

## Funcion

Traducir un brief visual en espanol colombiano a un prompt en ingles optimizado para OpenAI / ChatGPT Images, generar la imagen directamente cuando la API este disponible, evaluar el resultado contra `context/visual-style.md` y guardar el entregable en `output/`.

## Cuándo se activa

- "Genera la imagen para este post"
- "Necesito la portada del carrusel"
- "Dame el banner para el evento"
- "Haz una imagen para Instagram / LinkedIn / Stories"
- Cuando VIRA AI, carousel-builder o event-announcement necesitan un asset visual

## Prerrequisito

La API key debe existir en `.env`:

```text
OPENAI_API_KEY=...
```

Nunca escribir la API key en el chat, en prompts, en fichas de salida ni en archivos de configuracion compartidos.

## Proceso obligatorio

### Paso 1 - Cargar marca visual

Antes de crear cualquier prompt:

1. Leer `context/visual-style.md`.
2. Revisar las referencias de `context/img-creator/`, especialmente `ai-academy.png` y el logo oficial.
3. Confirmar paleta, tipografia, composicion y criterios de aceptacion NEBULA.

### Paso 2 - Extraer brief

Identificar:

- Tipo de pieza: post, portada, banner, historia, fondo, icono o elemento para Canva.
- Red y proporcion: 1:1, 4:5, 9:16 o 16:9.
- Avatar: Camper, Profesional/Educador, Empresa o mixto.
- Mensaje visual central.
- Si requiere fondo transparente.
- Zonas limpias para texto/logo.

Si el brief es insuficiente y no se puede inferir, preguntar solo lo necesario.

### Paso 3 - Elegir configuracion OpenAI

Usar el modelo de imagen disponible en OpenAI / ChatGPT Images para la cuenta activa. No hardcodear un proveedor externo ni recomendar alternativas fuera de OpenAI.

Seleccionar parametros segun objetivo:

| Necesidad | Configuracion |
|---|---|
| Imagen final para post/banner | alta calidad, PNG o JPEG |
| Elemento para Canva | PNG, fondo transparente si la API lo soporta |
| Instagram 1:1 | cuadrado |
| Instagram 4:5 / Stories 9:16 | vertical |
| LinkedIn / Facebook | horizontal |

### Paso 4 - Construir prompt en ingles

Estructura:

```text
[SUBJECT]: ...
[SCENE]: ...
[STYLE]: OpenAI / ChatGPT Images, Campuslands AI Academy NEBULA brand system
[COLOR PALETTE]: #0B0826, #A239CA, #5FB4F4, #9A8CF2, #6FD6E0, #56D0A8, white
[TYPOGRAPHIC DIRECTION]: Poppins-inspired bold headline space, Roboto Mono HUD label style, but no rendered text
[LIGHTING]: cinematic cyan screen light, violet/magenta rim glow, premium educational tech atmosphere
[COMPOSITION]: include official logo safe area, clean Canva text space, social media aspect ratio
[MOOD]: inspiring, expert, accessible, human, Colombian/Latin American tech education
[NEGATIVE]: no text, no watermark, no logo, no fake brand marks, no robots, no stock photo, no distorted anatomy
```

Usar los bloques exactos de `context/visual-style.md` cuando aplique.

### Paso 5 - Generar

Ejecutar la llamada a OpenAI / ChatGPT Images con la configuracion elegida. Guardar la imagen dentro de una carpeta propia:

```text
output/[YYYY-MM-DD]_imagen_[descripcion-clara]/asset.png
```

### Paso 6 - Evaluar

Comparar contra los criterios de `context/visual-style.md`:

- Paleta NEBULA correcta.
- Zona de logo limpia.
- Sin texto accidental.
- Sin logos externos.
- Persona natural y latinoamericana si aplica.
- Espacio claro para copy/CTA.
- Estetica tech educativa premium.

Si falla: ajustar prompt y regenerar. Maximo dos intentos automaticos antes de entregar la mejor version con nota clara.

### Paso 7 - Guardar ficha

Guardar siempre:

```text
output/[YYYY-MM-DD]_imagen_[descripcion-clara]/contenido.md
```

Estructura:

```markdown
# IMG - [Tema] - [YYYY-MM-DD]

**Para:** [tipo de pieza]
**Red social:** [red]
**Formato:** [proporcion/dimension]
**Avatar objetivo:** [avatar]
**Proveedor:** OpenAI / ChatGPT Images
**Fondo transparente:** [si/no]

## Prompt
[prompt completo]

## Archivo generado
output/[carpeta]/asset.png

## Notas de evaluacion
[criterios cumplidos, intentos, ajustes]
```

### Paso 8 - Entregar

Mostrar la imagen o ruta local al usuario y confirmar la carpeta guardada. Despues, si forma parte de una sesion de contenido, el control vuelve a `document-exporter` y `memory-manager` para formato y encuesta.

## Restricciones absolutas

- Solo OpenAI / ChatGPT Images para generacion visual.
- Prompts siempre en ingles.
- No texto dentro de imagen salvo brief explicito.
- No logos inventados ni marcas de terceros.
- No personas reales reconocibles.
- No entregar imagen solo en chat: debe existir archivo local.
- No guardar archivos sueltos directamente en `output/`.

## Conexion con otras skills

| Skill | Relacion |
|---|---|
| `social-post-generator` | Genera visual para post |
| `carousel-builder` | Genera portada o fondo visual |
| `event-announcement` | Genera banner y version vertical |
| `ab-variant-creator` | Genera variantes visuales con una variable aislada |
| `prompt-engineer` | Fallback para entregar prompt cuando la API de OpenAI no este disponible |
| `brand-voice-enforcer` | Verifica coherencia de marca del concepto |

