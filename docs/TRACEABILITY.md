# Traceability & Confidence

Jede rekonstruierte Eigenschaft wird als Claim mit Quelle geführt.

## Confidence-Klassen

| Code | Bedeutung |
|---|---|
| M | direkt am aktuellen Objekt gemessen / kalibrierter Scan |
| O | am aktuellen Objekt sichtbar oder in 3D beobachtet |
| H | historische/handwerkliche Zeichnung oder Notiz |
| X | externe Kontextquelle |
| I | aus mehreren Quellen abgeleitet |
| U | unbekannt / noch nicht belegt |

Ein numerisches Maß darf nur ohne Warnhinweis in die finale Geometrie eingehen, wenn es mindestens **M** oder eine sauber dokumentierte Kombination aus O/H/I besitzt.

## Konfliktregel

Bei Widersprüchen gilt nicht automatisch „neu schlägt alt“ oder „Scan schlägt Zeichnung“.

Stattdessen:
1. beide Claims behalten,
2. Quellen separat zitieren,
3. möglichen Grund dokumentieren (Reparatur, Saison, Messfehler, Scanartefakt, andere Bauteilvariante),
4. gezielte Feldmessung definieren,
5. erst danach einen Wert als Rekonstruktionsparameter wählen.

## Evidence-IDs

- `PHOTO-68xx` — Originalfoto
- `DRAW-*` — aus Foto transkribierte Zeichnung/Notiz
- `SCAN-20261007-01-PLY`
- `SCAN-20261007-01-GLB`
- `MEAS-*` — neue Feldmessung
- `COMP-*` — Bauteil
- `CLAIM-*` — konkrete Aussage/Abmessung

## Raw vs. Derived

Raw-Dateien werden niemals überschrieben.

Derived Assets (bereinigte Punktwolken, registrierte Scans, Meshes, GLB, Viewer-LOD, Texturen) müssen ihren Ursprung auf Raw-IDs zurückführen.
