# ASTRA BRUTE-FORCE RECONSTRUCTION — Mission Contract

Stand: 2026-10-07

## Ziel

Nach Eingang der zusätzlichen Wasser-/Rahmenfotos soll Astra die maximal mögliche Rekonstruktionsstufe versuchen:

ein vollständiges, räumlich und funktional plausibles 3D-System des Kleinen Schäferrads an seinem realen Standort an der Regnitz.

Das Ergebnis darf bewusst über die gesicherte Evidenz hinausgehen, muss diese Überschreitung aber sichtbar markieren.

## Zwei Wahrheiten parallel

### EVIDENCE MODEL
Nur direkt belegte / gemessene / beobachtete Geometrie.

### BRUTE-FORCE SYNTHETIC MODEL
Bestmögliche technische Rekonstruktion fehlender Verbindungen, Rahmen, Stifte, Keile, Mortisen, Auflager und Funktionsbeziehungen aus:
- vorhandenen Fotos
- historischen Zeichnungen
- Punktwolke / GLB
- neuen Wasser-/Rahmenfotos
- Feldforschung zu fränkischen/regnitztypischen Schöpfrädern
- konstruktiver Plausibilität
- Holzbau-/Zimmermannslogik
- Montage-/Demontagezwängen
- Hydrodynamik und Lastpfaden.

Kein synthetischer Teil darf später versehentlich als gemessen ausgegeben werden.

## Astra darf im Brute-Force-Modus

- verdeckte Verbindungen als Kandidaten modellieren,
- mehrere Mortisen-/Keil-/Verstiftungsvarianten automatisch erzeugen,
- Varianten nach Kollisionsfreiheit, Montagefähigkeit, Lastpfad und Quellenkompatibilität ranken,
- fehlende Rahmenkonstruktionen aus Bild-/Scanbeziehungen ergänzen,
- stationäre Tragwerke ghosted/semisolid modellieren,
- Wasser, Ufer und Strömungsrichtung als Standortmodell integrieren,
- plausible historische Reparatur-/Ersatzvarianten modellieren,
- mehrere Zustände vergleichen: eingebaut / demontiert / Exploded / Arbeitsannahme.

## Externe Feldforschung

Vor der finalen Geometriesynthese gezielt recherchieren:
- historische Schöpfräder an der Regnitz und in Möhrendorf/Oberndorf,
- typische Konstruktion der Radstatt, Lagerstöcke, Trog-/Rinnenanschlüsse,
- Arm-/Wellenverbindungen traditioneller Holz-Schöpfräder,
- Keile, Holznägel, Zapfen/Mortisen, Ringsegmente,
- Wasserführung und funktionale Geometrie,
- bekannte Maße/Proportionen verwandter Räder,
- lokale Terminologie und Baupraxis.

## Standortmodell

Rekonstruiere nicht nur den Radkörper.

Zielumfang:
- Regnitz-Ufer / Wasserkörper
- reale Radposition
- Himmelsrichtungen
- Fließrichtung
- Land-/Wasserseite
- Radstatt
- Lagerstöcke / Lagerbalken
- untere Rahmen und Halter
- seitliche Führungs-/Auffangrahmen
- Trog
- Rinne
- Zubringer / weitere Holzgestelle
- Wasserlinie
- plausible Drehrichtung
- Kontakt des Rades mit Wasser.

## Geometrische Suchstrategie

Für unsichere Baugruppen nicht eine Form raten, sondern Variantenraum erzeugen.

Beispiel Welle/Arme:
- gerade Arme
- gekröpfte Arme
- unterschiedliche axiale Ebenen
- versetzte Mortisen
- überkreuzte / ineinandergreifende Innengeometrie
- Keil-/Holznagel-Kandidaten.

Bewertung je Variante:
- passt zu sichtbaren Eintrittspunkten?
- kollisionsfrei?
- montierbar / demontierbar?
- plausibler Kraftfluss?
- vereinbar mit historischen Skizzen?
- vereinbar mit Scan/Fotos?
- minimale Zusatzannahmen?

## Visuelle Kennzeichnung

Verified / measured: solid.
Observed: solid mit Quellenhinweis.
Historical-only: technische Kontur.
Synthetic-plausible: halbtransparent / amber outline.
Alternative candidate: umschaltbare Variante.
Unknown: bewusst offen.

## Ausgabe

Maximale Zielausgabe:
- vollständige Three.js-Szene,
- Master-GLB/GLTF,
- hierarchische Component-/Instance-Struktur,
- stationärer Standortkontext,
- Wasser-/Strömungsszene,
- Exploded View,
- Demontage-/Montagezustände,
- Schnittansichten,
- Kandidatenvarianten für verdeckte Verbindungen,
- technische Zeichnungen aus Modell,
- Field-Pack-V2-Skizzen direkt aus derselben Geometrie,
- Provenance/Confidence Layer.

## Gate

BRUTE-FORCE FUNCTIONAL RECONSTRUCTION READY

Dieses Gate bedeutet:
- vollständiges funktionales Systemmodell vorhanden,
- alle großen Rahmen-/Tragwerkskomponenten enthalten oder explizit unbekannt,
- Standort und Wasserfunktion räumlich nachvollziehbar,
- unsichere Verbindungen als Kandidaten sichtbar,
- nichts synthetisch Ergänztes als gemessen ausgegeben.