import os
from PIL import Image, ImageOps, ImageFilter

here = os.path.dirname(os.path.abspath(__file__))
img = Image.open(os.path.join(here, "photo.jpg")).convert("L")
w, h = img.size
img = img.crop((int(w*0.14), int(h*0.02), int(w*0.86), int(h*0.80)))
img = ImageOps.autocontrast(img, cutoff=1)
img = img.filter(ImageFilter.UnsharpMask(radius=3, percent=120))
W, H = 62, 34
img = img.resize((W, H))
ramp = "@&#W%G8P5SYJ?7*!~^:. "  # pure ASCII, dark -> light
n = len(ramp)
lines = []
for yy in range(H):
    row = ""
    for xx in range(W):
        v = img.getpixel((xx, yy)) / 255.0
        v = v ** 0.75
        if v > 0.90:
            row += " "
            continue
        row += ramp[min(n - 1, int(v * n))]
    lines.append(row.rstrip())
open(os.path.join(here, "ascii.txt"), "w", encoding="utf-8").write("\n".join(lines))
print("ascii written:", len(lines), "lines")
