# MUX Design Grammar v2 — Story + Werkstatt

Stand: 2026-10-07

## One identity, two densities

Das Projekt verwendet **ein gemeinsames Token-System und eine gemeinsame visuelle Identität**.

### Story / Intro
- großzügiger,
- emotionaler,
- fotografischer,
- Handwerk und Menschen zuerst,
- ausreichend Weißraum.

### Werkstatt / Analyse
- dieselben Farben, Typografie und Akzente,
- deutlich kompakter,
- technische Linien statt großer Karten,
- höhere Informationsdichte,
- Rad/Zeichnung/Foto bekommt die Fläche,
- UI-Chrome bleibt zurückhaltend.

### Feldmodus
- gleiche Identität,
- extrem reduzierte Dichte,
- eine Aufgabe pro Bildschirm,
- große Bedienelemente.

## Shared tokens

Canonical source:
`src/styles/tokens.css`

Core:
- paper: #fafbf7
- warm paper: #f6f4ed
- ink: #172b25
- green: #193e35
- lime: #dbe987
- muted: #5b6962
- line: #d7ddd4
- amber/open question: #a96b1e

## Anti-patterns

Nicht:
- jede Information in eine Karte stecken,
- große dunkle Container als Standard,
- Marketing-Komponenten in der Werkstatt wiederholen,
- enorme vertikale Abstände auf kleinen Screens,
- Forschungsjargon als primäre Navigation.

## Density rule

Story erzählt.

Werkstatt vergleicht und prüft.

Feldmodus führt durch den nächsten Handgriff.

Diese drei Modi dürfen unterschiedliche Dichte haben, müssen aber eindeutig zum selben Produkt gehören.
