# Auditoria General Del Workspace VIRA AI

Fecha: 2026-06-30  
Agente aplicado: VIRA QA  
Alcance: revision general de archivos existentes en la carpeta actual, contexto, skills, agentes, memoria, output y estructura operativa.

## Resumen Ejecutivo

El workspace esta bien encaminado como sistema de agentes de marketing para Campuslands AI Academy: tiene contexto institucional, skills modulares, agentes para Codex/Claude, memoria central y carpetas de output. Sin embargo, hay riesgos importantes de seguridad, consistencia y mantenimiento.

## Actualizacion Posterior A La Revision

Decisiones aplicadas el 2026-06-30:

1. `.env` se conserva porque el usuario confirmo que la API key actual es inutil y desea mantener el archivo local.
2. Los claims de empleabilidad se ajustaron a un punto medio: Campuslands mantiene un compromiso fuerte de formacion, acompanamiento y conexion con oportunidades laborales, sin prometer empleo absoluto sin condiciones.
3. NEBULA queda como sistema visual prioritario para AI Academy. El verde institucional queda como acento secundario de conexion con Campuslands.
4. Las rutas absolutas del agente de video se mantienen porque son necesarias para operar con el repo externo `video-use`; se documentaron como integracion externa controlada en `context/video-storage-policy.md`.
5. Para videos, se eligio una reparacion no destructiva: no borrar fuentes ni renders; documentar politica de conservacion, archivo y salida canonica en `output/videos_output/`; reforzar `.gitignore` para futuros binarios e intermedios.
6. Se completaron fichas `contenido.md` faltantes en las tres carpetas de imagen con datos verificables de archivo, dimensiones, peso y notas de trazabilidad.

Prioridad inmediata:

1. Mantener `.env` local y evitar imprimir o compartir su contenido.
2. Usar los nuevos claims matizados de empleabilidad.
3. Usar NEBULA como prioridad visual.
4. Tratar VIRA Video Editor como integracion externa controlada.
5. Aplicar la politica de video antes de borrar o archivar intermedios.
6. Mantener fichas `contenido.md` en cada nuevo asset visual.

## Hallazgos Criticos

### 1. Secreto sensible en `.env`

Existe un archivo `.env` local con una API key real de OpenAI.

Riesgo:
- Exposicion accidental por copia, backup, captura, sincronizacion o commit.
- Aunque `.gitignore` incluye `.env` y `*.env`, el secreto sigue presente en el workspace.

Accion recomendada:
- Revocar/rotar la key en OpenAI.
- Mantener `.env` local, pero crear `.env.example` sin secretos.
- Agregar una regla operativa: nunca leer ni imprimir `.env` salvo auditoria de seguridad.
- Considerar mover secretos a variables de entorno del sistema.

### 2. Promesa de empleabilidad demasiado absoluta

Archivos afectados:
- `context/campuslands.md`: "Empleabilidad Garantizada", "Compromiso de empleo en maximo 12 meses", "Garantia explicita de empleabilidad".
- `context/audience-profiles.md`: "Empleo garantizado en maximo un ano".
- `context/instructions.md`: "Promesa: Empleo garantizado".
- `VIRA-AI-PROMPT-UNIVERSAL.md`: "Promesa: empleo en maximo 12 meses".

Contradiccion:
- `AGENTS.md` y reglas globales dicen no prometer empleabilidad de forma absoluta o sin matiz.
- `brand-voice-enforcer` exige matizar claims de empleabilidad.
- Pero varios contextos canonicos siguen autorizando formulaciones absolutas.

Accion recomendada:
- Definir una frase unica aprobada legal/comercialmente. Ejemplo:
  "Campuslands trabaja con un modelo de acompanamiento y conexion con oportunidades laborales, con compromisos sujetos a condiciones del programa."
- Mover cualquier claim fuerte a una seccion de "Claims sensibles: usar solo si el equipo confirma vigencia y condiciones".

### 3. Identidad visual contradictoria

Archivos afectados:
- `context/ai-academy.md` y `context/instructions.md` indican paleta verde `#00A651`, blanco y negro.
- `context/visual-style.md` declara sistema NEBULA con fondo `#0B0826`, acentos violeta, azul, teal y glow.
- `document-exporter` ya usa colores NEBULA en ejemplos.

Riesgo:
- VIRA IMG puede crear piezas en NEBULA mientras otros agentes piden verde/blanco/negro.
- Inconsistencia visual entre flyers, imagenes, documentos y videos.

Accion recomendada:
- Definir jerarquia:
  - Identidad institucional base: verde/blanco/negro.
  - Sistema AI Academy vigente: NEBULA.
  - Uso del verde: solo como color institucional secundario o sello Campuslands si aplica.
- Actualizar `ai-academy.md` e `instructions.md` para que apunten a `visual-style.md` como fuente visual vigente.

### 4. Rutas absolutas externas en VIRA Video Editor

Archivos afectados:
- `.codex/agents/vira-video-editor.toml`
- `.claude/agents/vira-video-editor.md`

Problemas:
- Dependen de `C:\Users\adolf\Developer\video-use`.
- Guardan memoria tecnica fuera del workspace.
- Referencian rutas absolutas de FFmpeg, logo y toolchain.
- Chocan con la regla de memoria que pide rutas relativas dentro del proyecto, salvo integraciones muy controladas.

Accion recomendada:
- Crear un archivo `context/video-toolchain.md` con la configuracion tecnica.
- Definir variable `VIDEO_USE_ROOT`.
- Mantener dentro del agente solo instrucciones portables.
- Registrar memoria de proyecto dentro de `.claude/agent-memory/vira-video-editor/` o `context/memory-log.md`, no como dependencia oculta externa.

### 5. Binarios pesados e intermedios dentro del workspace

Archivos grandes detectados:
- Videos fuente en `videos/`: 687 MB, 430 MB, 277 MB.
- Outputs finales en `output/videos_output/`: 207 MB, 217 MB, 81 MB.
- Intermedios en `videos/edit/pe_work/`, `videos/edit/pe_final/`, `_prev_session/`: multiples archivos entre 10 MB y 180 MB.

Riesgo:
- El workspace crece rapido y se vuelve dificil de respaldar, sincronizar o revisar.
- Mezcla fuentes, renders intermedios, outputs finales y evaluaciones.

Accion recomendada:
- Mantener:
  - `videos/source/` para insumos originales.
  - `videos/projects/[nombre]/` para proyectos activos.
  - `output/videos_output/` solo para finales entregables.
  - `archive/videos/` o almacenamiento externo para sesiones cerradas.
- Agregar politica de limpieza: borrar o archivar intermedios luego de entregar final aprobado.

## Archivos O Carpetas Candidatos A Limpieza

### `output/video_output/`

Carpeta vacia detectada. Parece duplicado o typo de `output/videos_output/`.

Accion:
- Eliminar si no se usara, o estandarizar todos los agentes a una sola ruta.

### `output/_tools/`

Contiene scripts de generacion de flyers dentro de `output/`.

Riesgo:
- `output/` deberia ser para entregables, no tooling.

Accion:
- Mover a `tools/`, `scripts/` o `internal-tools/`.
- Si se mantienen, documentar que `_tools/` no es entregable.

### Carpetas de imagen sin ficha `contenido.md`

No tienen `contenido.md`:
- `output/2026-06-24_imagen_hero-ia-academy/`
- `output/2026-06-24_imagen_poster-reclutamiento/`
- `output/2026-06-24_imagen_profesional-feed/`

Contradiccion:
- `image-generator` exige guardar siempre ficha `contenido.md` con prompt, uso, ruta y notas.

Accion:
- Reconstruir ficha minima para cada imagen si se conoce el prompt.
- Si no se conoce, crear ficha de trazabilidad indicando "prompt original no disponible".

### `.agents/`

Carpeta presente pero aparentemente vacia.

Accion:
- Eliminar si no tiene uso.
- O documentar su funcion si sera un contenedor futuro.

## Informacion Incorrecta O Riesgosa

### Datos temporales que requieren verificacion recurrente

Ejemplos:
- Seguidores de Instagram/Facebook.
- CEO/vocero.
- sedes activas.
- expansion internacional Guatemala octubre 2025.
- acuerdos y becas.
- "mayoria contratada en los primeros 3 meses".

Riesgo:
- Son datos cambiantes. Si se usan como "verificados" sin fecha/fuente, pueden quedar obsoletos.

Accion:
- Agregar columna `fuente` y `fecha_verificacion` en `context/campuslands.md`.
- Crear una rutina mensual de VIRA Scout para validar datos institucionales.

### Fuentes de tendencias sin politica de navegacion

`context/instructions.md` y `content-strategy.md` piden investigar tendencias actuales en redes y noticias.

Riesgo:
- Si el agente no tiene navegacion activa o no cita fuentes, puede inventar actualidad.

Accion:
- En `trend-researcher`, exigir:
  - fuente,
  - fecha,
  - enlace,
  - por que es relevante,
  - nivel de confianza.

## Contradicciones Operativas

### Memoria Codex: `.codex/memory/` vs `.codex/agent-memory/`

`AGENTS.md` y `Claude.md` dicen que Codex debe usar `.codex/memory/`, pero el mapa real y carpetas existentes incluyen `.codex/agent-memory/`.

Accion:
- Elegir una sola ruta canonica.
- Si la decision vigente es `.codex/memory/`, migrar o archivar `.codex/agent-memory/`.
- Actualizar mapa real y agentes.

### `AGENTS.md` vs `Claude.md`

`Claude.md` dice que si hay duda se aplique la regla mas reciente y concreta de `Claude.md`, pero `AGENTS.md` es el archivo maestro para Codex.

Riesgo:
- Dos fuentes maestras pueden divergir.

Accion:
- Definir `AGENTS.md` como fuente canonica universal.
- Hacer que `Claude.md` sea un wrapper que remite a `AGENTS.md`, no una copia completa.

### Flujo de cierre estricto vs excepciones de QA/Analytics

`AGENTS.md` y `Claude.md` dicen que no se puede saltar ningun paso del cierre. `memory-manager` permite adaptar u omitir encuesta en sesiones de validacion o analiticas.

Accion:
- Incorporar la excepcion en `AGENTS.md` y `Claude.md`.
- Mantener una regla clara: "QA/Analytics guardan reporte y preguntan utilidad; contenido publicable usa encuesta 1-5".

## Falta De Informacion

Faltan fuentes verificables para:
- cifras de seguidores,
- estado exacto de sedes,
- condiciones de empleabilidad,
- vigencia del acuerdo con empresa de EE.UU.,
- terminos de becas,
- expansion Guatemala,
- politica legal de claims comerciales.

Falta documentar:
- responsable humano de aprobar claims sensibles,
- frecuencia de actualizacion del contexto,
- politica de almacenamiento/archivo de video,
- politica de secretos,
- flujo de aprobacion visual,
- convencion unica para outputs de video.

## Malas Practicas Detectadas

1. Secreto real en archivo local del workspace.
2. Rutas absolutas duras en agentes.
3. Duplicacion de instrucciones maestras entre `AGENTS.md`, `Claude.md`, agentes y prompt universal.
4. Output usado tambien como carpeta de herramientas.
5. Intermedios pesados mezclados con entregables.
6. Carpetas de imagen sin ficha de trazabilidad.
7. Claims comerciales fuertes sin fuente, condicion o fecha de verificacion.
8. Agente de video en Claude usa `model: opus`, mientras la memoria indica optimizacion de costo hacia modelos menores en algunos agentes.
9. Instrucciones visuales duplicadas entre contexto, skills, agentes y documentos de output.

## Sugerencias Priorizadas

### Prioridad Alta

1. Rotar la API key y dejar `.env.example`.
2. Resolver claims de empleabilidad.
3. Unificar paleta visual bajo NEBULA o documentar la convivencia con verde institucional.
4. Arreglar VIRA Video Editor para no depender de rutas absolutas externas sin configuracion.
5. Crear fichas `contenido.md` faltantes en carpetas de imagen.

### Prioridad Media

1. Convertir `Claude.md` y `VIRA-AI-PROMPT-UNIVERSAL.md` en derivados generados desde `AGENTS.md`.
2. Mover `output/_tools/` a `tools/`.
3. Eliminar `output/video_output/` si esta vacia y no tiene funcion.
4. Agregar `fuente` y `fecha_verificacion` a datos institucionales.
5. Crear `context/claims-policy.md` para frases autorizadas, restringidas y prohibidas.

### Prioridad Baja

1. Crear script de auditoria que revise:
   - carpetas de output sin `contenido.md`,
   - archivos grandes,
   - secretos,
   - rutas absolutas,
   - divergencias entre AGENTS/Claude/agentes.
2. Crear indice `README.md` del workspace.
3. Separar memoria historica, memoria activa y aprendizajes operativos.

## Validacion De Marca

Revision aplicada contra reglas vigentes:
- Tono: espanol colombiano, cercano y experto.
- Alcance: auditoria interna de VIRA AI/Campuslands AI Academy.
- Veracidad: solo se reportan hallazgos observados en archivos locales.
- Restricciones: no se inventan cifras ni se repite el secreto encontrado.
- CTA operativo: priorizar seguridad, consistencia de claims y limpieza del workspace.
