# brand-logos/

Carpeta de logos para Motion Graphics Automatizados de VIRA Video Editor.

Cuando el agente detecta el nombre de una herramienta o plataforma en el transcript, busca el PNG correspondiente aquí y lo overlayea en el video durante el tiempo que el ponente lo menciona.

## Convención de nombres

`<nombre-clave>.png` — fondo transparente, mínimo 320px de ancho, proporción original.

## Logos esperados

| Nombre clave | Herramienta |
|---|---|
| `gemini.png` | Google Gemini |
| `google-ai-studio.png` | Google AI Studio |
| `chatgpt.png` | ChatGPT / OpenAI ChatGPT |
| `openai.png` | OpenAI (logo general) |
| `vira-ai.png` | VIRA AI (logo del sistema) |
| `claude.png` | Claude / Anthropic |
| `copilot.png` | GitHub Copilot / Microsoft Copilot |
| `midjourney.png` | Midjourney |
| `stable-diffusion.png` | Stable Diffusion |
| `runway.png` | Runway ML |
| `google.png` | Google (logo general) |
| `meta.png` | Meta (logo general) |

## Fallback

Si el logo no está en esta carpeta, el agente genera un badge de texto en el video usando el estilo ASS `Impact_HUD` con el nombre de la herramienta. Agregar el PNG elimina el fallback de texto.
