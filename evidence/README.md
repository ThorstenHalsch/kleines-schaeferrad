# Evidence Store

Dieses Verzeichnis ist die Referenz für **alle** Projektquellen, nicht nur 3D-Scans.

## Aktuell erfasst

- 30 JPEG-Feldaufnahmen (`IMG_6816.jpeg` … `IMG_6861.jpeg`, mit Lücken in der Kameranummerierung),
- 1 Screenshot der Scaniverse-Exportoptionen (`IMG_6863.png`),
- 1 Scaniverse-Punktewolke (PLY),
- 1 Scaniverse-Mesh (GLB),
- Projektkontext aus dem Feldgespräch.

Die Dateien werden in `manifest.json` mit SHA-256 registriert.

## Wichtiger technischer Status

Die Roh-Binärdateien liegen derzeit im ChatGPT-Projekt/Evidence-Ingest vor und sind dort bitgenau gehasht. Der GitHub-Connector kann Textdateien direkt schreiben, überträgt aber diese lokalen Binärdateien nicht automatisch aus dem Projekt-Dateispeicher in Git.

Darum gilt:
- **Manifest + Provenienz sind bereits Repository-Baseline.**
- Die Raw-Binaries müssen anschließend bitgenau in `evidence/raw/` übernommen werden (vorzugsweise Git LFS).
- Kein Asset gilt als vollständig archiviert, bevor Repository-Datei und SHA-256 gegen das Manifest geprüft wurden.

Die Baseline darf diesen Unterschied nicht verschleiern.
