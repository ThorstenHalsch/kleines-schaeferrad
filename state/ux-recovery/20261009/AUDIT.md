# Unabhängiger UX-Audit — 09.10.2026

**Verdict: CONDITIONAL GO für die Review des Recovery-Plans. Gate: UX RECOVERY PLAN REVIEW READY.** Keine produktive UX-Abnahme, Demontagefreigabe oder neue Rekonstruktionsiteration.

## Prüfgrundlage und Autorität

Ausgangspunkt ist PR #10, Branch `work/ux-audit-semantic-contract-20261009`, initialer Head `1ba182061038c6bf28468b26c8a2ba39d04b14b8`. Sein Produktionsstand entspricht `main` nach PR #9: `1de62e702e6a1f0b818ab4a6ad0d27c111ac720a`. Die drei zusätzlichen Dateien waren Dokumentation. Die UX-01–10 im ursprünglichen Audit wurden als Hypothesen behandelt, nicht als Abnahme.

Die veröffentlichte Seite wurde direkt geöffnet und ihre 126 Ressourcen einschließlich Manifest und Service Worker heruntergeladen und gehasht. GitHub-Pages-Run [37893675784](https://github.com/jdistlr/kleines-schaeferrad/actions/runs/37893675784) bestätigt erfolgreiche Build- und Deploy-Jobs genau dieses main-Commits. Manifest: `ks-field-eeb53c48cbdc68f3`, 124 Preload-URLs, 87.710.471 Bytes. Details: [deployment.json](evidence/deployment.json), [deployed-files.json](evidence/deployed-files.json).

Die veröffentlichten PDFs sind **nicht bytegleich** mit `output/pdf/` im Commit. A4 ist pixelgleich; A3 unterscheidet sich auf Seiten 3, 5, 6, 7, 9. PR #9 änderte den Generator, ohne die eingefrorenen PDF-Dateien neu zu committen. Der Pages-Build erzeugt die neuere Druckfassung. Die Prüfung unten bezieht sich ausdrücklich auf die heruntergeladenen finalen Pages-Dateien, die unter `evidence/print-live/` unverändert archiviert sind. [Pixel-/Hashvergleich](evidence/print-comparison.json).

## Tatsächlich ausgeführte Prüfung

- Direkte Cloud-Browser-Interaktionen: Start → Werkstatt → Kumpf → Quellenstatus → Feld. Dort kein WebGL; deshalb zusätzlich separater CI-Browser mit Software-WebGL. Lokaler Chrome konnte wegen `socket() failed: Operation not permitted` nicht starten. Diese Umgebungsfehler werden nicht als genereller Websiteausfall ausgegeben.
- [Matrix-Run 37895326410](https://github.com/jdistlr/kleines-schaeferrad/actions/runs/37895326410), Commit `65fa679`: Chromium **141.0.7390.37**, 21 vollständige Seitenscreenshots plus Interaktionen. [Rohbericht](evidence/ci/report.json).
- [Gezielter Folge-Run 37895794821](https://github.com/jdistlr/kleines-schaeferrad/actions/runs/37895794821), Commit `3b5e94b`: nur offene Wasser-, Wiederaufnahme-, Medien- und Bewegungsfragen. [Rohbericht](evidence/followup/followup.json).
- 11 finale A3-Seiten und 2 finale A4-Seiten in Farbe und Graustufen gerendert und visuell geprüft. Maßstab der Bildschirmprüfung ist keine physische Druckabnahme.
- Ausschließlich ausdrücklich als `SIMULATION` bezeichnete Testwerte und eine unveränderte bereits öffentliche Repository-Fotodatei in frischen Browserkontexten. Keine echten Aufnahmedaten, keine Erhebung am Rad.

| Profil | Start / Werkstatt / Feld | Beobachtung |
|---|---|---|
| Desktop 1440×1000 | alle ausgeführt | Modell sichtbar; viele Variantenregler vor Arbeitsabsicht |
| Tablet 768×1024 | alle ausgeführt | kein horizontaler Seitenüberlauf |
| 390×844 | alle ausgeführt | kein Seitenüberlauf; langer Weg bis Modell/Messformular |
| 320×740 | alle ausgeführt | kein Seitenüberlauf; Optionsbezeichnungen gekürzt; Modell erst weit unten |
| 200 % Text, 1280×1000 | alle ausgeführt | Überschrift überlagert Foto; kein Seitenüberlauf schützt davor |
| Reduced motion, 1440×1000 | alle ausgeführt | Kamera-/Wasserbewegung nicht vollständig unterdrückt |
| Dark preference, 390×844 | alle ausgeführt | warme helle MUX-Fläche bleibt erhalten; keine unlesbare automatische Inversion |

200 % bedeutet hier: vorab berechnete Schriftgröße jedes Elements verdoppelt, ohne Seitenzoom oder Containervergrößerung. Das ist eine reproduzierbare Textvergrößerungsprobe, **kein behaupteter Safari- oder OS-Dynamiktext-Test**. Mobile Profile emulieren Viewports, keine Hardwarekamera oder echte Touchgesten. Die Überlaufheuristik meldete absichtlich außerhalb liegende Skip-Links und horizontal scrollbar angelegte Quellengalerien; diese wurden nicht blind zu Defekten erklärt. 22-px-Checkboxen wurden ebenfalls nicht ohne ihr klickbares Label bewertet (Labelhöhe 40 bzw. 46 px).

Full-page-Screenshots können den sticky Header an der vorherigen Scrollposition abbilden. Daraus wurde kein separater Überlagerungsdefekt abgeleitet. Im Folge-Run ist `next` direkt nach dem asynchronen Speichern noch ein alter Titel; der nach Reload beobachtete Scan-Auftrag bestätigt die tatsächliche Fortsetzung. Ein frühes Wasser-Screenshot enthält noch nicht das nachgeladene Foto; die spätere Wiederaufnahme zeigt es. Kein dauerhafter Bildausfall behauptet.

## Journeys und Gegenproben

| Aufgabe | Ergebnis und belastbare Grenze |
|---|---|
| Modell entdecken | Startlink funktioniert, 3D unter CI-WebGL sichtbar; Desktop und mobile Reihenfolge geprüft |
| Kumpf, Quelle, Annahme | Teilfinder, Quellenstatus, Truth/Brute-Umschaltung, Kandidat B und Öffnen einer Originalquelle im separaten Tab funktionieren. Warnung „Maße nicht nachgemessen“ sichtbar. Kein Geometrie- oder Maßnachweis daraus. |
| Dringende Wasseraufnahme | Direkter sichtbarer Einstieg **gescheitert**, Link durch CSS versteckt. Über „Alle Schritte“, Eintrag 17, erreichbar. P1 bleibt offen. |
| Mehrere Messungen | Ein Messobjekt mit sechs Feldern. 123 durch 456 ersetzt; Reload und Import bewahren 456. Keine zweite Messung möglich. Das ist fehlende Funktion, kein Beweis willkürlicher Datenkorruption. |
| Originalfoto / Referenz | 730.724 Originalbytes bleiben im Export erhalten; SHA-256 vor/nach Export identisch. Hash in `report.json`. Manipulierte Prüfsumme wird abgewiesen. Dateiname und gewählte Ansicht bleiben erhalten. |
| Export / Import | JSON-Export → frischer Browserkontext → Import → Reload ausgeführt. Wert 456 und Originalbild wiederhergestellt. Abweichender Aufgabenstand wird ausdrücklich abgewiesen, nicht überschrieben. Kein zweites physisches Gerät getestet. |
| Offline-Rückkehr | Nach „Offline bereit · 124 Dateien“ Netzwerk deaktiviert, Reload, Wert 456 und Offline-Export erhalten. Keine Erstinstallation ohne Netz und kein Betrieb unter Speicherdruck nachgewiesen. |
| Partner / Ereignis | Synthetischer Teileintrag ohne Partner, Medien oder Ereignis wurde akzeptiert. Status bleibt keine fachliche Freigabe. Vor-/Nachher-Nachweis wird nicht verbindlich gefordert. |
| Navigation / Tastatur | Mobiles Menü öffnet, Feldlink funktioniert. Enter öffnet Aufgabenindex, Tab erreicht „Zur aktuellen Aufgabe“ mit sichtbarem Fokusring. Kein vollständiger Screenreader- oder 3D-Tastaturtest. |
| WebGL fehlt | Verständliche Meldung, Teilfinder/Quellen bleiben funktionsfähig. Leere Modellfläche und weiter aktive Modellregler verschwenden den Einstieg. |

## Priorisierte Defekte

P0 = belegter unmittelbarer Verlust/irreversibles Fehlverhalten ohne gangbaren Ausweg. **Kein P0 wurde nachgewiesen.** P1 = erheblicher Verlust an Evidenzqualität, Auffindbarkeit oder Zugang im Kernablauf. P2 = begrenzte Reibung, Verständlichkeit oder Abnahme-/Betriebsrisiko. Die P0-Aufnahmeprioritäten im Field-Kit sind eine andere Skala als UX-Defektprioritäten.

| ID | Rang | Reproduktion / Nachweis | Nutzerwirkung | Kleinste sinnvolle Korrektur nach Review |
|---|---|---|---|---|
| UXR-01 | P1 | Feld öffnen. Wasserlink, Hinweis auf zusätzliche Messblätter und Videooriginale unsichtbar. `src/styles/field.css:136` versteckt alle `.field-context p` und `.phase-track`. [Desktop-Beweis](evidence/browser-04-field-entry.jpg), [320px](evidence/ci/phone320-feld.png), [Index](evidence/ci/journey-keyboard.png). | Zeitkritischer Auftrag erst an Position 17; notwendige Ausweichwege sind unsichtbar. Vor Abschaltung kann Wissen verloren gehen. | Eigene sichtbar getestete Wasseraktion; Aufnahmefenster als kleine Navigation; Messblatt-/Video-Hinweise kontextuell am jeweiligen Schritt. Keine globale Rücknahme aller Dichte-Regeln. |
| UXR-02 | P1 | Referenzaufgabe → Messung. Nur ein Wert mit Endpunkten, Werkzeug, Einheit, Unsicherheit. [Formular](evidence/ci/journey-single-measurement.png), [mobil](evidence/followup/followup-mobile-measurement.png). | DATUM/AXIS/Kontrollstrecke oder mehrere Querschnitte nicht getrennt dokumentierbar. Neuer Wert ersetzt den alten, wenn dasselbe Feld verwendet wird. | Additive Messliste mit stabilen Mess-IDs, Foto-/Teilbezug und bewahrtem v1-Import; bis dahin sichtbarer Messblatt-Ausweg. |
| UXR-03 | P1 | Teileformular mit Pflichtfeldern ausfüllen, Partner/Foto/Ereignis leer lassen, bestätigen. [Gespeicherter Eintrag](evidence/ci/journey-partner-empty.png). | Zuordnung der geöffneten Verbindung kann trotz „lokal gesichert“ fehlen. | Bei kritischen Verbindungsschritten Partner und Vor-/Nachher-Ereignis verlangen **oder ausdrücklich begründet offen lassen**. Frühe Inventarisierung nicht global blockieren. |
| UXR-04 | P1 | Werkstatt bei 320/390 px öffnen. Vier technische Kandidatenregler stehen vor Ansichten und Modell; Bezeichnungen abgeschnitten. [320px](evidence/ci/phone320-werkstatt.png), [Kandidat](evidence/ci/journey-candidate-b.png). | Bedienung beginnt mit Modellkonfiguration; „Truth“, „Brute-Force“, „führend“ wirken autoritativer als der Belegstand und verdrängen die Arbeitsfrage. | Entdecken / Genauer prüfen / Festhalten innerhalb derselben Oberfläche. Varianten unter bestehendes Details-Element, immer sichtbarer knapper Kandidatenstatus. |
| UXR-05 | P1 | Start bei 1280 px, Textgrößen verdoppeln. [Screenshot](evidence/ci/text200-story.png). | „Schäferrad.“ ragt in die Bildspalte; Abschluss wird verdeckt. Kein horizontaler Scrollbalken, dennoch Inhaltsüberlagerung. | Text- und Bildspalte intrinsisch umbrechen lassen, Titelumbruch sichern. Kein neues Stylekit. |
| UXR-06 | P2 | `/feld/?task=TASK-WATER` öffnen, weiter zu Fotos, reload. [Schritt 1 nach Reload](evidence/followup/followup-query-resume.png). | Queryparameter setzt bei jedem Start den Schritt zurück. Eingaben bleiben erhalten, Arbeitsposition nicht. Normale Feld-URL setzt dagegen fort. | Deep-Link einmal konsumieren bzw. expliziten Sprung von Wiederaufnahme unterscheiden; Task-ID statt Änderung der Arrayreihenfolge. |
| UXR-07 | P2 | Foto hinzufügen, „Entfernen“, exportieren. [Budget](evidence/followup/followup-removed-photo-budget.png), Rohbericht: 0 Referenzen, 1 exportiertes Foto. | Entferntes Foto bleibt im Medienbestand, Export und 250-MB-Limit. Menge auf Bildschirm und Sicherung widerspricht sich. Kein Datenverlust nachgewiesen. | „Zuordnung lösen“ ehrlich benennen; referenzierte/unzugeordnete Medien getrennt zählen. Endgültige Bereinigung erst explizit nach Sicherung, nicht automatisch. |
| UXR-08 | P2 | Reduced motion → Betrieb → 3 s warten, zwei Canvas-Aufnahmen mit 1,2 s Abstand. [Befund](evidence/followup/followup.json), Frames vorhanden. | Wasserpfeile ändern sich trotz „Rad angehalten“; Kameraübergänge beachten Systemeinstellung nicht. | Nicht notwendige Bewegung und Kamera-Lerp bei reduced motion stoppen; Betrieb nur nach explizitem Start. |
| UXR-09 | P2 | WebGL deaktiviert / im Cloud-Browser nicht verfügbar. [Ausfallansicht](evidence/ci/journey-webgl-fallback.png). | Große leere Fläche und funktionslose Regler vor funktionierendem Teilfinder. | Ausfallfläche kompakt, Regler deaktivieren, direkter Sprung zu Teilfinder/Originalen. |
| UXR-10 | P2 | Kumpf auswählen, Galerie/Quellenstatus öffnen. [Screenshot](evidence/ci/journey-kumpf.png). | „Foto öffnen“ bei Zeichnungen; Dateikennung/Quellentyp nicht an den ersten Thumbnails, englisches „all-vessel equivalence“. Vier Referenzfotos im Text erwähnt, aber nicht in der ersten Fünfergalerie. | Kurze Original-ID, Typ und Geltungsbereich; relevante Referenzfotos über vorhandene Quellen erreichbar hervorheben. Quellenautorität unverändert. |
| UXR-11 | P2 | Pages-PDF und `output/pdf` vergleichen. [Vergleich](evidence/print-comparison.json). | Review kann eine andere Helligkeit/Beschriftung als der Ausdruck betreffen. | Später Generator, eingefrorene PDFs und Deployment-Manifest gemeinsam versionieren; keine automatische Quellenänderung. |
| UXR-12 | P2 | Finale A3-Blätter KS-31/KS-51 in Graustufen lesen. [KS-31](evidence/print-live/a3-06-gray.png), [KS-51](evidence/print-live/a3-09-gray.png). | Geometrie erkennbar, aber kleine helle Raster-Bildunterschriften sind gegenüber der großen Nutzfläche schwach. | Entscheidungssatz als normalen Drucktext daneben setzen; bestehende Bilder/Geometrie unverändert. Physische Probe vor Feldabnahme. |
| UXR-13 | P2 | Frischer Feldstart lädt atomar 87,7 MB/124 URLs, Status zunächst „wird geprüft“. [Manifest](evidence/deployment.json). | Wartezeit/Netzkosten; Erstnutzer kann den Online-Vorlauf unterschätzen. Kein langsames Mobilnetz gemessen. | Größe und Fortschritt erklären, Wiederholung sichtbar; Cache-Aufteilung erst nach separater Daten-/Offline-Abnahme. |
| UXR-14 | P2 | Werkstatt Ebenen-Checkboxen: Labelhöhe 40 px, „Nur Auswahlbereich“ 46 px. [Messung](evidence/followup/followup.json). | Einige Touchflächen unterschreiten das projektinterne 44-px-Ziel. | Label-Padding korrigieren; nicht bloß das sichtbare Checkboxquadrat zählen. Keine pauschale WCAG-Nichtkonformität behauptet. |

## Visuelle Druckprüfung

Die pauschale Ausgangshypothese „synthetische Platten sind zu dunkel“ ist **für die veröffentlichte Fassung nicht bestätigt**. PR #9 hellt ausschließlich synthetische Renderplatten auf; Originaldateien werden nicht verändert. A3 KS-11, KS-31, KS-40 und KS-51 sind im Graustufen-Softproof als Formen unterscheidbar. Die Kennzeichnung „SYNTHESE – AUFGEHELLT / UNBESTÄTIGT“ steht daneben. Das ist eine Druckanpassung, keine neue Modellevidenz.

| Seiten | Prüfung |
|---|---|
| A3 1–2, 4, 8, 10 | Linienansichten intakt, keine abgeschnittenen Hauptüberschriften; feine Linien bleiben druckerabhängig |
| A3 3, 5–7, 9 | Original/Synthese getrennt, relevante Bilder vorhanden; kleine rasterisierte Legenden bleiben Leserisiko, besonders KS-31/51 |
| A3 11 | Fünf Ereignisse und Aufnahmefelder erkennbar; Begleittexte klein, Probedruck nötig |
| A4 1–2 | 21 Aufgaben mit Zeitfenster; Wasseraufnahme zuerst; schwarz/weiß tragfähig, keine beobachtete Überlagerung |

Native PDF-Textgrößen und Seitenabmessungen: [pdf-metadata.json](evidence/print-live/pdf-metadata.json), [print-comparison.json](evidence/print-comparison.json). Raster-Bildbeschriftungen sind durch Textextraktion nicht vollständig abgedeckt. Kein Papier, Drucker, Blendlicht, nasse Handschuhe oder realer Arbeitsplatz verfügbar: **physische Tageslicht-/Graustufenabnahme OFFEN**.

## Gegenüberstellung zum ursprünglichen UX-01–10

UX-01 bestätigt (UXR-04); UX-02 verschärft (UXR-01: nicht nur schwacher, sondern versteckter Link); UX-03/04 bestätigt (UXR-02/03); UX-05 differenziert (Aufhellung wirksam, kleine Legenden und Versionierung offen); UX-06 weiterhin echter Hardware-Gate; UX-07 bestätigt, nachrangige Sprachkorrekturen; UX-08 kein pauschaler Overflow, aber Textüberlagerung/Bewegung/Hitflächen; UX-09 keine Fertigungsfreigabe sichtbar behauptet, „Truth“ dennoch missverständlich; UX-10 kein eigener veröffentlichter Render-Review-Einstieg gefunden, aber für diesen P1-Plan zurückgestellt. Kein neuer Galerie-/Plattformbau.

## Grenzen und nächster Beschluss

Der unabhängige Audit weist **fünf P1-Befunde und neun P2-Befunde**, keinen belegten P0 aus. Alle kleinsten P1-Korrekturen stehen in [RECOVERY-PLAN.md](RECOVERY-PLAN.md); kein produktiver Fix wurde vorgenommen. Die semantische Evidence/Engineering/Experience-Trennung bleibt Diskussionsentwurf.

Vor realer Field-Freigabe: iPhone/Safari Kamera/Dateitypen, Speicher/Wiederaufnahme, Export und Import auf zweitem Gerät, offline nach Tab-/App-Neustart sowie physischer A3/A4-Probedruck prüfen. Verlustszenarien unter vollem Speicher, unterbrochenem Import und 250-MB-Grenzlast sind nicht akzeptiert. Die vorhandene „Field workbench acceptance“ war bereits am initialen PR-Head rot (Run 37894488501, `page.goto`-Timeout beim lokalen Werkstattstart); diese vorhandene Abnahme wurde nicht repariert oder zu grün umgedeutet. Unsere grünen Audit-Jobs bedeuten, dass Beobachtungen gesammelt wurden, nicht dass die Website fehlerfrei ist.
