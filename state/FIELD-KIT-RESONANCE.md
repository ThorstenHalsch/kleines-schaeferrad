# Field Kit Resonance — Integration Review

Stand: 2026-10-07  
Reviewed head before integration polish: `949fc6725ed0c780bbb215c9e80e9ccd8e255093`

## Verdict

**PRE-DISASSEMBLY FIELD KIT READY — accepted for integration.**

The gate is deserved as an operational pre-disassembly kit, not as a finished reconstruction.

What changed fundamentally:
- the project now has a real field-facing mode, not only an analysis workbench;
- Web and paper are driven from the same 21-task model;
- scan coordinate handling now distinguishes axis normalization from registration;
- arm/shaft uncertainty is rendered as competing hypotheses rather than hidden geometry;
- a real physical instance register can be built during disassembly without pre-invented parts;
- offline use and lossless media backup have executable evidence;
- the printable Field Pack is now an operational artifact rather than future documentation.

## Strongest results

### 1. Canonical Bill of Tasks

`data/field-tasks.json` contains 21 tasks:
- 10 BEFORE_RELEASE
- 4 DURING_RELEASE
- 3 AFTER_RELEASE
- 4 AFTER_REMOVAL
- 4 P0++ arm/shaft tasks
- 10 explicit stop-before-release tasks

The sequencing is based on irreversible information loss rather than on a guessed dismantling method.

### 2. Arm / shaft uncertainty is treated correctly

The viewer and PDF offer:
- open/unknown form,
- straight placeholder,
- possible dogleg,
- staggered/coplanar/reversed axial-layer alternatives,
- explicit unknown interior zones.

No mortise or hidden interlock has been invented.

### 3. Scan handling is epistemically safer

The GLB now has a documented right-handed Rx(+90°) Y-up→Z-up normalization.

States are separated:
- RAW_EXPORT
- AXIS_NORMALIZED
- ROUGH_ALIGNED
- MECHANICALLY_REGISTERED
- METRICALLY_CALIBRATED

Mechanical transform, field scale and human side confirmation remain null. The workbench uses a separate scan view so an unregistered fragment no longer visually claims coincidence with the mechanical model.

### 4. Field Mode is materially useful

`/feld/` implements:
- one task at a time,
- photo views,
- measurement endpoints/tool/uncertainty,
- verbatim craft explanation separated from interpretation,
- explicit unknown/blocked state,
- resume,
- physical instance/event capture,
- backup/import.

A blocked task does not silently become completed.

### 5. Offline / data-loss posture is credible for an alpha field kit

Automated acceptance demonstrated:
- 28 photos,
- 20,460,272 original bytes,
- SHA-256 verification,
- offline restart,
- fresh-context offline import,
- IndexedDB persistence.

This remains browser-local and is correctly documented as non-guaranteed storage; regular external export is mandatory.

### 6. Printable working set exists

`KS-Field-Pack-A3.pdf`:
- 38 A3 landscape pages,
- 21 task sheets,
- stop cards,
- arm/shaft hypothesis sheets,
- conflict comparison sheets,
- instance/event/storage/open-point registers,
- final completeness check.

`KS-Einsatzleitung-A4.pdf` provides the compact 21-task running order.

The rendered PDF was reviewed during integration. The drawing language is clear, writable, high-contrast and appropriately non-decorative.

## Integration polish performed after Astra handoff

Two non-architectural UX defects were fixed before merge:
1. mobile Field Mode navigation no longer floats over and obscures task text;
2. internal component-family codes no longer appear as the primary human-facing family label in Field Mode.

## Remaining human gates

The project is **not FIELD-VALIDATED** yet.

Still mandatory:
- physical current iPhone / Safari preload → flight mode → real camera → restart → export/import;
- actual 60–80-year-old target-user review;
- daylight / wet hand / possible glove handling;
- HUMAN-01 side A/B → LAND/WATER + flow + rotation confirmation;
- DATUM-A/B/C and axis-marker placement and measurement;
- real arm profiles/end pairing/axial order/interior geometry;
- real field records and physical instance IDs.

## Non-blocking refinements after first real use

- The 38-page A3 pack is intentionally comprehensive; the A4 leader sheet should be the primary running index.
- The PDF header still uses “FIELD PACK”; a later wording polish to “Werkstatt- und Aufnahmeplan” is desirable but not a release blocker.
- The Story page remains deliberately more spacious than Workshop/Field; real user feedback should decide whether further compression is needed.
- Lazy-loaded story imagery should be visually rechecked in live Pages after deployment; CI full-page screenshots may not force all offscreen lazy images to load.

## Next truth-changing event

The next major project advance must come from **real disassembly evidence and human calibration**, not another round of inferred geometry.

After field capture:
1. ingest exports and original media;
2. validate identities, measurements and provenance;
3. register scans to measured datums;
4. promote only supported values from hypothesis to current-as-built;
5. start the next high-fidelity reconstruction session.
