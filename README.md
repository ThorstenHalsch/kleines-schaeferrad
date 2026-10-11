# Kleines Schäferrad — evidenzbasierte Rekonstruktion

**BASELINE UNDERSTANDING READY** — Verständnis-/Capture-Human-Gate, keine fertige oder maßhaltige Rekonstruktion.

43 Originaldateien individuell geprüft; Zeichnungen, aktueller Bestand, Kontext und 3D-Exporte sind gleichberechtigte Evidenz mit sichtbaren Konflikten.

Start: [Baseline](docs/BASELINE.md), [Audit](docs/EVIDENCE-AUDIT.md), [Einzelanalysen](docs/SOURCE-ANALYSIS.md), [Conflict Matrix](docs/CONFLICT-MATRIX.md), [Human Calibration](docs/HUMAN-CALIBRATION.md), [Capture-Plan](docs/CAPTURE-BEFORE-DISASSEMBLY.md), [Fortsetzung](state/NEXT-WORK-SESSION.md).

Originale nach Checkout prüfen: `python scripts/verify_evidence.py`. Keine externe Python-Abhängigkeit dafür. Für die Scanforensik: NumPy, Matplotlib, Pillow und `python scripts/audit_scans.py`. Alle Claims und alle Modellannahmen sind maschinenlesbar unter `data/`.

## Originalquellen

Fotos, fotografierte Zeichnungen und Scans liegen unter [`evidence/raw/`](evidence/raw/README.md), nach Komponenten sortiert. Die Verzeichnisse je Bauteil enthalten direkte Bildlinks und Querverweise. Historische Pfade sind in [`evidence/component-index.json`](evidence/component-index.json) auf die aktuelle Ablage abgebildet.
