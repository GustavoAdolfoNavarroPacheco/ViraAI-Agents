# -*- coding: utf-8 -*-
"""v2 assembly: re-render PiP segments with NEBULA gradient panel, reuse full-cam
segments, then concat in 3 sections joined by 0.3s cross-dissolves.

Usage:
    python build_v2.py pip      # re-render only the 9 PiP segments (12..20)
    python build_v2.py assemble # concat 3 parts + xfade -> base.mp4
    python build_v2.py all      # both
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EDL = json.load(open(os.path.join(HERE, "edl.json"), encoding="utf-8"))
OFF = EDL["pip_offset_cam_minus_pan"]
SRC = EDL["sources"]
LOGO = EDL["logo"]
PANEL = os.path.join(HERE, "panel.png")
FPS = 30

QSV = ["-c:v", "h264_qsv", "-global_quality", "18", "-preset", "fast", "-look_ahead", "1"]
AENC = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]

GRADE_CAM = "eq=contrast=1.07:saturation=1.06"
GRADE_SCR = "eq=contrast=1.03:saturation=1.02"

# PiP camera geometry inside the gradient panel
PIP_W, PIP_H = 480, 270
BORDER = 3
MARCA = "0xA239CA"
# panel.png is 530x340; placed bottom-center-right
PANEL_W, PANEL_H = 530, 340
PANEL_X = (1920 - PANEL_W) // 2 + 160      # 855
PANEL_Y = 1080 - PANEL_H - 40              # 700
CAM_X = PANEL_X + 22                        # 877  (inside panel, left pad)
CAM_Y = PANEL_Y + 42                        # 742  (top strip for violeta border)

XF = 0.3  # cross-dissolve duration


def afade(dur):
    d = max(0.0, dur - 0.03)
    return f"afade=t=in:st=0:d=0.03,afade=t=out:st={d:.3f}:d=0.03"


def build_pip(seg, out):
    a, b = seg["start"], seg["end"]
    dur = b - a
    pan = SRC["Pantalla"]
    cam = SRC["Cam"]
    ca = a + OFF
    fc = (
        f"[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,"
        f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={FPS},{GRADE_SCR}[bg];"
        # cam zoom 1.25 toward face -> crop -> pip size -> MARCA border via pad
        f"[1:v]scale=2400:1350,crop=1536:864:432:183,scale={PIP_W}:{PIP_H},setsar=1,fps={FPS},{GRADE_CAM}[cz];"
        f"[cz]pad={PIP_W+2*BORDER}:{PIP_H+2*BORDER}:{BORDER}:{BORDER}:color={MARCA}[cam];"
        # gradient panel behind cam
        f"[3:v]format=rgba[pnl];"
        f"[bg][pnl]overlay={PANEL_X}:{PANEL_Y}[b1];"
        f"[b1][cam]overlay={CAM_X}:{CAM_Y}[pp];"
        f"[2:v]scale=180:-1[lg];"
        f"[pp][lg]overlay=W-w-30:30[outv]"
    )
    cmd = ["ffmpeg", "-y",
           "-ss", f"{a:.3f}", "-i", pan,
           "-ss", f"{ca:.3f}", "-i", cam,
           "-i", LOGO,
           "-i", PANEL,
           "-filter_complex", fc,
           "-map", "[outv]", "-map", "0:a",
           "-af", afade(dur),
           "-t", f"{dur:.3f}",
           "-r", str(FPS), "-vsync", "cfr",
           *QSV, *AENC, "-movflags", "+faststart", out]
    return cmd


def seg_path(seg):
    return os.path.join(HERE, f"seg_{seg['id']}.mp4")


def render_pip():
    for seg in EDL["segments"]:
        if seg["layout"] != "pip":
            continue
        out = seg_path(seg)
        print(f">>> {seg['id']} (pip) {seg['end']-seg['start']:.2f}s", flush=True)
        r = subprocess.run(build_pip(seg, out), capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr[-2500:]); sys.exit(f"FAILED {seg['id']}")
    print("DONE pip render")


def concat_copy(seg_list, out):
    txt = out + ".txt"
    with open(txt, "w", encoding="utf-8") as f:
        for s in seg_list:
            f.write(f"file '{seg_path(s).replace(chr(92), '/')}'\n")
    cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", txt,
           "-c", "copy", "-movflags", "+faststart", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-1500:]); sys.exit(f"concat failed -> {out}")


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", path], capture_output=True, text=True)
    return float(r.stdout.strip())


def assemble():
    segs = EDL["segments"]
    partA = [s for s in segs if s["id"][:2] in {f"{i:02d}" for i in range(1, 12)}]
    partB = [s for s in segs if s["layout"] == "pip"]
    partC = [s for s in segs if s["id"][:2] in {f"{i:02d}" for i in range(21, 27)}]
    pA = os.path.join(HERE, "partA.mp4")
    pB = os.path.join(HERE, "partB.mp4")
    pC = os.path.join(HERE, "partC.mp4")
    concat_copy(partA, pA)
    concat_copy(partB, pB)
    concat_copy(partC, pC)
    dA, dB = probe(pA), probe(pB)
    oa = dA - XF
    ob = dA + dB - 2 * XF       # offset for 2nd xfade on the (A+B) stream
    print(f"durA={dA:.3f} durB={dB:.3f} oa={oa:.3f} ob={ob:.3f}")
    fc = (
        f"[0:v][1:v]xfade=transition=fade:duration={XF}:offset={oa:.3f}[vab];"
        f"[vab][2:v]xfade=transition=fade:duration={XF}:offset={ob:.3f}[outv];"
        f"[0:a][1:a]acrossfade=d={XF}[aab];"
        f"[aab][2:a]acrossfade=d={XF}[outa]"
    )
    base = os.path.join(HERE, "base.mp4")
    cmd = ["ffmpeg", "-y", "-i", pA, "-i", pB, "-i", pC,
           "-filter_complex", fc,
           "-map", "[outv]", "-map", "[outa]",
           "-r", str(FPS), "-vsync", "cfr",
           *QSV, *AENC, "-movflags", "+faststart", base]
    print(">>> xfade assemble -> base.mp4", flush=True)
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stderr[-2500:]); sys.exit("assemble failed")
    print(f"DONE base.mp4  total={probe(base):.3f}s")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    if mode in ("pip", "all"):
        render_pip()
    if mode in ("assemble", "all"):
        assemble()
