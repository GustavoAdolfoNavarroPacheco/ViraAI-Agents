# MEMORY.md — VIRA Video Editor

> Memoria de proyecto VIRA AI (Agente AI - Claude). Toda la memoria del agente se consolida en `.claude/agent-memory/vira-video-editor/` (relativa a la raíz del proyecto).

## Sesiones de edición completadas

| Sesión | Fecha | Archivo fuente | Plataforma | Output | Notas |
|---|---|---|---|---|---|
| — | 2026-06-25 (aprox) | VideoBase_SinEditar.mp4 | Reels | output/videos_output/VideoBase_Reels_v1.mp4 | Primera edición del proyecto; clips gradeados en videos/edit/_prev_session/ |
| — | 2026-06-30 | PromptEngineering V10 Cam+Pantalla | YouTube 16:9 | output/videos_output/PromptEngineering_Video10_v1.mp4 | Dual-source 3:57; upgrade v2 con panel gradiente NEBULA en PiP, 6 estilos NEBULA + Poppins Bold, 2 cross-dissolves. Ver [promptengineering_v10_dualsource.md] |

## Memorias detalladas
- [PromptEngineering V10 dual-source](promptengineering_v10_dualsource.md) — sync offset 361.4, panel gradiente PiP, instalación Poppins+fontsdir, ASS xfade-aware

## Patrones confirmados

- Fuente de video en: `videos/` (raíz del proyecto)
- Output de video en: `output/videos_output/`
- Clips intermedios en: `videos/edit/<sesion>/clips_graded/`
- Transcripts en: `videos/edit/<sesion>/transcripts/`
- GPU QSV confirmada funcional en esta máquina

## Pendientes

- Confirmar si el usuario quiere versión LinkedIn (landscape) del VideoBase además de la versión Reels
- Registrar preferencias de pacing y estilo de subtítulos una vez el usuario dé feedback sobre VideoBase_Reels_v1.mp4
