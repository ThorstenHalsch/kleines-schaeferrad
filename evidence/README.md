# Evidence Store

43 Originaldateien, byteverifiziert, vollständig individuell geprüft. Das Manifest trennt Rohdateien, Derivate, Kontext und zukünftige Quellen. Alte Manifestfassung bleibt als Auditbeleg erhalten.

Originalbytes sind unverändert in `raw/` archiviert. Nach Checkout: `python scripts/verify_evidence.py`. Die 40 JPEGs, PNG, PLY und GLB werden gegen Größe, SHA-256 und Git-Blob-Hash geprüft. Rohdaten nicht überschreiben.

`derived/`: Contact Sheets und Scanstatistiken/-ansichten. Bildderivate haben ergänzende Base64-Archive zur Wiederherstellung; sie sind keine unabhängige Evidenz. `context/`: begrenzter Gesprächs- und externer Kontext. `audit/`: Ausgangsmanifest und vollständige Quellinventarliste.
