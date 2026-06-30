# -*- coding: utf-8 -*-
"""Generate dynamic Nebula ASS subtitles on the OUTPUT timeline for the dual-source edit."""
import json, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
EDL = json.load(open(os.path.join(HERE, "edl.json"), encoding="utf-8"))
TDIR = os.path.join(os.path.dirname(HERE), "transcripts")
OUT_ASS = r"C:/Temp/reels.ass"
FONT = "Arial"  # Poppins not installed -> Arial fallback

SRC_JSON = {
    "Cam": "PromptEngineering Video 10 Cam.json",
    "Pantalla": "PromptEngineering Video 10 Pantalla.json",
}

# minimal ASR-error corrections (whole word, case-insensitive)
FIX = {
    r"\bfew shots\b": "few-shot", r"\bfew shot\b": "few-shot",
    r"\bzero shot\b": "zero-shot", r"\bcero shot\b": "zero-shot",
    r"\bciro\b": "zero", r"\bsiro\b": "zero", r"\bguía\b": "IA",
    r"\bempezarlo\b": "pensarlo", r"\bquiero empezarlo\b": "quedó en pensarlo",
    r"\bisso\b": "eso", r"\bfew-shots\b": "few-shot",
}

KEY_TERMS = ["few-shot", "zero-shot", "ejemplo", "ejemplos", "contexto",
             "formato", "estilo", "shot", "prompt", "humano"]
IMPACT_PHRASES = ["eso es few-shot", "ahora si suena a mi", "ahora sí suena a mí",
                  "few-shot", "lo cambia absolutamente todo"]


def load_words(src):
    d = json.load(open(os.path.join(TDIR, SRC_JSON[src]), encoding="utf-8"))
    out = []
    for w in d["words"]:
        if w["type"] != "word":
            continue
        t = w["text"].strip()
        if not t:
            continue
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
    s = int(t)
    cs = int(round((t - s) * 100))
    if cs == 100:
        cs = 0; s += 1
    return f"{h:d}:{m:02d}:{s:02d}.{cs:02d}"


def chunk_words(words):
    """Group words into 2-4 word cues, breaking on sentence punctuation and >0.6s gaps."""
    cues = []
    cur = []
    for i, w in enumerate(words):
        cur.append(w)
        txt = w["t"]
        end_punct = bool(re.search(r"[.?!:]$", txt))
        gap_next = (words[i + 1]["s"] - w["e"]) if i + 1 < len(words) else 99
        if len(cur) >= 4 or end_punct or gap_next > 0.6 or (len(cur) >= 2 and gap_next > 0.35):
            cues.append(cur)
            cur = []
    if cur:
        cues.append(cur)
    return cues


def classify(text, is_pip, idx, total, last_style):
    low = fix_text(text).lower().strip(" ,.")
    has_num = bool(re.search(r"\d", text)) or any(
        n in low.split() for n in ["dos", "veinte", "tres"])
    is_key = any(re.search(r"\b" + re.escape(k) + r"\b", low) for k in KEY_TERMS)
    is_impact_phrase = any(p in low for p in IMPACT_PHRASES)
    # first / last cue overall -> Impact
    if idx == 0 or idx == total - 1:
        return "Impact"
    if has_num:
        return "Stat"
    if is_impact_phrase and not is_pip:
        return "Impact"
    if is_key and last_style != "Highlight":
        return "Highlight"
    return "Spoken"


def main():
    words_cache = {s: load_words(s) for s in SRC_JSON}
    events = []
    offset = 0.0
    # first pass: build all cues with output times
    all_cues = []
    for seg in EDL["segments"]:
        a, b = seg["start"], seg["end"]
        dur = b - a
        # word must START within the segment (no leaked boundary fragments)
        ws = [w for w in words_cache[seg["src"]]
              if w["s"] >= a - 0.05 and w["s"] < b - 0.04]
        for cue in chunk_words(ws):
            cs = max(0.0, cue[0]["s"] - a) + offset
            ce = min(dur, cue[-1]["e"] - a) + offset
            if ce <= cs:
                ce = cs + 0.4
            text = fix_text(" ".join(w["t"] for w in cue)).strip()
            if not text:
                continue
            all_cues.append({"s": cs, "e": ce, "text": text, "pip": seg["layout"] == "pip"})
        offset += dur

    # enforce a readable minimum duration; extend into available gap before next cue
    MINDUR = 0.55
    for i, c in enumerate(all_cues):
        nxt = all_cues[i + 1]["s"] if i + 1 < len(all_cues) else c["e"] + MINDUR
        if c["e"] - c["s"] < MINDUR:
            c["e"] = min(c["s"] + MINDUR, max(c["e"], nxt - 0.02))

    # drop unreadable fragments (audio still speaks them)
    all_cues = [c for c in all_cues if (c["e"] - c["s"]) >= 0.22]

    total = len(all_cues)
    last_style = "Spoken"
    for i, c in enumerate(all_cues):
        style = classify(c["text"], c["pip"], i, total, last_style)
        last_style = style
        txt = c["text"]
        # prevent caption overrun into next cue
        if i + 1 < total and c["e"] > all_cues[i + 1]["s"]:
            c["e"] = max(c["s"] + 0.3, all_cues[i + 1]["s"] - 0.02)
        if style in ("Impact", "Highlight", "Stat"):
            txt = txt.upper()
        txt = txt.replace("\n", " ")
        events.append((c["s"], c["e"], style, txt))

    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1920
PlayResY: 1080
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Spoken,{FONT},52,&H00FFFFFF,&H000000FF,&H00000000,&H64000000,0,0,0,0,100,100,0,0,1,3,1,2,60,60,350,1
Style: Highlight,{FONT},58,&H00CA39A2,&H000000FF,&H00FFFFFF,&H00000000,1,0,0,0,100,100,0,0,1,3,1,2,60,60,350,1
Style: Impact,{FONT},82,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,5,2,8,60,60,80,1
Style: Stat,{FONT},78,&H00E0D66F,&H000000FF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,4,2,8,60,60,90,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = [header]
    for s, e, style, txt in events:
        lines.append(f"Dialogue: 0,{ass_time(s)},{ass_time(e)},{style},,0,0,0,,{txt}")
    os.makedirs(os.path.dirname(OUT_ASS), exist_ok=True)
    open(OUT_ASS, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    # stats
    from collections import Counter
    cnt = Counter(st for _, _, st, _ in events)
    print(f"wrote {OUT_ASS}  cues={len(events)}  {dict(cnt)}")
    print(f"total timeline = {offset:.2f}s")


if __name__ == "__main__":
    main()
