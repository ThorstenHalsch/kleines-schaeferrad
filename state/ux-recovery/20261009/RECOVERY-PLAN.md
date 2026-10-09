# Kleiner Recovery-Plan — nur zur Review

**Status: REVIEW READY, NICHT ZUR IMPLEMENTIERUNG FREIGEGEBEN.** Bezug: [AUDIT.md](AUDIT.md), P1 UXR-01–05. MUX-Tokens, Manrope, Papier/Holz/Graphit, zurückhaltendes Grün und die drei Dichten bleiben erhalten. Kein neues Navigationsprodukt, keine neue Modellgeometrie.

## Reihenfolge und minimale Pakete

| Paket | Behebt | Exakt vorgeschlagener Umfang | Bewusste Grenze |
|---|---|---|---|
| R1 — richtige Aufnahme jetzt | UXR-01 | Sichtbare Aktion „Rad läuft noch? Wasseraufnahme zuerst“. Kleine Fensterwahl: vor Stillsetzen / vor Lösen / direkt danach / vor Abfahrt. Vorhandene Task-IDs referenzieren. Messblatt-/Video-Hinweise an den betroffenen Eingabeschritten anzeigen. | Keine Umsortierung des persistierten Task-Arrays, keine automatische Demontagefolge, keine Datenmigration. UXR-06 nur als notwendige Deep-Link-Rückkehrbedingung mit absichern. |
| R2 — zusammengehörige Evidenz | UXR-02/03 | Wiederholbare Messzeilen; kritische Partner-/Ereigniszuordnung oder ausdrückliche offene Begründung. Originaldatei-Referenz je Messung. „Aufgenommen – gemeinsam prüfen“ bewahren. | Erst nach gesicherter realer Aufnahme und Review; keine spontane Form-/Schemaänderung im laufenden Einsatz. Keine Freigabe-Automatik, kein CAD-Schema. |
| R3 — Modell verständlich betreten | UXR-04 | „Entdecken“ zeigt Modell, Teilfinder und Quellenstatus. „Genauer prüfen“ öffnet bestehende Varianten/Scan-Details. „Festhalten“ öffnet vorhandene Befunderfassung oder passenden Feldauftrag. Technische Namen sekundär, Kandidatenstatus direkt am Bild. | Gleiche Routen, gleiche Komponenten und Regler; keine neue Plattform, Renderbibliothek, Kameraflüge oder neue Geometrie. |
| R4 — Text bleibt lesbar | UXR-05 | Intrinsischer Umbruch der vorhandenen Hero-Spalten/Überschrift bei Textvergrößerung; Foto bleibt Bild, Text bleibt Text. | Kein Redesign, keine neuen Inhalte, keine Feldschemaänderung. |

R1 zuerst reviewen. R3/R4 können später getrennt von R2 umgesetzt und zurückgenommen werden. Keine P2-Sammelreparatur in diesen Paketen. Medienbereinigung, Druckversionsprozess, Bewegungsdetails, 44-px-Nachpflege und neue Render-Galerie bleiben ausdrücklich nachgeordnet; bei einem Paket zufällig nötige Korrekturen müssen in dessen Review benannt werden.

## Abnahme, bevor ein späterer UX-PR als fertig gelten darf

**R1:** Frischer und fortgesetzter Feldstart auf 320/390/768/1440 px. Wasseraktion im ersten sinnvollen Handlungsbereich und per Tastatur erreichbar. Zwei Aktionen maximal zum Wasserauftrag. „Noch offen“ bleibt erlaubt. Fensterwahl verändert nur Sicht/Navigation. Reload nach Deep-Link bewahrt Auftrag und Eingabeschritt; Rückkehr aus Sicherung/Index verliert keine Eingaben. Bis auf geprüfte Navigation alle 21 Task-IDs, Reihenfolge und Antworten bytegleich. Zusatzmessung/Video-Ausweg sichtbar, keine Videoupload-Funktion vorgetäuscht.

**R2:** Eine alte v1-Sicherung mit Foto und Messwert unverändert importieren; zwei neue Messungen mit verschiedenen Endpunkten erfassen; neu laden; exportieren; in frischem Kontext importieren. Alle Werte, Einheiten, Unsicherheiten und Originalbytes bleiben erhalten. Abweichende Mess-/Medien-/Ereignis-IDs erzeugen einen sichtbaren Konflikt statt „last write wins“. Ein kritischer Verbindungsschritt ohne Partner/Vorher/Nachher wird entweder begründet offen gespeichert oder kann nicht als vollständig aufgenommen gelten. Unbekannte Partner dürfen nicht durch erfundene IDs ersetzt werden. Inventarisieren eines noch eingebauten Teils bleibt möglich. Speicherung allein setzt nie `ACCEPTED`, `METRIC_VERIFIED` oder `RELEASED`.

**R3:** Besucher findet Kumpf über Teilfinder ohne technische Reglerwahl. Fachperson erreicht alle heutigen Kandidaten und Quellen weiterhin mit höchstens einem zusätzlichen Aufklappen. Modellwechsel behält Auswahl und Quellenbezug. An jeder Darstellung bleibt „Rekonstruktionsvorschlag – aktuelle Maße offen“ o. ä. sichtbar. Begriffe „Truth“/„Brute-Force“ dürfen interne Kennungen bleiben, gelten aber nicht als Gütesiegel. Beobachtung, Fachwissen, offene Annahme und Synthese nicht zu einem grünen Status zusammenziehen.

**R4:** 1280 px mit exakter 200-%-Textprobe wiederholen; zusätzlich echte Browserzoom-/iOS-Textgrößenprüfung. Keine Überschrift verdeckt Bild/Text/Bedienung. 320/390/768/1440 bleiben intakt, Tabfolge unverändert. Ein Scrollbreiten-Test allein reicht nicht.

Gemeinsame spätere Freigabebedingung: erst vorliegende reale Demontageevidenz sichern und reviewen, separat beauftragten kleinen UX-PR erstellen, auf echtem iPhone/Safari und mit bestehender Sitzung testen. Keine Umsetzung durch dieses Plan-Gate autorisiert.

## Rückwärtskompatible Messung — Vorschlag, keine Migration

Kleinster fachlicher Satz je Messung: stabile `measurement_id`, Eigenschaft, Rohwert, Einheit, Endpunkt A/B, Werkzeug/Auflösung, Unsicherheit mit Einheit, reale Teil-/Partner-ID oder offene Begründung, Originalmedien-IDs, Person/Zeit und Aufnahmeereignis. Unlesbare/fehlende Angaben ausdrücklich offen lassen; keine synthetischen Standardwerte.

Der bestehende v1-Import bleibt lesbar. Ein einzelnes `measurement` wird beim Lesen deterministisch als eine Zeile projiziert; Original-v1-Paket bleibt unverändert verfügbar. **Kein stilles Überschreiben des Legacy-Objekts und kein v1-Export, der mehrere Werte auf einen reduziert.** Für den späteren Schreibvertrag v2-Paketkennung mit expliziter Versionsprüfung vorsehen. Ältere Clients müssen v2 verständlich ablehnen; ein gesonderter v1-Export wäre nur für verlustfrei darstellbare Sitzungen zulässig. Import zuerst vollständig validieren, dann atomar schreiben. Vor jeder Migration externe Sicherung; Rollback nutzt diese v1-Sicherung, nicht rückwärts verworfene neue Daten.

Bei Verbindungen: ein Ereignis verbindet beide realen Partner und Vorher-/Nachher-Medien, nicht nur Freitext in zwei unabhängigen Aufgaben. Ein Revisionswechsel ergänzt Herkunft und ersetzt keine frühere Beobachtung. Alte Einträge ohne diese Angaben bleiben **Altbestand, Zuordnung offen**, nicht nachträglich freigegeben.

Die vorhandenen Zustände OPEN / IN_PROGRESS / CAPTURED_UNREVIEWED / BLOCKED_UNKNOWN bleiben verständlich und prüfbar. Eine spätere fachliche Entscheidung muss Person, Zeitpunkt, Aussageumfang und Begründung speichern; ein „am Teil geprüft“-Häkchen ist keine Experten- oder Fertigungsfreigabe. Der umfassendere Vertrag in `docs/SEMANTIC-RECONSTRUCTION-CONTRACT-DRAFT.md` bleibt weiterhin DRAFT.

## Reale Abnahme noch ausstehend

| Prüfung | Verantwortungsrolle | Nachweis |
|---|---|---|
| Kamera/Dateitypen auf iPhone/Safari, Originale behalten | tatsächlicher Feldanwender | Gerät/OS/Browser, Originalname/Hash, Screenshots; HEIC-Konvertierung ausdrücklich erkennen |
| App schließen, neu öffnen, Flugmodus; Export → zweites Gerät → Import | Feldanwender + technische Begleitung | zwei unabhängige geöffnete Sicherungen, gleiche Mess-/Fotoanzahl und Hashes |
| Speicher knapp, Export unterbrochen, große Sitzung | technische Begleitung mit separaten Testdaten | kein falsches „gesichert“, Originalexport unverändert, Wiederaufnahme nachvollziehbar |
| A3/A4 Graustufen auf tatsächlichem Drucker im Tageslicht | Thorsten/Team | KS-31 und KS-51 inklusive kleiner Legenden lesbar; Markierungen und Platz für reale Notizen |

Bis dahin ist Papier plus separat gesicherte Originalkamera-Dateien der bereits vorhandene Ausweichweg. Der Audit hat keine neue fachliche Freigabe dafür erzeugt.

## Review-Fragen

1. R1 als ersten minimalen UX-PR nach der vorgesehenen Evidenzsicherung priorisieren?
2. Für R2: Partner und Ereignis nur an kritischen Verbindungsschritten verbindlich machen, mit begründetem „offen“ als gleichwertigem ehrlichem Ergebnis?
3. Für R3 die deutschen Arbeitswege „Entdecken / Genauer prüfen / Festhalten“ innerhalb der vorhandenen Oberflächen akzeptieren?
4. Wer übernimmt echte iPhone-/Zweitgeräte- und Druckprobe? Ohne zugeordneten Prüfer bleiben diese Gates offen.

Diese Fragen stehen zur Review. Es wurde niemand angeschrieben und keine Antwort vorweggenommen.
