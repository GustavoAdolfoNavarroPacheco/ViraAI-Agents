# Entrega Video - Prompt Engineering Video 10

Fecha: 2026-06-30  
Agente: VIRA Video Editor  
Plataforma objetivo: YouTube largo horizontal  
Duracion maxima solicitada: 7 minutos  

## Archivo Final

`output/videos_output/PromptEngineering_Video10_youtube_horizontal_v3.mp4`

## Metadatos Verificados

- Duracion: 237.3 segundos (3:57)
- Resolucion: 1920 x 1080
- FPS: 30
- Audio: AAC, 48 kHz, stereo
- Bitrate aproximado: 6.57 Mbps
- Peso: 194,831,600 bytes

## Fuentes Usadas

- `videos/PromptEngineering Video 10 Pantalla.mp4`
- `videos/PromptEngineering Video 10 Cam.mp4`

## Decisiones De Edicion

- Formato horizontal para YouTube largo.
- Edicion dual-source: pantalla como fuente principal en la demo y camara como PiP cuando aplica.
- Duracion final bajo el limite de 7 minutos.
- PiP reubicado hacia el lateral derecho para liberar la zona inferior de subtitulos.
- Transiciones suaves entre bloques principales mediante cross-dissolve corto.
- Cortes basados en claridad narrativa, evitando sensacion brusca.

## Subtitulos

- Subtitulos ASS quemados en el video final.
- Ubicacion: parte inferior centrada.
- Estilo: NEBULA moderado, Poppins Bold.
- Variacion visual suave:
  - Spoken: 135 cues
  - Impact_Marca: 4 cues
  - Impact_HUD: 2 cues
  - Highlight_Teal: 10 cues
  - Highlight_Violeta: 1 cue
- Total: 152 eventos de subtitulo.

## QA Realizado

- Verificacion con `ffprobe` de duracion, resolucion, FPS y audio.
- Capturas de control generadas en:
  - `videos/edit/pe_final/eval/v3_0012.jpg`
  - `videos/edit/pe_final/eval/v3_0145.jpg`
  - `videos/edit/pe_final/eval/v3_0330.jpg`
- Revision visual:
  - subtitulos inferiores centrados;
  - subtitulos no invaden rostro;
  - PiP no tapa subtitulos;
  - logo visible.

## Archivos Tecnicos Generados

- `videos/edit/pe_final/build_v3.py`
- `videos/edit/pe_final/make_ass_v3.py`
- `videos/edit/pe_final/base_v3.mp4`
- `C:/Temp/reels_v3.ass`

