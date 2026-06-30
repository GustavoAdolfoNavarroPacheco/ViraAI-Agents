---
name: visual-style-nebula
description: Sistema visual NEBULA de Campuslands AI Academy, actualizado desde la imagen base oficial `context/img-creator/ai-academy.png` y optimizado para OpenAI / ChatGPT Images.
---

# Sistema De Diseño NEBULA - Campuslands AI Academy

> Fuente de verdad visual para VIRA IMG, `image-generator` y cualquier entregable grafico de Campuslands AI Academy.
> Esta version prioriza la imagen base oficial `context/img-creator/ai-academy.png`.

---

## 0. Regla De Generacion Visual

Toda generacion de imagenes del proyecto debe operar solamente con **OpenAI / ChatGPT Images**.

- Skill operativa: `skills/image-generator/SKILL.md`
- Prompts: siempre en ingles
- Texto dentro de imagen: evitarlo por defecto; el equipo agrega texto final en Canva
- Guardado: cada asset debe ir en carpeta propia dentro de `output/[YYYY-MM-DD]_imagen_[descripcion]/`
- Ficha: siempre guardar `contenido.md` con prompt, modelo, uso, ruta del archivo y notas de evaluacion

No usar ni recomendar proveedores alternativos en instrucciones vigentes.

---

## 1. Logo

**Archivos oficiales:**

- `context/img-creator/ia-academy-logo.png`
- `context/img-creator/ia-academy-logo.jpg`

**Lectura visual vigente:**

El logo usado en piezas actuales combina un isotipo tipo casco/astronauta en trazo blanco con el wordmark `campuslands IA ACADEMY`. La version principal funciona sobre fondos oscuros.

**Reglas:**

| Regla | Aplicacion |
|---|---|
| Posicion | Esquina superior izquierda o franja superior cuando el diseño requiere header |
| Color | Blanco sobre fondo oscuro; navy profundo sobre fondo claro si aplica |
| Zona segura | Minimo 5% de margen alrededor |
| Generacion | En imagenes generadas, reservar zona limpia; no intentar recrear el logo salvo brief explicito |
| Composicion | Si la pieza incluye header, usar contenedor oscuro con borde fino claro/neon |

**Bloque de prompt para reservar logo:**

```text
top-left area reserved for the official Campuslands AI Academy logo, clean dark empty space, no text, no symbols, no faces, no bright particles competing with the logo zone
```

---

## 2. Identidad Visual

**Nombre del sistema:** NEBULA
**Descriptor oficial (del documento de marca):** HUD CÓSMICO — identidad visual para infografías y piezas gráficas.

**Concepto oficial:** tecnologia aplicada, claridad, sofisticacion accesible.

**Sensacion objetivo:** futurista, clara, humana, educativa, sofisticada y memorable. Debe sentirse tech sin verse frio, corporativo generico ni de stock.

---

## 3. Paleta Oficial Observada En `ai-academy.png`

| Nombre | Hex | Uso principal |
|---|---|---|
| Fondo Abismo | `#0B0826` | Fondo base oscuro, espacio profundo, paneles principales |
| Marca | `#A239CA` | Titulares acento, glow magenta/violeta, energia visual |
| Datos / HUD | `#5FB4F4` | Lineas HUD, indicadores, barras, elementos de interfaz |
| Violeta Puente | `#9A8CF2` | Gradientes, tarjetas glass, bordes suaves |
| Teal | `#6FD6E0` | Conectores, acentos secundarios, nodos, lineas |
| Exito | `#56D0A8` | Confirmaciones, acentos positivos, detalles de avance |
| Blanco | `#FFFFFF` | Titulares, texto principal sobre fondo oscuro |
| Blanco Suave | `#DCE8FF` | Texto secundario, parrafos, microcopy |

### Gradientes

| Gradiente | Uso |
|---|---|
| `#9A8CF2 -> #5FB4F4 -> #A239CA` | Gradiente NEBULA principal, barras, botones, acentos hero |
| `#5FB4F4 -> #6FD6E0` | Datos/HUD, lineas tecnicas, conectores |
| `#0B0826 -> #171047` | Profundidad del fondo |
| `#A239CA` con glow | Numeros grandes, halo visual, enfasis de marca |

### Regla De Color

El fondo oscuro debe dominar. Los acentos no deben convertir la pieza en una mancha morada plana: usar magenta/violeta para foco, azul HUD para claridad, teal para tecnologia y blanco para legibilidad.

---

## 4. Tipografia

La imagen base establece esta jerarquia:

| Rol | Fuente | Peso | Uso |
|---|---|---|---|
| Titulares y cifras | Poppins | ExtraBold / Bold | H1, numeros grandes, frases de impacto |
| Texto de soporte | Poppins | Regular / Medium | Subtitulos, parrafos cortos, CTA |
| Labels y microcopy | Roboto Mono | Regular / Medium | Badges, HUD, codigos, etiquetas, metadatos |

**Reglas:**

- Titulares: Poppins Bold/ExtraBold, blanco con palabra clave en `#A239CA` o gradiente NEBULA.
- Labels: Roboto Mono en mayusculas, tracking moderado, color `#6FD6E0` o blanco.
- Cuerpo: Poppins Regular/Medium, alto contraste, maximo 2-3 lineas por bloque visual.
- Evitar fuentes serif, manuscritas o estilo corporativo tradicional.

---

## 5. Composicion

### Formatos

| Formato | Dimension base | Uso |
|---|---|---|
| Instagram Feed cuadrado | 1080 x 1080 | Posts, portadas |
| Instagram Feed portrait | 1080 x 1350 | Flyers y carruseles |
| Stories / Reels / TikTok | 1080 x 1920 | Historias, anuncios verticales |
| LinkedIn / Facebook | 1200 x 630 o 1536 x 1024 | Banners horizontales |

### Patrones NEBULA

- Fondo espacial oscuro con estrellas/puntos sutiles.
- Paneles tipo HUD/glass con bordes finos neon.
- Conectores, nodos y lineas orbitales.
- Cifra o elemento hero grande cuando la pieza es conceptual.
- Persona protagonista cuando la pieza es emocional, inspiracional o promocional.
- Espacios limpios para agregar copy en Canva.

### Layout Vertical Recomendado

1. Header con logo o zona reservada.
2. Hero visual o persona en zona superior/media.
3. Titular grande en Poppins.
4. Badges o tarjetas informativas.
5. CTA inferior en gradiente NEBULA.

---

## 6. Guia Fotografica

### Personas

- Campers: jovenes latinoamericanos de 18 a 28 años, ropa casual tech, expresion autentica, energia de avance.
- Profesionales: personas latinoamericanas de 28 a 50 años, look moderno sin traje formal, actitud de decision y aprendizaje.
- Empresas: lideres y equipos en ambientes educativos/tech, no sala de juntas generica.

### Iluminacion

- Cinematic rim light.
- Luz cian/azul desde pantalla o interfaz.
- Glow magenta/violeta como acento, no como relleno total.
- Contraste alto y rostro legible.

### Evitar

- Fotos de stock corporativas.
- Trajes, corbatas, apretones de mano.
- Robots humanoides, globos terraqueos, candados, engranajes.
- Fondos blancos planos salvo brief de variante clara.
- Texto inventado o ilegible dentro de la imagen.

---

## 7. Elementos UI

| Elemento | Estilo |
|---|---|
| Tarjetas glass | Fondo `#0B0826` con transparencia, borde `#5FB4F4` o `#9A8CF2` |
| Badges | Roboto Mono, borde neon, radio moderado |
| CTA | Gradiente `#9A8CF2 -> #5FB4F4 -> #A239CA`, texto blanco Poppins Bold |
| Conectores | Lineas finas `#6FD6E0` o `#5FB4F4` |
| Nodos | Puntos blancos/teal/azules con glow suave |
| Numeros hero | Poppins ExtraBold, glow `#A239CA` |

---

## 8. Bloques De Prompt Para ChatGPT Images

### Fondo NEBULA

```text
deep cosmic navy background #0B0826, subtle star field, refined HUD interface lines, glassmorphism panels, thin cyan and teal connectors, soft magenta-violet glow accents #A239CA, blue data highlights #5FB4F4, sophisticated futuristic education brand aesthetic
```

### Persona Camper

```text
young Latin American student, 18 to 28 years old, casual modern tech clothing, authentic confident expression, cinematic cyan screen light on face, subtle violet rim light, deep NEBULA background, hopeful and focused mood, not a stock photo
```

### Persona Profesional

```text
Latin American professional, 28 to 50 years old, modern accessible clothing, no suit and no tie, interacting with holographic AI interface, confident and curious expression, cinematic lighting, deep navy NEBULA environment, editorial quality
```

### Estilo Obligatorio

```text
Campuslands AI Academy NEBULA brand system, Poppins-inspired bold headline space, Roboto Mono HUD labels style, palette #0B0826 #A239CA #5FB4F4 #9A8CF2 #6FD6E0 #56D0A8, clean composition with empty area for Canva text overlay, premium educational technology design, human and aspirational
```

### Negativo

```text
no text, no watermark, no logo, no fake brand marks, no generic corporate stock photo, no robots, no globe icons, no padlock icons, no gears, no distorted anatomy, no blurry faces, no overexposed skin, no orange generic gradient
```

### Composicion 9:16

```text
portrait 9:16 composition, official logo area reserved at top-left, subject or hero element in upper half, lower third clean and dark for CTA and copy overlay, dynamic diagonal flow, HUD particles and connectors in background
```

### Composicion 4:5

```text
portrait 4:5 social feed composition, strong hero visual, clean margins, top-left logo safe area, readable empty zones for title and CTA, premium NEBULA HUD frame elements
```

### Composicion 16:9

```text
landscape 16:9 LinkedIn banner composition, subject on right third, clean dark copy space on left, subtle orbital lines and glass panels, professional but not corporate
```

---

## 9. Referencias Oficiales

| Archivo | Leccion |
|---|---|
| `ia-academy-logo.png` / `.jpg` | Logo oficial, uso sobre fondo oscuro |
| `ai-academy.png` | Fuente principal de paleta, tipografia y lenguaje HUD cosmico |
| `ia-academy.jpg` | Variante clara con division diagonal y tarjetas UI |
| `ia-academy1.jpg` | Patron vertical dark con persona + laptop + CTA |
| `ia-academy2.jpg` | Variante vertical dark con texto acento purpura |
| `ia-academy3.jpg` | Persona interactuando con holograma IA, tono emprendedor |

---

## 10. Criterios De Aceptacion

Una imagen pasa si cumple al menos 6 de 8:

- [ ] Usa fondo dominante `#0B0826` o variante oscura coherente.
- [ ] Aplica acentos de la paleta oficial observada.
- [ ] Reserva zona limpia para logo.
- [ ] No contiene texto generado accidentalmente.
- [ ] No contiene logos de terceros ni marcas inventadas.
- [ ] Si hay persona, se ve latinoamericana, natural y no de stock.
- [ ] Tiene espacio claro para copy/CTA en Canva.
- [ ] Se siente como tecnologia educativa premium, no ciencia ficcion generica.

---

## 11. Variantes Por Pieza

| Tipo | Direccion visual |
|---|---|
| Educativo | HUD, datos, tarjetas, diagramas abstractos |
| Inspiracional | Persona protagonista, luz humana, gesto de avance |
| Promocional | Layout con zona CTA fuerte, badges y hero visual claro |
| Evento | Version 9:16 y 16:9, espacio para fecha/hora agregada en Canva |
| Carrusel | Portada con titular grande y UI visual consistente |
| LinkedIn B2B | Mas sobrio, mas espacio negativo, menos glow |

