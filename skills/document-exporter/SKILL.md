---
name: document-exporter
description: Guarda el entregable final en una carpeta propia dentro de output/ y pregunta al usuario en qué formato adicional desea recibirlo. Formatos soportados: .md (default obligatorio), .pdf, .docx, .xlsx (solo datos tabulares), .txt. Se invoca después de brand-voice-enforcer y antes de la encuesta de satisfacción de memory-manager.
---

# Document Exporter

## Función

Convertir el contenido final ya validado por `brand-voice-enforcer` al formato que el equipo necesita, y guardarlo en `output/`. Siempre se ejecuta **después de la validación de marca y antes de la encuesta de satisfacción**.

## Cuándo se activa

- Al final de **cualquier sesión** de VIRA AI o sus agentes satélite
- Después de que `brand-voice-enforcer` haya validado el contenido
- Antes de ejecutar la encuesta de satisfacción y el registro final de `memory-manager`
- Cuando el usuario pide explícitamente "dame esto en PDF / Word / Excel"

## Formatos soportados

| Formato | Extensión | Cuándo usarlo | Herramienta |
|---|---|---|---|
| Markdown (default) | `.md` | Siempre disponible; ideal para edición posterior en Canva/Notion | Escritura directa |
| Texto plano | `.txt` | Copiar-pegar rápido, sin formato | Escritura directa |
| Word | `.docx` | Presentaciones internas, revisión del equipo, clientes | python-docx |
| PDF | `.pdf` | Entregables finales para aprobación, archivos de referencia | Pandoc (preferido) o fpdf2 |
| Excel | `.xlsx` | Parrillas/calendarios con estructura tabular | openpyxl |

---

## Proceso obligatorio

### Paso 1 — Crear carpeta y guardar Markdown obligatorio

Antes de preguntar formatos adicionales, crear la carpeta del entregable:

```powershell
New-Item -ItemType Directory -Force -Path "output\[YYYY-MM-DD]_[tipo]_[descripcion-clara]"
```

Guardar siempre el archivo base:

```text
output/[YYYY-MM-DD]_[tipo]_[descripcion-clara]/contenido.md
```

El `.md` es obligatorio aunque el usuario pida PDF, Word, Excel o texto plano.

### Paso 2 — Preguntar formato adicional al usuario

Después de guardar `contenido.md`, mostrar exactamente este bloque en el chat:

---
**¿En qué formato adicional deseas recibir este entregable?**

`1` · Mantener solo Markdown `.md` *(ya guardado, listo para Notion/Canva)*  
`2` · Word `.docx` *(para revisión del equipo o clientes)*  
`3` · PDF `.pdf` *(entregable final para aprobación)*  
`4` · Excel `.xlsx` *(solo para parrillas o calendarios con tabla)*  
`5` · Texto plano `.txt` *(copiar-pegar rápido)*  
`0` · No necesito formato adicional  

---

Esperar respuesta antes de proceder. Si el usuario no responde o dice "sigue", asumir opción `1` (solo Markdown).

### Paso 3 — Generar archivos adicionales

#### Opción 1 — Markdown (`.md`)

No genera archivo adicional; confirma que el `.md` ya existe:

```
✅ Guardado en: output/[carpeta]/contenido.md
```

#### Opción 2 — Word (`.docx`)

Verificar si `python-docx` está disponible, instalarlo si no está, y ejecutar:

```python
# Guardar como script temporal y ejecutar
import subprocess, sys

# Instalar si no está disponible
subprocess.run([sys.executable, "-m", "pip", "install", "python-docx", "-q"], check=True)

from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
import re

doc = Document()

# Estilo base
style = doc.styles['Normal']
style.font.name = 'Calibri'
style.font.size = Pt(11)

# Título del documento
titulo = doc.add_heading('[TÍTULO DEL ENTREGABLE]', 0)
titulo.runs[0].font.color.rgb = RGBColor(0x3D, 0x37, 0xEF)  # Azul NEBULA

# Agregar contenido (procesar markdown básico)
# [El agente inserta el contenido del entregable aquí, parseando ## como headings, ** como bold, etc.]

doc.save('output/[carpeta]/contenido.docx')
print("Guardado en: output/[carpeta]/contenido.docx")
```

> El agente adapta este script al contenido específico del entregable antes de ejecutarlo.

#### Opción 3 — PDF (`.pdf`)

**Método A — Pandoc (verificar primero):**

```powershell
# Verificar si pandoc está disponible
$pandoc = Get-Command pandoc -ErrorAction SilentlyContinue
if ($pandoc) {
    pandoc "output\[carpeta]\contenido.md" -o "output\[carpeta]\contenido.pdf" --pdf-engine=xelatex -V geometry:margin=2cm
    Write-Host "PDF generado con Pandoc: output/[carpeta]/contenido.pdf"
}
```

**Método B — Python fpdf2 (fallback si no hay Pandoc):**

```python
import subprocess, sys
subprocess.run([sys.executable, "-m", "pip", "install", "fpdf2", "-q"], check=True)

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Helvetica", size=11)

# Título
pdf.set_font("Helvetica", "B", 18)
pdf.set_text_color(61, 55, 239)  # Azul NEBULA #3D37EF
pdf.cell(0, 12, "[TÍTULO DEL ENTREGABLE]", ln=True)
pdf.ln(4)

# Contenido
pdf.set_font("Helvetica", size=11)
pdf.set_text_color(0, 0, 0)
# [El agente inserta el contenido aquí, línea por línea]

pdf.output("output/[carpeta]/contenido.pdf")
print("Guardado en: output/[carpeta]/contenido.pdf")
```

#### Opción 4 — Excel (`.xlsx`)

Solo disponible cuando el entregable tiene estructura tabular (parrilla de contenido, calendario, tabla de análisis).

```python
import subprocess, sys
subprocess.run([sys.executable, "-m", "pip", "install", "openpyxl", "-q"], check=True)

import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()
ws = wb.active
ws.title = "[Nombre del entregable]"

# Colores NEBULA
COLOR_HEADER = "3D37EF"   # Azul eléctrico
COLOR_SUBHEADER = "5040A8" # Púrpura
COLOR_TEXT = "080B2A"      # Fondo abismo (para texto oscuro en celdas claras)
COLOR_ACCENT = "00D4FF"    # Cian neón

# Encabezado
header_font = Font(name="Calibri", bold=True, color="FFFFFF", size=12)
header_fill = PatternFill("solid", fgColor=COLOR_HEADER)

# [El agente construye la tabla según la estructura del entregable específico]
# Ejemplo para parrilla: Fecha | Día | Red Social | Tipo | Pilar | Tema | Avatar | Hora

wb.save("output/[carpeta]/contenido.xlsx")
print("Guardado en: output/[carpeta]/contenido.xlsx")
```

#### Opción 5 — Texto plano (`.txt`)

```powershell
# Convertir el .md a .txt eliminando sintaxis markdown
$content = Get-Content "output\[carpeta]\contenido.md" -Raw
$content = $content -replace '#+ ', '' -replace '\*\*', '' -replace '\*', '' -replace '`', ''
Set-Content "output\[carpeta]\contenido.txt" $content -Encoding UTF8
Write-Host "Guardado en: output/[carpeta]/contenido.txt"
```

### Paso 4 — Confirmar entrega

Después de generar los archivos, mostrar en el chat:

```
✅ Entregable guardado en:
   📁 output/[YYYY-MM-DD]_[tipo]_[descripcion-clara]/
       📄 contenido.md
       📄 contenido.pdf   ← (solo si se generó)
       📄 contenido.docx  ← (solo si se generó)
```

---

## Estructura de carpetas en output/

Cada entregable se guarda en su **propia carpeta** dentro de `output/`. Nunca se depositan archivos sueltos directamente en `output/`.

### Patrón de nombre de carpeta

```
output/[YYYY-MM-DD]_[tipo]_[descripcion-clara]/
```

| Segmento | Regla |
|---|---|
| `YYYY-MM-DD` | Fecha ISO — permite orden cronológico automático |
| `[tipo]` | Categoría del entregable (ver tabla de tipos) |
| `[descripcion-clara]` | 3–5 palabras en kebab-case que describan el contenido específico, no el formato |

### Tabla de tipos oficiales

| Tipo en carpeta | Cuándo usarlo |
|---|---|
| `post` | Un post para una sola red social |
| `posts-multicanal` | Posts para 2 o más redes en la misma sesión |
| `ab-test` | Variantes A/B/C de cualquier pieza |
| `guion` | Guion de reel, TikTok o video |
| `carrusel` | Carrusel de diapositivas |
| `calendario` | Calendario editorial mensual o semanal |
| `parrilla` | Parrilla de contenido en formato tabla/Excel |
| `evento` | Flujo de anuncio D-7/D-3/D-1/día/post-evento |
| `formato-informativo` | Comunicado para WhatsApp, email o pantalla |
| `informe-tendencias` | Research brief de VIRA Scout |
| `validacion` | Reporte de validación de VIRA QA |
| `reporte-analytics` | Análisis de VIRA Memory/Analytics |
| `prompt-imagen` | Prompt para generación de imagen o video |
| `campaña` | Paquete mixto que no encaja en un solo tipo |

### Archivos dentro de la carpeta

Dentro de cada carpeta, los archivos se llaman siempre igual independientemente del tipo de entregable:

```
output/[carpeta]/
    contenido.md      ← siempre presente (guardado automático)
    contenido.pdf     ← si el usuario eligió opción 3
    contenido.docx    ← si el usuario eligió opción 2
    contenido.xlsx    ← si el usuario eligió opción 4
    contenido.txt     ← si el usuario eligió opción 5
```

### Ejemplos de estructura correcta

```
output/
├── 2026-06-24_posts-multicanal_ia-academy-todos-los-canales/
│   ├── contenido.md
│   └── contenido.pdf
├── 2026-06-24_ab-test_linkedin-avatar2-masterclass-ia-generativa/
│   └── contenido.md
├── 2026-07-01_calendario_editorial-julio-2026/
│   ├── contenido.md
│   └── contenido.xlsx
└── 2026-07-03_guion_reel-machine-learning-camper/
    └── contenido.md
```

### Cómo construir el nombre de carpeta

1. Toma la fecha actual en formato `YYYY-MM-DD`.
2. Elige el tipo de la tabla anterior.
3. Para la descripción, usa las palabras clave del contenido — no del formato:
   - MAL: `post_instagram_md` (describe el formato, no el contenido)
   - MAL: `contenido_marketing_general` (demasiado vago)
   - BIEN: `avatar2-masterclass-ia-generativa` (describe qué y para quién)
   - BIEN: `linkedin-empresas-soberania-tecnologica` (canal + avatar + ángulo)
   - BIEN: `julio-2026-todos-los-canales` (período + alcance)

---

## Restricciones

- **Nunca omitir la pregunta de formato adicional** después de guardar `contenido.md`
- **El `.md` siempre se guarda primero** independientemente del formato adicional elegido
- **Nunca guardar archivos sueltos directamente en `output/`**
- **Sin instalar librerías de terceros con acceso a internet** durante la generación salvo pip (python-docx, fpdf2, openpyxl son librerías estándar de producción de documentos)
- **Sin subir archivos a servicios externos** — todo se guarda localmente en `output/`
- **Si la conversión falla**, entregar el `.md` y explicar el error con el comando exacto que falló

---

## Conexión con otras skills

| Skill/Agente | Relación |
|---|---|
| `brand-voice-enforcer` | Se ejecuta ANTES — el contenido ya viene validado |
| `memory-manager` | Se ejecuta DESPUÉS — primero exportar, luego encuesta de satisfacción y registro de la sesión |
| Todos los agentes VIRA | Cada agente llama esta skill como penúltimo paso (antes de memory-manager) |
