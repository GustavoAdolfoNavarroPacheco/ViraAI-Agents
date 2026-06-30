---
name: promptengineering-v10-dualsource
description: Reusable technical facts for the PromptEngineering V10 dual-source YouTube edit (sync offset, gradient PiP panel, Poppins install, xfade-aware ASS)
metadata:
  type: project
---

PromptEngineering Video 10 (Prompt Engineering / few-shot tutorial) — dual-source YouTube long-form edit. Final at `output/videos_output/PromptEngineering_Video10_v1.mp4` (1920x1080, ~3:57, -14.6 LUFS). Working dir: `videos/edit/pe_final/` (edl.json, build_v2.py, make_ass_v2.py, panel.png, seg_*.mp4, base.mp4).

**Why:** Source has two files — `PromptEngineering Video 10 Cam.mp4` (presenter, own clean audio, many retakes) and `PromptEngineering Video 10 Pantalla.mp4` (ChatGPT demo screen, own audio). 26-segment EDL picks cleanest retake of each beat; each segment carries its own synced audio so there is no cross-source drift.

**How to apply (reusable facts for any re-edit / v2 of this project):**
- **Dual-source sync offset:** `Cam_time = Pantalla_time + 361.4`. Found by matching identical phrases across both transcripts. Use this for any new PiP segment.
- **Section structure:** segs 01-11 = Cam full-frame (intro+explanation), 12-20 = Pantalla full-frame bg + Cam face-PiP (demo), 21-26 = Cam full-frame (when-to-use + outro). Two 0.3s cross-dissolves at the 11→12 and 20→21 boundaries.
- **NEBULA gradient PiP panel (landscape):** `panel.png` is 530x340 gradient #0B0826→#9A8CF2 (diagonal) with 3px VIOLETA border, generated via ffmpeg `gradients` filter. Placed bottom-center-right at x=855,y=700. Cam (480x270, 1.25x face-zoom, 3px MARCA border) overlaid inside at x=877,y=742. Reads as a "presenter zone" — much better than a bare floating thumbnail.
- **Poppins for libass:** Poppins is NOT installed system-wide. Installed per-user TTFs to `%LOCALAPPDATA%\Microsoft\Windows\Fonts` + HKCU font registry, AND copied to `C:\Temp\fonts`. Burn with `ass=reels.ass:fontsdir=fonts` run from cwd `C:\Temp`. Verified libass picks `Poppins-Bold` (weight 700) — no Arial fallback.
- **xfade-aware ASS timing:** ASS timeline must subtract the dissolve overlaps — partB cues shift -0.3s, partC cues shift -0.6s. make_ass_v2.py probes actual rendered seg durations and applies this. 185 cues, 6 NEBULA styles (no stroke, drop shadow only, Bold).
- **ChatGPT brand badge:** no PNG in brand-logos/ (folder has only README), so used Impact_HUD ASS text badge fallback at demo start (~1:38).

See [[promptengineering-v10-session]].
