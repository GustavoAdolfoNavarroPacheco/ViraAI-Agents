---
name: openai-nebula-prompting
description: Regla vigente para generar assets visuales NEBULA con OpenAI / ChatGPT Images.
metadata:
  type: project
---

VIRA IMG debe generar assets visuales solamente con OpenAI / ChatGPT Images y debe usar `context/visual-style.md` como fuente de verdad visual.

**Why:** El proyecto unifico la generacion visual para evitar contradicciones entre proveedores y mantener consistencia de marca.

**How to apply:** Antes de cualquier imagen, leer `context/visual-style.md`, construir prompt en ingles, reservar zona de logo, evitar texto renderizado y guardar asset + `contenido.md` en `output/[YYYY-MM-DD]_imagen_[descripcion]/`.
