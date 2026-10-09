# UX Recovery Audit — 2026-10-09

Scope: static code / IA audit, NOT a completed visual-browser or physical Safari audit. Source: main after PR #9. No model changes.

## Findings (independent review targets)
- UX-01 P1: Workshop shows model-mode, overlap direction, synthetic jet speed and paddle pitch alongside scene navigation before the user selects a task. This exposes engineering configuration before intent. Preserve all controls but move advanced candidate settings behind explicit Investigate mode.
- UX-02 P1: Field landing displays text instructions and a phase track but the time-critical 'before shutdown' capture is one link among other controls. Add a dedicated entry decision by capture window, especially before shutdown / before release / immediately after / before departure.
- UX-03 P1: Field form currently offers one measurement field per task; additional values rely on photographed sheets. Design a backward-compatible multi-measurement structure, each with endpoints, units, tool, uncertainty, original media ID.
- UX-04 P1: Partner identity and before/after event provenance must be mandatory at critical connection steps, not buried in narrative.
- UX-05 P1: Printed synthetic model plates are dark; print-only brightness compensation was committed, but rebuilt final PDF pixels have not been independently inspected. Audit print legibility on A4/A3 in grayscale and daylight.
- UX-06 P1: Physical iPhone/Safari camera, storage, export/import and offline return path must be checked on actual hardware before field use. Browser automation does not prove this.
- UX-07 P2: Workshop has many dense technical terms, while Human UX contract mandates German human language and one primary question per surface. Make Discover / Investigate / Document entry paths without duplicating apps.
- UX-08 P2: Workbench and Field navigation need route and back-state review at 320px, 200% text, keyboard, reduced motion, touch targets and no overflow.
- UX-09 P2: Current GLB visualizations are not a manufacturing CAD master. Label export status and prevent implied '100% accurate' claims.
- UX-10 P2: Review/gallery of 32 canonical renders lives under output, not necessarily published static Pages. Make explicit discoverable review route only after asset size/offline budget checks.

## Evidence / severity
All findings above are hypotheses grounded in code structure and previous audit documents. Do not claim a live screenshot was visually inspected in this audit. Actual severity must be verified with screenshots and interaction traces.

## Acceptance plan
1. Screenshot matrix: desktop 1440, tablet 768, phone 390 and 320, 200% text; light/dark system, long labels.
2. Journeys: visitor opens wheel and selects Kumpf; expert compares Truth/Brute; field operator opens urgent pre-shutdown task, captures media and two measurements, resumes, exports/imports on second device.
3. Check no lost IndexedDB data, stable task IDs, existing source authority labels, PDF links, and offline cache budget.
4. Review print proof: original photo unchanged; brightened synthetic image legible in grayscale; status visibly synthetic.
5. Produce severity, reproduction steps, screenshot evidence, and prioritized minimal fixes. No untested green status.

## Sequencing
Until demolition capture is secured: avoid risky field UI changes. After evidence intake: small UX PRs, beginning with mode separation and capture-window navigation. Preserve existing MUX tokens, human-language contract and three density levels.
