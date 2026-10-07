# Scan Registration Plan

Stand: 2026-10-07

## Current problem

Das aktuelle GLB-Overlay wird im Three.js-Viewer ohne mechanische Achsnormalisierung geladen.

Workbench:
- mechanische Darstellung: Z-up,
- GLTF: Y-up.

Damit ist ein sichtbarer Kippfehler erwartbar.

Zusätzlich existiert noch keine mechanische Registrierung.

## Bekannte Exportrelation

Aus Scan-Forensik:

`(Xg, Yg, Zg) = (Xp, Zp, -Yp)`

Diese Relation erklärt PLY↔GLB Exportachsen, nicht die Lage zum mechanischen Wasserrad-Koordinatensystem.

`adopted_mechanical_transform = null` bleibt verbindlich.

## Registration states

Jeder Scan erhält künftig einen expliziten Zustand:

- RAW_EXPORT
- AXIS_NORMALIZED
- ROUGH_ALIGNED
- MECHANICALLY_REGISTERED
- METRICALLY_CALIBRATED

Der Viewer zeigt diesen Status immer sichtbar.

## Next technical steps

1. GLTF Y-up in mechanisches Z-up normalisieren.
2. Richtungs-/Handedness-Prüfung visuell gegen Fotos.
3. Noch keine LAND/WATER-Zuordnung erzwingen.
4. Gemeinsame Referenzmarker am verbleibenden Tragwerk festlegen.
5. Mindestens drei nicht kollineare Referenzpunkte mit IDs.
6. Paarweise Distanzen und Höhen-/Achsenbezug messen.
7. Marker in allen zukünftigen Scans sichtbar halten.
8. Transformationen als Datenobjekt speichern, nicht hardcodiert im Viewer.
9. Rohscan niemals verändern.

## Field marker concept

Beispiel:
- DATUM-A
- DATUM-B
- DATUM-C
- AXIS-L
- AXIS-W

Für jeden Marker:
- Foto,
- physische Beschreibung,
- Koordinate sobald bestimmt,
- Messunsicherheit,
- Bestand nach Demontage ja/nein.

## Important distinction

Axis normalization is not registration.

Rough visual alignment is not metrology.

Only independently measured references may promote a transform to mechanically registered / metrically calibrated.
