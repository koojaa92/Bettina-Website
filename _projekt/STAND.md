# Bettina Website: Projektstand und offene Punkte

Stand: 2026-10-07. Vorschau: https://koojaa92.github.io/Bettina-Website/ (Entwurf 1, noindex). Phase: Entwurf vor Interview.
Feedbackrunden: 0 von [vereinbart].

## Was steht
- Marke und Positionierung: offen, kommt aus dem Interview.
- Startseite: Entwurf 1 (Hero mit drei Zeilen, Angebote, Wie ich arbeite, Wer ich bin, Aktuelles, Kontakt-Aufruf). Texte und Fotos aus der alten Seite, Wortlaut unverändert.
- Unterseiten: Einzelbegleitung, Paarbegleitung, Workshops & Seminare, Über mich, Kontakt (Pfade wie auf der alten Seite: /about/, /contact/, /datenschutzerklarung/). Impressum und Datenschutz nur Platzhalter.
- Technik und SEO: 8 Seiten als Ordner mit index.html, eine styles.css, eine main.js (Menü am Handy), Schriften und Bilder im Repo (bilder/ als WebP, schriften/). `noindex` und `Disallow: /` sind gesetzt, sitemap.xml mit github.io-Adresse, llms.txt noch Platzhalter, keine Meta-Beschreibungen (Phase 6). Bei 390 und 1280 px geprüft, kein seitliches Überlaufen. Nicht geprüft: echtes iPhone.
- Vorschau: Adresse oben (Groß- und Kleinschreibung beachten, GitHub Pages aktiv; `_projekt/` und `_werkstatt/` werden nicht ausgeliefert). Domain wird erst später verbunden.

- Werkstatt-Standards aus `website-werkstatt` (main) übernommen am 2026-10-06: Skill `frontend-design`, `_werkstatt/HANDBUCH.md` (aktualisiert), `_werkstatt/KI-WERKZEUGKASTEN.md`, `_projekt/DESIGN.md` (Vorlage, inzwischen mit Entwurf 1 gefüllt) und der Abschnitt „Design“ in `CLAUDE.md`. Bettina-Einträge unverändert.

- Design: `_projekt/DESIGN.md` beschreibt Entwurf 1 (Palette aus ihren Fotos, Literata und Nunito Sans selbst gehostet). Nicht freigegeben.

## Offene Punkte
### Vor Freigabe des Entwurfs klären (aus der alten Seite aufgefallen)
- [ ] Bildrechte der drei Porträts (Fotograf, Lizenz) und Zustimmung, sie im öffentlichen Repo zu führen
- [ ] Rechtliche Texte: Heilpraktikerin, "Therapie", "Heilungsimpulse", Traumaarbeit, substanzunterstützte Begleitung: Hinweis "keine Heilkunde"/Heilmittelwerbegesetz prüfen
- [ ] Textfehler der alten Seite, bewusst unverändert übernommen: "Paarbelgeitung" (Angebot Paarbegleitung), "In meinen Workshops und Seminare", "Kindern ziehen aus", Satzrest "zudem: Selbsterfahrung … Köln an." (Einzelbegleitung)
- [ ] Kontakt-Text nannte ein Formular, es gibt keins: Formular-Hinweis im Entwurf gestrichen (nur Mail-Link). Telefonnummer der alten Seite bewusst nicht übernommen, ihr Wunsch klären
- [ ] Workshops: Webinar vom 23.06.2026 ist vorbei und wurde nicht übernommen, Seite zeigt "Derzeit ist kein Termin eingetragen". Webinar-Bild (KI-Optik) nicht übernommen
- [ ] Impressum und Datenschutz: Angaben von ihr (Kleinunternehmerin nach § 19 UStG laut Angebotstexten, keine USt-IdNr. erfinden)

### Von der Kundin
- [ ] Material liefern (Checkliste aus der Kunden-Handreichung: Absicht, Referenzseiten, Angebote, Fotos, vorhandene Texte, Pflichtangaben, Kanäle)
- [ ] Zugänge prüfen: Login bei Domain-Anbieter, alter Website (falls vorhanden), Mailpostfach, Google
- [ ] Interview-Termin
### Von Jakob / Claude
- [ ] Interview führen (Phase 2), Leitfaden aus dem Fragenpool zusammenstellen
- [ ] Domain klären: gibt es eine, wo liegt sie, wo das DNS, hängt E-Mail daran (Handbuch Abschnitt 16)
- [ ] E-Mail klären: Kontaktadresse, Postfach
- [ ] Konten klären: GitHub (Weg A oder B), Domain-Anbieter, Google, GoatCounter (Handbuch Abschnitt 4)
- [ ] Angebot, Paket und Zahl der Feedbackrunden schriftlich festhalten (steht nicht im Repo)
- [ ] Nach dem Interview: `_projekt/GRUNDLAGE.md` füllen, Freigabe holen, Marken-Regeln in `CLAUDE.md` eintragen
### Später
- [ ] Vor Live-Gang: `noindex` in allen HTML-Dateien und `Disallow: /` in robots.txt entfernen, sitemap.xml und llms.txt mit echter Domain füllen
- [ ] Phase 4: erster Entwurf und Live-Gang (erst nach freigegebener Grundlage)
- [ ] Phase 6: SEO, Impressum, Datenschutz
- [ ] Phase 7: Übergabe und Befähigung

## Entschieden (nicht wieder aufmachen)
- Dies ist ein eigenständiges Projekt, unabhängig von essential-guidance.space.
- Gerüst wird in diesem Repo gebaut (nicht im Vorlagen-Repo): nur neutral, ohne Design und Inhalte. Echtes Design und Texte erst nach Phase 3.
- Vorschau läuft über GitHub Pages unter der github.io-Adresse, keine Domain nötig. Kein Bauen im Artefakt.
- Arbeitsstil: wenig Technik zeigen, bei echten Problemen fragen, Alternativen nennen. Technik-Fragen (Domain, Umzug, GitHub) kurz und knapp erklären, bei Screenshots Schritt für Schritt führen.
- Das Repo ist öffentlich: Nur das sachliche Destillat kommt hinein, nichts Persönliches (keine Transkripte, privaten Notizen, Preise der Zusammenarbeit).
