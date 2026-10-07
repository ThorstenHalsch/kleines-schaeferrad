# Pre-Disassembly Field Kit — Abnahme FK-01

Stand: 2026-10-07. Ausgangspunkt: `69b26eb4037c0eacdf0554819bb0e35f0cc36819` auf `work/pre-disassembly-field-kit-20261007`.

Gate: **PRE-DISASSEMBLY FIELD KIT READY**.

Die Abnahme betrifft das vorbereitete digitale und druckbare Aufnahme-Kit. Sie bestätigt keine Ist-Geometrie, mechanische Scan-Registrierung oder Freigabe einer Demontagemethode. Die ausdrücklich in Phase I zugelassenen menschlichen Restprüfungen sind unten aufgeführt.

## Phasen und materialisierte Ergebnisse

| Phase | Ergebnis / Nachweis |
| --- | --- |
| A — Sprache und MUX | Eingefrorene Story erhalten, gemeinsame Navigation und Field-Einstieg ergänzt. Werkstatt mit dichter technischer Oberfläche, deutschen offenen Vergleichen und neutralen Seiten A/B. `src/styles/tokens.css` unverändert. Bei großem Text bricht der Inspektor unter das Modell um. |
| B — Scan | `data/scan-transforms.json`: GLTF Y-up → Z-up durch Rx(+90°), Determinante +1, inverse numerisch geprüft. Permanente Achsentriade. Scan separat vom Modell; RAW_EXPORT, AXIS_NORMALIZED und ausdrücklich ungeprüftes ROUGH_ALIGNED. REGISTERED/CALIBRATED ohne Feldnachweise nicht freigeschaltet. Drei Datum- und zwei Achsmarker vorbereitet. |
| C — Arm/Welle | `data/arm-hypotheses.json` und gemeinsame Modellgeometrie: offen, gerade, gekröpft; drei axiale Varianten. Arm-Innenbereiche ausgelassen, unbekannte Zonen markiert. Keine Mortisen oder unsichtbaren Verbindungen ergänzt. P0++-Aufnahmen mit den Hypothesen verknüpft. |
| D — Feldmodus | `/feld/`: eine Aufgabe mit schrittweiser Foto-/Mess-/Erklärungsaufnahme, Zurück/Weiter, Entwurfswiederaufnahme und sichtbarer Speicherung. Unbekannt verlangt Person und Grund; blockiert statt fälschlich erledigt. |
| E — Bill of Tasks | `data/field-tasks.json`: 21 eindeutige Aufgaben mit allen geforderten Feldern, Quellen, Reihenfolge, Timing und Fertigkriterien. Web und PDF lesen dieselbe Datei. |
| F — Instance Register | `data/instance-register.json`, UI und lokale Ereignisse. Tatsächliches Register bleibt leer; reale IDs nur nach ausdrücklicher Beobachtung/Markierung. Historische Marken, Benennung, Lage, Partner, Zustand, Ausbau und Lagerplatz getrennt erfasst. |
| G — Papiermappe | `output/pdf/KS-Field-Pack-A3.pdf`: 38 Seiten A3 quer, 21 Aufgabenblätter, STOPP-Karten, fünf Arm-/Wellenbilder, zwölf offene Vergleiche, Register und Abschlusscheck. `KS-Einsatzleitung-A4.pdf`: einseitiger Kurzplan. Modellbilder aus derselben Geometrie wie der Viewer, keine nachgezeichnete zweite Logik. |
| H — Offline | Service Worker mit atomarem vollständigem Vorrat, IndexedDB für Originalfotos, Speicherhinweise, verlustfreier Export/Import mit SHA-256. 28 Fotos / 20.460.272 Originalbytes, Offline-Neustart und frischer Offline-Import bestanden. |
| I — Acceptance | Build, Astro check, 8 bestehende und 6 neue Tests; Desktop, 320 px, iPhone-Emulation, 200 % Text; Wiederaufnahme, Originalfotos, Aufgabenabschluss, Teil-/Ereignisaufnahme und Offline-Sicherung geprüft. Details in `state/field-kit/browser/validation.json`. |

## Ausgeführte Prüfungen

- `npm run build`, `npm run check`, `npm run test:workbench`, `npm run test:field`, `python scripts/verify_evidence.py` erfolgreich. Alle 43 Originale und 10 bisherigen Ableitungen unverändert; 355 Aussagen, Teile-/Verbindungsgraph und Konfliktbaseline unverändert.
- Browserabnahme des funktionalen Stands `07f35c66031a870937c1a05dfcf781af69b23048`: [GitHub Actions 37680670509](https://github.com/jdistlr/kleines-schaeferrad/actions/runs/37680670509), erfolgreich. Bestehende Werkstattabnahme [37680678422](https://github.com/jdistlr/kleines-schaeferrad/actions/runs/37680678422) ebenfalls erfolgreich.
- Abschließender Lauf nach einer Beschriftungskorrektur und zusätzlicher Prüfung der vergrößerten Schrift nach Wiederaufnahme: [GitHub Actions 37681272448](https://github.com/jdistlr/kleines-schaeferrad/actions/runs/37681272448) auf `27874181872d51c7055724f5a1d0004e640a2d8d`, erfolgreich. Auch die bestehende Werkstattabnahme [37681280739](https://github.com/jdistlr/kleines-schaeferrad/actions/runs/37681280739) ist erfolgreich.
- Kein horizontaler Seitenüberlauf in den geprüften Profilen; sichtbare Buttons mindestens 44 px. Field-Hauptbuttons mindestens 56 px per Layout. Die Zielgrößenprüfung ist keine vollständige WCAG-Zertifizierung.
- Browserbilder visuell geprüft; ursprünglicher schmaler 200-%-Inspektor korrigiert. Archivierte WebP-Abzüge sind verkleinerte Review-Kopien; unveränderte Original-PNGs liegen im referenzierten CI-Artefakt. Die Textvergrößerung wird auf den geprüften Screens injiziert; es ist kein physischer Safari-Zoomtest.
- PDF: alle 38 Seiten gerendert und visuell geprüft, finale Armblätter/STOPP-Blatt/Vergleiche/A4 nach Korrekturen geprüft; kein Text außerhalb der Seite. Geänderte Armblätter zeigen unbekannte Zonen gestrichelt. `state/field-kit/pdf-validation.json` enthält Formatprüfung und Dateihashes. Aufgaben-/PDF-Parität und Quellhash automatisiert geprüft.
- Belastungstest nutzt ein Original-JPEG wiederholt unter SIMULATION-Namen. Er belegt Byteerhalt und Speicherablauf, keine Vielfalt realer Kameradateien und keinen tatsächlichen Demontageeinsatz. Testinstanzen in den Abnahmen sind als Simulation gekennzeichnet und nicht ins reale Register übernommen.

Der lokale Browserdownload war technisch nicht nutzbar (HTML statt Chromium-Archiv). Browsernachweise stammen deshalb aus den tatsächlich ausgeführten GitHub-Actions-Läufen, nicht aus einer behaupteten lokalen Prüfung.

## Verbleibende menschliche Kalibrierung

1. Physisches aktuelles iPhone/Safari: Vorladen, Flugmodus, Aufnahme, Neustart, Export und Wiederöffnung mit realen Kameradateien.
2. Tatsächliche 60–80-jährige Zielnutzer: Lesbarkeit von Papier und Bildschirm, Aufgabenverständnis, Bedienung bei Tageslicht, Nässe und ggf. Handschuhen.
3. HUMAN-01: Seite A/B, Land/Wasser, Fluss und Drehrichtung gemeinsam bestätigen. Numerische Händigkeit ist geprüft; visuelle mechanische Orientierung ist nicht bestätigt.
4. DATUM-A/B/C und Achsmarker real setzen und messen; erst danach mechanische Transformation und Feldmaßstab bestimmen. `adopted_mechanical_transform`, `field_scale` und `human_side_confirmation` bleiben null.
5. Reale Armform, Endpaarung, axiale Reihenfolge und geöffnete Innengeometrie aufnehmen. Keine Hypothese wurde zu Ist-Geometrie befördert; keine Scannetzlöcher repariert; Gaussian Splats nicht als metrische Evidenz benutzt.

Betrieb, Grenzen und Sicherung: [FIELD-USE.md](FIELD-USE.md). Kein Backend, kein Merge und kein Deploy im Rahmen dieser Session. Arbeit endet am dokumentierten Kit-Gate; weitere Geometriearbeit beginnt erst mit realen Befunden.
