# NEXT ASTRA WORK SESSION — Brute-Force Functional Reconstruction

Status: **PREPARED — noch nicht starten**  
Ausgangspunkt nach Merge: Maintenance-Coherence-Stand auf `main`.

Verbindlicher Missionsvertrag:
`state/ASTRA-BRUTE-FORCE-RECONSTRUCTION.md`

## Startbedingung

Die Session soll beginnen, sobald:
1. der aktuelle Maintenance-Rebuild gemergt und deployed ist;
2. die vorhandenen Wasserseitenbilder als Kontextquelle übernommen sind;
3. möglichst weitere Bilder aus `docs/PHOTO-CAPTURE-TODO.md` vorliegen.

Weitere Bilder verbessern die Rekonstruktion, sind aber kein Grund, bereits vorhandene Evidenz erneut zu vereinfachen.

## Mission

Erzeuge die maximal plausible funktionale Rekonstruktion des **gesamten technischen Systems**:

- Radkörper,
- Welle und Armvarianten,
- Kränze / Krümmlinge,
- Kümpfe / Schaufeln,
- Keile / Stifte / Befestiger,
- Lager und Lagerstöcke,
- Radstatt,
- obere / untere / seitliche Rahmen,
- Trog und Rinne,
- Wasserlinie,
- Regnitz-Ufer,
- Fließrichtung und plausible Radfunktion,
- Standortorientierung / Himmelsrichtungen sobald belastbar.

Nicht nur ein Radmodell, sondern ein Systemmodell.

## Forschungsauftrag

Vor Geometriesynthese gezielt öffentliche Quellen zu historischen Regnitz-/Möhrendorfer Wasserschöpfrädern recherchieren:

- traditionelle Radstatt- und Lagerkonstruktionen,
- Arm-/Wellenverbindungen,
- Mortisen, Keile, Holznägel und Verstiftungen,
- typische Krümmling-/Kumpf-/Schaufelverbindungen,
- Trog-/Rinnen-Wasserführung,
- verwandte erhaltene Räder,
- historische Proportionen und Terminologie.

Quellenmaterial und daraus abgeleitete Annahmen getrennt speichern.

## Brute-Force-Regel

Astra darf fehlende Mechanik synthetisch ergänzen, wenn sie als solche sichtbar bleibt.

Für verdeckte Verbindungen mehrere Kandidaten erzeugen und ranken nach:
- Foto-/Scanverträglichkeit,
- historischen Zeichnungen,
- Kollisionsfreiheit,
- Montage-/Demontierbarkeit,
- plausiblem Kraftfluss,
- Holzbau-/Zimmermannslogik,
- minimalen Zusatzannahmen.

Keine synthetische Geometrie als gemessen ausgeben.

## Pflichtdarstellungen

- Evidence-only model
- best-ranked synthetic model
- alternative connection candidates
- installed state
- exploded state
- cutaways / shaft interior candidates
- stationary frame context
- water/site context
- provenance/confidence overlay

## UX-Vertrag

Die vorhandene Maintenance-UX bleibt verbindlich:
- human-facing Deutsch,
- Source-Stylekit-Tokens,
- keine aufgeblasenen Marketingkomponenten,
- Modell dominant,
- technische Details progressiv,
- visuelle Werkstatt-/Messführung aus `data/visual-guides.json`.

Astra darf die UX für neue 3D-Funktionen erweitern, aber nicht erneut ein Cockpit bauen.

## Gate

Stoppe bei:

**BRUTE-FORCE FUNCTIONAL RECONSTRUCTION READY**

Das Gate verlangt:
- vollständiges funktionales Systemmodell,
- stationäre Rahmen-/Lager-/Wasserkomponenten enthalten oder explizit offen,
- verdeckte Verbindungen als gerankte Kandidaten,
- Standort-/Wasserfunktion räumlich nachvollziehbar,
- Evidence vs Synthetic jederzeit unterscheidbar,
- Modell/Zeichnungen/visuelle Feldhilfen aus derselben Geometriebasis,
- nachvollziehbare Quellen- und Annahmenmatrix.
