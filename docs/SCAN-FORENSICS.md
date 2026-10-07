# Scan-Forensik

Beide unveränderten Exporte wurden binär geparst, einzeln projiziert und visuell beurteilt. Skript: `scripts/audit_scans.py` (NumPy, Matplotlib, Pillow), Statistik `evidence/derived/scan-audit.json`.

| Merkmal | PLY | GLB |
|---|---|---|
| Koordinaten/Vertices | 75.619 | 56.117 |
| Dreiecke | keine | 78.043 |
| Bounds XYZ, Exporteinheiten | 6,02969 × 7,03438 × 4,50313 | 5,41553 × 4,60182 × 6,80901 |
| Auffälligkeit | 1.214 wiederholte Positionsdatensätze | 30.775 Randkanten, 0 nichtmannigfaltige Kanten, 0 exakt flächenlose Dreiecke |
| Inhalt | Float XYZ, RGB, Little Endian | Position, UV, ein eingebettetes JPEG, untransformierte Nodes |

PLY-Header und Payload passen exakt zusammen; alle Koordinaten sind endlich. GLB-Header/Dateilänge, Indexbereich und Accessor-Bounds stimmen. Die Randkantenstatistik zeigt ein offenes Mesh; sie ist kein Qualitätsbeweis für lokale Detailtreue. PLY enthält weder Normalen noch Unsicherheiten, Bauteil-IDs oder physische Maßeinheiten im Header.

Orthographisch sind Kranzbögen, Wellen-/Armumfeld, einzelne Schaufelfragmente und Radstatt erkennbar. Bankvegetation, Boden-/Gerüstkontext und isolierte Fragmente gehören ebenfalls zum Capture. Oberer/unterer Kranz ist abschnittsweise unterbrochen, schmale Hölzer und Gefäßoberflächen sind lückenhaft. Die Fotos zeigen Details, die der Scan nicht trägt. Reflexion, Bewegung, Verdeckung und Rekonstruktionsverfahren sind mögliche Ursachen, kein im Einzelpunkt belegtes Ursachenlabel.

Vorläufige **semantische Regionen**, keine exakte Segmentierung: (1) Radkranz-/Armbögen, (2) Achs-/Nabenbereiche, (3) Pfosten/Querträger/Trog, (4) grüne Uferflächen, (5) isolierte Fragmente. Farben allein trennen kein Moos am Rad von Vegetation. Deshalb keine unbelegte Prozentzahl brauchbarer Punkte, kein automatisches Entfernen und kein Durchmesser-Fit aus gemischten Punkten.

Der Achsenkandidat Xg=Xp,Yg=Zp,Zg=−Yp erreicht 94,95 % PLY-Punkte innerhalb 0,05 Exporteinheiten zu einem GLB-Vertex; die spiegelnde Variante erreicht nur 16,73 %. NN-Abstände vergleichen Vertices, keine Flächen; sie sichern weder Messgenauigkeit noch exakte Punktkorrespondenz. Unterschiedliche Bounds bleiben als Export-/Oberflächendifferenz dokumentiert.

**Tatsächlich nutzbar:** grobe sichtbare Lage-/Formhinweise und spätere Registrierungskandidaten. **Nicht nutzbar ohne neue Evidenz:** vollständige Ist-Abmessungen, Mortisentiefen, Kranzabstände, verdeckte Verbindungen, geschlossene Gefäßinnenräume, Wasserstand oder vollständige Inventarzählung. Die Größe der Gesamt-Bounding-Box ist nicht der Raddurchmesser. Keine Mesh-Reparatur, Lochfüllung oder Geometrieableitung durchgeführt.
