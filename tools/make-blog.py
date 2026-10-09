#!/usr/bin/env python3
"""Baut den Blog aus Markdown-Dateien in blog/beitraege/.

Neuen Beitrag anlegen: Datei blog/beitraege/mein-beitrag.md mit diesem Kopf schreiben:
---
titel: Titel des Beitrags
datum: 2026-11-02
auszug: Ein bis zwei Sätze für die Übersicht.
bild: dateiname.webp        (optional, liegt in bilder/)
bild_alt: Beschreibung des Bildes
---
Text mit  ## Zwischenüberschrift,  - Aufzählung,  **fett**,  *kursiv*,  [Link](https://…),  > Zitat

Danach im Projektordner:  python3 tools/make-blog.py
Dateien, die mit einem Unterstrich beginnen (zum Beispiel _vorlage.md), werden ausgelassen.
Erzeugt: blog/<name>/index.html für jeden Beitrag, die Übersicht in blog/index.html, den Startseiten-Teaser
und die Einträge in sitemap.xml (jeweils zwischen den Markern <!-- BLOG:start --> ... <!-- BLOG:end -->)."""
import re, pathlib, datetime as dt, html

ROOT = pathlib.Path(__file__).resolve().parent.parent
SITE = "https://koojaa92.github.io/Bettina-Website"
MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
esc = html.escape

def lies(pfad):
    s = pfad.read_text(encoding="utf-8")
    m = re.match(r"---\s*\n(.*?)\n---\s*\n(.*)", s, re.S)
    if not m:
        raise SystemExit(f"{pfad.name}: Kopf zwischen --- fehlt")
    meta = {}
    for z in m.group(1).splitlines():
        if ":" in z:
            k, v = z.split(":", 1); meta[k.strip()] = v.strip()
    for k in ("titel", "datum"):
        if k not in meta:
            raise SystemExit(f"{pfad.name}: '{k}' fehlt im Kopf")
    meta["slug"] = pfad.stem
    meta["text"] = m.group(2).strip()
    return meta

def inline(t):
    t = esc(t)
    t = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", lambda m: f'<img src="../../bilder/{m.group(2)}" alt="{m.group(1)}" loading="lazy">', t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", t)
    return t

def markdown(text):
    out, liste, absatz = [], [], []
    def abs_():
        if absatz:
            out.append("<p>" + inline(" ".join(absatz)) + "</p>"); absatz.clear()
    def lst():
        if liste:
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in liste) + "</ul>"); liste.clear()
    for z in text.splitlines():
        if not z.strip():
            abs_(); lst(); continue
        if z.startswith("### "): abs_(); lst(); out.append(f"<h3>{inline(z[4:])}</h3>")
        elif z.startswith("## "): abs_(); lst(); out.append(f"<h2>{inline(z[3:])}</h2>")
        elif z.startswith("> "): abs_(); lst(); out.append(f"<blockquote>{inline(z[2:])}</blockquote>")
        elif re.match(r"[-*] ", z): abs_(); liste.append(z[2:])
        else: lst(); absatz.append(z.strip())
    abs_(); lst()
    return "\n".join(out)

def datum_lang(d):
    d = dt.date.fromisoformat(d)
    return f"{d.day}. {MONATE[d.month-1]} {d.year}"

def karte(b, pre):
    bild = (f'<div class="bild"><img src="{pre}bilder/{b["bild"]}" alt="{esc(b.get("bild_alt", ""))}" loading="lazy"></div>'
            if b.get("bild") else '<div class="bild"><figure class="platzhalter r43" role="img" aria-label="Kein Bild"><span>Bild folgt</span></figure></div>')
    return (f'<a class="beitrag" href="{pre_link(pre)}{b["slug"]}/">{bild}<span class="datum">{datum_lang(b["datum"])}</span>'
            f'<h3>{esc(b["titel"])}</h3><p>{esc(b.get("auszug", ""))}</p></a>')

def pre_link(pre):
    return "blog/" if pre == "" else ""

beitraege = sorted([lies(p) for p in (ROOT / "blog" / "beitraege").glob("*.md") if not p.name.startswith("_")], key=lambda b: b["datum"], reverse=True)

# Rahmen (Kopf und Fuß) aus der Übersichtsseite übernehmen
uebersicht = (ROOT / "blog" / "index.html").read_text(encoding="utf-8")
kopf_teil = uebersicht[: uebersicht.index('<main id="inhalt">')]
fuss_teil = uebersicht[uebersicht.index("</main>"):]
def tiefer(t):
    return re.sub(r'(href|src)="\.\./', r'\1="../../', t)
kopf_teil, fuss_teil = tiefer(kopf_teil), tiefer(fuss_teil)

for b in beitraege:
    ziel = ROOT / "blog" / b["slug"] / "index.html"
    ziel.parent.mkdir(parents=True, exist_ok=True)
    kopf = re.sub(r"<title>.*?</title>", f"<title>{esc(b['titel'])} · Lebensfäden</title>", kopf_teil)
    bildteil = (f'<div class="artikel-bild"><img src="../../bilder/{b["bild"]}" alt="{esc(b.get("bild_alt", ""))}"></div>' if b.get("bild") else "")
    seite = (kopf + '<main id="inhalt">\n'
             f'<header class="artikel-kopf"><div class="innen"><p class="datum">{datum_lang(b["datum"])}</p><h1>{esc(b["titel"])}</h1></div></header>\n'
             f'{bildteil}\n<article class="artikel">\n{markdown(b["text"])}\n<a class="zurueck" href="../">← Alle Beiträge</a>\n</article>\n' + fuss_teil)
    ziel.write_text(seite, encoding="utf-8")

def ersetze(rel, start, ende, inhalt):
    f = ROOT / rel
    if not f.exists():
        return
    s = f.read_text(encoding="utf-8")
    muster = re.compile(r"(<!-- " + start + r"[^>]*-->)(.*?)(<!-- " + ende + r" -->)", re.S)
    if muster.search(s):
        f.write_text(muster.sub(lambda m: m.group(1) + inhalt + m.group(3), s), encoding="utf-8")

# Übersicht
if beitraege:
    raster = '<div class="blog-raster">' + "".join(karte(b, "../") for b in beitraege) + "</div>"
    raster = raster.replace('href="../blog/', 'href="')
else:
    leer = '<div class="beitrag beitrag-leer"><div class="bild"><figure class="platzhalter r43" role="img" aria-label="Platz für einen Beitrag"><span>Platz für einen Beitrag</span></figure></div><span class="datum">folgt</span><h3>Der erste Beitrag erscheint bald.</h3></div>'
    raster = f'<p class="einleitung">Der erste Beitrag erscheint bald.</p><div class="blog-raster">{leer * 3}</div>'
ersetze("blog/index.html", "BLOG:start", "BLOG:end", raster)

# Teaser auf der Startseite (nur wenn es Beiträge gibt)
if beitraege:
    n = 3
    teaser = ('<section class="abschnitt tint"><div class="innen"><h2>Aus dem Blog</h2><div class="blog-raster">'
              + "".join(karte(b, "") for b in beitraege[:n]) + '</div><div class="knoepfe"><a class="knopf leise" href="blog/">Alle Beiträge</a></div></div></section>')
else:
    teaser = ""
ersetze("index.html", "BLOG-TEASER:start", "BLOG-TEASER:end", teaser)

# Sitemap
urls = "".join(f"\n  <url><loc>{SITE}/blog/{b['slug']}/</loc><lastmod>{b['datum']}</lastmod></url>" for b in beitraege) + ("\n  " if beitraege else "")
ersetze("sitemap.xml", "BLOG-URLS:start", "BLOG-URLS:end", urls)
print(f"{len(beitraege)} Beitrag/Beiträge gebaut")
