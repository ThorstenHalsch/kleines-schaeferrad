# Capture before Disassembly

**Zeitkritisch.** Ziel ist nicht maximale Datenmenge, sondern die Informationen zu retten, die nach der Zerlegung nicht mehr beobachtbar sind.

## P0 — unbedingt vor der Zerlegung

### 1. Globale Geometrie
- Außendurchmesser des Rads an mindestens zwei Achsen.
- Innendurchmesser/Radkranz-Innenkante.
- Abstand der beiden Radkranzebenen.
- gesamte axiale Breite.
- Mittelpunkt/Achshöhe über einem festen Referenzpunkt.
- Wasserlinie relativ zur Achse.
- mindestens zwei lange Referenzstrecken sichtbar in Fotos/Scans.

### 2. Welle / Nabe / Arme
- 360°-Fotoring um beide Wellenenden und jede Armgruppe.
- Nahaufnahmen jedes unterschiedlichen Zapfen-/Keil-/Mortisentypus.
- Breite/Höhe/Dicke der Arme direkt an der Welle und am Kranz.
- Eintrittswinkel und Lage der Arme markieren.
- Wellenquerschnitt und sichtbare Bearbeitungsspuren.

### 3. Krümmlinge / Radkränze
- jeder Stoßtyp frontal + seitlich.
- Segmentlänge, Breite, Dicke.
- Verbindung Arm ↔ Krümmling.
- Lochbilder, Nägel, Keile, Bänder und Reparaturstellen.

### 4. Kümpfe / Schöpfgefäße
- mindestens einen vollständig sichtbaren Kumpf aus mehreren Richtungen.
- Öffnungsmaße, Tiefe, Wandstärken.
- Anstellwinkel zum Kranz.
- Überlappung benachbarter Kümpfe.
- Befestigung auf Innen- und Außenseite.
- Abstand/Teilung um den Umfang.

### 5. Schaufeln / strömungswirksame Teile
- Länge, Breite, Dicke und Anstellwinkel.
- Befestigung am Rad.
- Teilung und Beziehung zu Armen/Kümpfen.

### 6. Radstatt / Lager / Trog
- beide Lagerpunkte und ihre Bezugslage zur Welle.
- tragende Hölzer mit Querschnitten.
- Gießtrog/Auffangrinne relativ zum oberen Scheitel.
- Flussrichtung, Land-/Wasserseite eindeutig dokumentieren.

## P0 — während der Zerlegung

Das ist wahrscheinlich die wertvollste Phase des gesamten Projekts.

Für **jedes entfernte Bauteil**:
1. vor dem Lösen fotografieren,
2. physische temporäre ID vergeben,
3. Orientierung markieren: Land/Wasser, links/rechts, oben/unten,
4. direkt nach Ausbau Vorder-/Rückseite fotografieren,
5. Verbindungspartner und Kontaktflächen fotografieren,
6. relevante Maße nehmen,
7. repräsentative bzw. einzigartige Teile einzeln scannen,
8. Demontagereihenfolge protokollieren.

Empfohlenes Schema:
`KS-<component>-<running-number>`

Beispiel: `KS-KRU-03`, `KS-ARM-07`, `KS-KUM-12`.

## Scan-Regeln

- Schlechte Scans **nicht löschen**.
- Teilscans getrennt behalten.
- PLY + GLB vom selben Scan als Paar sichern.
- keine automatische Bereinigung vor Raw-Ingest.
- Maßstab immer durch reale Referenzstrecke absichern.
- glänzendes Wasser und bewegte Vegetation nicht als Geometrie interpretieren.
- bei Einzelteilen möglichst 360° + Ober-/Unterseite, gleichmäßige Belichtung, viel Überlappung.

## Sehr sinnvoll

Nicht-invasive ArUco/AprilTag-Karten oder deutlich vermessene Maßstäbe **neben** den Bauteilen platzieren. Nichts auf historische Oberflächen kleben, wenn dadurch Material gefährdet wird.
