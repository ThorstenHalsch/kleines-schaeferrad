# NEXT ASTRA WORK SESSION — Field Reconstruction Workbench Alpha

Branch-Ausgangspunkt: `main` nach Research Page Draft 01.

## Mission

Transformiere die bestehende Research Page von einer primär publizierenden Darstellung in ein **zweischichtiges System aus Story Page + Field Reconstruction Workbench**.

Die Baseline bleibt Source of Truth. Historische Werte, aktuelle Beobachtung, Inferenz und Konflikt dürfen nie unmarkiert ineinanderfallen.

Diese Session darf jetzt ausdrücklich schwere technische Arbeit übernehmen:
- parametrische Hypothesengeometrie,
- Three.js,
- Volumen-/Komponentenmodell,
- Scan-Overlays und Registrierungsexperimente,
- Exploded Views,
- technische Projektionen,
- datengetriebene Feldinteraktion.

## Zuerst lesen

- `docs/UX-AUDIT-DRAFT-01.md`
- `docs/FIELD-WORKBENCH-ARCHITECTURE.md`
- `docs/BASELINE.md`
- `docs/HUMAN-CALIBRATION.md`
- `docs/HANDWERKSWISSEN-CAPTURE.md`
- `docs/DRAWING-LANGUAGE.md`
- `docs/CAPTURE-BEFORE-DISASSEMBLY.md`
- `data/components.json`
- `data/assembly.graph.json`
- `data/geometry.claims.json`
- `data/conflicts.json`
- `data/knowledge-gaps.json`
- `data/reference-system.json`
- `evidence/manifest.json`

## Phase A — Workflow before graphics

Definiere zuerst die tatsächlichen Nutzer-/Feldflüsse:

1. Teil finden.
2. Wissensstand verstehen.
3. offene Frage sehen.
4. zeigen / messen / vergleichen / erklären.
5. Observation Record erzeugen.
6. Änderung am Knowledge State sichtbar machen.

Baue daraus die IA für `/werkstatt/`. Die öffentliche Landing Page bleibt erhalten und verweist prominent dorthin.

Keine zusätzliche Card-Galerie als Ersatz für Workflow-Design.

## Phase B — Parametric Hypothesis Model v0

Baue ein bewusst unperfektes, aber strukturell brauchbares parametrisches Modell.

Regeln:
- stabile Component-IDs,
- drei durchgehende Arme vs. sechs Speichenenden korrekt unterscheiden,
- zwei Kranzebenen,
- segmentierte Krümmlinge,
- Kümpfe/Schaufeln zunächst parametrisch,
- Lager/Radstatt/Trog als separate stationäre Schicht,
- historische Dimensionen nur als Hypothesenparameter,
- alle nicht belegten Maße mit Range/null/provenance,
- Konflikte als Varianten, nicht durch Mittelwerte auflösen.

Erzeuge mindestens:
- assembled hypothesis,
- exploded hypothesis,
- land/water orthographic,
- shaft/arm focus,
- rim/kruemmling focus,
- vessel/paddle focus.

## Phase C — Three.js Workbench

Implementiere eine touch-sichere 3D-Arbeitsfläche.

Pflicht:
- große feste Standardansichten,
- Orbit erst nach expliziter Aktivierung,
- Reset,
- Component Pick,
- Layer Toggle: model / scan / historical / questions,
- Explode,
- simple section/cut if robust,
- uncertainty legend,
- Frage-/Messpins direkt an Komponenten,
- A/B-Hypothesenvergleich.

Keine Fotorealistik als Default.

## Phase D — Evidence-linked Inspector

Für ausgewählte Komponente:
- IDs / lokale Namen,
- Quellenbilder,
- relevante Claims,
- Konflikte,
- aktuelle Tasks,
- historische vs aktuelle vs hypothetische Maße,
- direkte Aktion: Messen / Foto / Erklärung / A-B-Auswahl.

Jeder sichtbare Wert muss bis zur Quelle zurückverfolgbar sein.

## Phase E — Field Capture Alpha

Definiere und implementiere Observation Records gemäß `FIELD-WORKBENCH-ARCHITECTURE.md`.

Mindestens:
- measurement,
- observation,
- identification,
- expert narrative,
- risk.

Für Alpha darf Speicherung lokal erfolgen (IndexedDB/local storage/file export), sofern Daten verlustarm exportierbar sind. Keine unnötige Backend-Plattform bauen.

Foto-/Audio-Capture nur, wenn Browser/API stabil und UX einfach bleibt.

## Phase F — Werkstattzeichnung v0

Erzeuge aus **derselben parametrischen Geometrie** erste technische Review-Blätter im etablierten 70er/80er-Werkstattstil.

Noch keine Fertigungsfreigabe.

Mindestens:
- KS-00 Systemübersicht,
- KS-10 Welle/Arme,
- KS-20 Kranz/Krümmling,
- KS-30 Kumpf,
- KS-60 Zusammenbau / Exploded.

Offene Maße sichtbar markieren statt erfinden.

## Phase G — Risk / Craft Knowledge Layer

Führe ein erstes strukturiertes Schema für:
- Quellen/Schwinden,
- Keil-/Passungsrisiken,
- Strömungs-/Stoßlasten,
- Verschleiß,
- Reparaturpraxis,
- Warnsignale.

UI-seitig direkt an Komponenten/Verbindungen anbinden.

## Phase H — Ergonomic field test

Die Workbench nicht nur technisch bauen, sondern mit einer simulierten oder realen Feldsequenz prüfen.

Prüfen:
- 320 px und aktuelles iPhone,
- Desktop,
- 200 % Textzoom,
- große Targets,
- keine hover-only Funktionen,
- keine hidden-gesture-only Funktionen,
- unterbrochene Aufgabe kann fortgesetzt werden,
- Standardansichten funktionieren ohne 3D-Erfahrung.

Wenn reale Nutzer verfügbar sind, mindestens 2–3 Personen aus der tatsächlichen Zielgruppe mit kurzen Tasks testen und Resultate materialisieren.

## Nicht tun

- Baseline-Widersprüche löschen,
- historische Maße als current as-built ausgeben,
- Scanlöcher automatisch als reale Geometrie schließen,
- große Backend-/Account-Plattform aufbauen,
- UI mit Marketingkarten aufblasen,
- „fertigen Digital Twin“ behaupten.

## Gate

Stoppe erst bei:

**FIELD RECONSTRUCTION WORKBENCH ALPHA READY**

Das Gate verlangt:
- navigierbares Hypothesenmodell,
- Component ↔ Claim ↔ Evidence ↔ Task-Verknüpfung,
- mindestens einen vollständigen Capture-Loop,
- erste technische Review-Blätter,
- dokumentierte Unsicherheitsdarstellung,
- ergonomische Testevidenz,
- klaren nächsten Feld-/Human-Calibration-Plan.
