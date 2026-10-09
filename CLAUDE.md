# CLAUDE.md – Regeln für diese Website

Gilt für jede Sitzung in diesem Repo. Lies zu Beginn auch `_projekt/STAND.md`. Bei einem neuen Projekt zusätzlich `_werkstatt/HANDBUCH.md`.

## Projekt
- Website für: Bettina Wyciok, Einzel- und Paarbegleitung sowie Workshops und Seminare in Freiburg, bei Furtwangen im Schwarzwald und online
- Repo: koojaa92/Bettina-Website. Live ist der Branch `main` (GitHub Pages).
- Domain: voraussichtlich die der bestehenden Seite, Anbieter und DNS noch zu klären. E-Mail an der Domain: [ja/nein]. MX- und TXT-Einträge nie ändern.
- Website-Typ und Ziel: [z. B. Angebots-Website mit Terminen / One-Pager / Portfolio]. Funktionen: [...]
- Aktuelle Phase: Entwurf 2 steht (aus den Texten und Fotos der alten Seite, nicht freigegeben, `noindex`). Entwurf 3 wird nach `_projekt/GRUNDLAGE.md` geplant. Das Interview und die freigegebene Grundlage stehen noch aus. Bewusste Entscheidung von Jakob, den Entwurf vor Phase 3 zu bauen.

## Arbeitsweise
- Sprache: Deutsch, Du-Form, sofern unten nicht anders festgelegt.
- Drei Modi: „nur zeigen“ = Vorschau, nichts ändern. „Sag erst, was du machen würdest“ = Optionen mit Empfehlung, dann warten. „Mach“ = umsetzen, prüfen, live, kurz berichten.
- Vor Phase 4 keinen Code schreiben. Erst Interview und freigegebene Grundlage (`_projekt/GRUNDLAGE.md`).
- Inhaltstexte nie ungefragt umschreiben, nur Vorschläge machen. Technik, Abstände und Struktur selbst verbessern.
- Bei größeren Eingriffen (Layout-Umbau, Texte, SEO-Titel) erst Optionen nennen.
- Bei Unklarem eine präzise Rückfrage statt drei Annahmen.
- Ehrlich sagen, was nicht geprüft werden konnte (echtes iPhone, echte Schrift).
- Entscheidungen sofort in diese Datei oder `_projekt/STAND.md` schreiben, nicht nur im Chat lassen.

## Technik
- Statisches HTML, eine `styles.css`, eine `main.js`. Kein Framework, kein Build-Schritt.
- Bei Änderungen an `styles.css` oder `main.js` die Versionsnummer (`?v=...`) in allen HTML-Dateien hochzählen.
- Jede Änderung bei 390 px und 1280 px per Screenshot prüfen.
- Entwickeln auf eigenem Branch, live mit `git push origin <branch>:main`.
- Abstände zwischen Abschnitten: für Bettina bewusst ruhig und großzügig (Abweichung von der Vorlage, siehe `_projekt/DESIGN.md`). Globale Regel am Ende von `styles.css`.
- Schriften selbst hosten oder über Bunny Fonts, nie direkt von Google Fonts.
- Formulare nur, wenn sie wirklich senden. Sonst Mail-Link.
- FAQ sichtbar und als FAQPage-JSON-LD im `<head>`, beides angleichen. FAQ-Abschnitte mit grauem Hintergrund.
- Termine (falls vorhanden) nur in `tools/termine.json`, danach `python3 tools/make-ics.py`.
- `llms.txt` und `sitemap.xml` bei Änderungen an Angeboten, Preisen oder Seiten mitpflegen.

## Design
- `_projekt/DESIGN.md` ist ein lebendiges Stilbuch, kein starres Regelwerk. Es ist der Ausgangspunkt, Abweichungen sind erwünscht.
- Was Jakob oder die Kundin bewusst anders entscheiden, gilt. Nie zurückdrehen und nie in einen Standard- oder Skill-Look zurückfallen. Die Entscheidung sofort in `DESIGN.md` nachtragen, damit sie bleibt.
- Vor jedem Bericht: Screenshots bei 390 und 1280 px, selbst prüfen.
- Skill: `frontend-design`. Keine weiteren Skills ohne Rückfrage installieren.
- Texte nie ungefragt ändern, auch wenn ein Skill das nahelegt.
- Keine KI-Bilder von Menschen.
- Hintergrund zu Skills und Werkzeugen: `_werkstatt/HANDBUCH.md` Abschnitt 20.

## Datenschutz im Repo
- Das Repo ist öffentlich. Keine Interview-Transkripte, privaten Notizen, Preise der Zusammenarbeit, Passwörter oder privaten Adressen ins Repo.
- Ordner mit Unterstrich (`_projekt/`, `_werkstatt/`) werden nicht als Website ausgeliefert, sind auf GitHub aber sichtbar.

## Recht
- Impressum nach § 5 DDG: Name, ladungsfähige Anschrift, Kontakt. USt-IdNr. nur, wenn vorhanden. Nie Nummern erfinden.
- Datenschutzerklärung nennt jedes eingebundene Tool.
- [Bei Begleitungsangeboten: Hinweis „keine Heilkunde, ersetzt keine Therapie, Teilnahme in Eigenverantwortung“.]

## Marke (Entwurf 9.10.2026, nicht freigegeben)
- Dachmarke und Wortmarke für alles: Lebensfäden (wird ausprobiert, an einer Stelle austauschbar). Absenderin immer sichtbar: Bettina Wyciok.
- Leitgedanke: Verbindung ist das Dach, Aufrichtung die Richtung.
- Angebote: Einzelbegleitung · Paar- und Beziehungsbegleitung · Inner Trance Dance · Kurse und Workshops (MSC).
- Orte: Freiburg · bei Furtwangen im Schwarzwald · online.
- Mail: kontakt@bettinawyciok.de, Betreff je Knopf.
- Anrede: Du (Bettina, 9.10.2026). Texte der alten Seite siezen und werden mechanisch umgestellt.
- Rechtliches: keine Wirkversprechen. Hinweise und Pflichtangaben erst festlegen, wenn Bettinas Angaben vorliegen. Keinen Wortlaut erfinden.
- Die eine Handlung: „Gespräch vereinbaren“ (Mail-Knopf mit Betreff, kein Buchungstool); bei Terminen „Anmelden“ (Mail-Knopf); bei MSC externer Link.
- Schreibweisen: Lebensfäden, Inner Trance Dance, Internal Family Systems (IFS), Mindful Self-Compassion (MSC).
- Wörter immer: Verbindung, Aufrichtung, Mitgefühl, Klarheit, Lebendigkeit, Boden, Wurzeln, Würdigung.
- Wörter nie: Selbstoptimierung, Potenzialentfaltung, Transformation, nachhaltige Veränderung, ganzheitlich, Heilungs- oder Erfolgsversprechen, kostenloses Erstgespräch.
- Gefühl: „sowohl als auch“. Ruhig im Aufbau, lebendig in Bild, Schrift und Farbe. Keine Pastell-Therapie-Optik, kein spiritueller Coaching-Look, Natur nicht als Wellness-Kulisse.
- Farben: Gelb/Gold (sparsam mit Schimmer) und Brombeer, Pink/Fuchsia offen. Wird mit Farbvergleich entschieden. Bisherige Töne (Blau, Rose) sind ihr zu dezent.
