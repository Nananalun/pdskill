#!/usr/bin/env python3
"""Prepare a start-frame workspace from a Markdown visual script and source frames.

The script is intentionally conservative. It extracts shot time ranges from a
Markdown table, chooses nearest local source frames, copies them into per-shot
folders, and writes a JSON manifest for manual/director review.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import shutil
from pathlib import Path


TIME_RE = re.compile(r"(?P<start>\d+(?:\.\d+)?)\s*[-~至到]\s*(?P<end>\d+(?:\.\d+)?)\s*s?", re.I)


def parse_duration(metadata_path: Path) -> float | None:
    if not metadata_path.exists():
        return None
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    duration = metadata.get("format", {}).get("duration")
    if duration is not None:
        return float(duration)
    for stream in metadata.get("streams", []):
        if stream.get("codec_type") == "video" and stream.get("duration"):
            return float(stream["duration"])
    return None


def table_rows(markdown: str) -> list[list[str]]:
    rows: list[list[str]] = []
    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line.startswith("|") or not line.endswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if not cells or all(set(cell) <= {"-", ":"} for cell in cells):
            continue
        rows.append(cells)
    return rows


def extract_shots(markdown: str) -> list[dict]:
    rows = table_rows(markdown)
    shots: list[dict] = []
    for cells in rows:
        joined = " | ".join(cells)
        match = TIME_RE.search(cells[0]) or TIME_RE.search(joined)
        if not match:
            continue
        if cells[0].lower() in {"time", "时间"}:
            continue
        start = float(match.group("start"))
        end = float(match.group("end"))
        shot_id = f"G{len(shots) + 1:02d}"
        shots.append(
            {
                "shot_id": shot_id,
                "time_range": f"{start:g}-{end:g}s",
                "start_seconds": start,
                "end_seconds": end,
                "cells": cells,
                "raw_row": joined,
            }
        )
    return shots


def sorted_frames(path: Path, pattern: str) -> list[Path]:
    return sorted(path.glob(pattern), key=lambda p: p.name)


def choose_frame(
    start_seconds: float,
    overview_frames: list[Path],
    opening_frames: list[Path],
    duration: float | None,
    opening_fps: float,
) -> tuple[Path | None, str]:
    if start_seconds <= 18 and opening_frames:
        index = max(1, int(math.floor(start_seconds * opening_fps)) + 1)
        index = min(index, len(opening_frames))
        return opening_frames[index - 1], f"opening_frames nearest to {start_seconds:g}s"

    if overview_frames:
        if duration and len(overview_frames) > 1:
            interval = duration / len(overview_frames)
        else:
            interval = 2.0
        index = max(1, int(math.floor(start_seconds / interval)) + 1)
        index = min(index, len(overview_frames))
        return overview_frames[index - 1], f"overview frames nearest to {start_seconds:g}s"

    return None, "no source frame available"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a per-shot start-frame manifest and reference folders.")
    parser.add_argument("--script", required=True, help="Markdown visual script path")
    parser.add_argument("--evidence-dir", required=True, help="Directory produced by prepare_video_evidence.py")
    parser.add_argument("--out", required=True, help="Output directory for start-frame workspace")
    parser.add_argument("--opening-fps", type=float, default=2.0, help="Opening frame sampling FPS")
    args = parser.parse_args()

    script_path = Path(args.script).resolve()
    evidence_dir = Path(args.evidence_dir).resolve()
    out_dir = Path(args.out).resolve()
    refs_dir = out_dir / "source-frame-refs"
    shot_dirs_dir = out_dir / "shots"
    refs_dir.mkdir(parents=True, exist_ok=True)
    shot_dirs_dir.mkdir(parents=True, exist_ok=True)

    markdown = script_path.read_text(encoding="utf-8")
    shots = extract_shots(markdown)
    duration = parse_duration(evidence_dir / "metadata.json")
    overview_frames = sorted_frames(evidence_dir / "frames", "*.jpg")
    opening_frames = sorted_frames(evidence_dir / "opening_frames", "*.jpg")

    manifest: list[dict] = []
    for shot in shots:
        frame, reason = choose_frame(
            shot["start_seconds"],
            overview_frames,
            opening_frames,
            duration,
            args.opening_fps,
        )
        shot_dir = shot_dirs_dir / shot["shot_id"]
        shot_dir.mkdir(parents=True, exist_ok=True)
        copied_frame = None
        if frame:
            copied_frame = refs_dir / f"{shot['shot_id']}-{frame.name}"
            shutil.copy2(frame, copied_frame)
            shutil.copy2(frame, shot_dir / f"source-{frame.name}")

        manifest.append(
            {
                **shot,
                "source_frame": str(copied_frame) if copied_frame else None,
                "source_frame_reason": reason,
                "shot_dir": str(shot_dir),
                "start_frame_output": str(shot_dir / f"{shot['shot_id']}-start.png"),
                "needs_director_review": True,
                "overlay_plan": {
                    "include_in_generated_image": [],
                    "add_in_post": [],
                },
            }
        )

    summary = {
        "script": str(script_path),
        "evidence_dir": str(evidence_dir),
        "out": str(out_dir),
        "shot_count": len(manifest),
        "duration_seconds": duration,
        "overview_frame_count": len(overview_frames),
        "opening_frame_count": len(opening_frames),
        "manifest": manifest,
    }
    (out_dir / "shot_manifest.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
