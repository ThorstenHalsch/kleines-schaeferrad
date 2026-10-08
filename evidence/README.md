# Evidence Store

43 Originaldateien, byteverifiziert, vollständig individuell geprüft. Das Manifest trennt Rohdateien, Derivate, Kontext und zukünftige Quellen. Alte Manifestfassung bleibt als Auditbeleg erhalten.

Originalbytes sind unverändert in `raw/` archiviert. Nach Checkout: `python scripts/verify_evidence.py`. Die 40 JPEGs, PNG, PLY und GLB werden gegen Größe, SHA-256 und Git-Blob-Hash geprüft. Rohdaten nicht überschreiben.

`derived/`: Contact Sheets und Scanstatistiken/-ansichten. Bildderivate haben ergänzende Base64-Archive zur Wiederherstellung; sie sind keine unabhängige Evidenz. `context/`: begrenzter Gesprächs- und externer Kontext. `audit/`: Ausgangsmanifest und vollständige Quellinventarliste.

## Fachbeiträge

- 2026-10-08: [Aufbau eines Kumpfes — Fachauskunft von ThorstenHalsch](../docs/FACHBEITRAG-KUMPF-20261008.md), mit vier unveränderten Originalfotos. [Ergänzendes Quellenmanifest und atomare Fachangaben](contributions/kumpf-20261008.json).

Fachbeiträge sind ergänzende Quellen für den späteren Abgleich. Das ursprüngliche 43-Dateien-Manifest bleibt als historische Baseline erhalten; der bestehende Prüflauf prüft diese neuen Beiträge noch nicht.
