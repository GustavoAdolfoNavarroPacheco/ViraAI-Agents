from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math


ROOT = Path(r"C:\Users\adolf\OneDrive\Documents\Agente AI - Claude")
OUT = ROOT / "output" / "flyer-completo-ia-academy-2026-06-25.png"
LOGO = ROOT / "context" / "img-creator" / "ia-academy-logo.png"
HERO = ROOT / "output" / "ia-academy-hero-2026-06-24.png"

W, H = 1080, 1920

FONT_REG = r"C:\Windows\Fonts\Roboto-Regular.ttf"
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
FONT_BODY = r"C:\Windows\Fonts\arial.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


F_TITLE = font(FONT_BOLD, 68)
F_SUB = font(FONT_BOLD, 44)
F_H2 = font(FONT_BOLD, 31)
F_H3 = font(FONT_BOLD, 24)
F_BODY = font(FONT_BODY, 22)
F_BODY_SM = font(FONT_BODY, 19)
F_LABEL = font(FONT_BOLD, 18)
F_CTA = font(FONT_BOLD, 29)
F_MICRO = font(FONT_REG, 16)


def rgb(hex_value):
    hex_value = hex_value.lstrip("#")
    return tuple(int(hex_value[i:i + 2], 16) for i in (0, 2, 4))


NAVY = rgb("#080B2A")
DEEP = rgb("#1A1060")
BLUE = rgb("#3D37EF")
PURPLE = rgb("#5040A8")
CYAN = rgb("#00D4FF")
MAGENTA = rgb("#C850FF")
WHITE = (255, 255, 255)
MUTED = (208, 221, 255)
SOFT = (230, 238, 255)


def gradient_bg(size):
    img = Image.new("RGBA", size, NAVY + (255,))
    px = img.load()
    w, h = size
    for y in range(h):
        t = y / max(1, h - 1)
        base = tuple(int(NAVY[i] * (1 - t) + DEEP[i] * t) for i in range(3))
        for x in range(w):
            glow = int(24 * max(0, 1 - ((x - 840) ** 2 + (y - 420) ** 2) / 520000))
            px[x, y] = (min(255, base[0] + glow), min(255, base[1] + glow), min(255, base[2] + glow * 2), 255)
    return img


def wrap(draw, value, fnt, max_width):
    lines = []
    for paragraph in value.split("\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            test = word if not current else current + " " + word
            if draw.textbbox((0, 0), test, font=fnt)[2] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
    return "\n".join(lines)


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_text(draw, xy, value, fnt, fill=WHITE, anchor=None, spacing=6):
    draw.multiline_text(xy, value, font=fnt, fill=fill, anchor=anchor, spacing=spacing)


def gradient_pill(base, box, left, right, radius=44):
    x1, y1, x2, y2 = box
    mask = Image.new("L", (x2 - x1, y2 - y1), 0)
    md = ImageDraw.Draw(mask)
    md.rounded_rectangle((0, 0, mask.width - 1, mask.height - 1), radius=radius, fill=255)
    grad = Image.new("RGBA", mask.size, left + (255,))
    gp = grad.load()
    for x in range(mask.width):
        t = x / max(1, mask.width - 1)
        color = tuple(int(left[i] * (1 - t) + right[i] * t) for i in range(3)) + (255,)
        for y in range(mask.height):
            gp[x, y] = color
    base.paste(grad, (x1, y1), mask)


def section_title(draw, x, y, title):
    draw_text(draw, (x, y), title, F_H2, WHITE)
    draw.line((x, y + 41, x + 120, y + 41), fill=CYAN + (220,), width=3)


base = gradient_bg((W, H))
draw = ImageDraw.Draw(base)

if HERO.exists():
    hero = Image.open(HERO).convert("RGBA")
    hero = hero.resize((W, int(W * hero.height / hero.width)))
    if hero.height < H:
        hero = hero.resize((int(H * hero.width / hero.height), H))
    hero = hero.crop(((hero.width - W) // 2, (hero.height - H) // 2, (hero.width + W) // 2, (hero.height + H) // 2))
    hero = hero.filter(ImageFilter.GaussianBlur(8))
    base = Image.alpha_composite(hero, Image.new("RGBA", (W, H), (8, 11, 42, 218)))
    draw = ImageDraw.Draw(base)

for i in range(95):
    x = int((math.sin(i * 18.31) * 9432.11 % 1) * W)
    y = int((math.sin(i * 73.73) * 17321.9 % 1) * H)
    r = 1 + (i % 3)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=CYAN + (70,))
    if i % 5 == 0:
        draw.line((x, y, min(W, x + 120), max(0, min(H, y + ((i % 7) - 3) * 18))), fill=BLUE + (42,), width=1)

draw.ellipse((-210, 180, 420, 790), outline=BLUE + (70,), width=3)
draw.ellipse((725, -120, 1250, 415), outline=CYAN + (58,), width=2)

# Header
rounded(draw, (54, 46, 1026, 198), 34, (5, 8, 35, 188), outline=WHITE + (42,), width=1)
logo = Image.open(LOGO).convert("RGBA")
logo_w = 425
logo_h = int(logo.height * logo_w / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
base.alpha_composite(logo, (82, 78))
gradient_pill(base, (760, 82, 995, 160), BLUE, MAGENTA, 38)
draw = ImageDraw.Draw(base)
draw_text(draw, (878, 105), "FORMAR SIN\nMIGRAR", F_LABEL, WHITE, anchor="ma", spacing=2)

# Hero copy
draw_text(draw, (70, 245), "IA ACADEMY", F_TITLE, WHITE)
draw_text(draw, (72, 323), "Inteligencia Artificial\npara el talento del territorio", F_SUB, CYAN, spacing=2)
intro = "División especializada de Campuslands para democratizar el acceso a competencias en IA en Colombia y Latinoamérica."
draw_text(draw, (72, 430), wrap(draw, intro, F_BODY, 900), F_BODY, MUTED, spacing=5)

# What is
rounded(draw, (58, 510, 1022, 678), 28, (8, 11, 42, 222), outline=CYAN + (100,), width=2)
section_title(draw, 92, 540, "¿Qué es?")
what = "Formación práctica en Inteligencia Artificial para jóvenes, profesionales, educadores y empresas. Opera en modalidad presencial y digital."
draw_text(draw, (92, 598), wrap(draw, what, F_BODY, 875), F_BODY, SOFT)

# Programs
rounded(draw, (58, 710, 1022, 1164), 30, (8, 11, 42, 224), outline=BLUE + (115,), width=2)
section_title(draw, 92, 742, "Oferta formativa")
programs = [
    ("IA Generativa", "ChatGPT avanzado, automatización y productividad."),
    ("Machine Learning", "Algoritmos, modelos predictivos y aplicaciones industriales."),
    ("Computer Vision", "Procesamiento de imágenes y video para casos reales."),
    ("Cursos básicos", "Entrada accesible para empezar sin conocimientos previos."),
    ("Formación docente", "Integración de IA en el aula y nuevas metodologías."),
]
x_positions = [92, 558]
y0 = 805
for idx, (title, body) in enumerate(programs):
    x = x_positions[idx % 2]
    y = y0 + (idx // 2) * 116
    w = 390 if idx != 4 else 856
    rounded(draw, (x, y, x + w, y + 88), 19, (26, 16, 96, 210), outline=CYAN + (92,), width=1)
    draw.ellipse((x + 18, y + 20, x + 35, y + 37), fill=CYAN + (240,))
    draw_text(draw, (x + 52, y + 12), title, F_H3, WHITE)
    draw_text(draw, (x + 52, y + 44), wrap(draw, body, F_BODY_SM, w - 72), F_BODY_SM, MUTED, spacing=3)

# Modalities and audiences
rounded(draw, (58, 1198, 1022, 1438), 30, (8, 11, 42, 226), outline=WHITE + (60,), width=1)
section_title(draw, 92, 1230, "Modalidad y públicos")
draw_text(draw, (92, 1292), "Presencial", F_H3, WHITE)
draw_text(draw, (236, 1292), "Sedes en Bucaramanga y ciudades activas.", F_BODY_SM, MUTED)
draw_text(draw, (92, 1335), "Digital", F_H3, WHITE)
draw_text(draw, (236, 1335), "Plataforma online para participantes en todo el país.", F_BODY_SM, MUTED)
draw_text(draw, (92, 1385), "Para jóvenes, profesionales, educadores y empresas.", F_BODY, SOFT)

# Campuslands context
rounded(draw, (58, 1470, 1022, 1658), 30, (8, 11, 42, 226), outline=PURPLE + (130,), width=2)
section_title(draw, 92, 1500, "Campuslands")
campus = "Empresa BIC fundada en Bucaramanga. Sedes activas: Bucaramanga, Puerta del Sol, Bogotá y Cúcuta. Sede principal: Zona Franca Santander. Visión: llevar oportunidades reales a los territorios."
draw_text(draw, (92, 1558), wrap(draw, campus, F_BODY_SM, 860), F_BODY_SM, MUTED, spacing=5)

# Contact
gradient_pill(base, (58, 1692, 1022, 1834), BLUE, MAGENTA, 54)
draw = ImageDraw.Draw(base)
draw.rounded_rectangle((58, 1692, 1022, 1834), radius=54, outline=WHITE + (90,), width=2)
draw_text(draw, (W // 2, 1718), "Pide información personalizada", F_CTA, WHITE, anchor="ma")
draw_text(draw, (W // 2, 1761), "+57 300 971 1559", F_H2, WHITE, anchor="ma")
draw_text(draw, (W // 2, 1802), "@ai.campuslands  |  campuslands.aiacademy.com.co", F_BODY_SM, WHITE, anchor="ma")

draw_text(draw, (76, 1870), "IA Generativa · Machine Learning · Computer Vision · Cursos básicos · Formación docente", F_MICRO, (190, 205, 242))

base.save(OUT)
print(OUT)
