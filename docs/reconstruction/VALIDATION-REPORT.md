# BRUTE-FORCE FUNCTIONAL RECONSTRUCTION READY

Stand: 08.10.2026. Gate für eine ungemessene, quellenbezogene Rekonstruktion und den Aufnahmebetrieb vor der Demontage.

Geprüfter Implementierungscommit: `96132aec62fdb8c4f391b60ce483c3867fe1fc94`.
Zielbranch: `work/bruteforce-functional-reconstruction-v2-20261008`.
Der abschließende Gate-Commit ergänzt diesen Stand ausschließlich um Prüfnachweise, Freigabestatus und Dokumentation.

## Ergebnis und Geltungsbereich

**TECHNICAL DRAWING QUALITY PASS** und **HUMAN UX QUALITY PASS**.

Das System enthält 279 benannte Modellobjekte, getrennte rotierende und stationäre Baugruppen, Welle mit Zapfenkandidaten, sechs gepaarte Armprofile, zwei segmentierte Kränze, Daubenkümpfe mit Böden und Reifen, Lang-/Kurzstifte, Schaufeln, Lager, Radstatt, Laufbohlen, Trog, Rinne und Rinnenstützen. Die Betriebsansicht ergänzt Wasser, angenommenes Ufer, Fließrichtung, Rotation, Wasseraufnahme und Wasserübergabe.

Das Gate bestätigt den dokumentierten Rekonstruktions- und Softwarestand. Aktuelle Ist-Maße, verborgene Verbindungen, Tragfähigkeit und die tatsächliche Demontagefolge sind nicht damit bestätigt. Die Formen sind technische Kandidaten; 24 Kumpfpositionen sind eine dokumentierte Erwartung, keine vor Ort abgeschlossene Zählung. Auch zwölf Dauben im Formkandidaten sind kein heutiger Zählnachweis.

## Phasenabnahme

| Phase | Materialisiertes Ergebnis | Prüfung |
| --- | --- | --- |
| A — Quellen | `data/reconstruction-evidence-map.json`: zehn mechanische Baugruppen mit Beobachtung, Historie, Foto-/Scanbedingungen, Konflikten, Kandidaten, Vertrauen und Feldfragen | 30 neue Anhänge bytegleich dem vorhandenen Archiv zugeordnet; 43 Baseline-Originale, zehn Ableitungen, 355 Claims und Referenzen validiert; 19 zusätzliche Originaldateien im Ergänzungsmanifest |
| B — Konstruktion | `data/external-construction-research-v2.json`, `SOURCE-RECONCILIATION.md` | Betreiberquelle, regionale Konstruktion/Montage, historischer Saisonbericht, musealer und kommunaler Kontext; Evidenz und Analogie getrennt |
| C — Koordinaten | `mechanics.mjs`, `scan-transforms.json`, eigener Scan-Arbeitsplatz | Ursprung Wellenachse/Kranzmittelebene; X Welle, Z oben; Seitenzuordnung offen; PLY/GLB getrennt; Solver prüft drei Referenzen, Achsrichtung/-lage und unabhängige Kontrollstrecke |
| D — Geometrie | `geometry.mjs`, `output/model/KS-Rekonstruktion-V2.glb`, `component-index.json` | Alle Hauptbaugruppen vorhanden; beide Enden aller sechs Arme erreichen ihre jeweilige Kranzebene; keine künstlichen realen Instanzen angelegt |
| E — Funktion | Betriebsansicht und `vesselState` | Positive X-Drehung, Eintauchen, Heben, geneigte Mündung und Ausschüttfenster; kein Wasser bei nicht erreichbarer Wasserlinie; Geschwindigkeit/Wasserstand bedienbar |
| F — Zeichnungen | elf SVG-/PDF-Blätter aus gemeinsamer Meshgeometrie und Originalfotos | Orthogonale Ansichten, vergrößerte Details, echte Schnitte, verdeckte Kanten, Achsen, Messendpunkte und geschlossen dargestellte Maßpfeile; materialgeprüfte Schraffur |
| G — Aufnahmeplan | elf A3-Blätter und zweitseitiger A4-Kurzplan | 21 kanonische Aufgaben vollständig zugeordnet; Vorher/Nachher und Partnerbezüge; STOPP bei Verlust von Einbauinformation |
| H — UX | kurze Startseite, modellzentrierte Werkstatt, aufgabenbezogener Feldmodus | Manrope, helle Papierhierarchie, feine Linien, zurückhaltende Radien; Grün als Akzent; keine doppelten Einstiegsblöcke; deutsche Dateiauswahl |
| I — Viewer | 13 kontextbezogene Modi, Schnitt, Explosion, Varianten, Quellenvergleich und Scanansicht | Kameraübergänge, Isolieren, transparente Umgebung, drei Innenverbindungen und vier Stiftvarianten; aktuelles Foto/historische Zeichnung neben Kandidatenstatus abrufbar |
| J — QA | `state/reconstruction/browser/`, `pdf-review/`, `quality-review.json`, Testprotokolle | Desktop, iPhone 13 Pro in Chromium emuliert, 320 px, tatsächliche 200-%-Schriftprüfung; Betriebs-/Scan-/Schnitt-/Explosionsansichten; alle A3-Seiten einzeln und als Übersicht visuell geprüft |
| K — Gate | dieser Bericht, `state/reconstruction/GATE.md` | Rekonstruktionsgate erreicht; Remote-Synchronisierung gesondert blockiert |

## Automatisierte Prüfung

- Produktionsbuild erfolgreich; drei Seiten und 119 Offline-Dateien.
- Astro: 0 Fehler, 0 Warnungen, 0 Hinweise.
- 22 Node-Tests erfolgreich. Sie prüfen unter anderem Geometriezuordnung, Armendpunkte, Varianten, Registrierungsfehler, Messverträge, Datenimport und Verlustschutz.
- Browserprüfung mit vier Profilen erfolgreich; sichtbare Bedienelemente mindestens 44 px, kein horizontaler Seitenüberlauf, keine verbotenen englischen Begriffe, internen IDs oder dekorativen Unicode-Pfeile in der Standardoberfläche.
- Offlineprüfung: 28 Fotos mit insgesamt 20.460.272 Originalbytes; Reload, Wiederaufnahme, ein Teileintrag, ein Ereignis, Export und Import in einem frischen Kontext. Alle Foto-Prüfsummen stimmen. Das ist ein synthetischer Lasttest mit wiederholtem Originalfoto, keine behauptete Feldsession.
- GLB-Kopf, Gesamtlänge, 279 Meshes und explizite Z-up/Y-up-Umrechnung geprüft. Jeder Modellknoten bleibt ein Kandidat; reale Instanz-IDs sind leer.
- Die lokale Browserinstallation erfolgt über eine temporäre Chromium-Laufzeit. Keine Laufzeitbinärdatei oder lokale Abhängigkeit wird ins Projekt eingecheckt. Ein physisches iPhone/Safari wurde nicht getestet.

## Geometrischer Gegencheck

`state/reconstruction/candidate-audit.json` dokumentiert eine deterministische 20-mm-Abtastung im verdeckten Wellenkern einer Kranzseite:

| Kandidat | Mehrfach belegte Stichproben | Rang | Konsequenz |
| --- | ---: | ---: | --- |
| Axial gestaffelte Durchsteckarme | 0 | 1 | Beste Arbeitsannahme; Restholz, Keile und Einführweg bleiben am Teil zu prüfen |
| Getrennte Einsteckarme | 0 | 2 | Getrennte Befestigung erforderlich; durchgehende Endpaarung entfällt |
| Gemeinsame Ebene | 420 | 3 | Zusätzliche Ausklinkungen oder geteilte Montage erforderlich |

Das ist ein begrenzter Variantenvergleich. Es ist weder ein vollständiger Maschinen-Kollisionsnachweis noch ein Festigkeitsnachweis. Die unbekannten Welleninnenflächen werden nicht als gemessene Mortisen erfunden. Der tatsächliche Ausziehweg kann erst nach Erfassung der Keile, Freigaben und Partnerflächen entschieden werden.

## Visuelle Gegenprüfung und behobene Befunde

1. In der ersten Browserrunde sichtbare englische Rohbezeichnung und Textpfeile entfernt; technische Rohdaten ausdrücklich in technische Details eingeordnet.
2. Die vorherige Startseite hatte wiederholte Einstiege und einen toten Aufbau-Anker. Beides entfernt.
3. Zu kleine mobile Schaltflächen vergrößert; Kamerabild für 320 px so angepasst, dass die Gesamtanlage vollständig sichtbar bleibt.
4. Native, je nach Browser englische Dateischaltflächen durch eigene deutsche Auswahlflächen ersetzt.
5. Die Kumpfmündung zeigte zunächst zur falschen axialen Seite. Der Kandidat gibt nun nach außen zum Trog ab; Trog seitlich aus der Kumpfbahn versetzt und Rinne abgestützt.
6. Separate metallische Zapfenkandidaten und ein kontaktfähiger Lagersitz ergänzt; tatsächliche Lagerform bleibt offen.
7. Die erste Schraffur übermalte Teile des hohlen Kumpfs. Geschlossene Dauben-/Stiftflächen und Prüfung gegen das tatsächliche Schnittmaterial verhindern dies.
8. Fotomarkierungen für Krümmlingstoß und Wasserübergabe waren zu generisch. Sie beziehen sich jetzt auf die jeweiligen Bildregionen.
9. Die Offline-Testnavigation wartete nicht auf den abgeschlossenen Aufgabenwechsel. Der Test wartet nun auf den gespeicherten, sichtbaren Zielzustand; die Anwendung wartet bei normaler Seitennavigation auf ausstehende Schreibvorgänge.
10. Die ursprüngliche 200-%-Prüfung vergrößerte nur rem-basierte Texte. Jetzt werden alle berechneten HTML-Schriftgrößen und Zeilenhöhen verdoppelt.

Die Abnahme ist eine direkte visuelle Prüfung durch den ausführenden Agenten. Eine zusätzliche unabhängige menschliche Abnahme wird nicht behauptet. Die früheren Gegenprüfungen bleiben nachvollziehbar in `INDEPENDENT-REVIEW.md`; frühere Bildstände liegen getrennt unter `pdf-review/prior-iteration/`.

## Samstag entscheidet

- Welleninnenraum, reale Arm-Endpaarungen, Öffnungen, Keile und Ausziehrichtungen.
- Kröpfung jedes Arms und tatsächliche axiale Staffelung.
- Funktion, Sitze und Zuordnung langer/kurzer Stifte an mindestens drei Kümpfen.
- Lagerkontakt und Zapfenform vor und nach Entlastung.
- Beide Kontaktflächen, Bohrungen und Reparaturen der Krümmlingstöße.
- Kumpfneigung, Schaufelanstellung, Befestigung und aktuelle Stückzahlen.
- Wasserseitiger Unterbau, Rahmenknoten, Pfostenfüße und historische Asymmetrie im heutigen Zustand.
- Wasserlinie, Drehrichtung, Übergabehöhe, Troganschluss und Rinnenverlauf im Betrieb.
- DATUM-A/B/C, AXIS-A/B und unabhängige Kontrollstrecke für die mechanische und metrische Scanregistrierung.

Die Originale von IMG_6875/6876 fehlen weiterhin. Ihre frühere Kontextbeschreibung bleibt sekundär; es wurde kein neuer eigener Bildbefund daraus behauptet. Die vorhandenen aktuellen Gesamt- und Rahmenaufnahmen tragen den jetzigen Kandidaten.

## Bereitstellung

**Empfehlung: Bereitstellung als ausdrücklich ungemessene Rekonstruktion zur gemeinsamen Prüfung.**

Keine Veröffentlichung oder Zusammenführung in `main` wurde ausgeführt. Die automatische Freigabeprüfung hat den GitHub-Push abgewiesen: Die Veröffentlichung an den Remote `jdistlr/kleines-schaeferrad` sei nicht ausdrücklich bestätigt und könne privaten Quelltext oder Historie offenlegen. Der fertig geprüfte Stand ist lokal im angeforderten Branch committet. Vor dem erneuten Push ist die konkrete Zustimmung des Nutzers erforderlich.

## Prüfbare Dateien

- `output/pdf/KS-Werkstatt-Aufnahmeplan-A3.pdf`
- `output/pdf/KS-Kurzplan-A4.pdf`
- `output/model/KS-Rekonstruktion-V2.glb`
- `output/model/component-index.json`
- `state/reconstruction/pdf-review/contact-sheet.jpg`
- `state/reconstruction/browser/validation.json`
- `state/reconstruction/quality-review.json`
- `state/reconstruction/candidate-audit.json`
- `state/reconstruction/attachment-verification.json`
- `state/reconstruction/export-validation.json`
