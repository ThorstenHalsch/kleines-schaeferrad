# UX RECOVERY PLAN REVIEW READY

Stand: 09.10.2026. **Erreicht als Review-Gate, Verdict CONDITIONAL GO.**

Der Auftrag aus `state/NEXT-UX-RECOVERY-WORK-SESSION.md` wurde als unabhängiger Beobachtungs- und Planungsauftrag ausgeführt. Kein produktiver UX-Patch, kein Merge, keine neue Rekonstruktionsiteration.

| Auftrag | Ergebnis |
|---|---|
| Pages vs. main | erfolgreicher main-Deploy `1de62e7` bestätigt; Ressourcen und finale PDFs archiviert/gehasht |
| Desktop/768/390/320, 200 % Text, reduced motion | 21 Matrix-Ansichten, sieben Profile inkl. dark, Chromium 141; echte Geräte ausdrücklich nicht substituiert |
| Modell / Kumpf / Quelle / Hypothese | Browserjourney mit originalem Quellbild, Modell-/Kandidatenwechsel ausgeführt |
| Dringende Aufnahme | versteckter Link als P1 reproduziert, erreichbarer Ausweg über Aufgabenindex getestet |
| Mehrere Maße / Originale / Export / Import / offline | Ein-Messwert-Grenze bestätigt; Originalhash, Wiederaufnahme, Konflikt- und Prüfsummenabwehr geprüft; fehlende Hardware-/Lasttests offen |
| A3/A4 final und Graustufen | 13 finale Pages-PDF-Seiten in beiden Modi visuell geprüft; fünf A3-Unterschiede zu Repo-PDF erklärt; physischer Ausdruck offen |
| Priorisierung | 0 belegte P0, 5 P1, 9 P2; Reproduktion, Bilder, Nutzerwirkung, Minimalfix verknüpft |
| Inkrementeller Plan | R1–R4 ausschließlich P1-Umfang, Datenkompatibilität und konkrete Abnahmekriterien vorgeschlagen |
| Review / Speicherung | Branch und PR #10 behalten; Evidenzen versioniert; keine fachliche oder produktive Freigabe vorweggenommen |

## Einstieg für Reviewer

1. [AUDIT.md](AUDIT.md) — unabhängiges Urteil und Gegenproben.
2. [RECOVERY-PLAN.md](RECOVERY-PLAN.md) — kleinste P1-Pakete und Entscheidungspunkte.
3. [EVIDENCE.md](EVIDENCE.md) — Prüfmatrix, Originaldateien und Reproduktion.

## Offene Gates

- iPhone/Safari, Kamera/Originalformat, echte Touch-/Textgrößeneinstellung und Import auf zweitem Gerät.
- Reale Offline-Rückkehr nach App-/Tab-Neustart, Speicherknappheit und Grenzlast.
- Tatsächlicher A3/A4-Graustufendruck bei Tageslicht.
- Fachliche Sichtung realer Demontageevidenz vor späteren UX-Implementierungen gemäß Arbeitsauftrag.
- Vorhandene ältere Field-workbench-CI-Abnahme ist nicht durch die erfolgreichen Audit-Jobs ersetzt. Ihr initialer PR-Run scheiterte bereits vor unseren Änderungen am lokalen `page.goto`-Timeout.

Die Testläufe sammeln auch negative Beobachtungen. „Workflow success“ ist **keine UX-Gesamtabnahme**. Alle Testmessungen/Teileinträge sind Simulation. Review dieses Plans kann jetzt beginnen; Implementierung nur durch gesonderten Auftrag.
