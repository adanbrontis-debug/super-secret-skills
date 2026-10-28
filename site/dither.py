"""Trama una imagen a dos tonos: tinta y el color del tramo de arcoíris de la skill.

Uso:  python3 -I site/dither.py ENTRADA SALIDA.png NUM TOTAL [--size 224] [--gamma 0.6] [--algo atkinson]

Necesita ffmpeg para leer la imagen. Todo lo demás es Python puro.
La salida es un PNG con paleta de 1 bit, así que pesa muy poco.
"""
import argparse
import struct
import subprocess
import sys
import zlib

INK = (17, 17, 17)
STOPS = ["#00a6e0", "#5b4bff", "#c13cff", "#ff2d8a", "#ff5a1f", "#ffb000", "#d7ff1f"]


def hex_rgb(h):
    n = int(h[1:], 16)
    return (n >> 16, (n >> 8) & 255, n & 255)


def sample(t):
    """Mismo arcoíris que usa el sitio, para que cada skill conserve su color."""
    t = min(1.0, max(0.0, t))
    p = t * (len(STOPS) - 1)
    i = min(len(STOPS) - 2, int(p))
    f = p - i
    a, b = hex_rgb(STOPS[i]), hex_rgb(STOPS[i + 1])
    return tuple(round(a[k] + (b[k] - a[k]) * f) for k in range(3))


def load_gray(path, size):
    cmd = ["ffmpeg", "-v", "error", "-i", path,
           "-vf", f"scale={size}:{size}:force_original_aspect_ratio=increase:flags=area,crop={size}:{size},format=gray",
           "-f", "rawvideo", "-"]
    raw = subprocess.run(cmd, check=True, capture_output=True).stdout
    if len(raw) != size * size:
        sys.exit(f"ffmpeg devolvió {len(raw)} bytes, esperaba {size * size}")
    return [v / 255.0 for v in raw]


def levels(px, lo_pct=0.02, hi_pct=0.98, gamma=1.0):
    s = sorted(px)
    lo, hi = s[int(len(s) * lo_pct)], s[int(len(s) * hi_pct) - 1]
    span = max(hi - lo, 1e-6)
    return [min(1.0, max(0.0, (v - lo) / span)) ** gamma for v in px]


def atkinson(px, w, h):
    """Atkinson reparte solo 3/4 del error: deja blancos y negros limpios, como en las Mac de los ochenta."""
    buf = px[:]
    out = bytearray(w * h)
    for y in range(h):
        for x in range(w):
            i = y * w + x
            old = buf[i]
            new = 1.0 if old >= 0.5 else 0.0
            out[i] = 1 if new else 0
            err = (old - new) / 8.0
            for dx, dy in ((1, 0), (2, 0), (-1, 1), (0, 1), (1, 1), (0, 2)):
                xx, yy = x + dx, y + dy
                if 0 <= xx < w and yy < h:
                    buf[yy * w + xx] += err
    return out


def floyd(px, w, h):
    """Floyd-Steinberg reparte todo el error: conserva mejor los medios tonos."""
    buf = px[:]
    out = bytearray(w * h)
    for y in range(h):
        for x in range(w):
            i = y * w + x
            old = buf[i]
            new = 1.0 if old >= 0.5 else 0.0
            out[i] = 1 if new else 0
            err = old - new
            for dx, dy, k in ((1, 0, 7), (-1, 1, 3), (0, 1, 5), (1, 1, 1)):
                xx, yy = x + dx, y + dy
                if 0 <= xx < w and yy < h:
                    buf[yy * w + xx] += err * k / 16.0
    return out


BAYER4 = [[0, 8, 2, 10], [12, 4, 14, 6], [3, 11, 1, 9], [15, 7, 13, 5]]


def bayer(px, w, h):
    """Patrón ordenado 4×4: la trama se ve como textura regular, igual que en los gráficos de 1 bit de los ochenta."""
    out = bytearray(w * h)
    for y in range(h):
        for x in range(w):
            t = (BAYER4[y % 4][x % 4] + 0.5) / 16.0
            out[y * w + x] = 1 if px[y * w + x] > t else 0
    return out


ALGOS = {"atkinson": atkinson, "floyd": floyd, "bayer": bayer}


def write_png(path, bits, w, h, dark, light):
    rows = bytearray()
    for y in range(h):
        rows.append(0)
        byte, n = 0, 0
        for x in range(w):
            byte = (byte << 1) | bits[y * w + x]
            n += 1
            if n == 8:
                rows.append(byte)
                byte, n = 0, 0
        if n:
            rows.append(byte << (8 - n))

    def chunk(tag, data):
        c = tag + data
        return struct.pack(">I", len(data)) + c + struct.pack(">I", zlib.crc32(c) & 0xFFFFFFFF)

    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", w, h, 1, 3, 0, 0, 0))
    png += chunk(b"PLTE", bytes(dark) + bytes(light))
    png += chunk(b"IDAT", zlib.compress(bytes(rows), 9))
    png += chunk(b"IEND", b"")
    with open(path, "wb") as f:
        f.write(png)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("num", type=int)
    ap.add_argument("total", type=int)
    ap.add_argument("--size", type=int, default=224)
    ap.add_argument("--gamma", type=float, default=0.6)
    ap.add_argument("--algo", choices=sorted(ALGOS), default="atkinson")
    a = ap.parse_args()
    px = levels(load_gray(a.src, a.size), gamma=a.gamma)
    bits = ALGOS[a.algo](px, a.size, a.size)
    color = sample((a.num - 0.5) / a.total)
    write_png(a.dst, bits, a.size, a.size, INK, color)
    print(f"{a.dst} · {a.size}px · color {'#%02x%02x%02x' % color}")


if __name__ == "__main__":
    main()
