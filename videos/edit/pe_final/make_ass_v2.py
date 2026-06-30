# -*- coding: utf-8 -*-
"""Generate dynamic 6-style NEBULA ASS on the OUTPUT timeline (xfade-aware).

Styles: Spoken, Impact_Marca, Impact_HUD, Highlight_Teal, Highlight_Violeta, StatBig.
No stroke (Outline=0), drop shadow only, Poppins Bold. Timeline matches base.mp4
built with two 0.3s cross-dissolves (partB shifted -0.3, partC shifted -0.6).
"""
import json, os, re, subprocess
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
EDL = json.load(open(os.path.join(HERE, "edl.json"), encoding="utf-8"))
TDIR = os.path.join(os.path.dirname(HERE), "transcripts")
OUT_ASS = r"C:/Temp/reels.ass"
FONT = "Poppins"
XF = 0.3

SRC_JSON = {
    "Cam": "PromptEngineering Video 10 Cam.json",
    "Pantalla": "PromptEngineering Video 10 Pantalla.json",
}

FIX = {
    r"\bfew shots\b": "few-shot", r"\bfew shot\b": "few-shot", r"\bfew-shots\b": "few-shot",
    r"\bzero shot\b": "zero-shot", r"\bcero shot\b": "zero-shot",
    r"\bciro\b": "zero", r"\bsiro\b": "zero", r"\bgu[ií]a\b": "IA",
    r"\bempezarlo\b": "pensarlo", r"\bquiero empezarlo\b": "quedo en pensarlo",
    r"\bisso\b": "eso",
}

# Colours libass &H00BBGGRR
WHITE = "&H00FFFFFF"
C_MARCA = "&H00CA39A2"
C_HUD = "&H00F4B45F"
C_TEAL = "&H00E0D66F"
C_VIOLETA = "&H00F28C9A"

TERMS = ["few-shot", "zero-shot", "shot", "prompt", "chatgpt", "modelo", "modelos",
         "formato", "contexto", "ejemplo", "ejemplos", "plantilla", "ia"]
ACTIONS = ["primero", "vamos", "controlar", "muestra", "muestrale", "ensena", "ensenar",
           "ensenale", "dale", "escribe", "escribeme", "mira", "fijate", "apoyado",
           "siguiendo", "ojo", "replico", "replica"]
HUD_PHRASES = ["razonan", "se potencia", "controlar la forma", "controlar el formato",
               "los modelos hoy", "razonar mejor", "para que sirve"]
MARCA_PHRASES = ["eso es few-shot", "ahora si suena a mi", "lo cambia absolutamente todo",
                 "cumplir esa promesa", "ensenar mostrando", "el resultado se potencia"]
NUMWORDS = {"cero": "0", "uno": "1", "dos": "2", "tres": "3", "cuatro": "4"}


def load_words(src):
    d = json.load(open(os.path.join(TDIR, SRC_JSON[src]), encoding="utf-8"))
    out = []
    for w in d["words"]:
        if w["type"] != "word":
            continue
        t = w["text"].strip()
        if t:
            out.append({"t": t, "s": w["start"], "e": w["end"]})
    return out


def fix_text(s):
    for pat, rep in FIX.items():
        s = re.sub(pat, rep, s, flags=re.IGNORECASE)
    return s


def ass_time(t):
    if t < 0:
        t = 0
    h = int(t // 3600); t -= h * 3600
    m = int(t // 60); t -= m * 60
    s = int(t); cs = int(round((t - s) * 100))
    if cs == 100:
        cs = 0; s += 1
    return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"


def chunk_words(words):
    cues, cur = [], []
    for i, w in enumerate(words):
        cur.append(w)
        end_punct = bool(re.search(r"[.?!:]$", w["t"]))
        gap_next = (words[i + 1]["s"] - w["e"]) if i + 1 < len(words) else 99
        if len(cur) >= 4 or end_punct or gap_next > 0.6 or (len(cur) >= 2 and gap_next > 0.35):
            cues.append(cur); cur = []
    if cur:
        cues.append(cur)
    return cues


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip())


def classify(text, is_pip, idx, total, last_impact):
    low = fix_text(text).lower().strip(" ,.?!:")
    words = low.split()
    has_num = bool(re.search(r"\d", text)) or any(n in words for n in NUMWORDS)
    if idx == 0:
        return "Impact_Marca", "Impact_Marca"
    if idx == total - 1:
        return "Impact_Marca", "Impact_Marca"
    if any(p in low for p in MARCA_PHRASES):
        return "Impact_Marca", "Impact_Marca"
    if any(p in low for p in HUD_PHRASES):
        return "Impact_HUD", "Impact_HUD"
    if has_num and len(words) <= 2:
        return "StatBig", last_impact
    if any(re.search(r"\b" + re.escape(a) + r"\b", low) for a in ACTIONS):
        return "Highlight_Violeta", last_impact
    if any(re.search(r"\b" + re.escape(t) + r"\b", low) for t in TERMS):
        return "Highlight_Teal", last_impact
    return "Spoken", last_impact


def main():
    words_cache = {s: load_words(s) for s in SRC_JSON}
    segs = EDL["segments"]
    # actual rendered seg durations + xfade-aware cumulative output offset
    pip_ids = {s["id"] for s in segs if s["layout"] == "pip"}
    durs = {s["id"]: probe(os.path.join(HERE, f"seg_{s['id']}.mp4")) for s in segs}
    cum = 0.0
    all_cues = []
    for si, seg in enumerate(segs):
        a, b = seg["start"], seg["end"]
        idnum = int(seg["id"][:2])
        xshift = (XF if idnum >= 12 else 0.0) + (XF if idnum >= 21 else 0.0)
        seg_out_start = cum - xshift
        ws = [w for w in words_cache[seg["src"]] if a - 0.05 <= w["s"] < b - 0.04]
        for cue in chunk_words(ws):
            cs = max(0.0, cue[0]["s"] - a) + seg_out_start
            ce = (cue[-1]["e"] - a) + seg_out_start
            text = fix_text(" ".join(w["t"] for w in cue)).strip()
            if not text:
                continue
            all_cues.append({"s": cs, "e": ce, "text": text, "pip": seg["layout"] == "pip"})
        cum += durs[seg["id"]]

    # readable minimum + no overrun
    MINDUR = 0.55
    for i, c in enumerate(all_cues):
        nxt = all_cues[i + 1]["s"] if i + 1 < len(all_cues) else c["e"] + MINDUR
        if c["e"] - c["s"] < MINDUR:
            c["e"] = min(c["s"] + MINDUR, max(c["e"], nxt - 0.02))
    all_cues = [c for c in all_cues if (c["e"] - c["s"]) >= 0.22]

    total = len(all_cues)
    events = []
    last_impact = "Impact_HUD"  # so first generic impact after Marca hook alternates
    for i, c in enumerate(all_cues):
        style, last_impact = classify(c["text"], c["pip"], i, total, last_impact)
        txt = c["text"]
        if i + 1 < total and c["e"] > all_cues[i + 1]["s"]:
            c["e"] = max(c["s"] + 0.3, all_cues[i + 1]["s"] - 0.02)
        if style != "Spoken":
            txt = txt.upper()
        # StatBig: lead with the big number element
        if style == "StatBig":
            for w, d in NUMWORDS.items():
                txt = re.sub(r"\b" + w.upper() + r"\b", d, txt)
        events.append((c["s"], c["e"], style, txt.replace("\n", " ")))

    # brand badge: ChatGPT during demo intro (Impact_HUD fallback, no PNG available)
    cumA = sum(durs[s["id"]] for s in segs if int(s["id"][:2]) <= 11)
    badge_s = cumA - XF + 0.1
    events.append((badge_s, badge_s + 2.6, "Impact_HUD",
                   r"{\an8\fs60\pos(960,155)}CHATGPT"))

    events.sort(key=lambda e: e[0])

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Spoken,{FONT},54,{WHITE},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,3,2,80,80,430,1
Style: Impact_Marca,{FONT},88,{C_MARCA},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,4,8,80,80,90,1
Style: Impact_HUD,{FONT},88,{C_HUD},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,4,8,80,80,90,1
Style: Highlight_Teal,{FONT},62,{C_TEAL},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,3,2,80,80,430,1
Style: Highlight_Violeta,{FONT},62,{C_VIOLETA},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,3,2,80,80,430,1
Style: StatBig,{FONT},150,{C_TEAL},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,5,5,80,80,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [header]
    for s, e, style, txt in events:
        lines.append(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},{style},,0,0,0,,{txt}")
    os.makedirs(os.path.dirname(OUT_ASS), exist_ok=True)
    open(OUT_ASS, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    cnt = Counter(st for _, _, st, _ in events)
    print(f"wrote {OUT_ASS} cues={len(events)} {dict(cnt)}")
    print(f"output timeline len ~= {cum - 2*XF:.2f}s")


if __name__ == "__main__":
    main()
