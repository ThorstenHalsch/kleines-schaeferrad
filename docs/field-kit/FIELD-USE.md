# Vor Ort arbeiten — Werkstatt- und Aufnahmeplan V2

Stand: 2026-10-07

Die Anwendung und der Papierplan verwenden weiterhin dieselben 21 kanonischen Arbeitsaufgaben aus `data/field-tasks.json`. Für Menschen werden diese Aufgaben jedoch **nicht mehr als 21 einzelne Formulare oder 21 einzelne Blätter präsentiert**.

Stattdessen führen acht gemeinsame technische Skizzen durch die Baugruppen. Messlinien, Fotostandpunkte, Datumspunkte und Scan-Aufträge stammen aus `data/visual-guides.json` und werden sowohl im Feldmodus als auch im A3-Plan verwendet.

## Die drei Arbeitsmittel

### A3 Werkstatt- und Aufnahmeplan

`KS-Werkstatt-Aufnahmeplan-A3.pdf`

12 Blätter:
- Ablauf / rote Linie
- 8 visuelle Baugruppenblätter
- Teile-/Ereignis-/Lagerregister
- alte Angaben und offene Varianten
- Abschlusskontrolle

Primär zum gemeinsamen Zeigen, Einzeichnen und handschriftlichen Arbeiten.

### Vor-Ort-Modus

`/feld/`

Zeigt:
1. aktuelle Arbeitsphase,
2. Baugruppenskizze,
3. hervorgehobene Foto- oder Messposition,
4. genau den nächsten Handgriff,
5. erst danach die dafür nötige Eingabe.

Interne TASK-/COMP-/CLAIM-IDs bleiben im gespeicherten Datensatz, aber nicht in der normalen Arbeitsführung.

### Werkstattmodell

`/werkstatt/`

Zum Vergleichen von:
- Radkörper,
- stationärem Tragwerk,
- offenen Stellen,
- Quellenbildern,
- Arm-/Wellenvarianten,
- Punktewolke.

Technische Varianten und Scanparameter sind bewusst eingeklappt. Der Werkstattmodus ist kein Ersatz für den Vor-Ort-Ablauf.

## Vor dem Einsatz

1. Auf dem tatsächlichen Gerät online `/feld/` öffnen und **Offline bereit** abwarten.
2. Flugmodus einschalten, Seite neu laden und eine ausdrücklich als TEST bezeichnete Aufnahme durchführen.
3. TEST-Sicherung exportieren und auf einem zweiten Gerät wieder einlesen.
4. A3-Plan bei 100 % drucken und die 50-mm-Kontrolllinie prüfen.
5. A4-Kurzplan `KS-Kurzplan-A4.pdf` und Stifte mitnehmen.
6. Erfahrene Monteure bestimmen Reihenfolge und Freigaben. Ein digitaler Status ersetzt keine Demontagefreigabe.

## Vor Ort

Die rote Linie bleibt immer:

**orientieren → aufnehmen → erst dann lösen → Partner zuordnen → sichern**

### Fotos

Die Skizze zeigt F01, F02 usw. als gewünschte Blickrichtungen.

- Übersicht und Detail zusammen aufnehmen.
- Kontaktpartner möglichst gemeinsam im Bild.
- Vor und nach dem Öffnen dieselbe Verbindung dokumentieren.
- Maßstab/Referenz ins Bild, wenn Geometrie erfasst wird.
- Rohbilder unverändert erhalten.

### Maße

Die Skizze zeigt M01, M02 usw.

Jeder Messwert braucht:
- Endpunkt A,
- Endpunkt B,
- Einheit,
- Werkzeug,
- geschätzte Unsicherheit,
- Foto der Messstrecke.

Zusätzliche Messungen dürfen auf Papier ergänzt und fotografisch gesichert werden.

### Scans

D-/S-Markierungen kennzeichnen Datum- und Scanbezüge.

- DATUM-A/B/C müssen am verbleibenden Tragwerk gesetzt werden.
- Marker in neuen LiDAR-/Photogrammetrie-Aufnahmen sichtbar halten.
- Gaussian Splats sind Oberfläche/Kontext, keine metrische Referenz.
- Die bestehende Punktewolke ist achsenbezogen dargestellt, aber weiterhin nicht mechanisch registriert.

### Reale Teile

Eine KS-ARM/KRU/KUM/PAD/KEI-ID erst vergeben, wenn ein reales Teil gesehen und beschriftet wurde.

Erhalten:
- alte Marke,
- lokaler Name,
- ursprüngliche Lage,
- Partner,
- Zustand,
- Ausbauereignis,
- Lagerplatz,
- Foto.

## Sicherung

Originale JPEG/PNG/WebP werden ohne Neucodierung als Blobs in IndexedDB gespeichert. Der Export enthält Originalbytes und SHA-256-Prüfsummen.

Getestete Simulation:
- 28 Fotos,
- rund 20 MB Originalbytes,
- Offline-Neustart,
- Export/Import in frischem Browserkontext.

Das ist **kein Ersatz für den physischen iPhone-Test**.

Browserdaten können durch Speicherknappheit, Privatmodus, gelöschte Websitedaten oder Geräteverlust verschwinden. Nach wichtigen Abschnitten exportieren und die Sicherung auf einem zweiten Medium wirklich öffnen.

## Noch offen vor FIELD-VALIDATED

- physisches aktuelles iPhone/Safari,
- reale Kameradateien,
- Tageslicht / nasse Hände / ggf. Handschuhe,
- 60–80-jährige Zielnutzer,
- Seite A/B → Land/Wasser,
- Fließ- und Drehrichtung,
- DATUM-A/B/C + AXIS-A/B,
- reale Rahmen-/Lagermaße,
- Armendpaarung, Kröpfung, axiale Reihenfolge und Welleninnengeometrie.

Weitere benötigte Aufnahmen: `docs/PHOTO-CAPTURE-TODO.md`.
