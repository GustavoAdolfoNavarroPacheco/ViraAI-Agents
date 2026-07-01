# Politica De Video Y Toolchain Externo

Fecha de vigencia: 2026-06-30  
Aplica a: VIRA Video Editor

## Decision Operativa

VIRA Video Editor opera mediante un repositorio externo especializado de edicion de video. Por esta razon, sus rutas absolutas hacia el toolchain `video-use`, FFmpeg y recursos tecnicos son necesarias y se consideran una **integracion externa controlada**.

Esta excepcion aplica solo al agente de video. Los demas agentes deben seguir usando rutas relativas del workspace y `context/memory-log.md` como memoria institucional.

## Rutas Permitidas Para VIRA Video Editor

- Toolchain externo: `$env:VIDEO_USE_DIR` (ver `SETUP.md` para configuración)
- FFmpeg local: ruta configurada en `.claude/agents/vira-video-editor.md` y `.codex/agents/vira-video-editor.toml`
- Logo oficial usado en renders: `context/img-creator/ia-academy-logo.png`
- Salida final dentro de este workspace: `output/videos_output/`

## Politica De Almacenamiento

### Conservar

- Videos fuente originales en `videos/` mientras el proyecto este activo.
- Archivos finales aprobados en `output/videos_output/`.
- Archivos de proyecto que permitan reconstruir el render: EDL, scripts de build, subtitulos y transcripciones.

### Archivar o limpiar despues de entrega aprobada

- Segmentos renderizados intermedios `seg_*.mp4`.
- Bases temporales como `base.mp4`, `base_clean.mp4`, `base_loud.mp4` cuando ya exista final aprobado.
- Frames de evaluacion si ya no se necesitan para QA visual.
- Carpetas `_prev_session/` cuando su aprendizaje ya este registrado en `context/memory-log.md` o memoria local del agente.

### Salida final

La ruta canonica para videos finales es:

```text
output/videos_output/
```

La carpeta `output/video_output/` se considera obsoleta si esta vacia. No debe usarse para entregas nuevas.

## Buenas Practicas

- No borrar fuentes ni renders finales sin confirmacion humana.
- Registrar en el reporte de entrega: archivo fuente, output final, duracion, formato, plataforma y decisiones principales de corte/subtitulos.
- Mantener la identidad visual NEBULA en subtitulos, overlays y composicion.
- Mantener subtitulos en la parte inferior centrados por defecto. La variacion visual debe ser suave: cambios moderados de color, tamano y enfasis, nunca bruscos ni demasiado frecuentes.
- Priorizar cortes comprensibles: eliminar errores y silencio muerto, pero conservar pausas cortas cuando ayudan a entender el tema. Evitar cortes abruptos que rompan la continuidad narrativa.
- Si el repo externo cambia de ubicacion, actualizar primero esta politica y luego los agentes.
