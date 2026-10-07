# GitHub Page — Style Transfer & Research Architecture

Referenz: https://thorstenhalsch.github.io/Webpage-preview/

## Übernommene visuelle Grammatik

Die neue Forschungsseite übernimmt bewusst die visuelle Sprache der VZO-Vorschau:
- Manrope,
- Papierweiß `#fafbf7`,
- tiefes Grün `#193e35`,
- Lime-Akzent `#dbe987`,
- weiche grüne Flächen,
- sehr große, enge Überschriften,
- runde 24–32 px Karten,
- Sticky Navigation,
- ruhige mobile-first Raster,
- fotografischer Hero mit Badge und Caption,
- sachliche Faktenstreifen,
- dunkle grüne Callout-Flächen.

Die Seite kopiert **nicht** die Vereinsinhalte. Sie übersetzt denselben Charakter in eine Research Experience.

## Informationsarchitektur

1. Hero: Objekt, Ort, Gate.
2. Baseline-Zahlen: 43 Originalquellen, 355 Claims, 12 Konflikte, 8 P0-Gaps.
3. „Was wir wissen“: Topologie, Evidenzmodell, Grenzen.
4. Anatomie: 22 Ontologieobjekte direkt aus `data/components.json`.
5. Evidenz: Originalquellen/Scanforensik.
6. Konflikte: direkt aus `data/conflicts.json`.
7. Demontage-Mission: direkt aus `data/knowledge-gaps.json`.
8. Handwerkswissen: expliziter Interview-/Tacit-Knowledge-Track.
9. Road to Digital Twin: L0–L4.

## Wahrheitsregel

Die Page ist eine Projektion der Baseline und keine zweite Datenbank. Zahlen, Konflikte und GAPs werden beim Build direkt aus den JSON-Artefakten geladen. `null` bleibt unbekannt. Historische Slots werden nicht als aktuelle Teile ausgegeben.


## Zweite visuelle Sprache: Werkstattzeichnung

Für technische Inhalte wird die VZO-Optik bewusst unterbrochen. Werkstattblätter orientieren sich an der klassischen Prüfzeichnungssprache aus `garden-torch-connector`: Schwarz/Weiß, A3-Logik, Achsenlinien, Maßketten, Schriftfeld, Revision und sichtbarer Prüfstatus.

Die vollständigen Regeln stehen in `DRAWING-LANGUAGE.md`. Die Page darf schon nichtmaßhaltige Baseline-Blätter zeigen; maßhaltige Projektionen und CAD-Ableitungen bleiben der späteren Astra-Session vorbehalten.
