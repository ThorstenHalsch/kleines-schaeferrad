# Repository- und Evidence-Audit

Ausgangspunkt: `work/pre-disassembly-baseline-20261007`, Commit `806819dc599c640ca6ec9c87e01efc9c322f5892`. Rekursiver Git-Tree nicht abgeschnitten: 13 Textdateien, keine Raw-Binaries oder Contact Sheets, kein AGENTS.md. PR-Liste leer. Aufruf des Git-Mirrors ohne Credential nicht möglich; der Branch wurde danach über zugängliche GitHub-Leseoperationen und öffentliche Git-Daten verifiziert.

## Manifestprüfung und Scope

Alle 33 bisherigen Manifestdateien wurden gegen reale Bytes geprüft: Dateigrößen und SHA-256 stimmen. Das Manifest war dennoch **unvollständig**: zehn zusätzliche JPEGs aus dem rekursiv gelisteten Projektordner fehlten. Aktuell 43 Dateien, Pagination beendet (`next_cursor=null`), davon 40 JPEGs (32 Unterlagen/8 Bestand), PNG, PLY, GLB. Inventar als `evidence/audit/folder-inventory.json`, alte Manifestfassung unverändert als `evidence/audit/prior-manifest-806819d.json` erhalten.

Keine bitgleichen Dubletten unter den 43 Dateien. Inhaltliche Mehrfachaufnahmen: 6816/17, 6818/19, 6824/25, 6828/29, 6833/6845, 6836/37, 6838/6840, 6842/43/44, 6846/47 und 6848/49/50/51/52. 6839 erscheint zusätzlich als Blatt in 6840. 6831 ist eine Neufassung von Montagewissen, kein zweiter unabhängiger aktueller Befund. Fotos 6855/56, 6858/59 und 6860/61 sind ähnliche aktuelle Ansichten, keine kopierten Dateien. PLY/GLB gehören offenbar zum selben Capture (Name/UI/Geometrie), aber sind keine bytegleichen oder gleichorientierten Exporte.

Alle 43 Originalquellen sind individuell analysiert. Lesbarkeitsgrenzen bleiben explizit in `data/source-analyses.json` und `docs/SOURCE-ANALYSIS.md`. Frühere Contact Sheets nicht als Datei gefunden; ihre Analyse wird nicht behauptet. Vier neue Sheets wurden aus allen 40 Originalfotos erzeugt. Der erreichbare Quellenbestand ist vollständig; Zugriff auf einen vollständigen historischen Chattranskript wird **nicht** behauptet. Gesprächskontext wird nach sichtbarem Auftrag und sekundärer Retrieval-Zusammenfassung getrennt geführt.

## Korrigierte Altannahmen

- 6828/29: ausdrücklich beschrifteter Schöpftrog, nicht unbestimmtes Längsteil.
- 6833/6845: industrielle Kontaktstreifen-Vorlage mit Annotationen; Kumpfzuordnung nicht bewiesen.
- 6836/37: Biegematrize, Fertigungshilfe, kein Radkranz.
- 6842/43/44: Brettprofil mit Skalierungsvarianten, keine belegte Wellenzeichnung.
- 12-kantige Hilfsgeometrie ist kein Beleg für zwölf Segmente je Kranz.
- 3 durchgehende Arme erzeugen 6 Speichenenden je Kranz; sechs unabhängige Armhölzer nicht annehmen.
- 24 Kümpfe und 24 Schaufeln sind publizierte Beschreibung; vollständige aktuelle Zählung fehlt.
- Bounding Box bezeichnet das Capture samt Umfeld; „m“ war als Feldkalibrierung nicht belegt.

## Archivierung

Alle 43 Originaldateien werden unverändert als reguläre Git-Blobs unter `evidence/raw/` archiviert. Größe, SHA-256 und Git-Blob-Hash sind geprüft. Die ursprünglich fehlgeschlagenen Einzelwrites funktionierten beim erneuten Versuch; eine Base64-Ersatzarchivierung ist daher nicht erforderlich. Bildderivate liegen separat unter `evidence/derived/`, mit Eltern und Hash im Manifest. Das Abschlussverfahren gleicht den vollständigen Remote-Git-Tree mit dem lokalen Inhalt ab.

## Ergebnis

Inventar, Einzelanalysen, Claims, Ontologie, Konflikte, Referenzkonvention und acht zeitkritische Capture-Aufträge sind materialisiert. Human Calibration betrifft konkrete Interpretationen/zu erfassenden Bestand, nicht unerledigte Sichtung. READY ist ein Verständnis-/Übergabegate, kein Maßhaltigkeits- oder Rekonstruktions-Gate.
