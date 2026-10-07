# Baseline Understanding & Evidence Reconstruction

Stand: 2026-10-07. Ausgangscommit: `806819dc599c640ca6ec9c87e01efc9c322f5892`. Human Gate: **BASELINE UNDERSTANDING READY**, wirksam nach verifiziertem Repository-Writeback. Offene Feldinterpretationen stehen in `HUMAN-CALIBRATION.md`.

## Was verstanden ist

Das Kleine Schäferrad ist ein System aus hölzerner Welle, zwei räumlich getrennten Arm-/Kranzebenen, segmentierten Krümmlingen, Daubengefäßen mit Spannringen, umfangsverteilten Schaufeln, vielfältigen Keilen/Stiften/Metallbefestigern und stationärer Radstatt mit Lager-/Trog-/Rinnenbezügen. Die Armzonen sind Regionen der Welle; separate Naben sind nicht belegt. Historische Montagebilder und publizierte Technikbeschreibung unterscheiden **drei durchgehende Arme von sechs Speichenenden je Kranz**. Die mittigen Endkennzeichen 1/4 werden historisch zuerst eingesetzt. Landkrümmlinge sind im Blatt als mit Kumpflöchern, Wasserkrümmlinge ohne diese bezeichnet. Aktuelle Fotos bestätigen zwei Kranzebenen, Arm-/Wellenkontakte, Holzkeile, Kranzstöße, Kumpfdauben/Spannringe und Trog-/Gerüstkontext. Verdeckte Passflächen sind unbestimmt.

## Quellen und Autorität

43 Originaldateien vollständig inventarisiert und individuell analysiert: 32 Unterlagenfotos, 8 Bestandsfotos, Screenshot, PLY und GLB. Das bisherige 33er Manifest war bytekorrekt, aber unvollständig. **355 atomare Claims**, 22 Ontologieeinträge, 17 Graphbeziehungen und 12 Konfliktfälle sind strukturiert. Nicht jeder Claim ist geometrisch: dokumentierte Maße, Materialien, Stückzahlen, Katalogkorrekturen und digitale Dateimessungen bleiben unterscheidbar.

Einheitenlose Zeichnungszahlen behalten ihre Form. Ø426/396 und R213/198 stützen eine Designinterpretation um 4,26/3,96 m, aber keine aktuelle Maßfreigabe. Holzmaßtabellen sind Beschaffungsempfehlungen. Zeichnungsvarianten (z.B. Dauben 22/24 mm und Ringlängen) werden parallel gehalten. Die lokale Reparaturgeschichte ist unbekannt. Kein aktueller Claim ist als maßhaltige Ist-Geometrie freigegeben.

Der Verein beschreibt 24 Kümpfe, 24 Schaufeln und sechs Krümmlinge je Kranz. Diese Zahlen werden als **extern erwartete Slots** modelliert, nicht als aus den Fotos gezählte Ist-Instanzen. Reale IDs und Umfangsfolge entstehen beim Capture. [Vereins-Technikbeschreibung](https://www.verein-zufriedenheit.com/info.html). Ort/Patenschaft: Möhrendorf/Oberndorf aus Repository/öffentlichem Kontext; alte Angaben Radnummer/Fluss-km sind ungeprüft.

## Scans

PLY: 75.619 Farbpunkte, 1.214 wiederholte Positionen. GLB: 56.117 Vertices, 78.043 Dreiecke, 30.775 offene Randkanten. Capture enthält Rad, Gerüst und Ufervegetation mit großen Lücken. Exportachsen unterscheiden sich; (Xp,Zp,−Yp) → GLB ist numerisch gut gestützter Kandidat. Keine mechanische Registrierung und kein verifizierter Feldmaßstab. Die Scans sind forensische Teilquellen und keine vollständige Rekonstruktion.

## Konflikte und nächste reale Evidenz

Die Conflict Matrix unterscheidet echte Zeichnungsvarianten, unklare Bezugsdimensionen, mögliche Reparaturzustände, verdeckte Fotobereiche und Capture-Defizite. Fehlende Scangeometrie beweist kein fehlendes Bauteil. Die bisherigen Unterlagen reichen nicht zur Entscheidung aller historischen/current Varianten. Kein Konflikt wird durch Mittelung oder Quellenrangfolge gelöscht.

Acht priorisierte Demontageaufträge retten: (1) globale Pose/Datum/Ringabstand, (2) Mortisen/Keile/Armfolge, (3) Krümmlingstöße, (4) Kumpfkontakte/Varianten, (5) reale Umfangsfolge und Kumpf-/Schaufelphase, (6) Lager-/Zapfenlage, (7) Wasser-/Trog-/Rinnenlage, (8) Demontageereignisse/Teilidentität. Konkrete Aufnahmen, Maße und Fertigkriterien stehen in `CAPTURE-BEFORE-DISASSEMBLY.md`.

## Einstieg und Stop-Grenze

- `EVIDENCE-AUDIT.md`, `SOURCE-CATALOG.md`, `SOURCE-ANALYSIS.md`: Audit und Einzelbefunde.
- `TRACEABILITY.md`, `data/geometry.claims.json`: atomare Evidenz.
- `data/components.json`, `data/assembly.graph.json`: Bauteile und Beziehungen.
- `CONFLICT-MATRIX.md`, `data/conflicts.json`: konkurrierende Aussagen.
- `REFERENCE-SYSTEM.md`, `data/reference-system.json`: mechanische Konvention ohne erfundene Maße.
- `data/knowledge-gaps.json`, `HUMAN-CALIBRATION.md`: gezielte Feldarbeit.

Noch kein finaler Viewer, Modell, repariertes Mesh, Hole Filling, Texturfinish oder Gaussian-Splat-Integration. Das Human Gate bedeutet: Quellen verstanden und Unsicherheit in ausführbare Capture-/Kalibrieraufträge überführt. Es bedeutet nicht, dass alle aktuellen Maße bekannt sind.
