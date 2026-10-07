# NEXT ASTRA WORK SESSION — Pre-Disassembly Field Kit & UX Refinement

Branch base: `work/pre-disassembly-field-kit-20261007`

## Mission

Bring the current Workbench Alpha from a technically functional research tool to a **pre-disassembly field system** that supports experienced craftspeople, produces a printable technical Field Pack, and preserves unresolved geometry as explicit questions.

Target gate:

**PRE-DISASSEMBLY FIELD KIT READY**

## Mandatory sources

Read first:
- `docs/UX-AUDIT-DRAFT-02.md`
- `docs/TONE-AND-LANGUAGE.md`
- `docs/MUX-DESIGN-GRAMMAR-V2.md`
- `docs/SCAN-REGISTRATION-PLAN.md`
- `docs/ARM-SHAFT-HYPOTHESES.md`
- `docs/PRE-DISASSEMBLY-FIELD-KIT.md`
- `docs/CAPTURE-BEFORE-DISASSEMBLY.md`
- `docs/HANDWERKSWISSEN-CAPTURE.md`
- `docs/DRAWING-LANGUAGE.md`
- `docs/workbench/HUMAN-PLAN.md`
- all current baseline JSON

## Design contract — one identity, three densities

Keep the shared MUX token system in `src/styles/tokens.css`.

- **Story / Intro:** warm, photographic, proud, moderately spacious.
- **Werkstatt / Analysis:** same identity, much denser and more technical; model, photos and drawings get the space, not cards/chrome.
- **Field Mode:** same identity, one task per screen and very large controls.

Do not copy marketing-style Astro cards into the workshop. Do not create a separate unrelated design system.

## Phase A — Human-facing language & aesthetic

Refactor public page and workbench:
- craftspeople-first German copy,
- pride, continuity and shared authorship,
- reduce Research/Claims/Conflict jargon in human UI,
- keep internal schemas unchanged,
- use paper/technical-workbench aesthetic,
- reduce card density and vertical waste,
- let wheel/photos/model dominate.

## Phase B — Orientation & scan correctness

Fix the current scan overlay architecture:
- normalize GLTF Y-up to mechanical Z-up,
- verify handedness,
- show permanent axis triad and orientation legend,
- distinguish RAW_EXPORT / AXIS_NORMALIZED / ROUGH_ALIGNED / REGISTERED / CALIBRATED,
- do not fake mechanical registration,
- store transform as data,
- prepare 3+ fixed field datum markers,
- do not assert LAND/WATER before HUMAN-01.

## Phase C — Arm/shaft hypothesis model

Replace the visually overconfident straight-arm presentation with explicit hypotheses.

Support at least:
- straight/simple placeholder,
- possible bent/dogleg representation,
- axial-layer alternatives,
- visible unknown mortise/interlocking zone.

Do not invent hidden joinery. Generate targeted P0++ field questions from these hypotheses.

## Phase D — Field Mode

Add a separate `/feld/` or explicit Field Mode.

Rules:
- one task per screen,
- very large controls,
- minimal free text,
- next/back,
- visible persistence,
- task completion state,
- supports photo, measurement, explanation and unknown,
- works without research terminology,
- analysis workbench remains separately available.

## Phase E — Shared task model

Create canonical structured task data used by both Web Field Mode and printable Field Pack.

Required fields:
- task_id
- component/family/instance
- timing
- irreversible_loss
- instruction
- photo_views
- measurement_endpoints
- tools
- questions
- media_requirements
- acceptance_evidence
- status

No duplicated handwritten task logic in templates.

## Phase F — Physical instance register

Prepare schema/UI for:
- KS-ARM/KRU/KUM/PAD/KEI IDs,
- historic marks,
- local name,
- installed position,
- partners,
- condition,
- removal event,
- storage location.

Do not pre-create unverified physical instances as facts.

## Phase G — Printable Field Pack

Generate a coherent printable PDF in the established classic technical drawing style.

Target:
- A3 landscape primary format,
- readable by 60–80-year-old workshop users,
- high contrast,
- large writing fields,
- STOP cards before irreversible actions,
- technical sketches where useful,
- conflict comparisons,
- arm/shaft P0++ pages,
- scan/photo instructions,
- craft-knowledge questions,
- event and part registers,
- final completeness checklist.

PDF must be generated from the same task/model data as Web Field Mode.

## Phase H — Offline robustness

Before gate:
- PWA/service-worker offline start,
- verify after one preload,
- test 20–50 photo session,
- storage warning,
- export while offline,
- document browser storage limitations.

Do not build a backend.

## Phase I — Acceptance

Automated:
- desktop
- 320 px
- iPhone emulation
- 200 % text
- offline reload
- task resume
- 20+ photo load
- PDF generation
- no horizontal overflow
- ≥44 px frequent touch controls

Human/manual remaining if unavailable:
- physical current iPhone Safari
- actual target users
- real field daylight/wet-hand test

## Stop conditions

Do not:
- promote hypothesis to current geometry,
- repair scan holes,
- assert LAND/WATER before human confirmation,
- claim Gaussian Splats as metric evidence,
- invent arm/mortise topology,
- build cloud platform/backend.

## Gate

Stop only at:

**PRE-DISASSEMBLY FIELD KIT READY**

Deliver:
- refined public page,
- refined analysis workbench,
- field mode,
- corrected scan coordinate handling,
- arm/shaft hypothesis layer,
- canonical task model,
- printable Field Pack PDF,
- offline evidence,
- validation report,
- remaining human calibration list.
