# Baseline Resonance & GitHub Page Brief

Stand: 2026-10-07  
Review-Basis: Branch `work/pre-disassembly-baseline-20261007`, Baseline-Commit `0076cab15106092c8aafbb900a30955fa9fc7cb8`.

## Abnahme

Die Understanding-Session wird als **BASELINE UNDERSTANDING READY** angenommen.

Das Gate bedeutet ausdrücklich:
- vorhandener Quellenbestand ist vollständig inventarisiert und einzeln analysiert,
- Raw Evidence ist bitgenau archiviert und verifizierbar,
- Aussagen sind atomar mit Provenienz und Confidence modelliert,
- Ontologie, Assembly-Beziehungen, Konflikte und Knowledge Gaps sind materialisiert,
- die verbleibende Unsicherheit wurde in konkrete Feldaufträge übersetzt.

Das Gate bedeutet ausdrücklich **nicht**:
- maßhaltiges As-Built-Modell,
- geklärte reale Teilinstanzen,
- mechanisch registrierte Punktwolke,
- vollständige Demontage-/Montagefolge,
- fertiger Digital Twin.

## Forschungszustand

Die stärkste Errungenschaft ist nicht ein einzelnes Maß, sondern die Trennung der Wahrheitsschichten:

1. historische Zeichnungs-/Überlieferungsevidenz,
2. beobachteter aktueller Bestand,
3. externe Technik-/Kontextbeschreibung,
4. digitale Scan-Artefakte,
5. explizite Inferenz, Konflikt und Unbekanntes.

Alle 355 Claims sind derzeit bewusst **nicht** als As-Built-Geometrie freigegeben. Das schützt die Rekonstruktion davor, historische Designwerte oder Scan-Bounding-Boxes als aktuelle Maße auszugeben.

## Konstruktives Verständnis

Aktuell gut gestützt:
- hölzerne Welle ohne belegte separate Nabe,
- zwei axial getrennte Arm-/Kranzebenen,
- drei durchgehende Armhölzer mit sechs Speichenenden je Kranz als historisch stark gestütztes Konstruktionsprinzip,
- segmentierte Krümmlinge,
- Kümpfe aus Dauben/Boden/Spannringen,
- umfangsverteilte Schaufeln,
- Keile/Stifte/Metallbefestiger,
- stationäre Radstatt mit Lager, Trog und Rinne.

Noch bewusst offen:
- LAND/WATER-Zuordnung in den aktuellen Ansichten,
- tatsächliche 2026er Varianten der Kumpf-/Ringmaße,
- aktuelle physische Instanzierung und Umfangsfolge,
- verdeckte Mortisen und Passflächen,
- Kranzebenenabstand, Lagerzentren und Feldmaßstab,
- Wasserlinie, Betriebsdrehrichtung und exakte funktionale Pose.

## Scan-Resonanz

PLY und GLB sind technisch valide, aber unvollständige Teilcaptures. Sie sind als forensische Evidenz wertvoll, nicht als Geometrie-Master.

Der gefundene PLY→GLB-Achsenkandidat ist nützlich für spätere Registrierung. Er ist keine mechanische Kalibrierung. Die Scanforensik bestätigt deshalb die ursprüngliche Multi-Evidence-Strategie: Fotos und Zeichnungen tragen Details, die im Scan fehlen; der Scan trägt räumliche Relationen, die Fotos allein nicht liefern.

## Was die GitHub Page jetzt sein sollte

Die erste Page darf **nicht so aussehen, als sei das Rad bereits rekonstruiert**. Sie sollte als interaktives Forschungsfenster funktionieren.

Empfohlene Informationsarchitektur:

1. **Hero / Objekt**
   - atmosphärisches Bestandsfoto,
   - kurze Erklärung des Kleinen Schäferrads und des Zeitfensters vor der Demontage,
   - Statusbadge: `BASELINE UNDERSTANDING READY`.

2. **What we know / What we don't**
   - verständliche Gegenüberstellung gesicherter Topologie und offener As-Built-Geometrie,
   - keine falsche metrische Präzision.

3. **Anatomy**
   - schematische, zunächst nicht maßhaltige Exploded-/Anatomieansicht aus den 22 Ontologiekomponenten,
   - anklickbare Bauteile führen zu Evidenz und Claims.

4. **Evidence Explorer**
   - historische Zeichnungen,
   - aktuelle Bestandsfotos,
   - PLY/GLB-Forensik,
   - pro Quelle Provenienz/Interpretation/Confidence.

5. **Scan Forensics**
   - PLY-/GLB-Orthoprojektionen und räumliche Ansicht,
   - Erklärung der Lücken und des Achsenkandidaten,
   - keine reparierte Fantasiegeometrie.

6. **Conflicts**
   - die 12 Konflikte als sichtbarer Teil des Forschungsprozesses,
   - Variante ≠ Fehler.

7. **Mission: Disassembly**
   - GAP-01…GAP-08 als kompakte Feldmission,
   - zeigt, welche Information beim Zerlegen verloren gehen kann.

8. **Road to Digital Twin**
   - L0 Raw Evidence → L1 Normalisierung → L2 parametrische Mechanik → L3 Surface Reality → L4 Site/Appearance.
   - Three.js als Integrations-/Viewer-Schicht, nicht als Ground Truth.

## Technische Page-Leitplanken

- Page liest möglichst direkt aus `data/*.json` und `evidence/manifest.json`; keine zweite manuell gepflegte Wahrheitskopie.
- Aktuelle `null`-Werte bleiben sichtbar unbekannt.
- historische/erwartete Slots dürfen nicht als aktuelle physische Teile visualisiert werden.
- Confidence und Evidence Class müssen UI-seitig unterscheidbar sein.
- Raw-Dateien werden nicht für die Landing Page ungefiltert geladen; Page nutzt kleine Derivate/Thumbnails.
- Three.js zunächst für Evidence-/Anatomie-Interaktion; kein vorgespiegeltes finales CAD.
- Mobile-first, da Feldnutzung auf iPhone relevant ist.

## Empfohlener nächster Branch

Von diesem akzeptierten Baseline-Zustand:
`work/github-pages-research-view-20261007`

Erste Page-Iteration: statische, sehr hochwertige Research-Landing-Page + datengetriebener Evidence Explorer + Scan-Forensics. Parametrisches 3D erst danach, wenn die Human-Calibration-/Demontage-Evidenz eingespielt ist.
