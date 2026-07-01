# Validacion De Operatividad - VIRA Video Editor

Fecha: 2026-06-30  
Alcance: revision de agente `vira-video-editor`, repo externo `video-use`, rutas, helpers, FFmpeg, videos actuales y outputs existentes.

## Conclusion

Si, Codex puede poner a funcionar el agente `vira-video-editor` en este workspace.

El entorno base existe y esta razonablemente listo:

- Repo externo `video-use`: disponible en `$env:VIDEO_USE_DIR`.
- Helpers requeridos: `transcribe.py`, `pack_transcripts.py`, `render.py`, `grade.py`, `timeline_view.py` disponibles.
- `uv`: disponible y funcional fuera del sandbox.
- FFmpeg: disponible y funcional fuera del sandbox.
- Encoder `h264_qsv`: disponible en FFmpeg.
- `libass`: disponible para subtitulos ASS.
- Logo oficial: disponible en `context/img-creator/ia-academy-logo.png`.
- Videos fuente actuales: disponibles en `videos/`.
- Outputs previos: disponibles en `output/videos_output/`.

## Validaciones Ejecutadas

### Rutas

Confirmado:

- `$env:VIDEO_USE_DIR`
- `$env:VIDEO_USE_DIR\helpers`
- `$env:VIDEO_USE_DIR\.env`
- `context/img-creator/ia-academy-logo.png`
- `C:\Temp`

### FFmpeg

FFmpeg 8.1.1 funciona fuera del sandbox y tiene:

- `h264_qsv` para H.264 con Intel Quick Sync.
- `hevc_qsv`, `av1_qsv`, `vp9_qsv` y otros encoders.
- `libass` / ASS para subtitulos quemados.

### Helpers

Funcionan fuera del sandbox:

- `uv run python helpers\transcribe.py --help`
- `uv run python helpers\render.py --help`
- `uv run python helpers\pack_transcripts.py --help`

## Condiciones Para Usarlo En Una Edicion Real

Para una ejecucion completa se necesita:

1. Nombre exacto del archivo de video.
2. Carpeta exacta donde esta el archivo.
3. Tipo de fuente: `single` o `dual`.
4. Plataforma objetivo: Instagram Reels, TikTok, YouTube Shorts, YouTube long-form o LinkedIn.
5. Permitir ejecucion fuera del sandbox para:
   - `uv run ...`
   - FFmpeg
   - transcripcion con ElevenLabs si se requiere generar transcript nuevo.

## Riesgos O Puntos A Corregir

1. El agente `.claude` esta mucho mas completo que `.codex`.
   - Recomendacion: ampliar `.codex/agents/vira-video-editor.toml` con las reglas criticas del agente Claude.

2. `uv` falla dentro del sandbox por acceso a cache en AppData.
   - Solucion operativa: ejecutar helpers fuera del sandbox con aprobacion.

3. La transcripcion depende de ElevenLabs.
   - Hay `.env` en el repo externo, pero la llamada real requiere acceso de red y permisos.

4. Poppins no esta instalado segun memoria previa del proyecto.
   - El sistema puede usar fallback Arial, pero para salida NEBULA ideal conviene instalar Poppins.

5. El agente de Codex no pregunta plataforma objetivo, mientras el agente Claude si.
   - Recomendacion: agregar esa pregunta al TOML de Codex.

## Estado Final

El agente puede funcionar. No esta bloqueado por estructura del repo ni por falta de herramientas base. La unica diferencia practica es que, para renderizar/transcribir videos reales, Codex necesitara permisos de ejecucion fuera del sandbox y, si no hay transcript ya existente, acceso a la API de transcripcion configurada en el repo externo.

