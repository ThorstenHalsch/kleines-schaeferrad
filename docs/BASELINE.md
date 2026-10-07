# Pre-Disassembly Baseline

Stand: 2026-10-07  
Status: **IN ARBEIT — noch nicht PRE-DISASSEMBLY BASELINE READY**

## Identität und Ort

Objekt: **Kleines Schäferrad**, eines der Möhrendorfer Wasserschöpfräder an der Regnitz, bei Oberndorf/Möhrendorf. Öffentliche Quellen führen es als Rad Nr. 7, linkes Regnitzufer, etwa Fluss-km 41,20, mit 24 Kümpfen. Die Patenschaft liegt beim Verein Zufriedenheit Oberndorf.

Öffentliche Kontextquellen:
- https://www.moehrendorf.de/ortsinfo-freizeit-vereine/sehenswertes-historie/wasserschoepfraeder
- https://www.verein-zufriedenheit.com/wasserrad.html

Diese Angaben dienen der Objektidentifikation, nicht als geometrische Ground Truth.

## Forschungsziel

Vor der unmittelbar bevorstehenden Demontage soll erstmals eine digitale Rekonstruktionsbasis entstehen, die später erlaubt:

- das Rad als Ganzes im Wasser zu zeigen,
- jedes konstruktive Segment einzeln zu untersuchen,
- den Montagezusammenhang nachvollziehbar zu machen,
- historische Zeichnungen mit dem tatsächlichen Bestand zu vergleichen,
- reale Oberflächen über Scans/Photogrammetrie zu erhalten,
- Rekonstruktionsannahmen von gemessener Geometrie zu unterscheiden.

## Bereits vorhandene Evidenz

### Zeichnungen / Überlieferung
30 aktuelle Fotoaufnahmen liegen vor. Der Großteil dokumentiert historische bzw. handwerkliche Zeichnungen und Notizen:
- Welle/Achse und Querschnitte,
- Reihenfolge von Armen und Krümmlingen auf Land- und Wasserseite,
- Stück-/Befestigerlisten,
- empfohlene Holzmaße und Holzarten,
- Kumpf-/Spannring-/Streifen-Details,
- Radkranz-, Arm- und Einbaugeometrie,
- Montage- und Maßnotizen.

### Aktueller Bestand
Sechs Fotos zeigen den eingebauten Zustand:
- Nabe/Welle und eingesetzte Arme,
- Seitenansichten des vollständigen Rades,
- Innenansichten mit Radkranz, Armen und Einbausituation,
- Wasser- und Traggerüstkontext.

### 3D
Ein Scaniverse-Capture ist als:
- PLY Farbpunktewolke: 75.619 Punkte,
- GLB Mesh: ca. 56.117 Vertices / 78.043 Faces,

vorhanden.

Die PLY-Bounding-Box ist etwa 6,03 × 7,03 × 4,50 m. Der Capture enthält Radteile **plus deutliche Fremdgeometrie** (Umgebung, Vegetation, Traggerüst, Wasser-/Scanartefakte). Er wird daher als forensische Teilquelle behandelt, nicht als fertiges Modell.

## Vorläufige konstruktive Hypothesen

Aus Zeichnungen und Fotos ist bereits belastbar genug, um eine Bauteiltaxonomie aufzubauen:
- Welle/Achse,
- zwei radiale Kranzebenen,
- Arme/Speichen,
- Krümmlinge als segmentierte Radkränze,
- Kümpfe/Schöpfgefäße und ihre Befestigungen,
- Schaufeln/Paddel bzw. strömungswirksame Holzteile,
- Metall-/Holzbefestiger, Keile, Spannringe/Streifen,
- Lager-/Traggerüst,
- Auffang-/Gießtrog und Wasserführung.

Die genaue Gleichsetzung historischer Begriffe mit allen heute sichtbaren Bauteilen ist noch Gegenstand der Forensik.

## Vorläufige Maße

In den dokumentierten Radkranzzeichnungen sind Maße um **Ø 4,26 m** und **Ø 3,96 m** erkennbar. Diese werden derzeit ausschließlich als **Zeichnungsevidenz** geführt. Sie werden erst nach Gegenprüfung mit Handmaß und/oder registrierter Punktwolke als Ist-Geometrie übernommen.

## Größte offene Risiken

1. Ringebenenabstand und axiale Gesamtbreite.
2. Exakte Wellen-/Naben-Mortisen und Keil-/Zapfenlogik.
3. Geometrie und Orientierung der Arme an Welle und Kranz.
4. Krümmling-Stöße und Befestigung zu den Armen.
5. Exakte Kumpfgeometrie, Überlappung, Anstellwinkel und Befestigung.
6. Schaufelgeometrie und Teilung.
7. Lagerpunkte und Radachse relativ zur Radstatt.
8. Wasserlinie und funktionale Lage im Fluss.
9. Unterschiede zwischen historischen Zeichnungen und aktuellem Reparaturzustand.
10. Teile, die erst während der Zerlegung sichtbar werden.

Der Feldplan in `CAPTURE-BEFORE-DISASSEMBLY.md` ist deshalb Teil der Baseline und nicht optional.
