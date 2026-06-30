# -*- coding: utf-8 -*-
"""Generate calmer NEBULA ASS subtitles for YouTube horizontal.

Subtitles stay bottom-centered by default. Dynamic style changes are restrained:
mostly Spoken, occasional Highlight/Impact, and StatBig only for important
numbers or section beats.
"""
import json, os, re, subprocess
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
EDL = json.load(open(os.path.join(HERE, "edl.json"), encoding="utf-8"))
TDIR = os.path.join(os.path.dirname(HERE), "transcripts")
OUT_ASS = r"C:/Temp/reels_v3.ass"
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

WHITE = "&H00FFFFFF"
C_MARCA = "&H00CA39A2"
C_HUD = "&H00F4B45F"
C_TEAL = "&H00E0D66F"
C_VIOLETA = "&H00F28C9A"

TERMS = ["few-shot", "zero-shot", "shot", "prompt", "formato", "ejemplo", "ejemplos", "IA"]
ACTIONS = ["controlar", "enseñar", "mostrar", "siguiendo", "apoyado", "replico"]
HUD_PHRASES = ["controlar la forma", "controlar el formato", "los modelos hoy"]
MARCA_PHRASES = ["eso es few-shot", "ahora si suena a mi", "enseñar mostrando", "lo cambia absolutamente todo"]
NUMWORDS = {"cero": "0", "uno": "1", "dos": "2", "tres": "3", "cuatro": "4"}


def load_words(src):
    d = json.load(open(os.path.join(TDIR, SRC_JSON[src]), encoding="utf-8"))
    return [
        {"t": w["text"].strip(), "s": w["start"], "e": w["end"]}
        for w in d["words"]
        if w["type"] == "word" and w["text"].strip()
    ]


def fix_text(s):
    for pat, rep in FIX.items():
        s = re.sub(pat, rep, s, flags=re.IGNORECASE)
    return s


def ass_time(t):
    t = max(0, t)
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
        if len(cur) >= 5 or end_punct or gap_next > 0.75 or (len(cur) >= 3 and gap_next > 0.45):
            cues.append(cur)
            cur = []
    if cur:
        cues.append(cur)
    return cues


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip())


def classify(text, idx, total, last_special_idx):
    low = fix_text(text).lower().strip(" ,.?!:")
    words = low.split()
    spacing_ok = idx - last_special_idx >= 3
    if idx == 0 or idx == total - 1:
        return "Impact_Marca", idx
    if spacing_ok and any(p in low for p in MARCA_PHRASES):
        return "Impact_Marca", idx
    if spacing_ok and any(p in low for p in HUD_PHRASES):
        return "Impact_HUD", idx
    if spacing_ok and len(words) <= 4 and any(re.search(r"\b" + re.escape(t.lower()) + r"\b", low) for t in TERMS):
        return "Highlight_Teal", idx
    if spacing_ok and len(words) <= 4 and any(re.search(r"\b" + re.escape(a.lower()) + r"\b", low) for a in ACTIONS):
        return "Highlight_Violeta", idx
    if spacing_ok and len(words) <= 2 and (bool(re.search(r"\d", text)) or any(n in words for n in NUMWORDS)):
        return "StatBig", idx
    return "Spoken", last_special_idx


def main():
    words_cache = {s: load_words(s) for s in SRC_JSON}
    segs = EDL["segments"]
    durs = {}
    for s in segs:
        path = os.path.join(HERE, f"seg_{s['id']}.mp4")
        durs[s["id"]] = probe(path)

    cum = 0.0
    all_cues = []
    for seg in segs:
        a, b = seg["start"], seg["end"]
        idnum = int(seg["id"][:2])
        xshift = (XF if idnum >= 12 else 0.0) + (XF if idnum >= 21 else 0.0)
        seg_out_start = cum - xshift
        ws = [w for w in words_cache[seg["src"]] if a - 0.05 <= w["s"] < b - 0.04]
        for cue in chunk_words(ws):
            cs = max(0.0, cue[0]["s"] - a) + seg_out_start
            ce = (cue[-1]["e"] - a) + seg_out_start
            text = fix_text(" ".join(w["t"] for w in cue)).strip()
            if text:
                all_cues.append({"s": cs, "e": ce, "text": text})
        cum += durs[seg["id"]]

    for i, c in enumerate(all_cues):
        nxt = all_cues[i + 1]["s"] if i + 1 < len(all_cues) else c["e"] + 0.7
        if c["e"] - c["s"] < 0.65:
            c["e"] = min(c["s"] + 0.65, max(c["e"], nxt - 0.03))
    all_cues = [c for c in all_cues if (c["e"] - c["s"]) >= 0.28]

    total = len(all_cues)
    events = []
    last_special = -10
    for i, c in enumerate(all_cues):
        style, last_special = classify(c["text"], i, total, last_special)
        if i + 1 < total and c["e"] > all_cues[i + 1]["s"]:
            c["e"] = max(c["s"] + 0.35, all_cues[i + 1]["s"] - 0.03)
        txt = c["text"].replace("\n", " ")
        if style != "Spoken":
            txt = txt.upper()
        if style == "StatBig":
            for w, d in NUMWORDS.items():
                txt = re.sub(r"\b" + w.upper() + r"\b", d, txt)
        events.append((c["s"], c["e"], style, txt))

    events.sort(key=lambda e: e[0])

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Spoken,{FONT},48,{WHITE},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,3,2,120,120,86,1
Style: Impact_Marca,{FONT},58,{C_MARCA},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,4,2,120,120,94,1
Style: Impact_HUD,{FONT},58,{C_HUD},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,4,2,120,120,94,1
Style: Highlight_Teal,{FONT},52,{C_TEAL},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,3,2,120,120,90,1
Style: Highlight_Violeta,{FONT},52,{C_VIOLETA},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,3,2,120,120,90,1
Style: StatBig,{FONT},72,{C_TEAL},&H000000FF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,4,2,120,120,104,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [header]
    for s, e, style, txt in events:
        lines.append(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},{style},,0,0,0,,{{\\an2}}{txt}")
    os.makedirs(os.path.dirname(OUT_ASS), exist_ok=True)
    open(OUT_ASS, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    cnt = Counter(st for _, _, st, _ in events)
    print(f"wrote {OUT_ASS} cues={len(events)} {dict(cnt)}")
    print(f"output timeline len ~= {cum - 2*XF:.2f}s")


if __name__ == "__main__":
    main()
