"""Build the optimised media set for the new site (WebP + one looping video).

Source photos: Pexels (free licence). Coach portraits: the club's own photos.
Run:  python tools/media.py
"""
from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / ".tmp" / "shortlist"
OUT = ROOT / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)
VIDEO_OUT = ROOT / "assets" / "video"
VIDEO_OUT.mkdir(parents=True, exist_ok=True)

# name, source id, aspect (w:h), focus (0=top, .5=centre, 1=bottom), max width
STOCK = [
    ("hero-action",     40136712, (4, 5), 0.42, 1200),
    ("racket-night",    32897040, (3, 4), 0.50, 1000),
    ("court-indoor",    38155778, (7, 5), 0.50, 1400),
    ("class-init",      34079995, (4, 3), 0.50, 1200),
    ("class-int",       36227708, (4, 3), 0.42, 1200),
    ("class-comp",      32349891, (4, 3), 0.46, 1200),
    ("coach-kids",      34399237, (3, 2), 0.50, 1200),
    ("mar-menor-sunset", 34052998, (16, 9), 0.55, 1400),
    ("playa-santiago",  19879692, (4, 5), 0.45, 1000),
    ("mar-menor-boats", 34122273, (4, 3), 0.45, 1200),
    ("snow",            16573043, (4, 3), 0.62, 1200),
    ("cove",            14853236, (3, 2), 0.50, 1200),
    ("facilities",      32474981, (7, 5), 0.50, 1400),
    ("woman-action",    40399379, (4, 5), 0.40, 1000),
    ("man-sitting",     33083430, (4, 5), 0.42, 1000),
    ("coast",           36732258, (4, 3), 0.50, 1200),
]

COACHES = [
    ("coach-dani",    "dani.jpg"),
    ("coach-alberto", "alberto.jpg"),
    ("coach-carlos",  "carlos.jpg"),
    ("coach-jorge",   "jorge.jpg"),
    ("coach-pedro",   "pedro.jpg"),
    ("coach-antonio", "antonio.jpg"),
]


def crop_to(img: Image.Image, aspect: tuple[int, int], focus: float) -> Image.Image:
    tw, th = aspect
    w, h = img.size
    target = tw / th
    if w / h > target:                    # too wide -> crop sides
        new_w = int(h * target)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:                                 # too tall -> crop vertically around focus
        new_h = int(w / target)
        top = int((h - new_h) * focus)
        img = img.crop((0, top, w, top + new_h))
    return img


def save_webp(img: Image.Image, dest: Path, quality: int = 78) -> None:
    img.save(dest, "WEBP", quality=quality, method=6)


def build_stock() -> None:
    for name, pid, aspect, focus, max_w in STOCK:
        src = SRC / f"{pid}.jpg"
        if not src.exists():
            print(f"!! missing {src}")
            continue
        img = Image.open(src).convert("RGB")
        img = ImageOps.exif_transpose(img)
        img = crop_to(img, aspect, focus)
        if img.width > max_w:
            img = img.resize((max_w, round(max_w * img.height / img.width)), Image.LANCZOS)
        dest = OUT / f"{name}.webp"
        save_webp(img, dest)
        print(f"{dest.name:26s} {img.width}x{img.height}  {dest.stat().st_size // 1024} KB")


def build_coaches() -> None:
    for name, filename in COACHES:
        src = ROOT / "img" / filename
        if not src.exists():
            print(f"!! missing {src}")
            continue
        img = Image.open(src).convert("RGB")
        img = ImageOps.exif_transpose(img)
        if name == "coach-jorge":          # source is a placeholder silhouette, skip
            continue
        w, h = img.size
        crop_w = int(w * 0.64)
        crop_h = int(crop_w * 5 / 4)
        left = int((w - crop_w) * 0.5)
        top = int((h - crop_h) * 0.20)
        img = img.crop((left, top, left + crop_w, top + crop_h))
        if img.width > 900:
            img = img.resize((900, round(900 * img.height / img.width)), Image.LANCZOS)
        dest = OUT / f"{name}.webp"
        save_webp(img, dest, quality=80)
        print(f"{dest.name:26s} {img.width}x{img.height}  {dest.stat().st_size // 1024} KB")


def build_og() -> None:
    src = SRC / "40136712.jpg"
    img = Image.open(src).convert("RGB")
    img = crop_to(img, (1200, 630), 0.35)
    img = img.resize((1200, 630), Image.LANCZOS)
    dest = OUT / "og.jpg"
    img.save(dest, "JPEG", quality=82, optimize=True, progressive=True)
    print(f"{dest.name:26s} 1200x630  {dest.stat().st_size // 1024} KB")


def build_video() -> None:
    src = ROOT / ".tmp" / "v992695.mp4"
    if not src.exists():
        print("!! missing source video")
        return
    dest = VIDEO_OUT / "club-loop.mp4"
    vf = (
        "eq=contrast=1.08:saturation=1.18:brightness=-0.03:gamma=0.98,"
        "scale=1280:720:force_original_aspect_ratio=increase,crop=1280:720,"
        "unsharp=5:5:0.4"
    )
    cmd = [
        "ffmpeg", "-y", "-loglevel", "error",
        "-i", str(src), "-t", "9.4",
        "-vf", vf,
        "-an", "-c:v", "libx264", "-profile:v", "high", "-crf", "28",
        "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        str(dest),
    ]
    subprocess.run(cmd, check=True)
    poster = VIDEO_OUT / "club-loop-poster.webp"
    subprocess.run([
        "ffmpeg", "-y", "-loglevel", "error", "-ss", "1.5", "-i", str(src),
        "-frames:v", "1",
        "-vf", "eq=contrast=1.06:saturation=1.14:brightness=-0.04:gamma=0.97,scale=1280:-1",
        str(VIDEO_OUT / "_poster.jpg"),
    ], check=True)
    Image.open(VIDEO_OUT / "_poster.jpg").save(poster, "WEBP", quality=76, method=6)
    (VIDEO_OUT / "_poster.jpg").unlink()
    print(f"{dest.name}  {dest.stat().st_size // 1024} KB")
    print(f"{poster.name}  {poster.stat().st_size // 1024} KB")


if __name__ == "__main__":
    build_stock()
    build_coaches()
    build_og()
    build_video()
