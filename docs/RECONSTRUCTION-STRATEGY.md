# Reconstruction Strategy

## Architektur

Die Rekonstruktion wird in fünf getrennten Schichten aufgebaut.

### L0 — Raw Evidence
Originalfotos, Zeichnungsfotos, PLY, GLB, Splats, spätere Einzelteilscans und Messprotokolle.

### L1 — Evidence Normalization
- Hash/Manifest,
- Orientierung,
- Quellenklasse,
- Bild-/Scanmetadaten,
- Transkription von Zeichnungen,
- Segmentierung und Registrierung.

### L2 — Parametric Mechanical Model
Ein maßhaltiges, bewusst nüchternes Komponentenmodell:
- stabile Component-IDs,
- Parameter statt freiem Modellieren,
- Assembly-Graph,
- Confidence pro Parameter.

Diese Ebene ist die mechanische Wahrheitsschicht.

### L3 — Surface Reality
Photogrammetrie-/LiDAR-Meshes werden auf L2 registriert. Schäden, Alterung, Werkzeugspuren und Verformung können damit erhalten werden, ohne die Mechanik aus einem verrauschten Mesh erraten zu müssen.

### L4 — Appearance / Site Reality
Gaussian Splats bzw. andere radiance-field-artige Darstellungen konservieren Atmosphäre, Vegetation, Wasser und den räumlichen Gesamteindruck.

## Three.js

Three.js ist **Viewer und Integrationsschicht**, nicht CAD-Wahrheitsquelle.

Der Viewer soll später umschalten können zwischen:
- parametrischem Rekonstruktionsmodell,
- realen Meshes,
- Punktwolken,
- Splats,
- Exploded View,
- Montagefolge,
- Confidence/Evidence Overlay.

## Rekonstruktionsregel

Ein schmutziger Scan wird nicht „repariert“, indem fehlende Flächen erfunden werden.

Stattdessen:
- brauchbare Geometrie extrahieren,
- mit Zeichnungen und Messungen registrieren,
- Lücken explizit markieren,
- erst auf der parametrischen Ebene rekonstruieren.

## Zielartefakte

- `model/master.glb` — segmentiertes Integrationsmodell.
- `data/assembly.graph.json` — Bauteil-/Verbindungsgraph.
- `data/geometry.claims.json` — Maße + Provenienz.
- `evidence/manifest.json` — Rohquellen.
- Three.js-Viewer.
- Demontage-/Montage-Timeline.

