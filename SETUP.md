# Instalación y Configuración — VIRA AI

Guía de instalación para ejecutar todos los agentes del proyecto en cualquier máquina.

---

## Componentes del sistema

| Componente | Descripción | Obligatorio |
|---|---|---|
| **Claude Code** | CLI de Anthropic — ejecuta todos los agentes | ✅ Siempre |
| **Variables de entorno** | Rutas locales para VIRA Video Editor | ✅ Si usas Video Editor |
| **video-use** | Toolchain Python de edición de video | ✅ Si usas Video Editor |
| **uv** | Gestor de paquetes Python (ejecuta video-use) | ✅ Si usas Video Editor |
| **ffmpeg** | Procesamiento y renderizado de video | ✅ Si usas Video Editor |
| **Poppins** | Fuente tipográfica para subtítulos NEBULA | ✅ Si usas Video Editor |
| **ElevenLabs API Key** | Transcripción automática de audio | ✅ Si usas Video Editor |
| **OpenAI MCP** | Generación de imágenes (vira-img) | Para vira-img |

---

## 1. Claude Code

Instalar el CLI de Claude Code:

```bash
npm install -g @anthropic-ai/claude-code
```

Verificar instalación:

```bash
claude --version
```

Autenticarse con tu cuenta de Anthropic:

```bash
claude auth login
```

---

## 2. Variables de entorno (obligatorio para VIRA Video Editor)

VIRA Video Editor depende de dos variables de entorno que definen las rutas locales de cada máquina. Deben configurarse una sola vez como variables persistentes del usuario.

### Desde PowerShell (recomendado)

```powershell
# Ruta completa a tu clon local del repositorio video-use
[System.Environment]::SetEnvironmentVariable('VIDEO_USE_DIR', 'C:\Users\TuUsuario\Developer\video-use', 'User')

# Ruta completa a la carpeta /bin de tu instalación de ffmpeg
# (ver sección 4 — ffmpeg para obtener esta ruta)
[System.Environment]::SetEnvironmentVariable('FFMPEG_BIN_DIR', 'C:\tools\ffmpeg\bin', 'User')
```

Cerrar y reabrir PowerShell para que los cambios tomen efecto. Verificar:

```powershell
echo $env:VIDEO_USE_DIR
echo $env:FFMPEG_BIN_DIR
```

### Desde la interfaz de Windows

1. Buscar **"Variables de entorno"** en el menú de inicio
2. Clic en "Editar las variables de entorno del sistema"
3. En la sección "Variables de usuario", crear:
   - `VIDEO_USE_DIR` → ruta completa a tu clon de video-use
   - `FFMPEG_BIN_DIR` → ruta completa a la carpeta `bin` de ffmpeg

> **Nota:** `VIRA_PROJECT_DIR` se detecta automáticamente desde el directorio de trabajo al iniciar Claude Code — no requiere configuración manual.

---

## 3. video-use (toolchain de edición de video)

El agente VIRA Video Editor ejecuta scripts Python del repositorio `video-use` para transcripción, corte y renderizado.

```powershell
# Crear carpeta Developer si no existe
New-Item -ItemType Directory -Force -Path "$HOME\Developer"

# Clonar el repositorio en la ruta definida en VIDEO_USE_DIR
git clone https://github.com/browser-use/video-use $env:VIDEO_USE_DIR
```

Instalar dependencias con uv:

```powershell
cd $env:VIDEO_USE_DIR
uv sync
```

Configurar las API keys:

```powershell
# Copiar la plantilla de ejemplo
Copy-Item "$env:VIDEO_USE_DIR\.env.example" "$env:VIDEO_USE_DIR\.env"

# Editar el archivo con tu editor preferido
notepad "$env:VIDEO_USE_DIR\.env"
```

Agregar al `.env`:

```
ELEVENLABS_API_KEY=tu_clave_de_elevenlabs_aqui
```

---

## 4. uv (gestor de paquetes Python)

uv es el gestor de paquetes y entornos virtuales utilizado por video-use.

```powershell
winget install astral-sh.uv
```

O vía pip:

```bash
pip install uv
```

Verificar:

```bash
uv --version
```

---

## 5. ffmpeg

ffmpeg es el motor de procesamiento de video. Se instala vía WinGet:

```powershell
winget install Gyan.FFmpeg
```

Después de instalar, obtener la ruta exacta al binario:

```powershell
(Get-Command ffmpeg -ErrorAction SilentlyContinue).Source
```

La ruta que aparece (sin el nombre del ejecutable) es el valor que debes usar para `FFMPEG_BIN_DIR`.

Ejemplo con instalación WinGet:
```
C:\Users\TuUsuario\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-x.x.x-full_build\bin
```

Verificar que funciona:

```bash
ffmpeg -version
```

---

## 6. Fuente Poppins (subtítulos NEBULA)

Los subtítulos dinámicos del sistema NEBULA requieren la fuente **Poppins Bold** instalada en Windows.

Instalación manual:

1. Descargar **Poppins** desde [Google Fonts](https://fonts.google.com/specimen/Poppins)
2. Seleccionar y descargar los pesos: `Bold (700)` y `ExtraBold (800)`
3. Abrir los archivos `.ttf` descargados
4. Clic derecho → **"Instalar para todos los usuarios"**

Verificar instalación:

```powershell
Test-Path "C:\Windows\Fonts\Poppins-Bold.ttf"
```

> Si Poppins no está instalada, el agente cae en fallback a `Arial` y lo indica en el reporte de entrega.

---

## 7. API Keys

### ElevenLabs (transcripción de audio)

1. Crear cuenta en [elevenlabs.io](https://elevenlabs.io)
2. Ir a **Profile → API Keys** → crear nueva clave
3. Agregar al archivo `$env:VIDEO_USE_DIR\.env`:
   ```
   ELEVENLABS_API_KEY=sk-...
   ```

### OpenAI / vira-img

El agente `vira-img` usa el MCP de OpenAI integrado directamente en claude.ai. No requiere configuración adicional — solo que la integración esté habilitada en tu cuenta de Claude.

---

## Verificación final

Ejecutar en PowerShell para confirmar que todo está correctamente configurado:

```powershell
# Variables de entorno
Write-Host "VIDEO_USE_DIR:  $env:VIDEO_USE_DIR"
Write-Host "FFMPEG_BIN_DIR: $env:FFMPEG_BIN_DIR"

# Herramientas
claude --version
uv --version
ffmpeg -version

# Repositorio video-use
Test-Path "$env:VIDEO_USE_DIR\helpers\transcribe.py"
Test-Path "$env:VIDEO_USE_DIR\.env"

# Fuente Poppins
Test-Path "C:\Windows\Fonts\Poppins-Bold.ttf"
```

Todos los checks deben devolver `True` o una versión válida antes de usar VIRA Video Editor.

---

## Estructura esperada tras la instalación

```
$env:VIDEO_USE_DIR/             ← Toolchain externo (repo video-use)
├── helpers/
│   ├── transcribe.py           ← Transcripción con ElevenLabs/Whisper
│   ├── pack_transcripts.py     ← Empaquetado de tomas
│   └── render.py               ← Render con ffmpeg
├── .env                        ← API keys (ElevenLabs, etc.)
└── pyproject.toml

Agente AI - Claude/             ← Este proyecto
├── .claude/agents/             ← Definición de agentes VIRA
├── context/                    ← Contexto de marca e identidad
│   └── img-creator/            ← Logos y recursos visuales
├── skills/                     ← Skills de los agentes
├── output/                     ← Contenido generado
│   └── videos_output/          ← Videos finales
└── videos/                     ← Videos fuente y ediciones
```
