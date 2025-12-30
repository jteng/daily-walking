"""Generate PNG app icons (192x192 and 512x512).

This script uses Pillow to render a simple blue rounded-square icon with a white
capital B in the center. It writes files into ./icons/icon-192.png and
./icons/icon-512.png.

Usage:
  python3 -m pip install pillow
  python3 scripts/generate_icons.py

If you prefer a different icon design, modify the drawing parameters below.
"""

from PIL import Image, ImageDraw, ImageFont
import os

OUT_DIR = os.path.join(os.path.dirname(__file__), "..", "icons")
os.makedirs(OUT_DIR, exist_ok=True)


def draw_icon(size, out_path):
    bg = (74, 144, 226)  # #4A90E2
    fg = (255, 255, 255)
    r = size // 8  # corner radius

    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # rounded rectangle background
    draw.rounded_rectangle([(0, 0), (size - 1, size - 1)], radius=r, fill=bg)

    # draw a white 'B' in the center
    try:
        # try to use a default sans-serif font; fallback to built-in font
        font = ImageFont.truetype("Arial.ttf", size * 40 // 100)
    except Exception:
        try:
            font = ImageFont.truetype(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", size * 40 // 100
            )
        except Exception:
            font = ImageFont.load_default()

    text = "B"
    # PIL versions differ: prefer font.getsize, fall back to draw.textbbox
    try:
        w, h = font.getsize(text)
    except Exception:
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
        except Exception:
            # last resort: estimate
            w = h = size * 0.4

    draw.text(((size - w) / 2, (size - h) / 2 - size * 0.03), text, font=font, fill=fg)

    img.save(out_path, format="PNG")
    print("Wrote", out_path)


if __name__ == "__main__":
    draw_icon(192, os.path.join(OUT_DIR, "icon-192.png"))
    draw_icon(512, os.path.join(OUT_DIR, "icon-512.png"))
