# Lebensfäden: Grundlage und Bauauftrag für Claude Code

Website von Bettina Wyciok. Entwurf vom 9.10.2026, **noch nicht von Bettina freigegeben**. Festlegungen siehe Abschnitt 0.
Repo-Fassung: Destillat ohne private Details, das Rohmaterial bleibt außerhalb des Repos.
Quelle: Bettinas Angaben (9.10.2026) und die alte Website.

**Legende für jede Aussage**
- **[B]** Bettina, wörtlich
- **[B~]** Bettinas Worte, gekürzt oder in Website-Form gebracht, ohne neuen Inhalt
- **[B-alt]** von ihrer alten Website
- **[J]** Jakobs Entscheidung oder Idee
- **[C]** Vorschlag von Claude
- **[fehlt]** Angabe fehlt, mit Bettina klären

---

## 0. Festlegungen (Stand 9.10.2026)

- **Anrede: Du.** Texte der alten Seite siezen und werden mechanisch auf Du umgestellt, ohne Inhalt zu ändern.
- **Gestaltung: „sowohl als auch“.** Ruhe und Weißraum als Grundlage, Kraft gezielt durch Bilder, Schrift und Farbe (Abschnitt 11).
- **Farbrichtung:** Gelb/Gold und Brombeer. Die genaue Farbwelt wird mit einem Vergleich entschieden.
- **Name:** „Lebensfäden“ wird jetzt ausprobiert, als Wortmarke und Dachmarke für alles. Er bleibt an genau einer Stelle austauschbar. „Bettina Wyciok“ ist immer sichtbar. Neue Domain voraussichtlich unter diesem Namen (.org), die bestehende Domain bleibt für E-Mail.
- **Anmeldung und Gespräch (9.10.2026):** Kein Buchungstool vorerst. „Gespräch vereinbaren“ und „Anmelden“ sind Knöpfe mit Mail-Link und vorausgefülltem Betreff. Gruppenangebote zeigen aktuelle Termine (`tools/termine.json`), jeder Termin hat einen „Anmelden“-Knopf per Mail. Bei MSC führt ein externer Link zu Details und Anmeldung.
- **Rechtliches:** Keine Wirkversprechen. Hinweise und Pflichtangaben (Impressum) erst festlegen, wenn Bettinas Angaben vorliegen. Keinen Wortlaut erfinden.
- **Persönliches** kommt nur auf die Seite, wenn Bettina es ausdrücklich freigibt.
- **Dieses Dokument enthält nur Website-Inhalte und Bauregeln.** Interview-Rohmaterial, Namensprüfung, rechtliche Einordnung und persönliche Notizen bleiben außerhalb des öffentlichen Repos.

---

## 1. Absicht

- Die Website soll „Menschen ansprechen, neugierig machen und Vertrauen schaffen“ **[B]**.
- Sie soll „nicht nur eine digitale Visitenkarte“ sein, „sondern ein lebendiger Ort, der informiert, inspiriert und sich weiterentwickelt“ **[B]**.
- Ihr roter Faden ist „Verbindung“ **[B]**.
- Sie soll eigenständig funktionieren. „Social Media steht für mich derzeit nicht im Mittelpunkt.“ **[B]**
- Was Besucher tun sollen: Kontakt aufnehmen, ein Gespräch vereinbaren oder sich direkt für Veranstaltungen anmelden **[B]**.
  - Die eine Handlung **[C]**: **„Gespräch vereinbaren“**. Bei Inner Trance Dance ist es „Anmelden“.
- Bettina will die Seite nach dem Relaunch selbst pflegen: Texte und Bilder ändern, Blog, Termine, Angebote, neue Seiten, auch das Design **[B]**. → Daraus folgt Technik, die einfach bleibt (Abschnitt 14).

## 2. Kern

- **In einem Satz [B]:** „Ich begleite Menschen dabei, wieder in Verbindung mit sich selbst zu kommen, sich besser zu verstehen und auch in schwierigen Lebenssituationen Halt, Klarheit und ihren eigenen Weg zu finden.“
- **Was sich durch alles zieht [B]:** „Verbindung ist das Dach meiner Arbeit. Aufrichtung ist eine wesentliche Richtung, in die sie führen kann.“
- **Haltung [B]:** „Es geht darum, mehr Kapazität für das Leben zu entwickeln, wie es tatsächlich ist.“
- **Wofür sie nicht gehalten werden will [B~]:** eine klassische Coachin mit schnellen Erfolgsversprechen, Selbstoptimierung, universelle Lösungen, Spiritualität als Aushängeschild, Menschen auf Probleme, Symptome oder Diagnosen reduzieren.
- **Was sie unterscheidet [B~]:** therapeutische Tiefe, dazu fast 30 Jahre Erfahrung in Unternehmen und internationalen Zusammenhängen. Sie arbeitet mit Verstand, Gefühl, Körper und Nervensystem und kann bleiben, wo es schmerzt.

## 3. Marke und Architektur

| Ebene | Inhalt | Herkunft |
|---|---|---|
| Dachmarke | **Lebensfäden** (Arbeitstitel, austauschbar) | [J] |
| Absenderin | **Bettina Wyciok**, immer sichtbar | [C] |
| Bedeutung des Namens | „Die unterschiedlichen Erfahrungen, Beziehungen und Entwicklungen, die unser Leben prägen und miteinander verwoben sind.“ | [B] |
| Leitgedanke | Verbindung (Dach) → Aufrichtung (Richtung) | [B] |
| Angebote | Einzelbegleitung · Paar- und Beziehungsbegleitung · Inner Trance Dance · Kurse und Workshops (MSC u. a.) | [B], Gruppierung [C] |
| Orte | Freiburg · bei Furtwangen im Schwarzwald · online | [B-alt] |
| Kontakt | kontakt@bettinawyciok.de | [B-alt] |

**Schreibweisen [C]:** Lebensfäden (mit ä, im Fließtext nie „Lebensfaeden“), Inner Trance Dance (ausgeschrieben, ohne Abkürzung), Internal Family Systems (IFS), Mindful Self-Compassion (MSC) bzw. „Achtsames Selbstmitgefühl“, Paar- und Beziehungsbegleitung.

## 4. Seitenstruktur und Navigation

Bettinas Wunsch: eine Startseite mit eigenen Unterseiten **[B]**. Der Aufbau folgt dem Muster von essential-guidance.space: Startseite mit gleich gebauten Angebots-Blöcken, dazu eine Unterseite pro Angebot **[J]**.

| Seite | Pfad | Herkunft |
|---|---|---|
| Startseite | `/` | [B] |
| Einzelbegleitung | `/einzelbegleitung/` (Pfad wie bisher) | [B] |
| Paar- und Beziehungsbegleitung | `/paarbegleitung/` (Pfad wie bisher) | [B] |
| Inner Trance Dance | `/inner-trance-dance/` (neu) | [B] |
| Kurse und Workshops (MSC, Workshops und Seminare) | `/workshops-seminare/` (Pfad wie bisher) | [B], Zusammenlegung [C] |
| Blog: „Gedanken“ oder „Blog und Inspiration“ | `/blog/` (neu) | [B], Titel offen |
| Über mich | `/about/` (Pfad wie bisher) | [B] |
| Kontakt | `/contact/` (Pfad wie bisher) | [B] |
| Impressum, Datenschutz | wie bisher | |

- **Navigation [C]:** Einzel · Paare · Inner Trance Dance · Kurse · Blog · Über mich, dazu der Knopf „Gespräch vereinbaren“. Am Handy klappt sie als Menü auf. Keine Untermenüs.
- **Termine [C]:** Erst wenn es regelmäßig Termine gibt, bekommen sie eine eigene Seite. Bis dahin erscheinen sie auf der Startseite und auf der jeweiligen Angebotsseite (Handbuch: weniger ist mehr).
- Die alten Pfade bleiben gleich, damit Google nichts verliert (Handbuch Abschnitt 16).

## 5. Startseite, von oben nach unten

Die Texte sind Vorschläge zur Freigabe. Bettinas Sätze sind so wenig wie möglich verändert.

**5.1 Hero (genau ein Bildschirm)**
- Wortmarke: **Lebensfäden**, darunter klein „Bettina Wyciok“ **[J]/[C]**
- Überzeile **[C]:** Einzel- und Paarbegleitung · Inner Trance Dance · Selbstmitgefühl · Schwarzwald, Freiburg und online
- H1, drei Optionen:
  - a) „Wieder in Verbindung kommen. Mit sich selbst, mit anderen, mit dem Leben.“ **[B~]**
  - b) „Mehr Kapazität für das Leben, wie es tatsächlich ist.“ **[B]**
  - c) „Was uns verbindet. Was uns trägt. Was neu entstehen darf.“
  - Empfehlung **[C]:** a) als H1 und b) als erster Satz darunter. Begründung: Der Name ist poetisch und deshalb erklärungsbedürftig, also muss die Überschrift konkret sagen, worum es geht. Das ist auch der Haupteinwand in der Analyse.
- Lead **[B]:** „Ich begleite Menschen dabei, wieder in Verbindung mit sich selbst zu kommen, sich besser zu verstehen und auch in schwierigen Lebenssituationen Halt, Klarheit und ihren eigenen Weg zu finden.“
- Knöpfe: „Angebote ansehen“ · „Gespräch vereinbaren“

**5.2 Der rote Faden (Was ist Lebensfäden?)**
- H2 **[C]:** „Der rote Faden: Verbindung“
- Text **[B]:** „Verbindung mit uns selbst, mit unserem Körper, unseren Gefühlen, Bedürfnissen und inneren Anteilen. Verbindung mit anderen Menschen, in Partnerschaften, Beziehungen und Gemeinschaft. Verbindung mit der Natur, dem Leben und möglicherweise etwas Größerem.“
- Zweiter Absatz **[B]:** „Ich glaube nicht, dass wir alle unsere Probleme lösen müssen, um gut leben zu können. Mir geht es darum, dass Menschen mehr Kapazität für das Leben entwickeln, wie es tatsächlich ist.“
- Kleine Zeile zum Namen **[B~]:** „Lebensfäden steht für die Erfahrungen, Beziehungen und Entwicklungen, die unser Leben prägen und miteinander verwoben sind.“

**5.3 Nächste Termine** (nur wenn es welche gibt, sie werden automatisch aus `tools/termine.json` aktuell gehalten)

**5.4 Angebote: vier Blöcke, alle gleich gebaut**
Jeder Block hat: Bild · Überzeile mit Fakten · Titel · Claim · zwei bis drei Sätze · zwei Knöpfe.

| | Einzelbegleitung | Paar- und Beziehungsbegleitung | Inner Trance Dance | Achtsames Selbstmitgefühl (MSC) |
|---|---|---|---|---|
| Überzeile | 1:1 · [Dauer fehlt] · Freiburg, bei Furtwangen oder online | Paare und andere Beziehungen · [Dauer fehlt] · Freiburg, bei Furtwangen oder online | Tanz · Gruppe · erster Termin in Planung · [Ort fehlt] | Kurs · Gruppe · [Format, Ort fehlen] |
| Claim [C aus B] | „An der eigenen Seite stehen.“ | „Verbindung miteinander und mit sich selbst.“ | „Über Musik und Bewegung einen anderen Zugang zu sich finden.“ | „Sich selbst in schwierigen Momenten freundlich begegnen.“ |
| Text [B~] | Für Menschen in Krisen und Übergängen und für alle, die sich selbst besser kennenlernen möchten. Mit IFS, Nervensystemarbeit sowie körperorientierten und achtsamkeitsbasierten Zugängen. | Für Paare, die sich voneinander entfernt haben, immer wieder in schwierige Muster geraten oder ihre Verbindung bewusst stärken möchten. Auch Eltern und erwachsene Kinder oder Freunde finden Raum. | Ein Erfahrungsraum mit Musik, Bewegung und Körperwahrnehmung, für Selbsterfahrung, Lebendigkeit und Verbindung, mit dem eigenen Körper, dem inneren Erleben und vielleicht mit etwas Größerem. | Kurse und Formate zum achtsamen Selbstmitgefühl: lernen, sich gerade in schwierigen Momenten mit mehr Verständnis, Freundlichkeit und Mitgefühl zu begegnen. |
| Knöpfe | Mehr erfahren · Gespräch vereinbaren | Mehr erfahren · Gespräch vereinbaren | Mehr erfahren · Anmelden (bis es einen Termin gibt: „Termin folgt“) | Mehr erfahren · Interesse melden |

**5.5 Wie ich arbeite** **[B]**
„Ich orientiere mich am Menschen und seinem Anliegen, nicht an einer vorgegebenen Methode.“ · „Ich arbeite mit dem Verstand, mit Gefühlen, mit dem Körper und dem Nervensystem.“ · „Ich kann auch dort bleiben, wo es schwierig wird und schmerzt. Gleichzeitig interessiert mich, was sich darüber hinaus zeigen und entwickeln möchte.“
Darunter eine schmale Leiste mit den Methoden **[B]:** IFS · Nervensystemarbeit · traumainformiert · körperorientiert · Achtsamkeit · Selbstmitgefühl (MSC)

**5.6 Wer ich bin** (Foto mit kurzem Text) **[B~]**
„Fast drei Jahrzehnte habe ich in Unternehmen und internationalen Zusammenhängen gearbeitet, Menschen geführt und Veränderungsprozesse begleitet. Heute lebe ich mitten im Schwarzwald, liebe Pflanzen und arbeite gern mit meinen Händen und der Erde.“ → Knopf „Mehr über mich“

**5.7 Aus dem Blog**: die drei neuesten Beiträge, sobald es welche gibt. Bis dahin entfällt der Abschnitt.

**5.8 Footer mit Einladung** **[B-alt]:** „Vielleicht ist jetzt ein guter Zeitpunkt für ein Gespräch?“, dazu Kontakt, Orte, Impressum, Datenschutz.

## 6. Angebotsseiten

Alle Angebotsseiten folgen derselben Abfolge (Handbuch Abschnitt 7): Kopf mit Überzeile → Einstieg mit Infobox (Wo, Wann, Dauer, Preis, Anmeldung) → Ablauf → Für wen und für wen nicht → Was Menschen mitnehmen → Termine (falls vorhanden) → FAQ → Hinweis.

**Einzelbegleitung**, Inhalte **[B]** aus dem Rohmaterial Teil A, Abschnitte 3, 7, 8 und 9:
- Ablauf: „Zunächst geht es darum, anzukommen und gemeinsam zu verstehen, was gerade wichtig ist. Ich höre zu, frage nach und unterstütze Menschen dabei, ihre inneren Erfahrungen, Gefühle, Reaktionen und Muster besser wahrzunehmen.“ Dann die vier „Manchmal …“-Sätze, als ruhige Liste.
- Für wen: die Liste aus Abschnitt 8, gekürzt auf fünf bis sechs Punkte **[B~]**. Für wen nicht **[B]:** „für Menschen, die ausschließlich schnelle Lösungen erwarten oder die Verantwortung für ihre Veränderung vollständig abgeben möchten.“
- Was Menschen mitnehmen: aus Abschnitt 9 **[B~]**. Dazu der Satz **[B]:** „Mir geht es nicht darum, dass Menschen dauerhaft auf meine Begleitung angewiesen sind.“
- Infobox **[fehlt]:** Dauer, Preis, Orte, Ablauf des Erstkontakts
- FAQ: Bettinas drei häufigsten Fragen **[fehlt]**

**Paar- und Beziehungsbegleitung**, Inhalte **[B]** aus Abschnitt 3 und 7:
- „Hier betrachten wir sowohl die Beziehung als auch das innere Erleben der beteiligten Menschen. Wir erkunden, welche Muster und Dynamiken zwischen ihnen entstehen, was darunterliegt und wie wieder mehr Verständnis und Verbindung möglich werden können.“
- Infobox und FAQ **[fehlt]**

**Inner Trance Dance**, Inhalte **[B]** aus Abschnitt 3 und 7 („In Gruppenformaten“):
- Ablauf eines Abends, Musik, Ort, Dauer, Preis, Anmeldeweg (z. B. Eventfrog) **[fehlt]**. Ein Bild mit Bewegung, aber nicht spirituell inszeniert.
- Termine aus `tools/termine.json`

**Kurse und Workshops**, MSC und weitere Formate:
- MSC **[B]**. Workshops und Seminare der alten Seite **[B-alt]** nur übernehmen, wenn Bettina sie weiter anbietet.
- Formate und Kooperationen, die noch in Entwicklung sind, erst zeigen, wenn sie fertig sind **[B]**.

**Hinweis auf allen Begleitungsseiten:** Wortlaut erst festlegen, wenn Bettinas Angaben vorliegen.

## 7. Über mich

Inhalte kommen aus Bettinas Material: Berufsweg, Methoden, die sie geprägt haben, wie sie einen Raum hält („Alles, was sich zeigt, darf zunächst da sein.“) und der Mensch (Schwarzwald, Pflanzen, Natur, Tanz). Weitere persönliche Themen und die Vision erst nach ihrer ausdrücklichen Entscheidung. Qualifikationen als Liste, wie auf der alten Seite.

## 8. Blog

- Themen **[B]:** Verbindung, IFS und innere Anteile, Nervensystem und Selbstregulation, Selbstmitgefühl, Beziehungen, Körper und Bewegung, Natur, persönliche Gedanken.
- Bettina will den Blog „selbstständig und unkompliziert“ pflegen **[B]**.
- Umsetzung **[C]:** Jeder Beitrag ist eine Markdown-Datei in `blog/beitraege/`. Ein kleines Skript `tools/make-blog.py` erzeugt daraus die HTML-Seiten und die Übersicht, genau wie `make-ics.py` bei den Terminen. Bettina sagt Claude Code dann zum Beispiel: „Hier ist mein Text, mach daraus einen Blogbeitrag mit diesem Foto.“ Es gibt keinen Build-Schritt auf dem Server und kein CMS.
- Zum Start reicht eine leere Blogseite mit Ankündigung oder ein erster Beitrag von ihr **[C]**.

## 9. Termine, Anmeldung, Kontakt

- Termine stehen nur in `tools/termine.json`, das Skript erzeugt daraus die Karten und Kalenderdateien (Vorlage: Repo koojaa92/Website-Essential-Guidance, Ordner `tools/`).
- Anmeldung für Veranstaltungen pro Termin über einen externen Link, zum Beispiel Eventfrog. Es gibt kein eigenes Bezahlsystem. Welches Werkzeug, ist **[fehlt]**.
- Gespräch vereinbaren: Knopf mit Mail-Link und vorausgefülltem Betreff. Ein Buchungstool ist nicht geplant. Anmelden zu Gruppenterminen ebenfalls per Mail-Knopf.
- Telefonnummer: Ob sie auf die Seite soll, ist **[fehlt]**.

## 10. Sprache

- **Anrede [B]:** Du.
- **Ton [B]:** „Persönlich, direkt, klar, warm und lebendig. Mit Tiefe, aber ohne künstliche Schwere. Professionell, ohne distanziert zu sein.“
- **Wörter, die tragen [B]:** Verbindung, Verbundenheit, Begegnung, Mitgefühl, Vertrauen, Geborgenheit · Aufrichtung, innere Kraft, Klarheit, Selbstvertrauen, Ausrichtung · Freude, Neugier, Lebendigkeit, Körper, Bewegung, Tanz · Boden, Wurzeln, Verwurzelung, Himmel, Weite, Natur · Achtung, Würdigung, Offenheit, Frieden, Zuversicht. Dazu Sätze, die sie geprägt hat: „an der eigenen Seite stehen“, „Kapazität für das Leben, wie es tatsächlich ist“.
- **Wörter, die nie vorkommen [B]:** Selbstoptimierung, Potenzialentfaltung, Transformation (als Schlagwort), nachhaltige Veränderung, ganzheitlich (ohne Erklärung), Heilungsversprechen, Erfolgsversprechen, spirituell aufgeladene Formulierungen ohne Inhalt.
- **Zusätzlich [C]:** kein „kostenloses Erstgespräch“ als Aufhänger (steht schon in CLAUDE.md), keine Wirkversprechen. Lieber „kann“ und „vielleicht“, wie Bettina selbst schreibt.

## 11. Gestaltung

**Gefühl [B]:** „Lebendig. Klar. Verbindend.“ Dazu Jakob **[J]:** klar, raumhaft, ruhig, modern, schick.
**Richtung [B]: „Sowohl als auch.“** Ruhe im Aufbau (Raum, klare Typografie, Dezenz), Kraft gezielt in Bild, Schrift und Farbe. Ruhige und lebendige Abschnitte wechseln sich ab.

**Farbe, Stand 9.10.2026 [B]:**
- Die bisherigen Töne (Blau, Salbei, Weinrot) sind ihr „zu dezent“.
- Ihr Wunsch: **Gelb, Gold, „mit Glitzer“**, dazu ein **Beerenton, Brombeer**: „Vielleicht ist es auch Brombeer am Ende.“
- Offen: wie dunkel das Brombeer sein soll und ob Pink oder Fuchsia dazugehört (im Gespräch: „dieses Pink, so wie du privat bist“).
- Die Pflanzenfarben-Idee (Indigo, Krapprot, Wau-Gelb) ist damit überholt. Neuer Ausgangspunkt: Gelb oder Gold und Brombeer.
- **Vorgehen [C]:** drei bis vier Farbwelten nebeneinander zeigen (Screenshot 390 und 1280 px) und mit Bettina auswählen. „Glitzer“ im Web heißt: sehr sparsam ein feiner Goldschimmer (zum Beispiel am Faden oder an einer Linie), nie flächig und nie verspielt.
- Jakobs Entscheidungen aus DESIGN.md gelten weiter, soweit Bettina nicht ausdrücklich anders will: kein Grün als Fläche, Bildplätze in Grau, keine Creme-Töne **[J]**. Die Entscheidung „Blau und leichtes Rot“ aus Entwurf 2 ist durch Bettinas Wunsch offen und wird mit dem Farbvergleich neu entschieden.
- Bettina will ausdrücklich nicht: „die üblichen Pastellfarben“, eine „klassische spirituelle Coaching-Website“ und Natur als „austauschbare Wellness-Kulisse“ **[B]**.

**Der Faden als Gestaltungselement:** Die Idee ist **[B]**, die Umsetzung **[C]**. Eine einzige feine, durchgehende Linie zieht sich durch die Seite. Sie verbindet die Abschnitte, läuft an Bildern vorbei und knüpft am Ende im Footer an. Sie ist als SVG gezeichnet und baut sich beim Scrollen langsam auf. Bei reduzierter Bewegung steht sie still. Sie kommt einmal pro Seite vor. Daraus kann später das Logo entstehen: Wortmarke plus Faden.

**Bilder:** „Eine eigenständige Bildsprache mit ausdrucksstarken Fotografien“ **[B]**. Die Kraft der Seite soll vor allem aus den Bildern kommen. Natur zeigt sich authentisch: Hände, Pflanzen, Räucherbündel, Schwarzwald, Bewegung beim Tanz. Ein Fotoshooting wird empfohlen **[C]**, wer fotografiert, ist offen **[B]**. Keine KI-Bilder von Menschen **[J]**. Bis die Bilder da sind, bleiben graue, beschriftete Bildplätze.

**Schrift:** Literata und Nunito Sans aus Entwurf 2 sind der Ausgangspunkt. Für „modern, schick“ und die neue Kraft werden drei Paare in Originalgröße nebeneinander verglichen, nummeriert. Die Entscheidung fällt am Bildschirm, nicht nach Beschreibung (Handbuch).

**Bewegung:** sanft. Nur der Faden bewegt sich und die Hero-Zeilen blenden einmal ein.

## 12. Offen und fehlt

- [ ] Name freigeben
- [x] Anrede: Du (entschieden 9.10.2026)
- [ ] Farbwelt wählen: drei bis vier Töne nebeneinander (Gold/Gelb, Brombeer, Pink oder Fuchsia)
- [ ] Angaben für Impressum und Hinweise von Bettina
- [ ] Pro Angebot: Dauer, Preis, Orte, Anmeldeweg; ITD-Termin und -Ort; MSC-Format
- [ ] Welche bisherigen Workshops und Formate bleiben sichtbar, Podcast
- [ ] Drei häufigste Fragen pro Angebot (FAQ)
- [ ] Texte für „Über mich“ freigeben
- [ ] Fotos: Bestand sammeln, Rechte klären, Shooting ja oder nein
- [ ] Telefonnummer ja oder nein
- [ ] Externer Link für den MSC-Kurs (Details und Anmeldung)
- [ ] Blogtitel
- [ ] Freigabe dieser Grundlage durch Bettina (Tor vor dem Bauen, Handbuch Phase 3)

---

## 13. Regeln für Entwurf 3

- Texte genau so übernehmen, wie sie in dieser Grundlage stehen. Nichts umschreiben. Einzige Ausnahme: die mechanische Umstellung auf Du. Wo [fehlt] steht: sichtbarer, grauer Platzhalter, nichts erfinden.
- Die Wortmarke „Lebensfäden“ steht an genau einer Stelle (Kopf) und ist austauschbar. „Bettina Wyciok“ ist immer sichtbar.
- Alte Pfade behalten (/einzelbegleitung/, /paarbegleitung/, /workshops-seminare/, /about/, /contact/). Neu: /inner-trance-dance/, /blog/.
- Startseite: vier gleich gebaute Angebotsblöcke wie bei essential-guidance.space (Überzeile, Titel, Claim, Text, zwei Knöpfe).
- Der Faden: eine feine SVG-Linie durch die Seite, baut sich beim Scrollen auf, bei prefers-reduced-motion statisch. Eine pro Seite.
- Farben: erst Vergleich (Abschnitt 11), dann Entscheidung. Schrift: drei Paare in Originalgröße, nummeriert, dann Entscheidung.
- Blog: blog/beitraege/*.md → tools/make-blog.py erzeugt HTML und Übersicht. Ohne Beiträge: Blogseite mit einem Satz Ankündigung, kein Blog-Abschnitt auf der Startseite.
- Termine: tools/termine.json + tools/make-ics.py nach Vorlage koojaa92/Website-Essential-Guidance.
- Gespräch vereinbaren und Anmelden: Mail-Knopf mit vorausgefülltem Betreff. Externe Links (zum Beispiel MSC-Anbieter) öffnen in neuem Tab (rel="noopener").
- noindex und Disallow bleiben gesetzt. Kein Rechtshinweis-Wortlaut erfinden.
- Entscheidungen sofort in DESIGN.md und STAND.md nachtragen.
