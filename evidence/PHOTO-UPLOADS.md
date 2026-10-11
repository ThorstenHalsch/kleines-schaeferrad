# Weitere Bilder ins Projekt aufnehmen

Neue Fotos vor dem ersten Commit verkleinern. Ein späterer Lösch- oder Ersetzungscommit entfernt die große Fassung nicht aus früheren Git-Commits. Die Kameraoriginale können außerhalb des Repositorys auf dem eigenen Rechner aufbewahrt werden.

Für normale Referenzbilder: JPEG, maximal 1600 Pixel an der langen Seite, Qualität 80. Für Zeichnungen, Zollstockablesungen oder feine Anschlüsse kann bewusst eine größere Auflösung nötig sein; dann einen scharfen Detailausschnitt oder eine größere Datei verwenden und die Wahl dokumentieren.

```bash
python -m pip install Pillow
python scripts/prepare-evidence-photos.py --component Welle /pfad/zu/neuen/Fotos/*.jpg
```

Das Skript schreibt kleine JPEGs nach `evidence/raw/<Komponente>/`, verweigert das Überschreiben vorhandener Quellen und lässt die Eingabedateien unverändert. Es erzeugt keine zusätzliche Originalkopie im Repository. EXIF-Ausrichtung wird angewendet; EXIF-Metadaten werden nicht in die Referenzkopie übernommen. Danach nur die vorbereiteten Dateien committen. Im Chat Dateiname und sichtbare Eigenschaften nennen.

Die elf Wellenbilder vom 10. Oktober 2026 sind auf ausdrücklichen Nutzerwunsch nun ausschließlich als verkleinerte Fassungen archiviert. Größe, Auflösung und Prüfsummen der entfernten Ausgangsdateien bleiben als Herkunftsmetadaten in `evidence/derived/welle-compression.json` erhalten. Die älteren 132 Rohquellen wurden nicht verändert.

## Nach der History-Bereinigung

Bestehende Klone besitzen möglicherweise weiterhin die alten Objekte. Am einfachsten einen frischen Klon anlegen; zuvor uncommittete Arbeiten sichern. Alte Branches mit den großen Fotos nicht erneut pushen oder in die bereinigten Branches mergen. GitHub kann verwaiste Objekte und alte PR-Ansichten intern weiter vorhalten; ein frischer normaler Klon lädt diese nicht herunter.
