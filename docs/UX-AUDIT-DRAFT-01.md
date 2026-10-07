# UX / Field-Workbench Audit — Draft 01

Stand: 2026-10-07  
Review-Ziel: aktuelle GitHub Page als Werkzeug für Rekonstruktion, Demontage und Wissenstransfer bewerten.

## Verdict

**Der erste Draft ist als Publikationsschicht brauchbar, als Arbeitsoberfläche aber noch zu passiv.**

Er erklärt:
- was das Projekt ist,
- welche Evidenzklassen existieren,
- welche Konflikte und Gaps offen sind.

Er unterstützt noch nicht ausreichend:
- ein konkretes Bauteil am realen Rad zu identifizieren,
- eine offene Frage genau dort zu beantworten,
- ein Maß mit sauber definierten Endpunkten aufzunehmen,
- Varianten gegeneinander zu prüfen,
- eine Erinnerung direkt an Teil/Ereignis zu binden,
- einen unsicheren 3D-Hypothesenraum gemeinsam zu diskutieren.

Das ist der wichtigste Architekturwechsel für die nächste Phase.

---

## Blinder Fleck 1 — Das UI ist um Inhalte organisiert, nicht um Arbeit

Aktuelle Hauptlogik:
`Anatomie → Zeichnungen → Evidenz → Konflikte → Demontage → Handwerkswissen`.

Das ist eine gute Publikationsgliederung. Vor Ort lautet die Denkbewegung aber eher:

1. **Welches Teil habe ich vor mir?**
2. **Was glauben wir darüber zu wissen?**
3. **Was ist hier noch unklar?**
4. **Was soll ich jetzt zeigen, messen oder erklären?**
5. **Was habe ich gerade beobachtet?**
6. **Was ändert diese Beobachtung an unserem Modell?**

Die nächste Oberfläche muss task-first statt chapter-first sein.

---

## Blinder Fleck 2 — Das Rad selbst ist noch nicht der Navigationsraum

Der Benutzer sollte nicht zuerst Menüs und Karten lesen müssen.

Das Rad muss zum primären Index werden:
- Teil im Foto / 2D / 3D anklicken,
- Teil-ID und lokaler Name erscheinen,
- historische Zeichnung daneben,
- aktuelle Evidenz daneben,
- offene Fragen direkt am Teil,
- ein Knopf: **Messen / zeigen / erklären**.

Die heutige Component-Liste ist Datenpräsentation. Sie ist noch kein Arbeitsmittel.

---

## Blinder Fleck 3 — Wir warten zu lange mit 3D

Ein unsicheres 3D-Modell ist **jetzt schon sinnvoll**, sofern es klar als Hypothese visualisiert wird.

Falsche Strategie:
> Erst perfekte Maße sammeln, dann 3D bauen.

Bessere Strategie:
> Jetzt ein parametrisches Hypothesenmodell bauen, damit die Leute sehen können, **wo unsere Annahmen falsch sind**.

3D wird damit nicht zum Ergebnis, sondern zum Fragegenerator.

Unsicherheit muss im Modell sichtbar sein:
- gemessen = normale Geometrie,
- aktuell beobachtet = solide, aber ohne behauptetes Maß,
- historisch = eigener Linientyp / Layer,
- inferred = transparent / gestrichelt / ghosted,
- conflicting = Varianten A/B umschaltbar,
- unknown = Lücke statt erfundener Fläche.

Keine Fotorealistik als Default.

---

## Blinder Fleck 4 — Claims sind atomar, aber UX-seitig nicht adressierbar

Wir besitzen 355 Claims, 12 Konflikte und 8 Gaps. In der Page erscheinen sie als Zusammenfassung.

Die Workbench braucht bidirektionale Navigation:

`Bauteil ↔ Claim ↔ Quelle ↔ Konflikt ↔ offene Aufgabe ↔ neue Beobachtung`

Ein Nutzer, der einen Krümmling auswählt, darf nicht suchen müssen, welche Claims dazu gehören.

---

## Blinder Fleck 5 — Messung ist noch kein Datenobjekt der UI

Ein Feldwert ist mehr als `4260 mm`.

Jede Messung braucht mindestens:
- Teil / Partner,
- Merkmal,
- Wert,
- Einheit,
- Endpunkt A / Endpunkt B,
- Werkzeug,
- geschätzte Unsicherheit,
- Einbauzustand,
- Land-/Wasserseite,
- Foto-/Video-Referenz,
- Person,
- Zeit,
- optional Kommentar.

Die Oberfläche soll nach Möglichkeit **die Messstrecke zeigen**, nicht nur ein Textfeld anbieten.

---

## Blinder Fleck 6 — Implizites Wissen ist noch eine Interviewliste

Der neue Handwerkswissen-Track ist richtig, muss aber direkt an die Geometrie gekoppelt werden.

Nicht:
> „Erzähl etwas über Keile.“

Sondern am ausgewählten realen Kontakt:
> „Warum zeigt dieser Keil in diese Richtung?“  
> „Was passiert hier nach zwei Wochen im Wasser?“  
> „Woran merkst du beim Einschlagen, dass er sitzt?“  
> „Was wäre zu eng / zu locker?“  
> „Ist diese Stelle schon einmal ausgefallen?“

Aus Antworten sollen strukturierte Knowledge Claims entstehen:
- mechanism,
- condition,
- consequence,
- warning sign,
- mitigation,
- source person,
- affected components.

---

## Blinder Fleck 7 — Failure Modes fehlen als eigene Ebene

Für einen Digital Twin reicht Geometrie nicht.

Zu erfassen:
- Quellen/Schwinden,
- Keilwanderung,
- Rissbildung,
- Auswaschung,
- Schaufel-/Kumpflast,
- Stoßlast,
- Schwingung,
- Lager-/Zapfenverschleiß,
- Wasserstandsabhängigkeit,
- Reparaturstellen,
- Montagefehler und ihre Symptome.

Diese Ebene darf zunächst qualitativ sein. Sie ist später Grundlage für technische Analyse.

---

## Blinder Fleck 8 — Historisch / aktuell / hypothetisch braucht visuelle Grammatik

Badges allein reichen nicht.

Die gleiche Regel muss überall gelten:
- Foto,
- Zeichnung,
- Tabelle,
- 3D,
- technische Zeichnung,
- Task.

Der Benutzer soll ohne Lesen erkennen:
**Das wurde gemessen / das sehen wir / das steht nur in einer alten Zeichnung / das vermuten wir.**

Der London-Charter-Grundsatz ist dafür passend: Heritage-Visualisierungen sollen den Status des dargestellten Wissens und die Unsicherheit erkennbar machen.

---

## Blinder Fleck 9 — Keine Variantenwerkbank

Gerade die Widersprüche sind produktiv.

Beispiele:
- 22 vs 24 mm,
- mehrere Ringlängen,
- unterschiedliche historische Blattstände,
- unbekannte aktuelle Reparaturvariante.

Statt eine Variante auszuwählen, braucht die Workbench:
- A/B umschalten,
- Differenzen hervorheben,
- „welche ist am realen Teil?“,
- Foto oder Maß direkt als Entscheidungsevidenz anhängen.

---

## Blinder Fleck 10 — Demontage ist noch Liste, nicht Ereignisfluss

GAP-01…08 sind gut definiert, aber am Samstag braucht man eine **laufende Ereignisoberfläche**:

`Teil vor Ausbau → Partner → lösen → freigelegte Flächen → messen → Teil ablegen → nächstes Ereignis`

Mit:
- Ereignisnummer,
- Teil-ID,
- Partner-ID,
- Vorher-/Nachher-Foto,
- Befestiger,
- Orientierung,
- Kommentar / Audio,
- Lagerort.

Die App muss das nächste sinnvolle Capture aktiv anbieten.

---

## Blinder Fleck 11 — Papier und Digital sind noch getrennt

Die Zielgruppe arbeitet seit Jahrzehnten mit Werkstattzeichnungen. Das ist ein Vorteil.

Jedes spätere Blatt sollte erhalten:
- Zeichnungsnummer,
- Teil-ID,
- klare Prüf-/Freigabekennung,
- QR/Shortcode zur digitalen Bauteilseite,
- markierte offene Messstellen,
- optional handschriftlich nutzbare Felder.

Umgekehrt soll die digitale Seite ein **A3-Druckblatt für genau dieses Teil** erzeugen können.

Das ist wahrscheinlich ergonomisch stärker als eine rein digitale Lösung.

---

## Blinder Fleck 12 — Alterstauglichkeit ist mehr als große Schrift

W3C nennt bei älteren Nutzern insbesondere sinkende Kontrastsensitivität, Feinmotorik und teilweise Kurzzeitgedächtnis/Konzentration. Für häufige Touch-Aktionen ist ein Zielmaß von 44×44 CSS px eine gute verschärfte Leitlinie.

Konsequenzen für die Werkstatt:
- große eindeutige Tasten,
- keine kleinen Hotspots als einziger Weg,
- keine Gesten ohne sichtbares alternatives Bedienelement,
- keine wichtigen Funktionen hinter Hover,
- feste Begriffe an festen Orten,
- ein Schritt pro Aufgabe,
- klarer Zurück-/Undo-Weg,
- hohe Kontraste,
- 200-%-Textzoom ohne Funktionsverlust,
- 3D-Orbit erst bewusst aktivieren,
- feste Standardansichten als große Schaltflächen.

---

## Blinder Fleck 13 — Keine Feldrobustheit

Am Rad herrschen andere Bedingungen als am Schreibtisch:
- Sonne,
- nasse/kalte Hände,
- Handschuhe,
- schlechte Verbindung,
- Lärm,
- mehrere Menschen schauen gemeinsam,
- Telefon wird oft nur mit einer Hand gehalten.

Die Workbench sollte daher langfristig:
- offlinefähig sein,
- Captures lokal puffern,
- später exportieren/synchronisieren,
- große Touchflächen nutzen,
- Foto/Audio mit sehr wenig Navigation starten,
- keine Daten verlieren, wenn der Browser geschlossen wird.

---

## Zielbild

Nicht eine immer komplexere Homepage.

Sondern zwei klar gekoppelte Oberflächen:

### 1. Story / Research Page
Öffentlich verständlich, ruhig, VZO-verwandt.
Zweck: erklären, dokumentieren, Fortschritt zeigen.

### 2. Werkstatt / Reconstruction Workbench
Zweck: gemeinsam am Rad arbeiten.

Primäre Navigation:
- **Rad**
- **Teile**
- **Messen**
- **Demontage**
- **Zeichnungen**
- **Erinnerungen**

Der Einstieg in jede Aufgabe erfolgt möglichst über das reale/virtuelle Bauteil.

---

## Nicht tun

- aktuelle Landing Page mit noch mehr Karten erweitern,
- Fotorealismus als Vertrauenserzeuger einsetzen,
- Unsicherheit in Tooltip-Texte verstecken,
- vor Ort freie große Formulare anbieten,
- 3D nur als Viewer behandeln,
- alte Zeichnungen ungeprüft in CAD umsetzen,
- eine „richtige“ Variante erzwingen, wenn zwei Hypothesen produktiver wären.
