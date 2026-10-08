# Schaufelstellung und Kumpfbefestigung — fachlicher Prüfauftrag

Erfasst am 2026-10-08. Fachquelle: ThorstenHalsch. Status: **Fachauskunft und Codebefund dokumentiert; direkte Punktwolkenprüfung noch offen.**

Die Rechenumgebung konnte die binäre Punktwolke ohne zusätzlichen Netzwerkzugriff nicht laden. Der Fachkenner hat anschließend erklärt, dass dieser Zugriff für den jetzigen Stand nicht notwendig ist. Deshalb wird hier keine eigenständig durchgeführte Scanprüfung oder Winkelmessung behauptet.

## Fachliche Korrektur zur Schaufelstellung

Originalaussage:

> Ich habe noch eine zusätzliche Information, die mit den Kumpfen nichts zu tun hat. In deinem Modell, das du erstellt hast, sind die Schaufelbretter parallel zum Radkranz. Die Schaufelbretter stehen aber im 90-Grad-Winkel zum Rad. Überprüfe das anhand einer Punktewolke. Ich hatte ein Schaufelrad explizit gescannt. Daran solltest du das erkennen. Gegebenenfalls kannst du auch schauen, ob du bezüglich der Kumpfbefestigung in der Punktewolke was erkennen kannst und daraus nochmal Insights als Markdown generieren.

Die fachliche Zielvorgabe lautet: **Schaufelbretter stehen im 90-Grad-Winkel zum Rad.** Die vom Fachkenner beanstandete Modellansicht ist als Korrekturhinweis zu behandeln.

Für die spätere geometrische Prüfung muss „zum Rad“ auf einen eindeutigen Bezug abgebildet werden: Rad-/Kranzebene, lokale Umfangstangente oder radiale Richtung. Ebenenwinkel und Drehrichtung innerhalb einer zur Radebene senkrechten Ebene sind unterschiedliche Angaben. Der Hinweis soll nicht durch eine ungeprüfte pauschale 90°-Drehung umgesetzt werden.

## Vorhandene Scanquellen und gesuchter Detailscan

Im durchgesehenen Dateibaum des Forks liegt ein Rohcapture mit zwei Exporten:

- [Scaniverse 2026-10-07 173556.ply](../evidence/raw/Scaniverse%202026-10-07%20173556.ply), SCAN-20261007-01-PLY.
- [Scaniverse 2026-10-07 173556.glb](../evidence/raw/Scaniverse%202026-10-07%20173556.glb), SCAN-20261007-01-GLB.

Das sind zwei Fassungen desselben Captures. Der vom Fachkenner genannte ausdrücklich erstellte Schaufelradscan konnte keiner separaten Datei zugeordnet werden. Der Fachkenner kennt den Dateinamen nicht. Der vorhandene Radscan ist eine mögliche Abgleichsquelle, aber noch nicht als der gemeinte Detailscan bestätigt.

[Scan-Forensik](SCAN-FORENSICS.md) beschreibt bereits lückenhafte Schaufel- und Gefäßoberflächen. Das ist eine frühere Untersuchung, kein neuer Befund dieser Sitzung. Die Exportachsen sind normalisiert, aber der Scan ist laut [scan-transforms.json](../data/scan-transforms.json) nicht mechanisch registriert und nicht metrisch kalibriert.

## Vorläufiger Codebefund zur Modellorientierung

Die aktuelle Datei [geometry.mjs](../src/workbench/geometry.mjs) baut Schaufeln in makeModel mit:

`beam([-p.ringDistance/2-.15,0,-.22],[p.ringDistance/2+.15,0,-.22],.055,.43)`

Die Schaufel wird anschließend um die X-Achse mit der jeweiligen Umfangsphase pa gedreht. Nach der Koordinatenkonvention liegt die Welle auf X und die Kranzebene in YZ.

Aus der Konstruktion lässt sich ablesen: Die Brettlänge verläuft entlang X; die breite Querschnittsrichtung verläuft vor der Umfangsdrehung entlang Y. Die schmale Dicke liegt entlang Z. Die breite Brettfläche spannt deshalb die Achsrichtung und die lokale Umfangstangente auf; ihre Normale ist radial. Als idealisierte Ebene ist diese Brettfläche damit bereits senkrecht zur Kranzebene YZ.

**Das ist eine Codeableitung, keine Widerlegung der fachlichen Beobachtung.** Die im Modell sichtbare Stellung kann dennoch falsch sein, insbesondere hinsichtlich radialer/tangentialer Anstellung, Position und Anschluss. Auch ist noch nicht festgelegt, welche konkrete Modellansicht der Fachkenner beanstandet. Ein reiner Codevergleich klärt die reale Ausführung nicht.

## Fachliche Zusammenhänge zur Kumpfbefestigung

Der [Kumpf-Fachbeitrag](FACHBEITRAG-KUMPF-20261008.md) enthält bereits die direkten Angaben:

- Zwölf Dauben und ein Kumpfboden; Bodenaufnahme in einer Einfräsung; drei Metallbänder.
- Zwei Dauben mit jeweils zwei Löchern für die Kumpfnägel.
- Zwei Kumpfnägel, ein längerer und ein kürzerer, befestigen den Kumpf am Krümmling.
- Benachbarte Kümpfe überlappen; diese Überlappung erfordert die unterschiedlichen Nagellängen.
- Der Fachkenner verweist auf Nagelfotos, eine Nagel-Punktewolke und den Radscan als Dokumentation.

[IMG_6822.jpeg](../evidence/raw/IMG_6822.jpeg) und [IMG_6832.jpeg](../evidence/raw/IMG_6832.jpeg) sind durch den vorhandenen [Quellenabgleich](reconstruction/SOURCE-RECONCILIATION.md) als Bilder der unterschiedlich langen Stifte bzw. eines langen Stifts beschrieben. Die separate Nagel-Punktewolke ist noch nicht eindeutig im Fork identifiziert.

Der wichtige neue funktionale Zusammenhang ist **Überlappung → unterschiedliche erforderliche Nagellängen**. Daraus folgt noch nicht, dass das Lang-/Kurzpaar die Neigung des Kumpfes erzeugt. Die tatsächlichen Nagelwege durch die beschriebenen Löcher und den Krümmling bleiben eine gezielte Prüfaufgabe.

## Späterer Scanabgleich für Astra

1. Scanidentität prüfen und die relevante Schaufel-/Kumpfregion isolieren; Umweltpunkte und stationäres Tragwerk nicht mitfitten.
2. Rad-/Kranzebene und Wellenachse aus erkennbaren Bauteilen bestimmen. Exportachsen allein ersetzen diese Bestimmung nicht.
3. Eine sichtbare Brettfläche segmentieren und eine Ebene fitten. Winkel zwischen Brett- und Radebene über ihre Normalen berechnen: α = arccos(|n Brett · n Rad|). Punktzahl, Auswahlregion und Ebenenresiduen dokumentieren.
4. Zusätzlich radial/tangentiale Anstellung prüfen. Ein 90°-Ebenenwinkel allein entscheidet diese nicht.
5. Benachbarte Kümpfe gemeinsam betrachten: Überlappungsrichtung, Kontaktlage, Krümmlinganschluss und erkennbares Lang-/Kurzpaar zuordnen.
6. Für verdeckte oder im Scan nicht aufgelöste Nagelwege keine Durchtrittsgeometrie erfinden. Fotos und Fachauskunft ergänzend verwenden.
7. Eigenen Bild-/Scanbefund, Fachauskunft und technische Ableitung getrennt protokollieren; geprüfte Projektionen oder markierte Ausschnitte beilegen.

**Noch kein neuer Scanbefund:** weder gemessener Schaufelwinkel noch bestätigte Nagelsitzgeometrie, Nagellängen oder quantitatives Überlappungsmaß. Diese Datei liefert die fachliche Korrektur, den transparenten Codebefund und den konkreten Prüfauftrag für die Fortsetzung.
