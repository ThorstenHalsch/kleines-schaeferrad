# Maintenance Coherence Audit — 2026-10-07

## Verdict

Der aktuelle Produktstand ist funktional reich, aber kognitiv überladen. Die Hauptursache ist nicht fehlende Funktionalität, sondern fehlende Hierarchie.

## Symptome

- Startseite mischt Story, Forschungsstatus und interne Terminologie.
- Werkstatt wirkt wie ein Steuerpult.
- Scan-Modus verdrängt/zerstört die mentale Kontinuität des Modell-Viewers.
- Kontextgeometrie des stationären Tragwerks ist zu stark reduziert.
- Feldmodus führt sequenziell, erklärt den Gesamtzusammenhang aber zu wenig.
- PDF ist vollständig, aber textdominant und zu lang.
- PDF-Zugang ist nicht prominent genug.
- Web und Papier besitzen Tasks, aber noch keine gemeinsame visuelle Aufnahmegrammatik.

## Maintenance-Ziel

Nicht mehr Features, sondern klare rote Linie, visuelle Führung, technische Ergonomie, verständliche Sprache, reduzierte Bedienkomplexität und vollständiger Systemkontext des Wasserrads.

## UI-Hierarchie künftig

### Startseite

Drei klare Einstiege: Das Rad verstehen; Werkstatt / Modell prüfen; Arbeitsplan für die Demontage. PDF und Feldmodus müssen sofort sichtbar sein.

### Werkstatt

Primär: Modell, Kontext, Teilwahl, Quellenvergleich. Sekundär: Varianten, Scan, technische Einstellungen. Advanced Scan Controls standardmäßig geschlossen.

### Feldmodus

Primär: Kontextbild/Skizze, aktueller Handgriff, Foto/Maß, Weiter. Aufgabenübersicht ist Orientierung, kein Pflichtdurchlauf.

### Papier

Baugruppenorientiert und visuell. 8–12 A3-Seiten statt 38 taskzentrierter Seiten.

## 3D-Kontext

Die Rekonstruktion muss das Wasserrad als Gesamtsystem zeigen: Radkörper, Welle, Lager, Lagerstöcke, Radstatt, untere Trag-/Halterahmen, seitliche Auffang-/Führungsrahmen, Trog, Rinne, Zubringer und stationäre Holzgestelle.

Was nicht sicher rekonstruiert ist: ghosted, separat schaltbar, Status context-observed, context-hypothesis oder context-unknown. Nicht automatisch aus dem Scan modellieren.

## Scan UX

Scan darf die Modellsteuerung nicht in einen zweiten Viewer zerreißen. Ziel: Modellnavigation bleibt stabil; Scan als Overlay oder synchronisierte Vergleichsansicht; gleiche Kameraorientierung; Scan-Einstellungen in Advanced Panel; Default nur aus, achsnormalisiert, grob ausgerichtet. Numerische XYZ/RX/RY/RZ nur Expert Mode.

## Erfolg

Maintenance ist erfolgreich, wenn weniger erklärt werden muss, obwohl nicht weniger Wissen vorhanden ist.