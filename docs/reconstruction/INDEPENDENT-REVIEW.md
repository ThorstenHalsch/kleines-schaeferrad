# Unabhängige Abnahme – Rekonstruktion V2

Status: IN ARBEIT. Kein Freigabe-Gate aus diesem Zwischenstand ableiten.

## Erste technische Gegenprüfung

- Registrierung: Identität akzeptiert; um 10 m parallel verschobene Achse abgewiesen; endliche, nicht degenerierte Eingaben erforderlich.
- Wasser: Eine unterhalb der erreichbaren Kumpfbahn liegende Wasserlinie erzeugt kein aufgenommenes Wasser.
- Quellenarchiv: 19 zusätzliche Originaldateien, Duplikatzuordnung und Prüfsummen liegen unverändert im Repository. Der Remote-Quellencommit `e3644d2f6946b676808c3bcb5c3194f5e3ec270d` besitzt denselben Dateibaum wie der lokale Quellencommit `7ba9c8e`.
- IMG_6875 und IMG_6876 sind bislang nur durch die vorhandene Kontextbeschreibung belegt. Originalbilder sind angefragt; kein eigener Bildbefund wird behauptet.

## Visuelle Iteration 1 – elf geometrieabgeleitete SVG-Blätter

Verdict: NOCH NICHT FREIGEGEBEN.

Positiv: gemeinsame Modellgeometrie, orthogonale Ansichten, verdeckte Kanten und echte Geometrieschnitte ersetzen symbolische Radskizzen.

Vor Freigabe zu beheben:

1. KS-11: Innenverbindungen als vergrößerte Detail-/Schnittansichten vergleichen; drei ganze dünne Armprofile zeigen die Innenunterschiede nicht ausreichend.
2. KS-10: Profilfläche besser nutzen; Endzonen, axiale Kröpfung und Kranzkontakt als konkrete Messbezüge zeigen.
3. KS-20: Stoß, Loch-/Stiftkandidat und Radienbezug brauchen ein vergrößertes Detail.
4. KS-40: dünne Vorderansicht der Schaufel durch sinnvolle Flächen-/Anschlussansicht ergänzen.
5. Maßlinien müssen klar definierte Endpunkte, Hilfslinien und echte Vektorpfeile erhalten.
6. Kritische Einbauzustände benötigen reale Fotoüberlagerungen; Projektionen allein ersetzen keinen Fotoabgleich.
7. Alle Blätter nach den Geometriekorrekturen neu erzeugen und das finale PDF seitenweise prüfen.

## Weitere konkrete Gegenprüfungen

- Kumpfmund muss beim Schöpfen und Ausschütten zur funktionalen Wasserbahn passen; eine radial nach außen geöffnete Tonne kann am Scheitel nicht wie gezeigt ausschütten.
- Armenden müssen die jeweilige Kranzebene erreichen. Axialer Mittelversatz darf keinen frei schwebenden Endanschluss erzeugen.
- Lang-/Kurzstifte müssen dem Foto IMG_6822 entsprechen: gekrümmte, zugespitzte Holzschäfte mit verdicktem Astkopf, keine quer angesetzten Balkenköpfe.
- Normale Bauteilauswahl darf keine englischen Rohnotizen oder dekorativen Unicode-Pfeile zeigen.
- Radkörper- und Tragwerksschalter müssen ihre Gruppen unabhängig steuern.

Browser-, Offline- und finale A3-Abnahme folgen nach dem baubaren Implementierungscheckpoint. Ein automatischer Testlauf allein setzt weder TECHNICAL DRAWING QUALITY PASS noch HUMAN UX QUALITY PASS.

## Abschlussprüfung 08.10.2026

Die oben genannten Befunde sind im Implementierungscommit `96132aec62fdb8c4f391b60ce483c3867fe1fc94` bearbeitet. Der abschließende Umfang, die konkreten Korrekturen, Prüfgrenzen und Bildnachweise stehen in `VALIDATION-REPORT.md` sowie `state/reconstruction/quality-review.json`. Der ursprüngliche Zwischenstatus oben ist historisch. Die aktuelle Bildprüfung wurde durch den ausführenden Agenten vorgenommen; sie wird nicht als zusätzliche unabhängige Personenprüfung ausgegeben.
