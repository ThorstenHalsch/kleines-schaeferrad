# UX / Reconstruction Audit — Draft 02

Stand: 2026-10-07  
Ausgangspunkt: Field Reconstruction Workbench Alpha auf main.

## Executive Verdict

Die technische Basis ist tragfähig, aber die Benutzeroberfläche ist noch zu stark aus Sicht von Forschung und Software strukturiert.

Der nächste Reifegrad entsteht nicht durch mehr UI-Komponenten, sondern durch drei Verschiebungen:

1. **Handwerk zuerst, Forschung dahinter.**
2. **Das Rad und der aktuelle Arbeitsschritt werden zur Navigation.**
3. **Web und Papier teilen dasselbe Aufgaben- und Evidenzmodell.**

Die aktuelle Workbench bleibt als Analysemodus wertvoll. Für die reale Demontage braucht es zusätzlich einen radikal vereinfachten Feldmodus.

---

## 1. Sprache und Identität

### Problem

Die öffentliche Seite und die Werkstatt sprechen zu häufig in Projekt-/Research-Sprache:
- Research View
- Baseline
- Claims
- Conflict Matrix
- Digital Twin
- Hypothese
- Evidence Explorer

Diese Begriffe sind intern korrekt, erzeugen extern aber Distanz.

### Ziel

Die Menschen, die das Rad seit Jahren oder Jahrzehnten erhalten, sollen als Wissensträger und Mitautoren angesprochen werden.

Leitidee:

> Ihr habt dieses Rad erhalten. Wir helfen dabei, euer Wissen so festzuhalten, dass es weitergegeben werden kann.

### Human-facing terminology

| Intern | Menschliche Oberfläche |
|---|---|
| Claim | Aussage / Befund |
| Conflict | Widerspruch / noch ungeklärt |
| Hypothesis | Arbeitsmodell / noch nicht nachgemessen |
| Evidence | Quelle / Nachweis |
| Expert narrative | Erfahrung aus der Werkstatt |
| Capture | Aufnahme / festhalten |
| Digital Twin | digitale Rekonstruktion |
| Unknown geometry | noch nicht nachgemessen |
| Validation | gemeinsam prüfen |

Interne JSON-/Code-Begriffe dürfen Englisch bleiben.

---

## 2. Visuelle Sprache

### Problem

Die Workbench ist aktuell zu schwer:
- dunkler Vollheader,
- viele gerahmte Panels,
- viele Fieldsets,
- hohe Informationsdichte,
- Engineering-Tool-Anmutung.

### Ziel

Visuelle Metapher: **helles Zeichenbrett / Werkbank**.

Leitlinien:
- warmes Weiß / Papier als Grundfläche,
- tiefes Grün nur als Identitätsakzent,
- technische Linien statt großer Containerflächen,
- Ocker für offene Fragen,
- Fotos und Radmodell dominieren,
- weniger Karten,
- größere Weißräume,
- UI nie visueller Hauptgegenstand.

Die 80er-Jahre-Werkstattzeichnung bleibt die zweite visuelle Sprache für technische Inhalte.

---

## 3. Werkstatt vs Feldmodus

### Analysemodus

Die bestehende `/werkstatt/` bleibt erhalten für:
- 3D-Analyse,
- Quellen,
- Claims,
- Konflikte,
- Hypothesenparameter,
- Protokoll,
- Zeichnungen.

### Feldmodus

Neue, stark reduzierte Oberfläche:
- eine Aufgabe pro Bildschirm,
- großes Teil / große Frage,
- maximal eine primäre Aktion,
- große Vor/Zurück-Schritte,
- sichtbare Speicherung,
- möglichst kein freies Scrollen durch lange Analysebereiche.

Beispiel:

> KS-ARM-02  
> Vor dem Lösen: Keil von beiden Seiten fotografieren.

[Foto Vorderseite]  
[Foto Rückseite]

Danach:

> Axiale Lage messen.

[Messung starten]

Danach:

> Warum sitzt der Keil so herum?

[Erklärung aufnehmen]

---

## 4. Räumliche Orientierung

Die aktuelle 3D-Arbeitsfläche bietet zu wenig Orientierung.

Pflicht künftig:
- LAND / WATER bzw. solange ungeklärt SIDE A / SIDE B,
- OBEN,
- Fließrichtung,
- Trog,
- Radstatt,
- Achsentriade,
- Blickrichtung,
- später Drehrichtung.

Die Orientierung muss permanent sichtbar sein und darf nicht nur in Buttonnamen existieren.

---

## 5. Scan Overlay

Der aktuelle GLB-Overlay darf nicht länger den Eindruck mechanischer Registrierung erzeugen.

Bekannt:
- GLTF ist Y-up,
- mechanisches Modell ist Z-up,
- PLY→GLB Exportachsenkandidat ist dokumentiert,
- mechanische Registrierung ist weiterhin null.

Künftig Statusstufen sichtbar unterscheiden:
1. raw export,
2. axis-normalized,
3. roughly aligned,
4. mechanically registered,
5. metrically calibrated.

Nur Stufe 4/5 darf wie ein deckungsgleiches Overlay wirken.

---

## 6. Arm-/Wellenzone

Die aktuelle Armgeometrie als gerade Quader ist nur ein Platzhalter und muss visuell als solche gekennzeichnet werden.

Neue offene Hypothesen:
- Arme möglicherweise gebogen / gekröpft,
- unterschiedliche axiale Einsteckebenen,
- ineinandergreifende Mortisen-/Armstruktur,
- Endpaare möglicherweise räumlich versetzt,
- Keile / Verriegelung eventuell funktional gekoppelt.

Diese Fragen werden nicht im Modell entschieden, sondern in Feldaufgaben übersetzt.

---

## 7. Physisches Teileinventar

Ontologie ist nicht Stückliste.

Während Demontage entsteht ein reales Instance Register:
- KS-ARM-001 …
- KS-KRU-001 …
- KS-KUM-001 …
- KS-PAD-001 …
- KS-KEI-001 …

Jede Instanz verbindet:
- Familie,
- lokalen Namen,
- Einbauposition,
- Partner,
- historischen Marker,
- Zustand,
- Lagerplatz,
- Medien,
- Ereignisse.

---

## 8. Offline- und Datenrobustheit

Vor Feldfreigabe notwendig:
- Offline-Start nach vorherigem Laden,
- getesteter Service Worker / PWA-Cache,
- Speicherwarnung,
- Session-Backup,
- realer Test mit 20–50 Fotos,
- Datenexport trotz Offlinezustand.

Langfristig Medien getrennt vom JSON-Manifest speichern; Base64-only ist für große Feldsessions nicht skalierbar.

---

## 9. Erfolgskriterien

Nicht:
- sieht professionell aus,
- 3D funktioniert,
- viele Features vorhanden.

Sondern:
- ein Monteur findet ein Teil ohne Erklärung,
- versteht, was noch offen ist,
- kann eine Aufgabe korrekt abarbeiten,
- kann unser Modell widersprechen,
- kann sein Erfahrungswissen an die richtige Stelle hängen,
- verliert keine Daten,
- kann mit Papier vollständig weiterarbeiten.
