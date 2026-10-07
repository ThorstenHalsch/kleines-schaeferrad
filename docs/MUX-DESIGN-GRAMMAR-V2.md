# MUX Design Grammar v3 — Story, Werkstatt, Vor Ort

Stand: 2026-10-07  
Referenz: `https://thorstenhalsch.github.io/Webpage-preview/`

## Source stylekit

Die visuelle Identität orientiert sich bewusst am ursprünglichen Referenzprojekt.

Canonical Tokens:
- Papier: `#fafbf7`
- Weiß: `#ffffff`
- Ink: `#172b25`
- Muted: `#5b6962`
- Tiefes Grün: `#193e35`
- Hover-Grün: `#285749`
- Lime: `#dbe987`
- Soft: `#edf1e7`
- Linie: `#dce2d9`
- Schrift: **Manrope Variable**
- Story-Radius: **24 px**

Canonical source in this repository:
`src/styles/tokens.css`

## Was wir übernehmen

- Manrope und die typografische Hierarchie.
- Warmes Papier statt klinischem Weiß.
- Dunkles Ink für technische Lesbarkeit.
- Tiefes Grün als Identitätsfarbe.
- Lime nur als kleiner positiver Akzent.
- Ruhige feine Linien.
- Weiche Story-Radien.
- Hochwertige Foto-/Text-Hierarchie.

## Was wir ausdrücklich nicht übernehmen

Die Referenzseite ist eine Kommunikations-/Vereinsseite. Unsere Werkstatt ist ein Arbeitsinstrument.

Deshalb **nicht** übernehmen:
- großvolumige Marketingkarten,
- riesige Callout-Flächen,
- große grüne Vollflächen,
- dekorative Badges in der Werkstatt,
- großzügige Abstände, die technische Nutzfläche vernichten,
- Card-Grid als Standardantwort auf jede Information.

## Eine Identität, drei Dichten

### 1. Startseite

Ruhig, fotografisch, stolz.

- 24px Story-Radien erlaubt.
- etwas mehr Weißraum.
- Grün als Akzent.
- maximal fünf inhaltliche Bewegungen.
- genau drei klare Arbeitswege: Arbeitsplan, Vor Ort, Werkstattmodell.

### 2. Werkstatt

Technisch und kompakt.

- 6–8px Radien.
- Linien und Gruppierung statt Karten.
- 3D-Modell ist die Hauptfläche.
- Einstellungen progressiv aufklappen.
- Quellen und Details erst nach Auswahl.
- kein dekoratives Grün.

### 3. Vor Ort

Visuell geführt.

- eine Baugruppe / ein Schritt.
- Skizze zuerst.
- Messlinie oder Fotostandpunkt hervorgehoben.
- Eingabe danach.
- große Touch-Ziele.
- keine Projektterminologie.

## Farbnutzung

### Grün
Erlaubt:
- Logo/Brand,
- primäre Aktion,
- Fotopositionen / Registrierpunkte,
- kleine Links/Statusakzente.

Nicht:
- ganze Seitenbereiche,
- mehrere große Panels nebeneinander,
- dauerhafte technische Hintergrundflächen.

### Lime
Nur:
- kleine Badge-/Highlight-Akzente,
- niemals als technische Statuswahrheit.

### Ocker
Reserviert für:
- offene Messpunkte,
- Konflikte,
- Unbekannt / nachmessen.

## Grundsatz

**Stylekit = Grammatik. Nicht Komponentenbibliothek.**

Die Oberfläche soll eindeutig zur Referenzfamilie gehören, ohne deren Marketingkomponenten auf ein technisches Werkzeug zu übertragen.
