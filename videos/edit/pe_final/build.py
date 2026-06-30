# -*- coding: utf-8 -*-
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
EDL = json.load(open(os.path.join(HERE, "edl.json"), encoding="utf-8"))
OFF = EDL["pip_offset_cam_minus_pan"]
SRC = EDL["sources"]
LOGO = EDL["logo"]
FPS = 30

QSV = ["-c:v", "h264_qsv", "-global_quality", "18", "-preset", "fast", "-look_ahead", "1"]
AENC = ["-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-ac", "2"]

GRADE_CAM = "eq=contrast=1.07:saturation=1.06"
GRADE_SCR = "eq=contrast=1.03:saturation=1.02"

# PiP geometry
PIP_W, PIP_H = 480, 270
BORDER = 3
PADW, PADH = PIP_W + 2 * BORDER, PIP_H + 2 * BORDER
PIP_X = (1920 - PADW) // 2 + 160   # bottom center, slightly right
PIP_Y = 1080 - PADH - 46
MARCA = "0xA239CA"


def afade(dur):
    d = max(0.0, dur - 0.03)
    return f"afade=t=in:st=0:d=0.03,afade=t=out:st={d:.3f}:d=0.03"


def build_full(seg, out):
    a, b = seg["start"], seg["end"]
    dur = b - a
    src = SRC[seg["src"]]
    grade = GRADE_CAM if seg["src"] == "Cam" else GRADE_SCR
    fc = (
        f"[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,"
        f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={FPS},{grade}[v];"
        f"[1:v]scale=180:-1[lg];"
        f"[v][lg]overlay=W-w-30:30[outv]"
    )
    cmd = ["ffmpeg", "-y",
           "-ss", f"{a:.3f}", "-i", src,
           "-i", LOGO,
           "-filter_complex", fc,
           "-map", "[outv]", "-map", "0:a",
           "-af", afade(dur),
           "-t", f"{dur:.3f}",
           "-r", str(FPS), "-vsync", "cfr",
           *QSV, *AENC, "-movflags", "+faststart", out]
    return cmd


def build_pip(seg, out):
    a, b = seg["start"], seg["end"]
    dur = b - a
    pan = SRC["Pantalla"]
    cam = SRC["Cam"]
    ca = a + OFF
    fc = (
        f"[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,"
        f"pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps={FPS},{GRADE_SCR}[bg];"
        # cam zoom 1.25 toward face, crop, scale to pip, border via pad
        f"[1:v]scale=2400:1350,crop=1536:864:432:183,scale={PIP_W}:{PIP_H},setsar=1,fps={FPS},{GRADE_CAM}[cz];"
        f"[cz]pad={PADW}:{PADH}:{BORDER}:{BORDER}:color={MARCA}[cam];"
        f"[bg][cam]overlay={PIP_X}:{PIP_Y}[pp];"
        f"[2:v]scale=180:-1[lg];"
        f"[pp][lg]overlay=W-w-30:30[outv]"
    )
    cmd = ["ffmpeg", "-y",
           "-ss", f"{a:.3f}", "-i", pan,
           "-ss", f"{ca:.3f}", "-i", cam,
           "-i", LOGO,
           "-filter_complex", fc,
           "-map", "[outv]", "-map", "0:a",
           "-af", afade(dur),
           "-t", f"{dur:.3f}",
           "-r", str(FPS), "-vsync", "cfr",
           *QSV, *AENC, "-movflags", "+faststart", out]
    return cmd


def main():
    only = None
    if len(sys.argv) > 1:
        only = set(sys.argv[1:])
    segs = EDL["segments"]
    listing = []
    for seg in segs:
        out = os.path.join(HERE, f"seg_{seg['id']}.mp4")
        listing.append(out)
        if only and seg["id"] not in only:
            continue
        cmd = build_pip(seg, out) if seg["layout"] == "pip" else build_full(seg, out)
        print(f">>> {seg['id']} ({seg['layout']}) {seg['end']-seg['start']:.2f}s", flush=True)
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr[-2500:])
            sys.exit(f"FAILED {seg['id']}")
    if only:
        print("test mode: skipping concat")
        return
    # concat
    concat_txt = os.path.join(HERE, "concat.txt")
    with open(concat_txt, "w", encoding="utf-8") as f:
        for p in listing:
            f.write(f"file '{p.replace(chr(92), '/')}'\n")
    base = os.path.join(HERE, "base.mp4")
    cc = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_txt,
          "-c", "copy", "-movflags", "+faststart", base]
    print(">>> concat -> base.mp4", flush=True)
    r = subprocess.run(cc, capture_output=True, text=True)
    if r.returncode != 0:
        print("copy concat failed, re-encoding...", r.stderr[-1500:])
        cc = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_txt,
              *QSV, *AENC, "-r", str(FPS), "-vsync", "cfr",
              "-movflags", "+faststart", base]
        r = subprocess.run(cc, capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stderr[-2000:]); sys.exit("concat failed")
    print("DONE base.mp4")


if __name__ == "__main__":
    main()
