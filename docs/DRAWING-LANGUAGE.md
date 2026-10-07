# Zeichnungssprache für das Kleine Schäferrad

Stand: 2026-10-07  
Referenzprojekt: `jdistlr/garden-torch-connector`, klassische Prüfzeichnungen D02/D-V03.

## Zielgruppe

Die technischen Blätter sollen nicht wie moderne Infografiken aussehen, sondern wie vertraute Werkstattunterlagen für Menschen, die seit Jahrzehnten mit Holzbau, Montage und Reparatur arbeiten.

Die moderne GitHub Page und die Werkstattzeichnungen bilden deshalb bewusst **zwei visuelle Sprachen**:

- Website: weich, zugänglich, modern, VZO-Stil.
- Zeichnung: schwarz/weiß, technisch, dicht, papierfähig, konservativ lesbar.

## Darstellungsregeln

Aus dem früheren Projekt übernehmen wir als Leitlinie:

- sichtbare Kanten ungefähr 0,5 mm,
- Maßlinien ungefähr 0,25 mm,
- Achsen und verdeckte Kanten ungefähr 0,18 mm,
- Achsen als Strich-Punkt,
- verdeckte Kanten gestrichelt,
- geschlossene Maßpfeile,
- Millimeter als Standard,
- Ø / R / Winkel explizit,
- Maßhilfslinien sauber getrennt von Bauteilkanten,
- klare Blickrichtung je Ansicht,
- Schnitte mit eindeutiger Schnittbezeichnung,
- Schriftfeld mit Zeichnungsnummer, Revision, Blatt, Maßstab, Datum, Status,
- Stückliste auf Zusammenbauzeichnungen,
- Druckkontrollstrecke auf finalen PDF-Blättern.

## Blattformat

Bevorzugt **A3 quer** für Werkstatt-/Montageblätter. Für große Übersichten des vollständigen Rads können spätere A2/A1-Derivate sinnvoll sein, aber A3 bleibt die transportable Basis.

## Statussprache

Solange reale 2026er Maße fehlen:

> PRÜFZEICHNUNG · NICHT ZUR FERTIGUNG / NICHT MASSHALTIG

Historische Zahlen werden sichtbar als solche markiert, z. B.:

- `HIST. ZEICHNUNG`
- `2026 GEMESSEN`
- `AUS FOTO ABGELEITET`
- `UNGEKLÄRT`
- `MONTEUR-AUSSAGE`

Nie soll eine Zahl allein durch ihre Position auf einem technischen Blatt wie eine bestätigte Fertigungsdimension wirken.

## Geplante Zeichnungssätze

Nach Human Calibration und Feldmessung:

1. **KS-00 Systemübersicht**
   - Gesamtansicht,
   - Land-/Wasserseite,
   - Referenzsystem,
   - Hauptbaugruppen.

2. **KS-10 Welle / Armzonen**
   - Welle,
   - Mortisen,
   - durchgehende Armhölzer,
   - Keile,
   - Lagerzapfen.

3. **KS-20 Kränze / Krümmlinge**
   - Segmentierung,
   - Stöße,
   - Lochbilder,
   - Kranzebenenabstand.

4. **KS-30 Kümpfe**
   - Dauben,
   - Boden,
   - Spannringe,
   - Aufhängung,
   - Varianten.

5. **KS-40 Schaufeln**
   - Geometrie,
   - Anstellwinkel,
   - Befestigung,
   - Umfangsphase.

6. **KS-50 Radstatt / Lager / Trog / Rinne**
   - stationäre Bezüge,
   - Achshöhen,
   - Wasserlinie,
   - funktionale Lage.

7. **KS-60 Zusammenbau**
   - Explosions-/Montageübersicht,
   - Stückliste,
   - Teil-IDs,
   - Einbaureihenfolge.

8. **KS-70 Demontage-/Prüfblätter**
   - reale Ereignisfolge,
   - Kontaktflächen,
   - Messstellen,
   - Prüfpunkte.

## Nicht behauptete Normkonformität

Der Stil orientiert sich an klassischer europäischer/DIN-naher Zeichenpraxis der 1970er/1980er Jahre, wie sie der Zielgruppe vertraut ist. Ohne vollständige Prüfung historischer Normausgaben wird **keine formale Normkonformität** behauptet.

## Astra-Grenze

Die Blattvorlage und visuelle Grammatik werden in der Page vorbereitet. Maßhaltige Projektionen, Schnitte, CAD-Geometrie, Exploded Views und generierte PDF-Zeichnungssätze gehören ausdrücklich in die spätere Astra-Work-Session.
