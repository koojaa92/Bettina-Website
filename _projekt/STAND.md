# Bettina Website: Projektstand und offene Punkte

Stand: 2026-10-09. Vorschau: https://koojaa92.github.io/Bettina-Website/ (Entwurf 3, `noindex`, nicht freigegeben).

## Was steht
- Entwurf 3 nach `_projekt/GRUNDLAGE.md`: Wortmarke „Lebensfäden“ mit „Bettina Wyciok“ im Kopf, Navigation Einzel · Paare · Inner Trance Dance · Kurse · Blog · Über mich plus „Gespräch vereinbaren“, kleine Symbole für Telegram, Instagram und E-Mail oben rechts (Telegram und Instagram ohne Link, ausgegraut, bis die Adressen vorliegen).
- Seiten: Start, `/einzelbegleitung/`, `/paarbegleitung/`, `/inner-trance-dance/`, `/workshops-seminare/` (Kurse und Workshops), `/blog/`, `/about/`, `/contact/`, Impressum und Datenschutz (Platzhalter).
- Farben: Fuchsia und Goldgelb auf Weiß, Schriften Literata und Nunito Sans. Siehe `DESIGN.md`. Der Faden läuft als feine Goldlinie durch die Seite.
- Alle Texte in Du. „Gespräch vereinbaren“ und „Anmelden“ sind Mail-Knöpfe. Fehlende Angaben sind sichtbare graue Platzhalter („fehlt“).
- Werkzeuge: `tools/make-termine.py` mit `tools/termine.json` (Terminkarten und `termine.ics`), `tools/make-blog.py` mit `blog/beitraege/*.md` (Vorlage `_vorlage.md`). Beide laufen mit `python3 tools/<name>.py`.
- Technik: statisches HTML, eine `styles.css`, eine `main.js`. `noindex` und `Disallow: /` gesetzt. Bei 390 und 1280 px geprüft, nicht auf einem echten iPhone.

## Bildplätze (Dateiname in `bilder/`, fehlt die Datei, steht ein grauer Platz)
`hero` (Start), `person` (Wer ich bin), `ueber-kopf` (Über mich), `raum` (Praxisraum, Paar-Karte und Einzelseite), `einzel` (Karte Einzel), `ifs` (bunte Figuren, Seite Einzel), `itd` (Inner Trance Dance), `msc` (MSC), `faden` (Natur, Startseite), `arbeit` (Fuchsia-Gemälde als Hintergrund bei „Wie ich arbeite“), `fuss` (Footer-Hintergrund), `einzel-kopf`, `paar-kopf`, `itd-kopf`, `kurse-kopf`, `blog-kopf`, `kontakt-kopf` (Bilder in den Seitenköpfen), `ort` (Haus im Schwarzwald, Über mich), `paar-raum`.
Vorhanden: `hero`, `person`, `ueber-kopf`, `raum`. Dateiformat WebP, Breite 1200 bis 1600 px.

## Offene Punkte
- [ ] Bilder als Dateien liefern und zuordnen (Liste oben)
- [ ] Links für Telegram-Gruppe und Instagram
- [ ] Inner Trance Dance: Termin, Ort, Dauer, Preis, Ablauf, Musik
- [ ] MSC: Zeit, Ort, Ablauf, Preis, externer Link
- [ ] Einzel und Paar: Ablauf einer Sitzung, für wen, was Menschen mitnehmen, häufigste Fragen, Hinweis
- [ ] Texte mit Bettina abgleichen und freigeben, inklusive Du-Fassung
- [ ] Fuchsia: Ton bestätigen (dunkler oder heller?)
- [ ] Impressum und Datenschutz mit ihren Angaben
- [ ] Domain, Link-Vorschau und Sitemap beim Live-Gang
- [ ] Vor Live-Gang: `noindex` und `Disallow` entfernen, `sitemap.xml` und `llms.txt` mit echter Domain füllen

## Entschieden
- Name „Lebensfäden“ wird als Wortmarke für alles ausprobiert (9.10.2026).
- Eigenständiges Projekt, unabhängig von essential-guidance.space.
- Vorschau über GitHub Pages, keine Domain nötig. Kein Bauen im Artefakt.
- Arbeitsstil: wenig Technik zeigen, bei echten Problemen fragen, Alternativen nennen.
- **Das Repo ist öffentlich: nur Website-Texte, Bauregeln und Stand. Keine Interviewinhalte, privaten Notizen, rechtlichen Einordnungen oder Namensprüfungen.**
