# Field Workbench Architecture

Stand: 2026-10-07  
Status: Konzept für Astra-Implementierung.

## Kerninteraktion

Die zentrale Schleife lautet:

**SELECT → UNDERSTAND → QUESTION → CAPTURE → UPDATE**

### SELECT
Teil auswählen über:
- 3D,
- technische Ansicht,
- Foto,
- Suche nach lokalem Namen / KS-ID.

### UNDERSTAND
Eine kompakte Karte zeigt:
- Bauteilname + lokale Namen,
- aktueller Kenntnisstatus,
- wichtigste Quellen,
- aktuelle/historische/hypothetische Werte getrennt.

### QUESTION
Maximal eine primäre Frage im Vordergrund:
- identifizieren,
- messen,
- vergleichen,
- erklären,
- Risiko beschreiben.

### CAPTURE
Je nach Frage:
- Zahl + Einheit,
- Messstrecke,
- Auswahl A/B,
- Foto,
- Audio,
- kurzer Freitext,
- „weiß ich nicht“.

### UPDATE
Vor Speichern sichtbar:
- Welche Claims werden dadurch gestützt/widerlegt?
- Welcher Konflikt/GAP wird kleiner?
- Ist es Beobachtung, Messung oder Expertenaussage?

---

## 3D Workbench

3D ist Hypothesenraum, nicht Dekoration.

### Mindestmodi
- Gesamtansicht,
- Landseite,
- Wasserseite,
- Welle,
- Kränze,
- Kümpfe,
- Schaufeln,
- Explode,
- Schnitt,
- Vergleich A/B,
- Messstellen,
- offene Fragen.

### Bedienprinzip
Auf Touch:
- Orbit standardmäßig gesperrt,
- große Taste **„Modell bewegen“**,
- große feste Ansichten,
- „Teil antippen“ als primäre Interaktion,
- Reset immer sichtbar.

### Unsicherheitsdarstellung
- observed/current: normal,
- measured/current: normal + Messsymbol,
- historical only: technische Kontur,
- inferred: transparent/ghost,
- conflicting: zwei Varianten,
- unknown: Lücke / Placeholder,
- scan fragment: eigener Overlay-Layer.

Die Legende bleibt immer erreichbar.

---

## Data Capture Schema

Neue Observation Records sollen mindestens tragen:

```json
{
  "id": "OBS-...",
  "question_id": "GAP-...",
  "event_id": "EVT-...",
  "component_ids": ["KS-..."],
  "relation_ids": [],
  "kind": "measurement|observation|identification|expert-narrative|risk",
  "value": null,
  "unit": null,
  "endpoints": null,
  "tool": null,
  "uncertainty": null,
  "side": "LAND|WATER|UNKNOWN",
  "state": "installed|during-release|removed",
  "person": null,
  "timestamp": null,
  "media": [],
  "quote": null,
  "interpretation": null,
  "confidence": null
}
```

Expert narrative und technische Interpretation bleiben getrennte Felder.

---

## Tacit Knowledge Schema

Für Erfahrungswissen zusätzlich:

- trigger / condition,
- mechanism,
- expected behaviour,
- failure consequence,
- warning sign,
- mitigation / repair practice,
- component IDs,
- source person,
- disagreement / alternate account.

Beispiel:
> „Den Keil nicht trocken ganz fest setzen.“

wird nicht nur als Zitat gespeichert, sondern später eventuell:
- condition: trocken vor Wasserkontakt,
- mechanism: Quellen des Holzes,
- consequence: Überpressung / Rissrisiko,
- mitigation: definierter Montagezustand,
- status: expert narrative until validated.

---

## Paper ↔ Digital

Jede Komponentenansicht soll langfristig ein Werkstattblatt erzeugen:

- A3 quer,
- KS-Zeichnungsnummer,
- Revision,
- Status,
- Ansichten/Schnitte,
- Stückliste,
- offene Maße als leere/markierte Felder,
- QR/Shortcode zurück zur Komponente,
- Platz für handschriftliche Notizen.

Die Arbeit darf komplett auf Papier begonnen und später digitalisiert werden.

---

## Field UX acceptance tests

Mit mindestens 2–3 realen Nutzern aus der Zielgruppe prüfen:

1. Ein genanntes Teil in ≤ 15 s finden.
2. Eine konkrete Messaufgabe ohne Erklärung starten.
3. Messwert + Foto ohne Datenverlust erfassen.
4. Zwischen historischem und aktuellem Wert unterscheiden können.
5. Eine Expertenaussage an ein Teil hängen können.
6. Eine 3D-Ansicht wieder auf eine bekannte Standardansicht zurücksetzen.
7. Kein kritischer Vorgang verlangt einen kleinen Touch-Hotspot oder eine versteckte Geste.
8. 200 % Textzoom bleibt funktionsfähig.
9. Häufige Controls ≥ 44 × 44 CSS px.
10. Nach Unterbrechung ist klar, wo die Aufgabe fortgesetzt wird.

Testkriterium ist nicht „gefällt mir“, sondern Aufgabe erfolgreich / Fehler / benötigte Hilfe / Zeit.
