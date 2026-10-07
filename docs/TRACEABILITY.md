# Traceability und Confidence

Alle atomaren Aussagen: `data/geometry.claims.json`. Jede hat stabile ID, Subjekt, Prädikat, Wert, Einheit, Evidenzklasse, Confidence, Scope und Quellenregion. Confidence bewertet die Lesbarkeit/Beobachtung der Aussage, nicht automatisch die Gültigkeit am Objekt 2026.

| Klasse | Bedeutung und Grenze |
|---|---|
| measured | Direkte Messung mit Methode. Bisher nur digitale Dateistatistik; **keine** kalibrierte Feldmessung. |
| observed-current | Auf aktuellem Foto/Scan sichtbar. Sichtbare Topologie, keine Perspektivmaße. |
| historical-drawing | Zeichnungs-/Notizinhalt; Varianten und Einheiten separat führen. |
| external-context | Benutzerkontext, überlieferte Zusammenfassung oder öffentliche Beschreibung; Herkunft unterscheiden. |
| inferred | Ableitung mit nachvollziehbarer Methode; nicht automatisch Ist-Geometrie. |
| conflicting | Dokumentierter Vergleich; hohe Confidence kann den Konflikt bezeichnen, nicht seine Lösung. |
| unknown | Kein belastbarer Wert; `null`, keine Nullgeometrie. |

`high/medium/low/unknown` sind qualitative Confidence-Werte ohne erfundene Wahrscheinlichkeiten. Alle aktuellen Claims haben `as_built_eligible=false`: Für maßhaltige Modellparameter fehlen Feldkalibrierung und eindeutige Teilezuordnung. Eine lesbare Zeichnungszahl allein reicht nie. Kein Mittelwert konkurrierender Varianten.

Originalfoto ≠ fotografiertes Blatt: Die IDs PHOTO-* bezeichnen Dateien. DOC-* Gruppen verhindern Mehrfachzählung derselben Zeichnung. Ein umgeschriebenes Blatt bleibt mit seiner Überlieferung verbunden. PLY/GLB sind zwei Exportfassungen desselben Captures, keine unabhängigen Messungen. Contact Sheets und Projektionen sind reine Derivate.

Assembly: Familien/Regionen, historische Positionen und extern erwartete Slots sind getrennt. EXPECTED-/HIST-IDs sind **keine** bereits identifizierten realen Teile. Neue KS-IDs erst vor Ort vergeben; alte Markierungen erhalten. Jede Kante hat Evidenz/Confidence und Status. Verdeckte Verbindungen bleiben offen.

Lineare Zahlen ohne explizite Einheit behalten `unit=null`. „426/396“ wird als Zeichnungsannotation geführt; plausible cm→m-Interpretation darf nicht als Messwert erscheinen. Die Holzmaß-Tabelle beschreibt Beschaffung und Empfehlungen, keine aktuelle Geometrie. Digitale Bounding Boxes verwenden Exportkoordinaten, nicht einen verifizierten metrischen Feldmaßstab.

Rohbytes bleiben unverändert unter `evidence/raw/`. SHA-256, Git-Blob-Hash und Dateigröße werden mit `python scripts/verify_evidence.py` geprüft. Jeder Derivat-Eintrag nennt Eltern und Hash. Frühere Manifestfassung bleibt als Auditbeleg erhalten.
