# CLAUDE.md – Regeln für diese Website

Gilt für jede Sitzung in diesem Repo. Lies zu Beginn auch `_projekt/STAND.md`. Bei einem neuen Projekt zusätzlich `_werkstatt/HANDBUCH.md`.

## Projekt
- Website für: [Name], [Angebot] in [Stadt]
- Repo: [owner/repo]. Live ist der Branch `main` (GitHub Pages).
- Domain: [domain], DNS bei [Anbieter]. E-Mail an der Domain: [ja/nein]. MX- und TXT-Einträge nie ändern.
- Website-Typ und Ziel: [z. B. Angebots-Website mit Terminen / One-Pager / Portfolio]. Funktionen: [...]
- Aktuelle Phase: [0–7, siehe Handbuch Abschnitt 5]

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
- Abstände zwischen Abschnitten eng halten. Globale Regel am Ende von `styles.css`.
- Schriften selbst hosten oder über Bunny Fonts, nie direkt von Google Fonts.
- Formulare nur, wenn sie wirklich senden. Sonst Mail-Link.
- FAQ sichtbar und als FAQPage-JSON-LD im `<head>`, beides angleichen. FAQ-Abschnitte mit grauem Hintergrund.
- Termine (falls vorhanden) nur in `tools/termine.json`, danach `python3 tools/make-ics.py`.
- `llms.txt` und `sitemap.xml` bei Änderungen an Angeboten, Preisen oder Seiten mitpflegen.

## Datenschutz im Repo
- Das Repo ist öffentlich. Keine Interview-Transkripte, privaten Notizen, Preise der Zusammenarbeit, Passwörter oder privaten Adressen ins Repo.
- Ordner mit Unterstrich (`_projekt/`, `_werkstatt/`) werden nicht als Website ausgeliefert, sind auf GitHub aber sichtbar.

## Recht
- Impressum nach § 5 DDG: Name, ladungsfähige Anschrift, Kontakt. USt-IdNr. nur, wenn vorhanden. Nie Nummern erfinden.
- Datenschutzerklärung nennt jedes eingebundene Tool.
- [Bei Begleitungsangeboten: Hinweis „keine Heilkunde, ersetzt keine Therapie, Teilnahme in Eigenverantwortung“.]

## Marke (verbindlich, nach Phase 3 füllen)
- Dachmarke: [Name]. Angebote: [A], [B], [C].
- Schreibweisen: [...]
- Ort immer gleich: [Ort, Adresse].
- Alle Mail-Links an: [mail]. Betreff je nach Button.
- Wörter, die immer vorkommen: [...]
- Wörter, die nie vorkommen: [...]
- Die eine Handlung für Besucher: [...]
- Schriften: [Überschrift], [Fließtext]. Farben: [...]
