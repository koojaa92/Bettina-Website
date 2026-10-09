# Übergabe: So arbeitest du selbstständig an deiner Website

Für Bettina. Stand: 2026-10-09. Dauer für die Einrichtung: etwa eine Stunde. Du brauchst keine Programmierkenntnisse. Wenn dein Bildschirm anders aussieht als hier beschrieben (Oberflächen ändern sich), mach einen Screenshot und schick ihn Jakob.

## Was du am Ende hast
- Ein eigenes GitHub-Konto, das die Website enthält (der „Speicher“ deiner Seite).
- Ein Claude-Konto, mit dem du der Seite per Chat sagst, was sich ändern soll („Claude Code“).
- Die Seite liegt unter deiner eigenen Adresse im Netz, erst auf der GitHub-Adresse, später unter deiner Domain.

## Was es kostet
- GitHub: kostenlos (das Repo muss öffentlich sein, dann ist das Hosting gratis).
- Claude Pro: rund 20 US-Dollar im Monat, jährlich günstiger. Aktuellen Preis auf claude.com/pricing prüfen. Claude Code ist darin enthalten.
- Domain: läuft getrennt, wird später verbunden.

## Schritt für Schritt

### Schritt 1: GitHub-Konto anlegen (10 Minuten)
1. Auf github.com gehen und „Sign up“ wählen.
2. E-Mail-Adresse angeben, die du wirklich liest, Passwort wählen (im Passwortmanager speichern).
3. **Benutzername sorgfältig wählen.** Er ist öffentlich sichtbar und Teil der Adresse deiner Seite (`benutzername.github.io/Bettina-Website/`). Neutral und dauerhaft, zum Beispiel dein Name oder „lebensfaeden“. Nachträglich ändern geht, aber die Adresse ändert sich dann mit.
4. E-Mail bestätigen. Danach die Zwei-Faktor-Anmeldung einschalten (Profilbild → Settings → Password and authentication). Aufbewahren der Wiederherstellungscodes nicht vergessen.
5. **Schick Jakob deinen Benutzernamen.** Den braucht er für die Übertragung.

### Schritt 2: Claude-Konto mit Pro-Abo (10 Minuten)
1. Auf claude.ai anmelden oder ein Konto erstellen.
2. Ein Pro-Abo abschließen (im Konto unter dem Menü „Upgrade“ oder „Plans“).
3. Prüfen, ob unter claude.ai/code der Bereich für Claude Code erreichbar ist.

### Schritt 3: Die Website zu dir übertragen (macht Jakob, du nimmst an)
1. Jakob überträgt das Repository `Bettina-Website` auf dein GitHub-Konto (siehe Abschnitt „Für Jakob“ unten).
2. Du bekommst eine E-Mail von GitHub mit einem Bestätigungslink. **Zeitnah annehmen**, die Anfrage verfällt nach kurzer Zeit.
3. Danach findest du das Repo unter `github.com/DEIN-BENUTZERNAME/Bettina-Website`. Alle Dateien und die gesamte Änderungsgeschichte sind mitgekommen.
4. Öffne im Repo **Settings → Pages**. Dort sollte stehen: Source „Deploy from a branch“, Branch `main`, Ordner `/ (root)`. Wenn nicht, so einstellen und „Save“ drücken. Nach ein bis zwei Minuten steht dort die neue Adresse deiner Seite: `https://DEIN-BENUTZERNAME.github.io/Bettina-Website/`. **Groß- und Kleinschreibung beachten.**
5. Schick Jakob die neue Adresse und, dass du die Seite siehst.

### Schritt 4: Claude mit deinem GitHub verbinden (10 Minuten)
1. Auf claude.ai/code gehen. Wenn du aufgefordert wirst, GitHub zu verbinden: „Connect GitHub“ bzw. „Mit GitHub verbinden“ wählen und anmelden.
2. Die **Claude-GitHub-App installieren**, wenn sie dich fragt. Wichtig: Wähle „Only select repositories“ und dort **nur `Bettina-Website`**. So hat Claude nur Zugriff auf diese eine Seite.
3. Prüfen: Auf claude.ai/code das Repo `Bettina-Website` auswählen können.

### Schritt 5: Deine erste Sitzung (15 Minuten)
1. Auf claude.ai/code ein neues Projekt bzw. eine neue Sitzung starten und das Repo `Bettina-Website` auswählen.
2. Als ersten Auftrag das hier einfügen:

```
Lies CLAUDE.md, _projekt/STAND.md, _projekt/GRUNDLAGE.md, _projekt/DESIGN.md und _projekt/UEBERGABE.md.
Fass mir in einfachen Worten zusammen: Wo stehen wir? Was fehlt noch? Was sollte ich als Nächstes entscheiden?
Noch nichts ändern. Ich bin keine Programmiererin. Erkläre kurz, zeig mir Vorschauen und frag nach, wenn etwas unklar ist.
```
3. Lies die Antwort. Wenn du etwas nicht verstehst, frag nach. Das ist der Normalfall.

## So arbeitest du ab jetzt (der Alltag)

### Die drei Sätze, die fast alles abdecken
- „Lies CLAUDE.md. Ändere [was] auf [Seite]. Prüfe bei Handy- und Computerbreite und stell live.“
- „Nur zeigen, nicht umsetzen: Wie sähe es aus, wenn …?“
- „Dreh die letzte Änderung zurück.“

### Die drei Arbeitsweisen
- **„Nur zeigen“**: Claude zeigt dir eine Vorschau, ändert nichts.
- **„Sag erst, was du machen würdest“**: Claude nennt Möglichkeiten mit Empfehlung und wartet.
- **„Mach“**: Claude setzt um, prüft und stellt live.

### Bilder hochladen
1. Im Chat auf die **Büroklammer** klicken und die Dateien als **Anhang** schicken (nicht kopieren und einfügen, sonst bekommt Claude sie nur zum Ansehen). Bei vielen Fotos eine ZIP-Datei.
2. Dazu sagen, wohin sie gehören. Plätze auf der Seite: Hero (Start), Person, Über mich, Einzelbegleitung, Paarbegleitung, Inner Trance Dance, Kurse, Footer, roter Faden, Ort. Die genaue Liste steht in `_projekt/STAND.md` unter „Bildplätze“.
3. **Fotorechte:** Nur Bilder verwenden, die du nutzen darfst. Bei Fotos mit anderen Menschen brauchst du deren schriftliches Einverständnis. Keine KI-Bilder von Menschen. Die Seite ist öffentlich, auch dieses Repo.
4. Alternative: Auf GitHub im Repo den Ordner `bilder` öffnen, „Add file → Upload files“, Dateien hineinziehen, „Commit changes“. Dann Claude sagen, was wohin soll.

### Termine
Sag Claude: „Neuer Termin: Inner Trance Dance am [Datum], [Zeit], [Ort], [Preis].“ Claude trägt es in `tools/termine.json` ein und baut die Karten. Der Knopf „Anmelden“ führt per Mail zu dir, oder du gibst einen externen Link an.

### Blog
Sag Claude: „Hier ist mein Text. Mach daraus einen Blogbeitrag mit diesem Foto.“ Claude legt den Beitrag als Datei in `blog/beitraege/` an und baut die Seite.

### Texte
Claude schreibt Texte nie ungefragt um. Wenn du etwas ändern willst, sag es genau so, wie du es haben möchtest, oder bitte um Vorschläge.

## Wer macht was
- **Du:** Texte, Bilder, Termine, Blog, kleine Änderungen an Farben und Abständen.
- **Mit Jakob besprechen:** neue Seiten, größere Umbauten der Struktur, Domain und E-Mail, rechtliche Texte (Impressum, Datenschutz, Hinweise zu deinem Angebot).
- Immer nur **eine Person gleichzeitig** an der Seite arbeiten lassen, sonst überschreiben sich Änderungen. Kurz absprechen.

## Das ist noch offen (Stand 9.10.2026)
- Entscheidung über den Namen „Lebensfäden“ (Wortmarke). Ein Probe-Name, der an einer einzigen Stelle austauschbar ist.
- Inhalte: Inner Trance Dance (Termin, Ort, Dauer, Preis, Ablauf), MSC-Kurs (Zeit, Ort, Ablauf, Preis, externer Link), Ablauf einer Sitzung, häufige Fragen, Hinweis zur Begleitung.
- Alle Texte mit dir abgleichen und freigeben, auch die Du-Fassung.
- Bilder: weitere Fotos und ihre Rechte.
- Telegram- und Instagram-Link für die kleinen Symbole oben rechts.
- Impressum und Datenschutzerklärung mit deinen Angaben.
- Domain und E-Mail klären, dann verbinden und die Suchmaschinen-Sperre (`noindex`) entfernen.
- Farbton und Schrift endgültig wählen.

## Wenn etwas hakt
- Schick Jakob einen **Screenshot** und sag, was du erwartet hast.
- Frag Claude: „Was ist hier schiefgelaufen? Erkläre es mir einfach.“
- Du kannst nichts kaputtmachen, was sich nicht zurückdrehen ließe: GitHub speichert jede Änderung als Version.

---

## Für Jakob: Übertragung des Repos (Weg A aus dem Handbuch)

**Vorher**
1. Bettina hat GitHub-Konto, Claude-Pro und dir ihren Benutzernamen geschickt.
2. Stand prüfen: `main` ist aktuell, die Seite läuft, `STAND.md` und `GRUNDLAGE.md` sind auf dem Endstand. Alles Private bleibt draußen (Repo ist öffentlich).
3. Alte Arbeitszweige (`claude/phase-1-setup`, `claude/entwurf-1`) können bleiben oder gelöscht werden, die Seite braucht nur `main`.

**Übertragen**
1. Auf GitHub das Repo `Bettina-Website` öffnen → **Settings** → ganz unten **Danger Zone** → **Transfer ownership**.
2. Als neuen Besitzer Bettinas Benutzernamen eintragen, den Repo-Namen zur Bestätigung eintippen, bestätigen.
3. Bettina bekommt eine E-Mail und muss annehmen.
4. Der alte Link leitet GitHub weiter. Der Pages-Link ändert sich auf `bettinas-benutzername.github.io/Bettina-Website/`.

**Nachher (gemeinsam, ca. 15 Minuten)**
1. Bettina prüft: Settings → Pages aktiv (Branch `main`, `/ (root)`), HTTPS an.
2. Bettina lädt dich als Collaborator ein: Repo → Settings → Collaborators → Add people.
3. Bettina installiert die Claude-GitHub-App nur für dieses Repo (siehe Schritt 4).
4. In `sitemap.xml` die alte Adresse `koojaa92.github.io` durch die neue ersetzen (macht Claude auf Zuruf).
5. In `_projekt/STAND.md` die neue Vorschau-Adresse eintragen.
6. Später: Domain verbinden (Handbuch Abschnitt 16: vier A-Einträge, CNAME `www`, Datei `CNAME` im Repo, MX und TXT nie ändern) und `noindex`/`Disallow` entfernen.

**Hinweis:** Dein Claude-Konto behält keinen Zugriff auf ihr Repo, bis sie die App installiert und dich eingeladen hat.
