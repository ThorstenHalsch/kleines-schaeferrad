# Compact Field Pack v2 — Visual Measurement & Capture Plan

Stand: 2026-10-07
Status: verbindliche Neuausrichtung nach Feld- und UX-Review.

## Ziel

Der bisherige 38-seitige Prüfplan ist als Nachweis vollständig, aber als Arbeitsmittel zu textlastig und zu fragmentiert.

V2 wird baugruppenorientiert statt taskorientiert.

Die 21 kanonischen Tasks bleiben im Datenmodell erhalten, erscheinen aber nicht mehr jeweils als eigene Seite.

## Grundregel

Jedes Arbeitsblatt beantwortet visuell fünf Fragen:

1. Welches Teil / welche Baugruppe?
2. Was glauben wir momentan?
3. Was ist daran noch unklar oder widersprüchlich?
4. Wo genau messen / fotografieren / scannen?
5. Was muss nach dem Öffnen erneut aufgenommen werden?

Text erklärt nur, was die Zeichnung nicht eindeutig zeigen kann.

## Zielumfang

### A3 Werkstatt- und Aufnahmeplan

Ziel: 8–12 A3-Seiten, nicht 38.

Empfohlene Struktur:

1. Systemübersicht / Orientierung
2. Welle & Arme — vor dem ersten Lösen
3. Welle & Arme — nach dem Öffnen / ausgebaut
4. Kranz & Krümmlinge
5. Kümpfe & Spannringe
6. Schaufeln / Schetter & Nachbarbezüge
7. Lager, Radstatt & stationäres Tragwerk
8. Trog, Rinne, Wasserlinie & Drehrichtung
9. Scan / LiDAR / Photogrammetrie / Splats
10. Teile-ID, Ereignis- und Lagerregister
11. Offene Konflikte / Variantenübersicht
12. Abschlusscheck

### A4 Kurzplan

Maximal 2 Seiten: Einsatzreihenfolge, STOPP-Punkte, Blattverweise und Backup-/Abschlusskontrolle.

## Visuelle Grammatik pro Blatt

### Hauptzeichnung

Mindestens 50–65 % der Seite. Zulässige Ansichten: orthogonal, Exploded, Schnitt, lokale Detailansicht, vereinfachte 3D-Isometrie oder Foto mit technischer Überzeichnung.

### Messpfeile

Jede geforderte Messung erhält M01, M02, ... mit Start- und Endpunkt, Pfeillinie, Einheit/Werkzeug falls wichtig, leerem Feld für Messwert und Konfliktverweis falls vorhanden.

Beispiel: M03  Innenfläche Daube ↔ Außenfläche Daube   ______ mm ± ____

### Fotopositionen

Kamera-Symbole F01, F02, ... mit Blickrichtung als Pfeil, Bildausschnitt und BEFORE/AFTER.

Beispiel: F04 BEFORE — Keilsitz von Seite A; F05 AFTER — freigelegte Partnerflächen gemeinsam.

### Scan-Aufträge

Eigene Symbole: S01 LiDAR/Photogrammetrie, G01 Gaussian Splat, D01 Datum/Referenzmarker. Metrisch, Oberfläche/Kontext und Registrierungsreferenz müssen klar unterschieden werden.

### Konflikte / Annahmen

Direkt an der Geometrie: ? = unbekannt; A/B = konkurrierende Variante; gestrichelte Kontur = Hypothese; schraffierte Zone = innen/unzugänglich; orange Maßlinie = Konflikt/nachmessen; schwarze Maßlinie = normale Aufnahme.

### Minimaler Textblock

Maximal: Warum jetzt? ein Satz; Nicht vergessen 3–5 Punkte; Frage an die Werkstatt 1–3 kurze Fragen.

## Baugruppenblätter

### Welle & Arme — BEFORE

Zeigen: Welle als transparente/geschnittene Arbeitsdarstellung, sechs sichtbare Armenden, Paarung ausdrücklich offen, axial mögliche Ebenen, unbekannte Innenzone.

Markierungen: F01/F02 axial Seite A/B; F03–F06 vier Schrägansichten; M01 axiale Eintrittslage je Arm; D01 Bezugsfläche; Paarung 1/4, 2/5, 3/6 nicht voraussetzen.

STOPP: Vor dem ersten Keilzug alle sichtbaren Eintrittsstellen und Marken erfassen.

### Welle & Arme — AFTER

Zeigen: freigelegte Wellenzone, mögliche Mortisen nur als offene Umriss-/Schraffurzone, ausgebauter Arm als Seiten-/Draufsicht.

Markierungen: M02 Einstecktiefe; M03 Eintritt/Austritt; M04 Kröpfung/Versatz; F07 Kontaktflächen; S01 Einzelteilscan.

### Kranz / Krümmlinge

Zeigen: Kranzsegment, Stoß, beide Ringseiten, radial vs axial klar getrennt.

Markierungen: M10 axiale Breite; M11 radiale Tiefe; M12 Lochabstand; F10/F11 beide Seiten; F12 nach Öffnung beide Partnerflächen. Konflikt 14 cm vs 15 cm nicht vermischen.

### Kümpfe / Spannringe

Zeigen: Kumpf eingebaut, Querschnitt, Daube, Nut, Boden, Spannringe.

Markierungen: M20 Daubendicke; M21 Außen-/Nutdurchmesser; M22 Bodenlage; M23–M25 Ringlängen/Überlappungen. Konflikte 22/24 mm, 244/264 vs 248/268 und 780/875/968 vs 784/880/972.

### Schaufeln

Zeigen: Schaufel zwischen beiden Kränzen, Vorder-/Rückseite, Beziehung zu Kumpf und Krümmling.

Markierungen: F30 eingebaut; F31 Vorder-/Rückseite; M30 Anstellung; M31 Befestigungslage.

### Lager / Radstatt / Tragwerk

Das Rad wird nicht isoliert gezeigt. Ghosted Kontext: Lagerstöcke, Auflager, untere Rahmen, seitliche Auffang-/Führungsrahmen, Holzgestelle, Trog-/Rinnenanschlüsse und weitere stationäre Zubringer.

Noch unbekannte Elemente als CONTEXT-UNKNOWN führen, ghosted statt erfunden, mit eigenen Foto-/Messaufträgen.

### Wasser / Trog / Rinne

Zeigen: Achse, Wasserlinie, Trog, Rinne, Fließrichtung, mögliche Drehrichtung.

Markierungen: M40 Achse–Wasser; M41 Trogöffnung; M42 Trog→Rinne; F40 datierte Wasserlinie.

## Datenmodell

Die bestehenden 21 Tasks bleiben Source of Truth für Logik und Status.

Neu benötigt: visual_sheet_id, callouts[], measurement_guides[], photo_guides[], scan_guides[], conflict_overlays[], hypothesis_overlays[]. Ein Blatt kann viele Tasks bündeln.

PDF, Web Field Mode und Werkstatt beziehen sich auf dieselben visuellen Guides.

## Field Mode Konsequenz

Auch die Web-Feldführung wird visueller: oben große Skizze/Detailansicht; darauf aktive Messlinie oder Kameraposition; darunter nur Jetzt aufnehmen, Messwert, Weiter.

Keine langen Erklärungstexte vor jeder Aktion.

## Abnahmekriterium

Ein erfahrener Monteur soll ein Blatt ansehen und ohne vorherigen Textblock erkennen können: welches Teil gemeint ist, wo er messen soll, aus welcher Richtung ein Foto gebraucht wird, welche Stelle noch unbekannt ist und ob er vor dem Lösen stoppen muss.