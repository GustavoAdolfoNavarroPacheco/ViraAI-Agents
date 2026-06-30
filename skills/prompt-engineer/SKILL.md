---
name: prompt-engineer
description: Construye prompts estructurados (ROL + CONTEXTO + FORMATO + RESTRICCIONES + VARIANTES). Para imágenes, los prompts deben estar orientados exclusivamente a OpenAI / ChatGPT Images y al sistema visual NEBULA. Usa esta skill cuando el usuario pida "un prompt para generar [imagen/video/texto]", "ayúdame a armar el prompt", o necesite delegar una tarea creativa.
---

# Prompt Engineer

## Función
Traducir una necesidad de contenido en un prompt reutilizable y bien estructurado. Si el prompt es visual, debe formularse para OpenAI / ChatGPT Images y usar `context/visual-style.md`.

## Cuándo se activa
- "Dame el prompt para generar una imagen de [tema] en ChatGPT Images"
- "Necesito el prompt para que el equipo de diseño genere [...]"
- Cuando `carousel-builder` o `script-writer` sugieren un visual que requiere generación con IA.

## Estructura obligatoria del prompt
1. **ROL**: quién/qué debe actuar la IA generativa ("Actúa como diseñador gráfico especializado en branding educativo tech").
2. **CONTEXTO**: marca, paleta/identidad visual de Campuslands desde `context/visual-style.md`, tema específico, avatar al que va dirigido.
3. **FORMATO**: dimensiones, tipo de archivo, estilo visual (flat design, fotografía real, ilustración), duración si es video.
4. **RESTRICCIONES**: qué evitar (logos de competidores, texto excesivo, clichés de stock photo genérico, contenido que no respete la identidad de marca).
5. **VARIANTES**: 2–3 variaciones del mismo prompt cambiando un solo elemento (color, ángulo, encuadre) para dar opciones.

## Proceso
1. Aclara con el usuario qué tipo de output generativo necesita (imagen, video, copy, audio).
2. Si es imagen, usa exclusivamente OpenAI / ChatGPT Images como destino del prompt.
3. Completa cada bloque de la estructura con el detalle suficiente para que sea ejecutable sin ambigüedad.
4. Entrega el prompt en bloque de código para fácil copia.

## Output esperado
```
ROL: ...
CONTEXTO: ...
FORMATO: ...
RESTRICCIONES: ...
VARIANTES:
1. ...
2. ...
3. ...
```

## Restricciones
- No generar prompts que pidan reproducir logos, personajes o marcas de terceros con derechos de autor.
- No generar prompts para crear contenido falso o engañoso (deepfakes de personas reales, testimonios falsos).
- Mantener coherencia con la identidad visual real de Campuslands cuando se conozca.
- Para imagenes, no recomendar proveedores distintos de OpenAI / ChatGPT Images.

## Conexión con otras skills
Apoya a `carousel-builder`, `script-writer`, `event-announcement` cuando necesitan un asset visual generado externamente.
