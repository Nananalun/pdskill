#!/usr/bin/env python3
"""Prepare local video evidence for short-video remake analysis.

Requires ffmpeg and ffprobe on PATH.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
from pathlib import Path


def run(cmd: list[str]) -> None:
    subprocess.run(cmd, check=True)


def capture_json(cmd: list[str]) -> dict:
    completed = subprocess.run(
        cmd,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
    )
    return json.loads(completed.stdout)


def count_files(path: Path, pattern: str) -> int:
    return len(list(path.glob(pattern)))


def tile_dims(count: int, max_cols: int) -> tuple[int, int]:
    if count <= 0:
        return (1, 1)
    cols = min(max_cols, count)
    rows = math.ceil(count / cols)
    return cols, rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract metadata, frames, tiles, and audio evidence from a video.")
    parser.add_argument("video", help="Input video path")
    parser.add_argument("--out", required=True, help="Output directory")
    parser.add_argument("--frame-interval", type=float, default=2.0, help="Seconds between overview frames")
    parser.add_argument("--opening-duration", type=float, default=18.0, help="Opening seconds to sample densely")
    parser.add_argument("--opening-fps", type=float, default=2.0, help="Opening sample FPS")
    parser.add_argument("--scale", default="216:384", help="Frame scale, e.g. 216:384")
    parser.add_argument("--max-overview-cols", type=int, default=6)
    parser.add_argument("--max-opening-cols", type=int, default=6)
    args = parser.parse_args()

    if not shutil.which("ffmpeg") or not shutil.which("ffprobe"):
        raise SystemExit("ffmpeg and ffprobe must be available on PATH")

    video = Path(args.video).resolve()
    out = Path(args.out).resolve()
    frames_dir = out / "frames"
    opening_dir = out / "opening_frames"
    frames_dir.mkdir(parents=True, exist_ok=True)
    opening_dir.mkdir(parents=True, exist_ok=True)

    metadata = capture_json([
        "ffprobe",
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(video),
    ])
    (out / "metadata.json").write_text(json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8")

    run([
        "ffmpeg",
        "-y",
        "-i",
        str(video),
        "-vf",
        f"fps=1/{args.frame_interval},scale={args.scale}",
        str(frames_dir / "frame_%03d.jpg"),
    ])

    run([
        "ffmpeg",
        "-y",
        "-i",
        str(video),
        "-t",
        str(args.opening_duration),
        "-vf",
        f"fps={args.opening_fps},scale={args.scale}",
        str(opening_dir / "open_%03d.jpg"),
    ])

    overview_count = count_files(frames_dir, "*.jpg")
    opening_count = count_files(opening_dir, "*.jpg")
    overview_cols, overview_rows = tile_dims(overview_count, args.max_overview_cols)
    opening_cols, opening_rows = tile_dims(opening_count, args.max_opening_cols)

    run([
        "ffmpeg",
        "-y",
        "-framerate",
        "1",
        "-i",
        str(frames_dir / "frame_%03d.jpg"),
        "-vf",
        f"tile={overview_cols}x{overview_rows}:margin=2:padding=2:color=white",
        "-frames:v",
        "1",
        "-update",
        "1",
        str(out / "overview_tile.jpg"),
    ])

    run([
        "ffmpeg",
        "-y",
        "-framerate",
        "1",
        "-i",
        str(opening_dir / "open_%03d.jpg"),
        "-vf",
        f"tile={opening_cols}x{opening_rows}:margin=2:padding=2:color=white",
        "-frames:v",
        "1",
        "-update",
        "1",
        str(out / "opening_tile.jpg"),
    ])

    audio_path = out / "audio_16k_mono.wav"
    run([
        "ffmpeg",
        "-y",
        "-i",
        str(video),
        "-vn",
        "-ac",
        "1",
        "-ar",
        "16000",
        str(audio_path),
    ])

    run([
        "ffmpeg",
        "-y",
        "-i",
        str(audio_path),
        "-filter_complex",
        "showwavespic=s=1200x240:colors=#2b6cb0",
        "-frames:v",
        "1",
        "-update",
        "1",
        str(out / "audio_waveform.png"),
    ])

    summary = {
        "video": str(video),
        "out": str(out),
        "overview_frames": overview_count,
        "opening_frames": opening_count,
        "overview_tile": str(out / "overview_tile.jpg"),
        "opening_tile": str(out / "opening_tile.jpg"),
        "audio": str(audio_path),
        "waveform": str(out / "audio_waveform.png"),
    }
    (out / "run_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
