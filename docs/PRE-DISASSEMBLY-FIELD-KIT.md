# Pre-Disassembly Field Kit — Specification

Stand: 2026-10-07

## Purpose

Das Field Kit ist ein eigenständiges Arbeitsmittel für die Demontage.

Es muss vollständig funktionieren:
- ohne Web-App,
- ohne Mobilfunk,
- parallel mit mehreren Personen,
- mit Handschuhen / nassen Händen,
- als Papierunterlage in der Werkstatt.

## Output

Bevorzugt A3 quer, schwarz/weiß grundlegend, technische Zeichnungssprache, große Felder für Handschrift.

Zusätzlich ein kompakter A4/A3-Übersichtsplan für die Einsatzleitung.

## Required sections

1. Deckblatt / Auftrag
2. Rollen und Ablauf
3. Orientierungsblatt
4. Referenzpunkte / Datum
5. Vor-dem-ersten-Lösen-Check
6. Welle / Arme P0++
7. Krümmlinge
8. Kümpfe
9. Schaufeln
10. Keile / Befestiger
11. Lager / Zapfen
12. Trog / Rinne / Wasserlinie
13. Scan-/Photogrammetrie-/Splat-Aufträge
14. lokale Begriffe / Handwerkswissen
15. Konfliktblätter
16. reales Teile-/ID-Register
17. Ereignislog
18. Lagerortregister
19. offene Punkte nach Demontage
20. Abschlusskontrolle

## Task card grammar

Jede Aufgabe erhält:

- Task-ID
- betroffene Teil-ID/Familie
- Zeitpunkt:
  - BEFORE_RELEASE
  - DURING_RELEASE
  - AFTER_RELEASE
  - AFTER_REMOVAL
- Warum diese Aufnahme jetzt nötig ist
- genaue Foto-/Messanweisung
- Messendpunkte
- benötigtes Werkzeug
- erwartete Medien
- offene Frage an Monteur
- Akzeptanzkriterium
- Feld für Ergebnis / Dateiname / Bemerkung

## Stop cards

Irreversible Schritte erhalten deutlich:

> STOPP — NOCH NICHT LÖSEN

Darunter die Pflichtaufnahmen.

## Scan guidance

Unterscheiden:
- Geometrie / Maß: Handmaß, LiDAR, Photogrammetrie mit Referenz
- Oberfläche / Kontext: Fotografie / Gaussian Splat
- verdeckte Mechanik: Detailfoto + Maßstab + lokale Detailphotogrammetrie nach Öffnung

Gaussian Splats sind keine Maßreferenz.

## Paper ↔ Web

Web und PDF nutzen dieselben:
- Task-IDs,
- Component IDs,
- Instance IDs,
- Event IDs,
- Statuscodes.

Keine manuell duplizierten Aufgabenlisten.
