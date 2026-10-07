# Vor Ort arbeiten — FK-01

Die Papiermappe und `/feld/` verwenden dieselben 21 Aufgaben aus `data/field-tasks.json`. Die Werkstatt ist zum Vergleichen da, der Feldmodus zum schrittweisen Aufnehmen. Alle neuen Angaben bleiben ungeprüfte Feldangaben; sie ändern keine Ist-Geometrie.

## Vor dem Einsatz

1. Auf dem tatsächlichen Gerät online `/feld/` öffnen und **Offline bereit** abwarten. Der Vorrat umfasst Seiten, Originalquellen, Scan, Schriften und PDFs (rund 39 MB).
2. Flugmodus einschalten, die Seite neu laden und eine ausdrücklich als TEST bezeichnete Aufnahme sichern, exportieren und auf einem zweiten Gerät wieder öffnen.
3. A3-Mappe quer bei 100 % drucken. Die 50-mm-Linie am Blattfuß nachmessen. A4-Kurzplan und Stifte mitnehmen.
4. Erfahrene Monteure bestimmen Ablauf und Freigaben. Eine erledigte Aufgabe ersetzt keine Freigabe zur Demontage.

## Aufnahme

Auftrag lesen, Person/Kürzel angeben, jede angeforderte Fotoansicht zuordnen, Maße mit Endpunkten, Werkzeug und Unsicherheit eintragen. Zusätzliche Messreihen und Skizzen als lesbare Fotos/Papierbelege mit Aufgaben-ID sichern; das Zahlenformular hält eine Messung je Aufgabe. Wörtliche Erklärung und eigene Deutung sind getrennte Felder. Externe Audio-/Videodateien erhalten einen Dateiverweis und müssen separat gesichert werden.

**Weiß ich nicht / noch nicht zugänglich** verlangt eine Begründung und kennzeichnet die Aufgabe als blockiert. Es ergänzt keinen Befund und hebt keinen STOPP auf. „Aufgenommen“ bedeutet lediglich: die angegebenen Nachweise wurden lokal erfasst und die erfassende Person hat das Fertigkriterium bestätigt. Eine fachliche Prüfung steht weiter aus.

Eine KS-ARM/KRU/KUM/PAD/KEI-ID erst vergeben, wenn das reale Teil gesehen und beschriftet wurde. Historische Marken unverändert abschreiben; Lage, Partner, Zustand, Person, Ausbauereignis und Lagerplatz zuordnen. Es gibt keine vorab erfundenen physischen Instanzen. Modellpositionen und erwartete Stückzahlen sind keine Inventarliste.

## Sicherung und Grenzen

Originale JPEG/PNG/WebP-Fotos werden ohne Neucodierung als Blobs in IndexedDB gespeichert. Der JSON-Export enthält die Originalbytes und SHA-256-Prüfsummen; Import prüft sie vor dem Speichern. Abweichende Einträge unter derselben ID werden nicht still überschrieben. Im Zweifelsfall Sicherungen getrennt halten und fachlich abgleichen.

Der getestete Belastungslauf enthält 28 Bilder und 20.460.272 Originalbytes. Er verwendet ein vorhandenes Originalfoto mehrfach mit SIMULATION-Dateinamen und ist ausdrücklich kein realer Feldversuch. App-Grenzen: 25 MB je Foto, 250 MB Medien je Sitzung, 350 MB je Importdatei. Base64 vergrößert den Export; beim Export/Import benötigt der Browser zusätzlich Arbeitsspeicher. Diese Grenzen sind keine garantierte Geräteleistung.

Browser dürfen lokale Daten bei Speicherknappheit, privatem Modus, gelöschten Websitedaten oder Geräteverlust verlieren. Die Speicheranzeige und eine Persistenzanfrage verhindern das nicht sicher. Nach jedem wichtigen Abschnitt exportieren, auf ein zweites Medium kopieren und die Sicherung öffnen. Offline-Vorrat und persönliche Feldaufnahmen sind getrennte Speicher. Ein vollständiger neuer Vorrat ersetzt alte App-Caches; persönliche Aufnahmen werden dabei nicht gelöscht. Es gibt keinen Server und keine automatische Cloud-Sicherung.

## Vor-Ort-Kalibrierung bleibt offen

- HUMAN-01: Seite A/B mit Land/Wasser, Fluss-/Drehrichtung und Fotos bestätigen.
- DATUM-A/B/C am verbleibenden Tragwerk, nicht kollinear; Fotos, drei Verbindungsstrecken, Höhenbezug und Unsicherheiten aufnehmen. Achsmarker A/B festlegen.
- Scan gegen diese Referenzen ausrichten und unabhängig skalieren. `AXIS_NORMALIZED` korrigiert nur Exportachsen; es ist keine mechanische Registrierung. `adopted_mechanical_transform` und `field_scale` bleiben null.
- Armendpaare, Kröpfung, axiale Reihenfolge und erst nach realer Öffnung sichtbare Verbindungen dokumentieren. Verdeckte Topologie bleibt unbekannt.
- Aktuelles physisches iPhone/Safari, Menschen der Zielgruppe sowie Tageslicht-/Nässe-/Handschuhbedienung vor dem realen Einsatz prüfen. Emulation ersetzt diese Abnahme nicht.
