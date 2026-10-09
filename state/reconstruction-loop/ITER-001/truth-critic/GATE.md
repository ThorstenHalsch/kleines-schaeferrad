# PRE-DISASSEMBLY EVIDENCE READY

Basis: main `e92bebd1201fe49bf2f0f598584cfd2832a48b96` nach PR #7. Datum: 2026-10-09.

**Unabhängiges Audit-Verdict: CONDITIONAL GO für Evidenzvorbereitung und Feldaufnahme.** Kein As-built-, Funktions-, Fertigungs- oder Demontage-Acceptance.

- [Audit mit zehn Befunden und Review aller 16 Renderpaare](AUDIT.md)
- [Priorisierte Aufgaben, Messreferenzen und Thorstens fünf offene Entscheidungen](CAPTURE-PLAN.md)
- [A3-Field-Kit mit fünf Entscheidungsansichten](../../../../output/pdf/KS-Werkstatt-Aufnahmeplan-A3.pdf)
- [Zweiseitige A4-Aufnahmefolge](../../../../output/pdf/KS-Kurzplan-A4.pdf)
- [Maschinenlesbare Prioritäten und Entscheidungen](../../../../data/pre-disassembly-evidence-gate.json)
- [Quellen-/Artefaktprüfung](verification.json), [PDF-Sichtprüfung](pdf-visual-review.json), [Field-Tests](field-tests.log), [Build](build.log), [Astro-Prüfung](astro-check.log)

Die 30 Anhänge sind byteidentisch zu vorhandenen Originalen. Alle 32 Render-Hashes und 16 Kamerapaare wurden geprüft. Zwei Modell-GLBs wurden gelesen; alle bestehenden Modelle, Originale, Kalibrierung, Workbench-Geometrie und Projektionspayloads bleiben unverändert. Keine neue Iteration oder synthetische Geometrie.

Alle 21 bestehenden Aufgaben besitzen Informationsgewinn, Irreversibilität, Demontagekontext-Risiko, Aufwand und Aufnahmefenster. Die digitalen Task-IDs und Arraypositionen wurden beibehalten, um gespeicherte Sitzungen nicht auf andere Aufgaben umzulenken. Die A4-Route hebt Wasser vor Stillsetzen und unmittelbar verlorengehende Verbindungen hervor.

## Offene Einsatzbedingungen

1. Verantwortliches Team legt sichere tatsächliche Freigabe-/Demontagefolge fest.
2. Physisches iPhone/Safari mit Kamera, Export und Wiederimport prüfen. Der gezielte automatisierte Browsercheck konnte mangels lauffähigem Chromium/Download nicht ausgeführt werden; [Status](browser-validation.json). Die vorhandene ältere Browserprüfung wird nicht als Prüfung dieser Revision ausgegeben.
3. Reale P0-Aufnahmen erzeugen und auf zweitem Gerät sichern. Papier und Originalkamera-/Videodateien stehen als Rückfallebene bereit.
4. Thorsten beantwortet D1–D5 am konkreten Teil bzw. Original; jede Antwort bleibt bis dahin UNANSWERED.

## Empfehlung

Als Nächstes **Vor-Ort-Evidenzaufnahme und anschließender Abgleich**. Danach fachlich entscheiden, welche Hypothesen geklärt sind und ob eine neue Rekonstruktionsiteration ausreichend belegt ist. Nicht automatisch ITER-002 beginnen.

Branch zur Review vorlegen; main unverändert lassen; Pull Request nicht mergen.
