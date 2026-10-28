"""Arma site/index.html a partir de skills/*/SKILL.md, la-lista.md y site/template.html.

Uso:  python3 -I site/build.py   (desde la carpeta brontis_skills)
"""
import base64
import json
import os
import pathlib
import re
import sys
import unicodedata

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
LISTA = ROOT / "la-lista.md"
TEMPLATE = ROOT / "site" / "template.html"
FICHAS = ROOT / "site" / "fichas.json"
ART = ROOT / "art" / "dither"
DIST = ROOT / "docs"  # GitHub Pages publica esta carpeta
# URL pública del sitio, sin la cual la vista previa en redes no puede apuntar a la imagen. Se puede dar por entorno.
SITE_URL = os.environ.get("SITE_URL", "")
OUT = ROOT / "site" / "index.html"

BLOCK_SLUGS = {
    "Encontrar la idea": "idea",
    "Escribirla": "escribirla",
    "Producirla con IA": "ia",
    "Venderla": "venderla",
    "Oficio": "oficio",
}


def norm(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]", "", s.lower())


def parse_lista():
    rows, block = {}, None
    for line in LISTA.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^## \d+ · (.+)$", line)
        if m:
            block = m.group(1).strip()
            continue
        m = re.match(r"^\| (\d+) \| \*\*(.+?)\*\* \| (.+?) \| (.+?) \| (.+?) \|$", line)
        if m and block:
            num, name, que, regla, origen = m.groups()
            rows[norm(name)] = {
                "num": int(num),
                "name": name.strip(),
                "que": que.strip(),
                "regla": regla.strip(),
                "origen": origen.strip(),
                "block": block,
                "blockSlug": BLOCK_SLUGS[block],
            }
    return rows


def parse_skill(path):
    text = path.read_text(encoding="utf-8")
    fm = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    desc = ""
    if fm:
        m = re.search(r"^description:\s*'(.*)'\s*$", fm.group(1), re.M)
        desc = m.group(1).replace("''", "'") if m else ""
    title = re.search(r"^# (.+)$", text, re.M).group(1).strip()
    return title, desc, text


def main():
    rows = parse_lista()
    fichas = json.loads(FICHAS.read_text(encoding="utf-8"))
    skills = []
    for d in sorted(SKILLS.iterdir()):
        f = d / "SKILL.md"
        if not f.is_file():
            continue
        title, desc, text = parse_skill(f)
        row = rows.get(norm(title))
        if not row:
            sys.exit(f"No encontré '{title}' ({d.name}) en la-lista.md")
        if "BRONTIS_EOF" in text:
            sys.exit(f"{d.name} contiene el marcador BRONTIS_EOF")
        ficha = fichas.get(d.name)
        if not ficha or len(ficha.get("pasos", [])) != 3 or not ficha.get("ejemplos"):
            sys.exit(f"Falta la ficha de {d.name} en site/fichas.json (3 pasos y al menos un ejemplo)")
        art = ART / f"{d.name}.png"
        img = "data:image/png;base64," + base64.b64encode(art.read_bytes()).decode() if art.is_file() else ""
        skills.append({**row, "slug": d.name, "title": title, "desc": desc, "md": text,
                       "pasos": ficha["pasos"], "ejemplos": ficha["ejemplos"], "img": img})
    skills.sort(key=lambda s: s["num"])
    if len(skills) != len(rows):
        faltan = set(r["name"] for r in rows.values()) - set(s["name"] for s in skills)
        sys.exit(f"Faltan carpetas para: {', '.join(sorted(faltan))}")
    data = json.dumps(skills, ensure_ascii=False).replace("</", "<\\/")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/[]", data)
    OUT.write_text(html, encoding="utf-8")
    print(f"{len(skills)} skills → {OUT.relative_to(ROOT)} ({OUT.stat().st_size // 1024} KB)")
    write_dist(html)


def write_dist(html):
    """Versión independiente para cualquier hosting: documento HTML completo con vista previa para redes."""
    head_end = html.index("</style>") + len("</style>")
    head, body = html[:head_end], html[head_end:]
    url = SITE_URL.rstrip("/") + "/" if SITE_URL else ""
    og = f"""
<meta property="og:type" content="website">
<meta property="og:title" content="Super Secret Skills.">
<meta property="og:description" content="Skills para Claude Code que te ayudan en el día a día. By Brontis.">
<meta property="og:image" content="{url}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Super Secret Skills.">
<meta name="twitter:description" content="Skills para Claude Code que te ayudan en el día a día. By Brontis.">
<meta name="twitter:image" content="{url}og.png">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
"""
    if url:
        og += f'<link rel="canonical" href="{url}">\n'
    doc = ("<!doctype html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
           "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
           + head + og + "</head>\n<body>\n" + body + "\n</body>\n</html>\n")
    DIST.mkdir(exist_ok=True)
    (DIST / "index.html").write_text(doc, encoding="utf-8")
    (DIST / "favicon.svg").write_text(FAVICON, encoding="utf-8")
    for extra in ("og.png", "CNAME"):
        src = ROOT / "site" / extra
        if src.is_file():
            (DIST / extra).write_bytes(src.read_bytes())
    print(f"docs/index.html listo ({(DIST / 'index.html').stat().st_size // 1024} KB)" + (f" · URL {url}" if url else " · sin URL pública todavía (SITE_URL)"))


FAVICON = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><defs><linearGradient id="g" x1="0" x2="1"><stop offset="0" stop-color="#00a6e0"/><stop offset=".4" stop-color="#c13cff"/><stop offset=".7" stop-color="#ff5a1f"/><stop offset="1" stop-color="#d7ff1f"/></linearGradient></defs><rect width="64" height="64" rx="14" fill="#111"/><text x="32" y="43" text-anchor="middle" font-family="Helvetica Neue, Arial, sans-serif" font-weight="700" font-size="30" letter-spacing="-1" fill="url(#g)">SSS</text></svg>
"""


if __name__ == "__main__":
    main()
