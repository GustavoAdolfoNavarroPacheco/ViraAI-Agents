from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
from pathlib import Path


ROOT = Path(r"C:\Users\adolf\OneDrive\Documents\Agente AI - Claude")
OUT = ROOT / "output" / "flyer-informativo-ia-academy-2026-06-24.png"
LOGO = ROOT / "context" / "img-creator" / "ia-academy-logo.png"
HERO = ROOT / "output" / "ia-academy-hero-2026-06-24.png"

W, H = 1080, 1350

FONT_REG = r"C:\Windows\Fonts\Roboto-Regular.ttf"
FONT_BOLD = r"C:\Windows\Fonts\arialbd.ttf"
FONT_BODY = r"C:\Windows\Fonts\arial.ttf"


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


F_TITLE = font(FONT_BOLD, 72)
F_TITLE_SMALL = font(FONT_BOLD, 54)
F_H2 = font(FONT_BOLD, 34)
F_H3 = font(FONT_BOLD, 28)
F_BODY = font(FONT_BODY, 25)
F_BODY_SM = font(FONT_BODY, 22)
F_LABEL = font(FONT_BOLD, 21)
F_CTA = font(FONT_BOLD, 31)
F_MICRO = font(FONT_REG, 18)


def hex_to_rgb(value):
    value = value.lstrip("#")
    return tuple(int(value[i:i + 2], 16) for i in (0, 2, 4))


NAVY = hex_to_rgb("#080B2A")
DEEP = hex_to_rgb("#1A1060")
BLUE = hex_to_rgb("#3D37EF")
PURPLE = hex_to_rgb("#5040A8")
CYAN = hex_to_rgb("#00D4FF")
MAGENTA = hex_to_rgb("#C850FF")
WHITE = (255, 255, 255)
MUTED = (204, 218, 255)


def vertical_gradient(size, top, bottom):
    w, h = size
    img = Image.new("RGB", size, top)
    pix = img.load()
    for y in range(h):
        t = y / max(1, h - 1)
        color = tuple(int(top[i] * (1 - t) + bottom[i] * t) for i in range(3))
        for x in range(w):
            pix[x, y] = color
    return img.convert("RGBA")


def rounded(draw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw, xy, value, fnt, fill=WHITE, anchor=None, spacing=8):
    draw.multiline_text(xy, value, font=fnt, fill=fill, anchor=anchor, spacing=spacing)


def wrap(draw, value, fnt, max_width):
    words = value.split()
    lines = []
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


def gradient_text(draw, xy, value, fnt, colors):
    x, y = xy
    bbox = draw.textbbox((x, y), value, font=fnt)
    mask = Image.new("L", (bbox[2] - bbox[0] + 8, bbox[3] - bbox[1] + 8), 0)
    md = ImageDraw.Draw(mask)
    md.text((4, 4), value, font=fnt, fill=255)
    grad = Image.new("RGBA", mask.size, colors[0] + (255,))
    gp = grad.load()
    for ix in range(mask.size[0]):
        t = ix / max(1, mask.size[0] - 1)
        c = tuple(int(colors[0][i] * (1 - t) + colors[1][i] * t) for i in range(3))
        for iy in range(mask.size[1]):
            gp[ix, iy] = c + (255,)
    base.paste(grad, (x - 4, y - 4), mask)


base = vertical_gradient((W, H), NAVY, (13, 10, 58))
draw = ImageDraw.Draw(base)

if HERO.exists():
    hero = Image.open(HERO).convert("RGBA")
    hero = hero.resize((W, int(W * hero.height / hero.width)))
    if hero.height < H:
        hero = hero.resize((int(H * hero.width / hero.height), H))
    hero = hero.crop(((hero.width - W) // 2, (hero.height - H) // 2, (hero.width + W) // 2, (hero.height + H) // 2))
    hero = hero.filter(ImageFilter.GaussianBlur(5))
    dark = Image.new("RGBA", (W, H), (8, 11, 42, 198))
    base = Image.alpha_composite(hero, dark)
    draw = ImageDraw.Draw(base)

# Decorative circuitry / nebula texture.
for i in range(70):
    x = int((math.sin(i * 12.989) * 43758.5453 % 1) * W)
    y = int((math.sin(i * 78.233) * 24634.6345 % 1) * H)
    r = 1 + (i % 3)
    draw.ellipse((x - r, y - r, x + r, y + r), fill=CYAN + (80,))
    if i % 4 == 0:
        x2 = min(W, x + 70 + (i % 90))
        y2 = max(0, min(H, y + ((i % 5) - 2) * 22))
        draw.line((x, y, x2, y2), fill=BLUE + (45,), width=1)

draw.ellipse((-260, 80, 430, 740), outline=BLUE + (70,), width=3)
draw.ellipse((760, -150, 1300, 390), outline=CYAN + (55,), width=2)
draw.line((70, 250, 1010, 205), fill=CYAN + (42,), width=2)

# Header glass panel.
rounded(draw, (54, 42, 1026, 194), 34, (5, 8, 35, 178), outline=WHITE + (36,), width=1)
logo = Image.open(LOGO).convert("RGBA")
logo_w = 430
logo_h = int(logo.height * logo_w / logo.width)
logo = logo.resize((logo_w, logo_h), Image.Resampling.LANCZOS)
base.alpha_composite(logo, (82, 72))
rounded(draw, (770, 79, 994, 155), 38, (61, 55, 239, 168), outline=CYAN + (120,), width=1)
text(draw, (882, 101), "FORMAR SIN\nMIGRAR", F_LABEL, WHITE, anchor="ma", spacing=3)

# Hero title.
text(draw, (76, 258), "IA ACADEMY", F_TITLE, WHITE)
gradient_text(draw, (76, 334), "aprende IA aplicada", F_TITLE_SMALL, (CYAN, MAGENTA))
subtitle = "La división especializada de Campuslands para formar talento en Inteligencia Artificial."
text(draw, (78, 420), wrap(draw, subtitle, F_BODY, 900), F_BODY, MUTED)

# Main information cards.
card_y = 530
rounded(draw, (58, card_y, 1022, 932), 34, (8, 11, 42, 218), outline=CYAN + (90,), width=2)
text(draw, (92, card_y + 34), "¿Qué puedes aprender?", F_H2, WHITE)

items = [
    ("IA Generativa", "ChatGPT, automatización y productividad con IA."),
    ("Machine Learning", "Modelos predictivos y aplicaciones industriales."),
    ("Computer Vision", "Procesamiento de imágenes y video con IA."),
    ("Cursos básicos", "Ruta de entrada sin conocimientos previos."),
    ("Formación docente", "IA aplicada al aula y nuevas metodologías."),
]

x1, x2 = 92, 558
y = card_y + 92
for idx, (title, body) in enumerate(items):
    col_x = x1 if idx < 3 else x2
    row_y = y + (idx % 3) * 92 if idx < 3 else y + ((idx - 3) * 120)
    rounded(draw, (col_x, row_y, col_x + 392, row_y + 72), 18, (26, 16, 96, 205), outline=BLUE + (110,), width=1)
    draw.ellipse((col_x + 18, row_y + 24, col_x + 34, row_y + 40), fill=CYAN + (230,))
    text(draw, (col_x + 50, row_y + 12), title, F_H3, WHITE)
    text(draw, (col_x + 50, row_y + 43), wrap(draw, body, F_BODY_SM, 320), F_BODY_SM, MUTED)

# Modalities and audience.
rounded(draw, (58, 966, 1022, 1128), 30, (8, 11, 42, 218), outline=WHITE + (60,), width=1)
text(draw, (92, 998), "Modalidad", F_H2, WHITE)
text(draw, (92, 1046), "Presencial en sedes activas + digital para participantes en todo el país.", F_BODY, MUTED)
text(draw, (92, 1084), "Para jóvenes, profesionales, educadores y empresas que quieren modernizar sus habilidades.", F_BODY_SM, (226, 235, 255))

# CTA footer.
cta_box = (58, 1164, 1022, 1274)
mask = Image.new("L", (cta_box[2] - cta_box[0], cta_box[3] - cta_box[1]), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.rounded_rectangle((0, 0, mask.width - 1, mask.height - 1), radius=55, fill=255)
cta_grad = Image.new("RGBA", mask.size, BLUE + (255,))
cta_pix = cta_grad.load()
for x in range(mask.width):
    t = x / max(1, mask.width - 1)
    c = tuple(int(BLUE[i] * (1 - t) + MAGENTA[i] * t) for i in range(3)) + (255,)
    for y in range(mask.height):
        cta_pix[x, y] = c
base.paste(cta_grad, (cta_box[0], cta_box[1]), mask)
draw = ImageDraw.Draw(base)
draw.rounded_rectangle(cta_box, radius=55, outline=WHITE + (90,), width=2)
text(draw, (W // 2, 1188), "Inscríbete o pide información personalizada", F_CTA, WHITE, anchor="ma")
text(draw, (W // 2, 1232), "+57 300 971 1559  |  @ai.campuslands  |  campuslands.aiacademy.com.co", F_BODY_SM, WHITE, anchor="ma")

text(draw, (78, 1304), "Campuslands AI Academy · IA Generativa · Machine Learning · Computer Vision", F_MICRO, (180, 197, 240))

base.save(OUT)
print(OUT)
