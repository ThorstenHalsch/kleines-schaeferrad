# Evidenz und Reproduktion

## Bindung an den Stand

- PR #10 initial: `1ba182061038c6bf28468b26c8a2ba39d04b14b8`.
- Produktionsbasis/main: `1de62e702e6a1f0b818ab4a6ad0d27c111ac720a`.
- Browsermatrix-Skript: Commit `65fa679e4c32ce3fcb783a0bdf0146c15c2d5ca1`.
- Folgeprüfung: Commit `3b5e94b0086eeda74e7bc7e78e366c78bc6cb7db`.
- `evidence/deployment.json`: main-Deployment, Manifest/Cache-ID.
- `evidence/deployed-files.json`: 126 exakt heruntergeladene Dateien mit SHA-256 und Bytezahl. Der Download ist eine Kopie, kein neuer Site-Build.
- `evidence/ci-provenance.json`: Run-/Artifact-IDs und ZIP-Hashes. Die extrahierten Nachweise sind hier im Git gespeichert; die 14-Tage-Retention der Actions-Artefakte ist daher nicht die alleinige Sicherung.
- `evidence/manifest.json`: Hashes sämtlicher auditierter Evidenzdateien (ohne das Manifest selbst).

## Browser-Nachweise

[Matrixbericht](evidence/ci/report.json) und [Folgebericht](evidence/followup/followup.json) enthalten Befunde, Fehler und den begrenzten Prüfkontext. Der blockierte Wasser-Direkteinstieg bleibt als negative Beobachtung erhalten. `executed:true` bedeutet beobachtet, nicht fehlerfrei.

| Übersicht | Beleg |
|---|---|
| Start, 1440/768/390/320 | [Kontaktbogen](evidence/screen-overviews/story-1.jpg) |
| Werkstatt, 1440/768/390/320 | [Kontaktbogen](evidence/screen-overviews/werkstatt-1.jpg) |
| Feld, 1440/768/390/320 | [Kontaktbogen](evidence/screen-overviews/feld-1.jpg) |
| Start, Text 200/reduced/dark | [Kontaktbogen](evidence/screen-overviews/story-2.jpg) |
| Werkstatt, Text 200/reduced/dark | [Kontaktbogen](evidence/screen-overviews/werkstatt-2.jpg) |
| Feld, Text 200/reduced/dark | [Kontaktbogen](evidence/screen-overviews/feld-2.jpg) |

Kontaktbögen sind beschriftete Ausschnitte der ersten Viewporthöhe, keine simulierten mobilen Webseiten. Die unveränderten vollständigen PNG-Screenshots und zugehörigen sichtbaren Texte liegen in `evidence/ci/`. Journey-Screenshots ebenfalls dort; gezielte mobile/Formular-/Wasser-/Bewegungsnachweise in `evidence/followup/`. Die Cloud-Browser-JPEGs zeigen einen unabhängigen Live-Durchgang mit nicht verfügbarem WebGL. Die `.ax.txt` dazu sind teilweise Differenz-Snapshots, kein vollständiger DOM-Export.

## Druck-Nachweise

Die beiden heruntergeladenen PDFs liegen unverändert in `evidence/print-live/`, neben allen 26 Farb-/Graustufen-PNGs und acht Kontaktbögen. Herkunft/Hash stehen in `deployed-files.json`. Vergleich zur eingefrorenen Repository-Fassung: [print-comparison.json](evidence/print-comparison.json). A4 pixelgleich trotz anderer PDF-Bytes; A3 Seiten 3/5/6/7/9 verschieden. Ursachen: Generatoränderung aus PR #9 (Aufhellung synthetischer Bilder und Beschriftungsgröße). Die Produktions-PDF-Dateien wurden durch diesen Audit **nicht** neu geschrieben.

- [A3 Graustufen 1–4](evidence/print-live/a3-gray-overview-1.jpg)
- [A3 Graustufen 5–8](evidence/print-live/a3-gray-overview-2.jpg)
- [A3 Graustufen 9–11](evidence/print-live/a3-gray-overview-3.jpg)
- [A4 Graustufen 1–2](evidence/print-live/a4-gray-overview-1.jpg)

## Wiederholbarkeit

Die Audit-Skripte benötigen Node 24 und isoliert Playwright 1.56.1 mit Chromium. Sie richten frische Kontexte ein und arbeiten nur mit synthetischen Einträgen; eine vorhandene Nutzersitzung wird nicht geöffnet. Sie rufen die öffentliche Pages-Seite auf und benötigen keinen Site-Build. `UX_PLAYWRIGHT` ist der absolute Pfad zu `playwright/index.mjs`; `UX_OUTPUT` das Ergebnisverzeichnis.

```sh
UX_PLAYWRIGHT=/absolute/path/to/playwright/index.mjs UX_OUTPUT=test-results/ux-recovery node tests/ux-recovery/browser-audit.mjs
UX_PLAYWRIGHT=/absolute/path/to/playwright/index.mjs UX_OUTPUT=test-results/ux-followup node tests/ux-recovery/followup.mjs
```

Der versionierte Audit-Workflow wurde beim ersten Testcommit für die Matrix, beim zweiten ausschließlich für die gezielte Folgeprüfung verwendet. Die jeweiligen Workflowfassungen sind über die Commits reproduzierbar; die aktuelle Workflowfassung wiederholt nur die Folgeprüfung. Keine Deployment-Berechtigungen (`contents: read`), kein Merge und kein Modell-/PDF-Generator in diesem Audit-Job.

Die vorhandenen PR-Workflows liefen daneben automatisch; deren bereits bestehende Build-/Testlogik wurde nicht verändert. Der initiale Field-workbench-Fehler ist als knapper Auszug in `evidence/existing-ci-failure.txt` dokumentiert; Ursache jenseits des beobachteten Timeouts nicht behauptet.

PDF-Proofs reproduzieren: heruntergeladenes PDF mit PyMuPDF bei Faktor 1,5 rendern, Graustufen per Pillow; `state/ux-recovery/20261009/print-proof.py`. Bildschirmproofs sind nicht als Papier-/Tageslichtprobe zu interpretieren. Dateien in `output/calibration/ITER-001`, Modellquellen, Mess-/Autoritätsdaten, Produktion unter `src/` und `public/` bleiben unverändert.
