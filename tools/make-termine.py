#!/usr/bin/env python3
"""Baut die Terminkarten und die Kalenderdatei aus tools/termine.json.

Termine ändern: nur tools/termine.json bearbeiten, dann im Projektordner:  python3 tools/make-termine.py
Die Karten stehen in den HTML-Seiten zwischen den Markern  <!-- TERMINE:start ... -->  und  <!-- TERMINE:end -->.
Karten nie direkt im HTML ändern.

Eintrag in termine.json:
  {"datum": "2026-12-05", "zeit": "19:00–21:30", "art": "inner-trance-dance",
   "ort": "Ort", "preis": "XX €", "hinweis": "optional", "extern": "https://… (optional, sonst Anmelden per Mail)"}
Arten: inner-trance-dance, msc, workshop. Optional: "titel" überschreibt den Standardtitel.
Vergangene Termine werden nicht ausgegeben."""
import json, re, pathlib, datetime as dt
from urllib.parse import quote

ROOT = pathlib.Path(__file__).resolve().parent.parent
MAIL = "kontakt@bettinawyciok.de"
ARTEN = {
    "inner-trance-dance": "Inner Trance Dance",
    "msc": "Achtsames Selbstmitgefühl (MSC)",
    "workshop": "Workshop",
}
LEER = {"inner-trance-dance": "Der erste Termin ist in Planung.", "msc": "Termin folgt.", "msc,workshop": "Termin folgt."}
SEITEN = ["index.html", "inner-trance-dance/index.html", "workshops-seminare/index.html"]
TAGE = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]
MONATE = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
KURZ = ["Jan", "Feb", "Mär", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Dez"]

def esc(t):
    return (t or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

termine = json.loads((ROOT / "tools" / "termine.json").read_text(encoding="utf-8"))
heute = dt.date.today()
termine = sorted([t for t in termine if dt.date.fromisoformat(t["datum"]) >= heute], key=lambda t: (t["datum"], t.get("zeit", "")))

def karte(t):
    d = dt.date.fromisoformat(t["datum"])
    titel = t.get("titel") or ARTEN.get(t["art"], t["art"])
    lang = f"{TAGE[d.weekday()]}, {d.day}. {MONATE[d.month-1]} {d.year}"
    zeile = " · ".join(x for x in [lang, t.get("zeit"), t.get("ort")] if x)
    extra = " · ".join(x for x in [t.get("preis"), t.get("hinweis")] if x)
    if t.get("extern"):
        knopf = f'<a class="knopf klein" href="{esc(t["extern"])}" target="_blank" rel="noopener">Anmelden</a>'
    else:
        betreff = quote(f"Anmeldung {titel} {d.day}. {MONATE[d.month-1]} {d.year}")
        knopf = f'<a class="knopf klein" href="mailto:{MAIL}?subject={betreff}">Anmelden</a>'
    return (f'<article class="termin" data-datum="{t["datum"]}"><div class="termin-datum"><b>{d.day}</b><span>{KURZ[d.month-1]}</span></div>'
            f'<div><h3>{esc(titel)}</h3><p>{esc(zeile)}</p>' + (f'<p>{esc(extra)}</p>' if extra else "") + f'</div>{knopf}</article>')

def ics():
    out = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Lebensfäden//Termine//DE", "CALSCALE:GREGORIAN", "X-WR-CALNAME:Lebensfäden Termine"]
    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    for t in termine:
        d = t["datum"].replace("-", "")
        z = re.findall(r"(\d{1,2}):(\d{2})", t.get("zeit", ""))
        titel = t.get("titel") or ARTEN.get(t["art"], t["art"])
        ev = ["BEGIN:VEVENT", f"UID:{t['datum']}-{t['art']}@lebensfaeden", f"DTSTAMP:{stamp}", "SUMMARY:" + titel]
        if len(z) >= 2:
            ev += [f"DTSTART;TZID=Europe/Berlin:{d}T{int(z[0][0]):02d}{z[0][1]}00", f"DTEND;TZID=Europe/Berlin:{d}T{int(z[1][0]):02d}{z[1][1]}00"]
        else:
            ev += [f"DTSTART;VALUE=DATE:{d}"]
        if t.get("ort"):
            ev.append("LOCATION:" + t["ort"].replace(",", "\\,"))
        ev.append("END:VEVENT")
        out += ev
    out.append("END:VCALENDAR")
    return "\r\n".join(out) + "\r\n"

MARKER = re.compile(r'(<!-- TERMINE:start (?P<attr>[^>]*?) -->)(?P<inhalt>.*?)(<!-- TERMINE:end -->)', re.S)

def baue(attr):
    a = {k: (v1 or v2) for k, v1, v2 in re.findall(r'(\w+)=(?:"([^"]*)"|(\S+))', attr)}
    arten = a.get("art", "alle")
    rahmen = a.get("rahmen", "block")
    maxn = int(a.get("max", "6"))
    titel = a.get("titel", "Termine")
    treffer = [t for t in termine if arten == "alle" or t["art"] in arten.split(",")][:maxn]
    if not treffer:
        if rahmen == "section":
            return ""
        return f'<div class="fehlt-block"><p>{LEER.get(arten, "Termin folgt.")}</p></div>'
    karten = '<div class="termine">' + "".join(karte(t) for t in treffer) + "</div>"
    if rahmen == "section":
        return f'<section class="abschnitt gold"><div class="innen"><h2>{esc(titel)}</h2>{karten}</div></section>'
    return karten

geaendert = 0
for rel in SEITEN:
    f = ROOT / rel
    if not f.exists():
        continue
    s = f.read_text(encoding="utf-8")
    neu = MARKER.sub(lambda m: m.group(1) + baue(m.group("attr")) + m.group(4), s)
    if neu != s:
        f.write_text(neu, encoding="utf-8"); geaendert += 1
if termine:
    (ROOT / "termine.ics").write_text(ics(), encoding="utf-8")
print(f"{len(termine)} kommende Termine, {geaendert} Seite(n) aktualisiert")
