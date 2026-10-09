# ITER-001 Independent Truth Critic

Basis: `e92bebd1201fe49bf2f0f598584cfd2832a48b96`, main nach Merge von PR #7; Prüfung 2026-10-09. Review durch einen separaten Audit-Durchgang, nicht durch eine neue Rekonstruktionsiteration. Keine externe Fachfreigabe behauptet.

**Verdict: CONDITIONAL GO ausschließlich für die vorbereitete Evidenzaufnahme.**

ITER-001 ist als beschrifteter Hypothesen- und Diskussionsbestand verwendbar. Eine aktuelle metrische Rekonstruktion, tatsächliche Montagefolge, nachgewiesene Wasserfunktion oder Demontagefreigabe ist damit **nicht** erreicht. Die Selbstbewertung „fixed“ bezeichnet überwiegend Änderungen innerhalb des Kandidatenmodells; sie schließt die entsprechende Realweltfrage nicht. Die qualitative SCORECARD ist keine unabhängige Genauigkeitsbewertung.

Das Dokumentations-Gate **PRE-DISASSEMBLY EVIDENCE READY** bezeichnet einen geprüften Aufnahmeplan mit nachvollziehbaren offenen Entscheidungen. Es setzt weder deren Antworten noch die erfolgreiche spätere Feldaufnahme voraus. Physischer iPhone-Test, Teamfreigabe und reale P0-Aufnahmen bleiben offene Einsatzbedingungen.

## Prüfweg und Abdeckung

- Alle 30 jetzt angehängten Originale gegen Repository-Originalbytes vergleichen, nicht als neue unabhängige Quellen zählen.
- Historische Zeichnungen und aktuelle Fotos aus `evidence/raw/` visuell sichten; Referenzfotos 1000046420–6423 im Detail. Wiederholte Fotos derselben Zeichnung sind keine unabhängigen Bestätigungen.
- Thorstens Wortlaut in `evidence/contributions/kumpf-20261008.json` und `schaufelstellung-20261008.json` gegen Baseline, Konfiguration und Metadaten prüfen.
- Alle 16 Truth/Brute-Kamerapaare visuell prüfen, Manifest/Hashes und GLB-Metadaten unabhängig lesen. Kein Neurendering, kein Export neuer Geometrie.
- Kalibrierungscode, Audit-Methoden und gespeicherte Ergebnisse gegeneinander lesen. Die vorhandenen Kollisions- und Modelltests werden nicht erneut als ITER-001-Arbeit ausgeführt.
- Vorhandene PLY/GLB, Exportrelation, Scan-Audit und Registrierungszustand prüfen. Eine neue Segmentierung oder Registrierung erfolgt nicht. Ein unbekanntes separates Scan-Artefakt wird nicht erfunden.
- Grenzen: Übersichtssichtung historischer Quellen ersetzt keine erneute Transkription aller 369 Claims; verdeckte Bauteile bleiben verdeckt. Animation wird anhand Code, Phasenbildern und gespeichertem Zyklus geprüft, nicht als reale Betriebsaufnahme gewertet.

Maschinenlesbare Prüfergebnisse: [verification.json](verification.json). Aufnahmeaufträge: [CAPTURE-PLAN.md](CAPTURE-PLAN.md). Entscheidungen und Ranking: `data/pre-disassembly-evidence-gate.json`. Der gesamte ursprüngliche ITER-001-Ausgabebestand bleibt eingefroren.

## Vier strikt getrennte Klassen

| Klasse | Akzeptierter Aussageumfang | Ausdrücklich nicht enthalten |
|---|---|---|
| **Accepted Evidence** | Identifizierte Originaldateien; sichtbare Oberfläche/Form/Anordnung; historische Zeichnung als historisches Dokument; beobachtete Nut und Öffnungen des Referenzteils | Aktuelle Ist-Maße aus Perspektive; verdeckter Nagelweg; Datierung/Identität des Referenzteils ohne Nachweis |
| **Expert-Supported Construction** | Thorstens Referenzaufbau: zwölf Dauben, Nutboden, drei Bänder, zwei gelochte Dauben mit je zwei Löchern; zwei verschieden lange Kumpfnägel zur Befestigung am Krümmling; Nachbarüberlappung als Funktionsgrund; 90°-Fachkorrektur mit noch zu zeigendem Bezug | Exakte metrische Ausführung, universelle Gleichheit aller eingebauten Kümpfe, automatisch radialer Pitch |
| **Unresolved Hypotheses** | Gerichtete Überlappung, Lochpaarung A/B/C oder andere, Kopf-/Einsteckseite, Durchquerung weiterer Kontakte, Innenverbindung Welle/Arme, realer Lagerkontakt, Umfangszahl, Schaufelpitch, Scan-Korrespondenzen | Automatische Freigabe durch plausible Bilder, erfolgreiche Tests oder ranghöchsten Kandidaten |
| **Synthetic Visualization** | Beide GLBs als geometrische Darstellungen; gewählte Displaymaße/-posen auch im Truth-GLB; 24 Kopien im Brute-Modell; animierter Wasserstand, Trogpose, Drehzahl und Strahl | Aufmaß, Fertigungsgrundlage, Tragfähigkeitsnachweis oder beobachtetes Verhalten |

Die Klasse gehört zur **einzelnen Aussage**, nicht pauschal zum ganzen Bild oder Bauteil. Ein Bild kann eine fachlich unterstützte Nut illustrieren, deren Tiefe trotzdem synthetisch ist. Historische Bemaßung ist akzeptierte Dokumentevidenz mit historischem Geltungsbereich. Sie ist keine aktuelle Messung. Die bestehende Quellenautorität wird nicht umgeschrieben.

## Unabhängige Befunde

| ID / Gewicht | Befund und Gegenprüfung | Konsequenz / Schließnachweis |
|---|---|---|
| TC-01 / P1 | Quellenrangfolge trennt Messung, Beobachtung, Fachwissen und Synthese sinnvoll. Aber `reference.metricStatus` wird pauschal an Dauben, Boden und Bänder weitergereicht, obwohl Nut-/Bohrungsmaße ungemessen sind. `baseOffset` ist synthetisch, fehlt jedoch in `reference.unmeasured`. Das ist Metadatenunschärfe, keine neue Messung. | Keine metrische Promotion. D1; pro Eigenschaft Messreferenz und Geltungsbereich dokumentieren. Bestehende Truth-Namen nur zusammen mit dieser Einschränkung verwenden. |
| TC-02 / P1 | 6420 zeigt oben eine sichtbare Nut und unten eine lose/abgelegte Scheibe; Bildorientierung allein bestimmt daher nicht Mündung/Boden. 6421 zeigt den geschlossenen, 6422 den offenen Querschnitt. Die 600/300/220-mm-Werte sind plausible Bildlesekandidaten, nicht unabhängig kalibriert. Gleiche 30°-Dauben, 14/8-mm-Nut, 12-mm-Bohrradius und gegenüberliegende Dauben 0/6 folgen aus Code. | Mündung/Nut/Boden am Original zeigen lassen; Endmaße in zwei Richtungen und Lochmitten von eindeutig bezeichnetem Ende aufnehmen. Kein bloßes Abnicken einer Zahlenliste. |
| TC-03 / P0 Aufnahme | `referenceKumpf()` berechnet Nagelende auf der angenommenen Ebene X=-0.495. Es benutzt dafür `vesselPose(0)` mit Defaultwerten, während die äußere Pose über Optionen geändert werden kann. A/B/C sind keine unabhängig bestätigten realen Befestigungen. Die Auszugprüfung verwendet gerade Endpunktverbindung und fünf Punktspuren, nicht vollständige gekrümmte Nagel- und Kopfkörper; eigenes Holz und Krümmling sind ausgeschlossen. | Aussage „zero conflicts“ auf den gespeicherten Default-Sampletest begrenzen. Modellvariante/Bedienoption erbt keine Prüfung. D2: beide tatsächlichen Wege, Kopf, Querschnitt, Krümmung, Sitz und Nachbarpartner vor/nach Ziehen dokumentieren. |
| TC-04 / P0 Aufnahme | 0.047116 rad Überlappung ist aus Projektionswinkeln eines synthetischen Körpers berechnet. Sie beweist weder realen Kontakt noch welcher Nachbar über welchem liegt. Kollisionsfreier Pose-Kandidat wurde zusammen mit Überstand/Phase gewählt. 24 gleichartige Plätze sind eine Annahme, keine Instanzzählung. | Vollständige gerichtete Umfangsfolge und mindestens eine detaillierte Dreiergruppe; jede Abweichung ergänzen. Überlappung als Fachwissen erhalten, ihre konkrete Realisierung offen lassen. |
| TC-05 / P0 Aufnahme | Algebra unabhängig nachvollzogen: jede Ebene span(X, aR+bT) steht zur Radebene YZ senkrecht. V2 und V3 können deshalb beide die unspezifische 90°-Aussage erfüllen. Radialer Pitch, 0.45-Slot-Phase und 70-mm-Überstand werden dadurch nicht bestätigt. | D3: Bezug zeigen, Brettnormalen-/Radialbezug messen, drei beschriftete Nachbarschaften erfassen. Funktionale Plausibilität ist unterstützend, kein Winkelmesswert. |
| TC-06 / P1 | Kontakt-Audit prüft Oberfläche einer repräsentativen Dreiernachbarschaft. Stationär-Audit prüft jeden sechsten Vertex einer Slot-0-Gruppe an 72 Positionen; `!nailHead` schließt Köpfe ausdrücklich aus. Innere Kreuzung ohne getroffenen Vertex, schmale Hindernisse und reale Varianten sind nicht abgedeckt. | Keine kontinuierliche Kollisions-, Zugangs- oder Demontagegarantie. Tatsächlichen Platz für Kopf, Werkzeug, Hand und Abstützung vor Ort von Fachteam beurteilen lassen. Kein erneuter Geometrie-Suchlauf in diesem Auftrag. |
| TC-07 / P0 Aufnahme | `calibratedCycle()` schreibt Drehzahl 2.2 rpm und Strahlgeschwindigkeit 1.8 m/s vor. Füllung folgt einem 180-Schritt-Heuristikmodell mit 0.15-m-Eintauchparameter, ohne Zuflusszeit oder Leistungsbilanz. Bei nassem Rand ist Füllung nicht an die berechnete Haltekapazität gebunden. Trogposition wurde für den Kandidaten verlegt. Eine abgefangene Flugbahn ist kein Energie-/Durchflussnachweis. | D5 vor Stillsetzen: reales Video mit Zeiten, gewähltem Kumpf, Verlusten und Trog; Wasserstand und Trogkanten im festen Bezugssystem. Bei fehlendem Betrieb nur statische Geometrie erfassen, Funktionsfrage offen. |
| TC-08 / P0 Aufnahme | `scan-transforms.json`: AXIS_NORMALIZED; mechanische Transformation, Maßstab und Seitenbestätigung null. PLY/GLB sind gekoppelte Exportdarstellungen, keine zwei unabhängigen Aufmaße. Die fehlende Identität des erwähnten Detail-Scans ist nicht sein Nichtexistenzbeweis. | Dateiname und Region von Thorsten; neue bleibende Marker + alte wiedererkennbare Merkmale. Fit-Punkte, unabhängigen Prüfpunkt, Residuen/Einheiten/Unsicherheit und Vorzeichen dokumentieren. Neue Marken tauchen nicht rückwirkend im alten Scan auf. |
| TC-09 / P0 Aufnahme | Historische Arm-/Kranzzeichnungen (6816–6819, 6831, 6848–6852) und Fotos (6808, 6853–6856, 6860–6861) begründen gezielte Fragen, nicht unsichtbare Innengeometrie. Truth-Ansichten 07–10 behalten historische Displaykörper; Detailoberflächen sind keine dokumentierten aktuellen Kontakte. | D4: Arm-Endpaarung und Reihenfolge, Mortisen/Restholz, beide Krümmlingflächen sowie Lagerkontakt unmittelbar vor/nach fachlicher Freigabe erfassen. Ringform und Rahmenlage vor Entlastung messen. |
| TC-10 / P0 Aufnahme | Ursprünglicher Field-Kit-Manifeststatus ist PENDING_VISUAL_AUDIT; alle Seiten REVIEW_REQUIRED. KS-31 war im Task-to-Sheet-Mapping nicht direkt erreichbar; digitale Aufgaben erfassen viele Messungen nur in einem Messfeld. Ein spätes TASK-WATER in der Liste kann den Betriebszeitpunkt verpassen. | Jetzt sichtbarer Verweis „vor Stillsetzen“, explizite Fenster/Prioritäten, KS-31 als Zusatzblatt, A4-Route. Mehrfachmessungen als beschriftetes Messblatt mit Originalfoto und Datei-ID, Video extern im Original sichern. Physischer Safari-Test bleibt Einsatzbedingung. |

P0 bezeichnet unwiederholbare **Aufnahmefenster**, nicht die Behauptung, das reale Rad sei gefährlich oder der Kandidat bewiesen falsch.

## Review aller Canonical Views

Je Zeile wurden beide vorhandenen Bilder angesehen; die Paarung ist ein kontrollierter Modellvergleich, kein Foto-Matching.

| Paar | Sichtbefund | Zulässiger Schluss / offene Frage |
|---|---|---|
| 01 | Drei Truth-Referenzkümpfe; Brute-Vollsystem | Unterschied in Population ausdrücklich synthetisch; Landseitenname vor Ort bestätigen |
| 02 | Gegenseite; Brute-Rahmen verdeckt Details | Verdeckung ist keine Evidenz fehlender Teile; Wasserseite bestätigen |
| 03 | Schrägblick macht axiale Anordnung sichtbar | Gewählte Displaypose, kein Aufmaß |
| 04 | Zweiter Schrägblick | Ergänzt Lesbarkeit, nicht Quellenunabhängigkeit |
| 05 | Axialbild mit drei vs vollständiger Population | Umfangsfolge real zählen |
| 06 | Gegenüberliegender Axialblick | Vorzeichen und Blickseite sichern |
| 07 | Welle/Arme als Schnittdarstellung | Historische Form sichtbar; durchgehende Endpaarung und Innenkontakt offen |
| 08 | Truth-Zapfen ohne Lager, Brute mit Sitz | Tatsächlichen Lagerkontakt aufnehmen |
| 09 | Gegen-Zapfen | Beide Seiten getrennt dokumentieren; Symmetrie nicht voraussetzen |
| 10 | Dargestellter Krümmlingstoß mit Lochformen | Lochbild und Passflächen nicht automatisch aktuell bestätigt |
| 11 | Referenz-Kumpf, Truth-Drahtschaufel; Brute-Nägel | Drahtdarstellung bleibt Pitch-Kandidat; Weg/Kopf fehlt als Ist-Nachweis |
| 12 | Drei geneigte Kümpfe | Gerichtete reale Überlappung nicht belegt |
| 13 | Truth leer, Brute-Unterbau | Bewusste fehlende Truth-Evidenz, kein defekter Export |
| 14 | Truth ohne Trog; Brute-Kanal | Empfangsposition synthetisch; Messung zwingend |
| 15 | Explodierte Kandidatenanordnung | Keine Ausbau- oder Montageanweisung |
| 16 | Truth ohne Wasser, Brute mit Wasserfläche | Wasserbild ist Illustration; kein beobachteter Betrieb |

## Priorisierung und Freigaben

Alle 21 bestehenden Aufgaben sind in `data/pre-disassembly-evidence-gate.json` gerankt. Informationsgewinn, Irreversibilität und Verlust von Demontagekontext werden jeweils ordinal 1–5 bewertet; Aufwand ist eine Schätzung pro erstem Set/Ereignis. Ein niedrig aufwendiger Werkbankwert wird nicht vor eine nur einmal erreichbare Innenfläche gezogen. Die Rangfolge ist **keine** Demontagereihenfolge.

Entscheidungen D1–D5 bleiben UNANSWERED. Thorsten bestätigt fachliche Aussagen mit konkretem Teil-/Foto-/Dateibezug und Geltungsbereich. Messende Person dokumentiert Rohwerte. Erst anschließendes Review darf einen Claim klassifizieren oder ein Hypothesenurteil ändern. Ein nicht sichtbarer Nagelweg bleibt unbekannt, auch wenn A rechnerisch passt.

## Nächste Phase

Feldaufnahme und Evidenzabgleich. Zuerst Betriebszustand/Bezugssystem sichern; dann die vom verantwortlichen Team festgelegten Öffnungsereignisse begleiten. Danach Originale, Partnerregister, Messblätter und Fachantworten gegen D1–D5 prüfen. Erst mit diesen Ergebnissen entscheiden, ob eine nächste Rekonstruktionsiteration sinnvoll und ausreichend bestimmt ist. Keine ITER-002 allein aus dem jetzigen CONDITIONAL GO ableiten.
