# 🤖 VIRA AI — Sistema Multi-Agente de Marketing para Campuslands AI Academy

> **V**irtual **I**ntelligent **R**esource **A**gent — Versión 2.1  
> Última actualización: 30 de junio de 2026

---

## 📋 Tabla de Contenido

- [Descripción General](#-descripción-general)
- [Arquitectura del Sistema](#-arquitectura-del-sistema)
- [Agentes](#-agentes)
- [Estructura de Carpetas](#-estructura-de-carpetas)
- [Descripción Archivo por Archivo](#-descripción-archivo-por-archivo)
  - [Archivos Raíz](#archivos-raíz)
  - [ai-context/ — Configuración para IAs](#ai-context--configuración-para-ias)
  - [context/ — Contexto de Marca](#context--contexto-de-marca)
  - [skills/ — Habilidades Modulares](#skills--habilidades-modulares)
  - [.claude/ — Configuración Claude](#claude--configuración-claude)
  - [.codex/ — Configuración Codex](#codex--configuración-codex)
  - [output/ — Entregables](#output--entregables)
  - [tools/ — Herramientas y Scripts](#tools--herramientas-y-scripts)
  - [videos/ — Material Audiovisual](#videos--material-audiovisual)
  - [archive/ — Material Archivado](#archive--material-archivado)
- [Flujo de Trabajo](#-flujo-de-trabajo)
- [Sistema de Memoria](#-sistema-de-memoria)
- [Plataformas Compatibles](#-plataformas-compatibles)
- [Requisitos Técnicos](#-requisitos-técnicos)
- [Qué Falta por Mejorar](#-qué-falta-por-mejorar)

---

## 🧠 Descripción General

**VIRA AI** es un ecosistema de agentes de inteligencia artificial diseñado para automatizar y optimizar toda la operación de marketing digital de **Campuslands AI Academy**. El sistema opera como un equipo autónomo de marketing capaz de:

- 📝 Crear publicaciones para redes sociales (Instagram, LinkedIn, TikTok, Twitter/X)
- 🎬 Editar videos para YouTube, Reels, TikTok y LinkedIn
- 🖼️ Generar imágenes y assets visuales
- 📅 Planificar calendarios editoriales y parrillas de contenido
- 🔍 Investigar tendencias de mercado y competencia
- ✅ Validar contenido contra estándares de marca
- 📊 Analizar rendimiento histórico y patrones
- 🧠 Aprender de forma autónoma mediante un sistema de memoria continua

El proyecto está construido sobre una arquitectura modular de `context + skills + agents + output`, compatible con **Claude (Anthropic)** y **Codex (OpenAI)** como motores de IA.

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────────────────────────┐
│                      USUARIO (Petición)                        │
└──────────────────────────┬──────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│                 VIRA AI ORQUESTADOR                             │
│  • Carga contexto desde context/                                │
│  • Identifica agente correcto                                   │
│  • Enruta la petición                                           │
└────┬──────────┬──────────┬──────────┬──────────┬───────────┬────┘
     │          │          │          │          │           │
     ▼          ▼          ▼          ▼          ▼           ▼
┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐ ┌────────┐
│VIRA IMG│ │ VIRA   │ │VIRA QA │ │ VIRA   │ │ VIRA   │ │ VIRA   │
│        │ │ Video  │ │        │ │ Scout  │ │Memory/ │ │Orquest.│
│        │ │ Editor │ │        │ │        │ │Analyt. │ │(propio)│
└────┬───┘ └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘ └───┬────┘
     │         │          │          │          │           │
     └─────────┴──────────┴──────────┴──────────┴───────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │   skills/ (19 skills)  │
              │   context/ (fuente     │
              │   de verdad)           │
              └───────────┬────────────┘
                          │
                          ▼
              ┌────────────────────────┐
              │  output/ (entregables) │
              │  memory-log (registro) │
              └────────────────────────┘
```

---

## 👥 Agentes

VIRA AI está compuesto por **6 agentes especializados**, cada uno con su archivo de configuración tanto para Claude (`.md`) como para Codex (`.toml`):

| # | Agente | Archivo Claude | Archivo Codex | Función |
|---|--------|---------------|---------------|---------|
| 1 | **VIRA AI Orquestador** | `vira-ai-orquestador.md` | `vira-ai-orquestador.toml` | Agente principal. Recibe la petición del usuario, carga contexto, identifica el agente y skills correctos, coordina la ejecución y gestiona el flujo de cierre de sesión. |
| 2 | **VIRA IMG** | `vira-img.md` | `vira-img.toml` | Generación de imágenes y assets visuales. Opera con la API de OpenAI/ChatGPT Images. Genera prompts en inglés y sigue el sistema de diseño NEBULA. |
| 3 | **VIRA Video Editor** | `vira-video-editor.md` | `vira-video-editor.toml` | Edición de video profesional. Corta, transcribe, agrega subtítulos y genera formatos para YouTube, Reels, TikTok y LinkedIn. Usa un toolchain externo (`video-use`) y FFmpeg. |
| 4 | **VIRA QA** | `vira-qa.md` | `vira-qa.toml` | Control de calidad. Valida que cada publicación, imagen o video generado cumpla los estándares de marca, tono, precisión de datos y lineamientos de Campuslands AI Academy. |
| 5 | **VIRA Scout** | `vira-scout.md` | `vira-scout.toml` | Investigación de mercado y tendencias. Diseñado para ejecutarse 1-2 veces por semana de forma autónoma, recolectando información del ecosistema IA/tecnología para alimentar la creación de contenido. |
| 6 | **VIRA Memory Analytics** | `vira-memory-analytics.md` | `vira-memory-analytics.toml` | Análisis de rendimiento histórico. Procesa los logs almacenados en `context/memory-log.md` para identificar patrones, métricas de satisfacción y oportunidades de mejora continua. |

### Tabla de Enrutamiento

| Tipo de Solicitud | Agente Asignado |
|---|---|
| Post, carrusel, guion, CTA, variantes, calendario, campaña o evento | VIRA AI Orquestador |
| Tendencias, noticias, competencia o research de mercado | VIRA Scout |
| Validar una pieza externa o auditar contenido ya creado | VIRA QA |
| Analizar memoria, rendimiento, patrones o estrategia histórica | VIRA Memory Analytics |
| Generar imagen, banner, portada, asset visual o prompt visual | VIRA IMG |
| Editar video, cortar, transcribir, subtítulos, Reels, TikTok, YouTube | VIRA Video Editor |

---

## 📂 Estructura de Carpetas

```text
Agente AI - Claude/
├── .claude/                          # Configuración específica para Claude
│   ├── agents/                       # Definiciones de agentes (formato .md)
│   │   ├── vira-ai-orquestador.md
│   │   ├── vira-img.md
│   │   ├── vira-memory-analytics.md
│   │   ├── vira-qa.md
│   │   ├── vira-scout.md
│   │   └── vira-video-editor.md
│   ├── agent-memory/                 # Memoria persistente por agente
│   │   ├── vira-ai-orquestador/
│   │   ├── vira-img/
│   │   ├── vira-memory-analytics/
│   │   ├── vira-qa/
│   │   ├── vira-scout/
│   │   └── vira-video-editor/
│   └── settings.local.json           # Permisos y configuración de Claude
│
├── .codex/                           # Configuración específica para Codex
│   ├── agents/                       # Definiciones de agentes (formato .toml)
│   │   ├── vira-ai-orquestador.toml
│   │   ├── vira-img.toml
│   │   ├── vira-memory-analytics.toml
│   │   ├── vira-qa.toml
│   │   ├── vira-scout.toml
│   │   └── vira-video-editor.toml
│   └── agent-memory/                 # Memoria persistente por agente
│       ├── vira-ai-orquestador/
│       ├── vira-img/
│       ├── vira-memory-analytics/
│       ├── vira-qa/
│       └── vira-scout/
│
├── ai-context/                       # Archivos maestros de configuración IA
│   ├── AGENTS.md                     # Archivo maestro para Codex/general
│   ├── Claude.md                     # Archivo maestro para Claude
│   └── VIRA-AI-PROMPT-UNIVERSAL.md   # Prompt portátil para cualquier IA
│
├── context/                          # Fuente de verdad de marca y operaciones
│   ├── campuslands.md                # Perfil institucional de Campuslands
│   ├── ai-academy.md                 # Info de la división AI Academy
│   ├── audience-profiles.md          # Avatares y perfiles de audiencia
│   ├── voice-type.md                 # Voz, tono y estilo de comunicación
│   ├── instructions.md               # Guía operativa de VIRA AI
│   ├── content-strategy.md           # Estrategia de contenido (4 pilares)
│   ├── visual-style.md               # Sistema de diseño NEBULA
│   ├── video-storage-policy.md       # Política de almacenamiento de video
│   ├── memory-log.md                 # Memoria institucional activa
│   ├── memory-log-archivo-2026-Q2.md # Archivo histórico de sesiones S1-S15
│   └── img-creator/                  # Assets visuales oficiales
│       ├── ai-academy.png            # Imagen base oficial del sistema visual
│       ├── ia-academy-logo.png       # Logo oficial para renders
│       ├── ia-academy.jpg            # Variantes de imagen de referencia
│       ├── ia-academy1.jpg
│       ├── ia-academy2.jpg
│       ├── ia-academy3.jpg
│       └── brand-logos/              # Logos oficiales de marca
│
├── skills/                           # 19 habilidades modulares
│   ├── ab-variant-creator/           # Creación de variantes A/B de contenido
│   ├── brand-voice-enforcer/         # Validación de voz de marca
│   ├── carousel-builder/             # Constructor de carruseles
│   ├── competitor-monitor/           # Monitoreo de competencia
│   ├── content-calendar-planner/     # Planificador de calendario editorial
│   ├── cta-generator/                # Generador de Call-To-Action
│   ├── document-exporter/            # Exportador de documentos (md, pdf, docx)
│   ├── event-announcement/           # Anuncios de eventos
│   ├── hashtag-optimizer/            # Optimizador de hashtags
│   ├── image-generator/              # Generación de imágenes con OpenAI
│   ├── memory-manager/               # Gestión de memoria y encuestas
│   ├── newsjacking/                  # Aprovechamiento de noticias virales
│   ├── performance-analyst/          # Análisis de rendimiento
│   ├── persona-adapter/              # Adaptación por avatar/persona
│   ├── prompt-engineer/              # Ingeniería de prompts
│   ├── script-writer/                # Escritor de guiones de video
│   ├── social-post-generator/        # Generador de posts para redes
│   ├── testimonial-formatter/        # Formateador de testimonios
│   └── trend-researcher/             # Investigador de tendencias
│
├── output/                           # Entregables finales
│   ├── README.md                     # Convenciones de nomenclatura
│   ├── [YYYY-MM-DD]_[tipo]_[desc]/   # Carpetas de entregables (18+ carpetas)
│   └── videos_output/                # Videos finales aprobados
│
├── tools/                            # Scripts y herramientas internas
│   ├── README.md                     # Documentación de herramientas
│   └── flyer-generation/             # Generación automatizada de flyers
│       ├── README.md
│       ├── generate_ia_academy_flyer.py
│       └── generate_ia_academy_full_flyer.py
│
├── videos/                           # Videos fuente para edición
│   ├── README.md                     # Documentación y política
│   ├── *.mp4                         # Videos fuente originales
│   └── edit/                         # Archivos de trabajo activos
│
├── archive/                          # Material archivado
│   ├── README.md                     # Política de archivo
│   ├── video-projects/               # Proyectos de video archivados
│   └── videos_output/                # Videos finales de versiones previas
│
├── .env                              # Variables de entorno (API keys)
├── .gitignore                        # Exclusiones de Git
└── README.md                         # Este archivo
```

---

## 📄 Descripción Archivo por Archivo

### Archivos Raíz

| Archivo | Descripción |
|---------|-------------|
| **`.env`** | Variables de entorno del proyecto. Contiene la `OPENAI_API_KEY` necesaria para la generación de imágenes con OpenAI. Este archivo está excluido del repositorio mediante `.gitignore` por seguridad. |
| **`.gitignore`** | Define qué archivos no deben subirse al repositorio Git. Excluye: variables de entorno (`.env`), caché de Python (`__pycache__/`), archivos de video pesados (`.mp4`) en `videos/`, `output/videos_output/` y `archive/`, y frames intermedios de edición (`.jpg`). |
| **`README.md`** | Documentación principal del proyecto (este archivo). |

---

### ai-context/ — Configuración para IAs

Esta carpeta contiene los archivos maestros que configuran el comportamiento de VIRA AI en diferentes plataformas de IA.

| Archivo | Tamaño | Descripción |
|---------|--------|-------------|
| **`AGENTS.md`** | 7.1 KB | **Archivo maestro general** (optimizado para Codex). Define la identidad del sistema, la regla principal de ejecución de 8 pasos, el mapa de archivos del workspace, la tabla de enrutamiento de agentes, las 19 skills disponibles, las reglas globales (lo que SIEMPRE y NUNCA debe hacer VIRA AI), y el flujo de cierre de sesión. Es la fuente de verdad operativa del sistema. |
| **`Claude.md`** | 4.9 KB | **Archivo maestro para Claude**. Réplica adaptada de `AGENTS.md` para ejecuciones en el entorno Claude. Si hay conflicto entre archivos, se aplica la regla más reciente de este documento. Mantiene sincronización con `AGENTS.md`. |
| **`VIRA-AI-PROMPT-UNIVERSAL.md`** | 36.3 KB | **Prompt portátil completo**. Versión autocontenida del Agente Orquestador que puede pegarse como system prompt en cualquier IA compatible. Incluye todo el conocimiento institucional, estrategia, perfiles de audiencia, reglas y capacidades en un solo bloque. Útil cuando la IA no reconoce el repositorio. |

---

### context/ — Contexto de Marca

Esta es la **fuente de verdad** del proyecto. Contiene toda la información institucional, estratégica y de marca que VIRA AI debe consultar antes de generar cualquier contenido.

| Archivo | Tamaño | Descripción |
|---------|--------|-------------|
| **`campuslands.md`** | 6.1 KB | **Perfil institucional de Campuslands**. Ficha técnica completa: nombre legal (CAMPUS LANDS S.A.S. BIC), fundación (2021, Bucaramanga), CEO (Diego Tarazona), sedes activas (Bucaramanga, Puerta del Sol, Bogotá, Cúcuta), expansión internacional (Guatemala), misión, visión, datos verificados de estudiantes, alianzas y logros. Único archivo autorizado para cifras institucionales. |
| **`ai-academy.md`** | 6.1 KB | **Información de AI Academy**. Detalla la división de IA de Campuslands: programas formativos (Masterclasses de IA Generativa, Machine Learning, Computer Vision), oferta educativa, enfoque pedagógico, público objetivo y propuesta de valor. Define el alcance operativo de VIRA AI. |
| **`audience-profiles.md`** | 5.9 KB | **Perfiles de audiencia (3 avatares)**. Define con precisión psicológica los tres públicos objetivo: **El Camper** (18-28 años, estratos 1-3, buscando primer empleo tech), **El Profesional** (profesionales buscando upskilling en IA), y **El Educador/Empresario** (instituciones y empresas). Incluye pain points, motivaciones, plataformas preferidas y promesas centrales por avatar. |
| **`voice-type.md`** | 5.6 KB | **Voz, tono y estilo**. Guía de los 5 atributos de personalidad de marca: Inspirador, Cercano, Experto, Optimista e Inclusivo. Define niveles de formalidad por plataforma, vocabulario permitido y prohibido, manejo de emojis, estructuras de copy y reglas de adaptación tonal. |
| **`instructions.md`** | 7.2 KB | **Guía operativa de VIRA AI**. Principios operativos fundamentales: foco absoluto en marketing, investigación autónoma de tendencias, psicología persuasiva (prueba social, escasez, autoridad, reciprocidad, identificación emocional), y reglas de ejecución. |
| **`content-strategy.md`** | 5.8 KB | **Estrategia de contenido**. Define los 4 pilares de contenido: Educativo (40%), Inspiracional (25%), Promocional (25%) y Comunidad (10%). Incluye distribución por plataforma, tipos de contenido por pilar, y principios estratégicos de publicación. |
| **`visual-style.md`** | 10.4 KB | **Sistema de diseño NEBULA**. Fuente de verdad visual completa: paleta de colores (gradientes neón, fondos oscuros), tipografía, composición, estilos fotográficos, reglas de uso de logo, tratamiento de imágenes, y especificaciones técnicas por formato (feed, stories, carrusel). Optimizado para generación con OpenAI/ChatGPT Images. |
| **`video-storage-policy.md`** | 2.6 KB | **Política de almacenamiento de video**. Define las reglas de dónde guardar cada tipo de archivo de video: fuentes originales en `videos/`, finales aprobados en `output/videos_output/`, intermedios en `archive/`. Documenta las rutas permitidas para el toolchain externo de VIRA Video Editor (FFmpeg, `video-use`). |
| **`memory-log.md`** | 13.2 KB | **Memoria institucional activa**. Sistema de aprendizaje continuo donde VIRA AI registra al final de cada sesión: tipo de contenido, calificación del usuario (1-5), aprendizajes y áreas de mejora. Las sesiones S1-S15 están archivadas. Incluye template estandarizado para nuevas entradas. |
| **`memory-log-archivo-2026-Q2.md`** | 9.6 KB | **Archivo histórico Q2 2026**. Contiene las sesiones S1 a S15 archivadas desde el memory-log principal. Se consulta solo para auditorías de VIRA Memory Analytics. |

#### context/img-creator/ — Assets Visuales

| Archivo | Tamaño | Descripción |
|---------|--------|-------------|
| **`ai-academy.png`** | 1.5 MB | Imagen base oficial del sistema visual NEBULA. Fuente primaria de referencia para toda generación de imágenes. |
| **`ia-academy-logo.png`** | 87.7 KB | Logo oficial de AI Academy. Usado en renders de video y como watermark en assets visuales. |
| **`ia-academy.jpg`** | 211 KB | Imagen de referencia variante 1 de AI Academy. |
| **`ia-academy1.jpg`** | 145.9 KB | Imagen de referencia variante 2. |
| **`ia-academy2.jpg`** | 176.6 KB | Imagen de referencia variante 3. |
| **`ia-academy3.jpg`** | 186.1 KB | Imagen de referencia variante 4. |
| **`brand-logos/`** | directorio | Carpeta con logos oficiales de Campuslands y AI Academy en diversos formatos. |

---

### skills/ — Habilidades Modulares

Cada skill es una carpeta que contiene al menos un archivo `SKILL.md` con las instrucciones que el agente debe seguir para ejecutar esa habilidad específica. Son módulos reutilizables que los agentes invocan según la petición.

| Skill | Descripción | Agente(s) que la usa(n) |
|-------|-------------|------------------------|
| **`social-post-generator`** | Genera publicaciones optimizadas para redes sociales (Instagram, LinkedIn, Twitter/X, TikTok). Adapta formato, tono y hashtags según la plataforma destino. | Orquestador |
| **`script-writer`** | Escribe guiones de video estructurados con hook, desarrollo y CTA. Soporta formatos cortos (Reels/TikTok) y largos (YouTube). | Orquestador |
| **`carousel-builder`** | Construye carruseles educativos o promocionales con estructura de slides, texto por lámina y narrativa progresiva. | Orquestador |
| **`content-calendar-planner`** | Planifica parrillas de contenido semanales o mensuales, distribuyendo publicaciones según los 4 pilares de la estrategia. | Orquestador |
| **`event-announcement`** | Crea anuncios de eventos (masterclasses, workshops, webinars) con toda la información logística y copy persuasivo. | Orquestador |
| **`ab-variant-creator`** | Genera variantes A/B de cualquier pieza de contenido para testing de copy, CTAs o enfoques diferentes. | Orquestador |
| **`persona-adapter`** | Adapta contenido existente al tono, vocabulario y motivadores específicos de cada avatar de audiencia. | Orquestador |
| **`hashtag-optimizer`** | Selecciona y optimiza hashtags por plataforma, combinando alta visibilidad con relevancia de nicho. | Orquestador |
| **`cta-generator`** | Genera Call-To-Action efectivos usando principios de psicología persuasiva adaptados al avatar. | Orquestador |
| **`trend-researcher`** | Investiga tendencias actuales en IA, tecnología y educación tech en redes sociales y medios especializados. | Scout |
| **`newsjacking`** | Identifica noticias virales o trending topics y los convierte en oportunidades de contenido alineado con la marca. | Scout |
| **`competitor-monitor`** | Monitorea la actividad de competidores directos e indirectos en el espacio de educación tech/IA. | Scout |
| **`brand-voice-enforcer`** | Valida que cualquier pieza de contenido cumpla con la voz, tono y lineamientos de marca definidos. Se ejecuta como paso obligatorio antes de entregar contenido final. | QA, Orquestador |
| **`document-exporter`** | Exporta entregables en múltiples formatos (`.md`, `.pdf`, `.docx`, `.txt`, `.xlsx`) y los guarda en la estructura de carpetas estandarizada de `output/`. | Todos |
| **`memory-manager`** | Gestiona la encuesta de satisfacción (calificación 1-5), procesa retroalimentación y registra la sesión en `context/memory-log.md`. | Todos |
| **`performance-analyst`** | Analiza métricas históricas de rendimiento de contenido, identifica patrones de éxito y oportunidades de mejora. | Memory Analytics |
| **`testimonial-formatter`** | Formatea testimonios de estudiantes y egresados en piezas de contenido verificadas y publicables. | Orquestador |
| **`prompt-engineer`** | Diseña y optimiza prompts para diferentes casos de uso, incluyendo prompts visuales para generación de imágenes. | Orquestador, IMG |
| **`image-generator`** | Orquesta la generación de imágenes usando la API de OpenAI/ChatGPT Images. Define parámetros técnicos, prompts en inglés y el flujo de guardado con ficha técnica. | IMG |

---

### .claude/ — Configuración Claude

| Archivo / Carpeta | Descripción |
|--------------------|-------------|
| **`settings.local.json`** | Permisos y configuración local de Claude. Define comandos permitidos (FFmpeg, Git, npm, etc.), acceso a APIs, integraciones MCP (OpenAI), y permisos de lectura/escritura web. |
| **`agents/`** | Contiene las definiciones de los 6 agentes en formato Markdown (`.md`), optimizadas para el entorno Claude. |
| **`agent-memory/`** | Directorio de memoria persistente local. Contiene una subcarpeta por cada agente donde se almacenan logs complementarios de sesión, aprendizajes específicos del agente y contexto acumulado. |

---

### .codex/ — Configuración Codex

| Archivo / Carpeta | Descripción |
|--------------------|-------------|
| **`agents/`** | Contiene las definiciones de los 6 agentes en formato TOML (`.toml`), optimizadas para el entorno Codex (OpenAI). Nota: Codex no tiene archivo de definición de VIRA Video Editor tan detallado como Claude. |
| **`agent-memory/`** | Directorio de memoria persistente local para Codex. Contiene subcarpetas para 5 agentes (VIRA Video Editor no tiene carpeta de memoria en Codex). |

---

### output/ — Entregables

Carpeta donde se guardan todos los resultados finales generados por VIRA AI.

| Elemento | Descripción |
|----------|-------------|
| **`README.md`** | Documenta la convención de nombres: `output/[YYYY-MM-DD]_[tipo]_[descripcion-clara]/contenido.md`. Define qué puede y qué no puede guardarse aquí. |
| **`videos_output/`** | Subcarpeta exclusiva para videos finales exportados y aprobados. No debe contener renders intermedios. |
| **Carpetas de entregables** | Actualmente contiene **18+ carpetas** de entregables generados, incluyendo: flyers, posts multicanal, parrillas de contenido, validaciones QA, ediciones de video y prompts. Cada carpeta sigue el formato `YYYY-MM-DD_tipo_descripcion/`. |

**Ejemplos de entregables generados:**
- `2026-06-24_parrilla_julio-2026/` — Parrilla de contenido para julio 2026
- `2026-06-24_posts-multicanal_ia-academy-promocional/` — Posts promocionales multicanal
- `2026-06-30_video_promptengineering-youtube-horizontal/` — Edición de video para YouTube
- `2026-08-01_parrilla_agosto-2026/` — Parrilla de contenido para agosto 2026

---

### tools/ — Herramientas y Scripts

Scripts internos reutilizables que automatizan procesos de generación de assets.

| Archivo | Descripción |
|---------|-------------|
| **`README.md`** | Documentación y reglas de la carpeta. Los scripts viven aquí, los resultados van a `output/`. |
| **`flyer-generation/`** | Herramienta de generación automatizada de flyers para AI Academy. |
| **`flyer-generation/generate_ia_academy_flyer.py`** | Script Python para generar flyers básicos de AI Academy con diseño programático. |
| **`flyer-generation/generate_ia_academy_full_flyer.py`** | Script Python para generar flyers completos con más elementos visuales y contenido expandido. |

> ⚠️ **Nota**: Esta carpeta es utilizada principalmente por Codex, ya que tiene capacidad de ejecución de scripts Python.

---

### videos/ — Material Audiovisual

Carpeta para videos fuente y proyectos activos de edición, exclusiva para VIRA Video Editor.

| Archivo | Tamaño | Descripción |
|---------|--------|-------------|
| **`README.md`** | 742 B | Documentación de contenido vigente y reglas de orden. |
| **`PromptEngineering Video 10 Cam.mp4`** | 720.9 MB | Video fuente de cámara del episodio 10 de Prompt Engineering. |
| **`PromptEngineering Video 10 Pantalla.mp4`** | 451.3 MB | Video fuente de pantalla/screencast del episodio 10. |
| **`VideoBase_SinEditar.mp4`** | 290.6 MB | Video fuente adicional sin editar. |
| **`edit/`** | directorio | Archivos de trabajo del proyecto de edición actual (transcripciones, EDL, scripts de build, subtítulos). |

---

### archive/ — Material Archivado

Material antiguo, versiones previas y archivos intermedios que se conservan por trazabilidad.

| Elemento | Descripción |
|----------|-------------|
| **`README.md`** | Política de archivo: qué va y qué no va aquí. |
| **`video-projects/`** | Proyectos de video archivados con renders intermedios y sesiones previas. |
| **`videos_output/`** | Videos finales de versiones anteriores que ya no son la entrega vigente. |

---

## 🔄 Flujo de Trabajo

Toda sesión de VIRA AI sigue un flujo de **8 pasos fijos** en orden estricto:

```
┌──────────────────────────────────────────────────────────┐
│ PASO 1 │ Petición del usuario                            │
├──────────────────────────────────────────────────────────┤
│ PASO 2 │ Carga de contexto → Identificación de agente    │
│        │ y skills → Generación del entregable →          │
│        │ Validación con brand-voice-enforcer              │
├──────────────────────────────────────────────────────────┤
│ PASO 3 │ document-exporter guarda contenido.md en        │
│        │ output/[fecha]_[tipo]_[desc]/ y pregunta        │
│        │ si desea formato adicional                       │
├──────────────────────────────────────────────────────────┤
│ PASO 4 │ Usuario indica formato deseado o confirma       │
├──────────────────────────────────────────────────────────┤
│ PASO 5 │ Entrega del archivo en formato solicitado       │
│        │ y confirmación de ruta                           │
├──────────────────────────────────────────────────────────┤
│ PASO 6 │ Encuesta de satisfacción (1-5) de               │
│        │ memory-manager                                   │
├──────────────────────────────────────────────────────────┤
│ PASO 7 │ Usuario califica y comenta                      │
├──────────────────────────────────────────────────────────┤
│ PASO 8 │ Registro de sesión en context/memory-log.md     │
│        │ con aprendizajes y retroalimentación             │
└──────────────────────────────────────────────────────────┘
```

---

## 🧠 Sistema de Memoria

VIRA AI cuenta con un sistema de memoria de **3 capas**:

| Capa | Ubicación | Propósito |
|------|-----------|-----------|
| **Memoria Institucional** (canónica) | `context/memory-log.md` | Fuente de verdad. Registro centralizado de todas las sesiones, calificaciones y aprendizajes. Se lee al inicio de cada sesión. |
| **Memoria de Agente (Claude)** | `.claude/agent-memory/[agente]/` | Memoria local complementaria por agente. Almacena contexto específico y patrones de cada agente en el entorno Claude. |
| **Memoria de Agente (Codex)** | `.codex/agent-memory/[agente]/` | Equivalente para el entorno Codex. |
| **Archivo Histórico** | `context/memory-log-archivo-*.md` | Sesiones archivadas para reducir el tamaño del log activo. Solo se consulta en auditorías. |

---

## 🖥️ Plataformas Compatibles

| Plataforma | Formato de Agentes | Uso Principal |
|------------|---------------------|---------------|
| **Claude (Anthropic)** | `.md` (Markdown) | Generación de contenido, QA, investigación, análisis, edición de video |
| **Codex (OpenAI)** | `.toml` | Generación de contenido, ejecución de scripts Python, generación de flyers |
| **Cualquier IA** | Prompt Universal | Usando `ai-context/VIRA-AI-PROMPT-UNIVERSAL.md` como system prompt |

---

## ⚙️ Requisitos Técnicos

| Requisito | Detalle |
|-----------|---------|
| **API Key de OpenAI** | Configurada en `.env` como `OPENAI_API_KEY`. Necesaria para generación de imágenes. |
| **FFmpeg** | Instalado localmente. Requerido por VIRA Video Editor para procesamiento de video. |
| **Git** | Para control de versiones del workspace. |
| **Python** | Para ejecución de scripts en `tools/` (generación de flyers). |
| **video-use** | Repositorio externo (`github.com/browser-use/video-use`) clonado en la ruta definida en `$env:VIDEO_USE_DIR`. Ver `SETUP.md` para instrucciones de instalación. |

---

## 🚧 Qué Falta por Mejorar

### 🔴 Prioridad Alta

| Área | Descripción del Problema | Estado Actual |
|------|--------------------------|---------------|
| **VIRA IMG — API Key sin créditos** | La generación de imágenes vía API de OpenAI no funciona porque no se han cargado créditos en la cuenta asociada a la API Key. Actualmente solo funciona mediante Codex (que usa su propia cuota). | ❌ No operativo vía API directa |
| **VIRA Scout — Automatización** | Está diseñado para ejecutarse automáticamente 1-2 veces por semana, pero la automatización programada (cron/scheduler) no está implementada. Se ejecuta solo de forma manual. | ⚠️ Solo manual |
| **Exportación a PDF/DOCX** | El `document-exporter` ofrece exportar a `.pdf`, `.docx`, `.txt` y `.xlsx`, pero la implementación real de conversión de formatos no está completamente validada en todos los entornos. | ⚠️ Parcialmente funcional |

### 🟡 Prioridad Media

| Área | Descripción del Problema | Estado Actual |
|------|--------------------------|---------------|
| **Dashboard de Métricas** | No existe un dashboard visual para ver las métricas acumuladas de `memory-log.md` (calificaciones, tendencias, rendimiento por agente). Todo se analiza manualmente o vía VIRA Memory Analytics en texto. | ❌ No existe |
| **Integración directa con redes sociales** | VIRA AI genera el contenido listo para publicar, pero no tiene integración directa con APIs de Instagram, LinkedIn, TikTok o Twitter/X para publicación automática. | ❌ No existe |
| **Sincronización AGENTS.md ↔ Claude.md** | Los archivos maestros deben mantenerse sincronizados manualmente. No hay un mecanismo automático para detectar discrepancias entre ambos archivos. | ⚠️ Manual |
| **VIRA Video Editor en Codex** | El archivo de configuración de VIRA Video Editor en Codex (`vira-video-editor.toml`, 4.5 KB) es significativamente más pequeño que su contraparte en Claude (`vira-video-editor.md`, 51.9 KB), sugiriendo que la funcionalidad de edición de video no está completamente portada al entorno Codex. | ⚠️ Incompleto |
| **Memoria de Codex para Video Editor** | VIRA Video Editor no tiene carpeta de `agent-memory` en `.codex/`, a diferencia de Claude donde sí existe. | ❌ Faltante |

### 🟢 Prioridad Baja (Mejoras Deseables)

| Área | Descripción del Problema | Estado Actual |
|------|--------------------------|---------------|
| **Testing automatizado** | No existen tests automatizados para validar que los skills generen output correcto, que los agentes se enruten bien, o que los archivos de contexto sean consistentes. | ❌ No existe |
| **Versionamiento de Skills** | Las skills no tienen control de versión individual. Si una skill se modifica, no hay forma de rastrear qué cambió ni revertir a una versión anterior (más allá de Git). | ❌ No existe |
| **Documentación de Skills** | Cada skill tiene un `SKILL.md` interno, pero no hay una documentación unificada que explique los parámetros, inputs esperados y outputs de cada skill de forma estandarizada. | ⚠️ Parcial |
| **Soporte multiidioma** | VIRA AI opera exclusivamente en español colombiano. No hay soporte para generar contenido en otros idiomas o adaptar el tono para audiencias internacionales (ej. Guatemala). | ❌ No existe |
| **Rotación automática del memory-log** | El archivado de sesiones del `memory-log.md` al archivo histórico se hace manualmente. Debería automatizarse cuando el log supere cierto tamaño. | ❌ Manual |
| **Assets visuales dinámicos** | Los assets en `context/img-creator/` son estáticos. No hay un sistema para actualizar automáticamente las imágenes de referencia cuando cambie la identidad visual. | ❌ Estático |
| **Métricas de competencia** | `competitor-monitor` puede investigar competidores, pero no hay un repositorio estructurado para almacenar y comparar datos de competencia a lo largo del tiempo. | ❌ No existe |
| **Pipeline CI/CD** | No hay integración continua para validar la estructura del proyecto, la consistencia de archivos o la integridad de los links entre documentos. | ❌ No existe |

---

## 📜 Licencia

Proyecto interno de **Campuslands AI Academy**. Uso exclusivo del equipo de marketing de IA.

---

## 👨‍💻 Autor

Desarrollado por Gustavo Navarro.

---

> *"Formar sin migrar"* — Campuslands AI Academy 🇨🇴

