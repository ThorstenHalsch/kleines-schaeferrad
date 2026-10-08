# NEXT ASTRA WORK SESSION — Recovery + Brute-Force Functional Reconstruction V2

Branch: `work/bruteforce-functional-reconstruction-v2-20261008`
Base: deployed `main` at `5cc016325f8bf8a5da88edf7c3719937636c1f34`

Status: **COMPLETED — BRUTE-FORCE FUNCTIONAL RECONSTRUCTION READY**

Abschluss: `state/reconstruction/GATE.md` und `docs/reconstruction/VALIDATION-REPORT.md`. Geprüfter Implementierungscommit: `96132aec62fdb8c4f391b60ce483c3867fe1fc94`. GitHub-Push durch automatische Freigabeprüfung blockiert; keine Veröffentlichung ausgeführt.

## Why this is a rebuild, not a patch

The current deployed product is a functional evidence/workflow prototype, but it has failed the intended quality bar in three coupled ways:

1. **Geometry:** too many primitive approximation meshes; current photos and historical drawings are not yet reconstructed into a convincing machine.
2. **UX:** visual hierarchy, language, color, scan comparison and navigation are still inconsistent and sometimes worse after incremental patches.
3. **Field drawings:** current schematic sketches are too trivial to guide real dismantling work.

Astra must therefore treat the current presentation geometry and current visual composition as **disposable implementation**, while preserving validated data, provenance, offline capture semantics and evidence contracts.

Do **not** optimize the existing primitive meshes or beautify the existing schematic drawings. Reconstruct the system coherently.

---

# Mission

Build the strongest technically plausible, evidence-traceable reconstruction currently possible of the **complete Kleines Schäferrad system at the Regnitz**, then rebuild the human experience around that reconstruction.

Target gate:

# **BRUTE-FORCE FUNCTIONAL RECONSTRUCTION READY**

The result should make it possible to understand:
- what the machine is,
- how the parts relate,
- how it is supported,
- how it rotates,
- how water is captured and handed to the trough/rinne,
- what is known,
- what is historically documented,
- what is technically reconstructed,
- and what Saturday's dismantling still must decide.

---

# Mandatory source hierarchy

Read and reconcile before implementation:

## Current multi-evidence baseline
- all `evidence/raw/` photographs and scans,
- current PLY and GLB,
- historical drawings and notes,
- all `data/*.json` geometry/claims/components/relations/conflicts,
- `docs/NEW-EVIDENCE-20261008.md`,
- `docs/CONTEXT-EVIDENCE-6875-6876.md`,
- `data/arm-hypotheses.json`,
- `data/kumpf-fastener-hypotheses.json`,
- `data/scan-transforms.json`,
- `docs/SAMSTAG-ABBAU-AUFNAHMEPLAN.md`,
- `docs/PHOTO-CAPTURE-TODO.md`.

## Human/UX contracts
- `docs/HUMAN-UX-QUALITY-CONTRACT.md`,
- `docs/MUX-DESIGN-GRAMMAR-V2.md`,
- `docs/TONE-AND-LANGUAGE.md`,
- `docs/DRAWING-LANGUAGE.md`.

## Important new evidence to exploit
- historical drawing showing a **cropped/dogleg arm profile** rather than a purely straight arm,
- historical Radstatt drawings explicitly identifying **Landseite / Wasserseite** and frame/lager dimension chains,
- current axial and oblique shaft/arm photographs,
- current lower and side frame photographs,
- current Kumpf/paddle photographs,
- long/short curved wooden Kumpf fasteners shown physically,
- waterside/context photographs showing the wheel as part of a larger stationary timber system.

Do not reduce these new sources back into the old simplified model.

---

# Phase A — Evidence reconstruction before geometry

Reconstruct the evidence map around real mechanical questions.

For every major component, produce:
- observed features,
- historical geometry,
- current photo constraints,
- scan constraints,
- field narrative,
- unresolved conflicts,
- candidate geometry,
- confidence.

Explicitly separate:
- current as-built,
- historical reference,
- reconstructed best candidate,
- alternative candidate,
- unknown.

Do not silently promote old drawing dimensions to current geometry.

---

# Phase B — External construction research

Conduct targeted public research into:
- Möhrendorf/Oberndorf Regnitz water-lifting wheels,
- historic Radstatt construction,
- timber shaft/spoke/arm joints,
- keyed / wedged / pinned timber machinery,
- Kumpf mounting and local terminology,
- wooden pin / Nagelholz / fastener practice,
- trough and discharge channel geometry,
- seasonal assembly and dismantling,
- comparable surviving Franconian wheels.

Store:
- source,
- relevant construction pattern,
- transferability to this wheel,
- confidence,
- whether it is evidence or analogy.

Research is allowed to expand candidate space, never to overwrite local evidence.

---

# Phase C — Canonical coordinate and registration architecture

The scan comparison must be rebuilt cleanly.

## Requirements
- one canonical mechanical coordinate frame,
- explicit world origin,
- explicit shaft axis,
- explicit Z/up,
- explicit Land/Wasser direction only when supported,
- PLY and GLB export transforms preserved separately,
- no free-floating scan beside the model in normal mode.

## Scan workflow
1. RAW_EXPORT
2. AXIS_NORMALIZED
3. ROUGH_ALIGNED
4. MECHANICALLY_REGISTERED
5. METRICALLY_CALIBRATED

Until Saturday datums exist:
- do not call 3 or 4 registration truth,
- provide a dedicated scan-alignment workspace,
- normal Werkstatt view should not be polluted by a drifting point cloud.

After field datums:
- solve transform from DATUM-A/B/C and AXIS-A/B,
- validate using independent control distance,
- report residual error.

---

# Phase D — Throw away primitive core geometry and reconstruct the machine

Existing Three.js boxes/cylinders are not sacred.

Rebuild geometry with proper component hierarchy.

## D1 Welle
Model:
- actual shaft body profile from photo/drawing constraints,
- visible ends,
- bearing journals/candidates,
- arm-entry regions,
- internal unknown zones.

## D2 Arms
Use the historical dogleg drawing as a real geometric constraint.

Generate candidate families:
- historically doglegged,
- straight/repair variant if still needed,
- axial layer alternatives,
- actual current-photo-compatible profile.

Do not model six unrelated independent sticks if evidence supports continuous paired arms.

## D3 Arm/shaft hidden joinery
Generate several candidates:
- independent mortises,
- staggered mortises,
- crossing/interlocking candidates,
- wedge/pin candidates.

Evaluate:
- collision,
- insertion/removal path,
- force path,
- photo entry points,
- historical plausibility,
- minimum unsupported assumptions.

## D4 Rim / Krümmlinge
Model:
- two actual rim planes,
- segmented curved members,
- candidate joints,
- hole/pin geometry,
- historical radii and current-photo proportions separately.

## D5 Kumpf
Model real barrel-like construction:
- staves,
- bottom,
- metal hoops,
- tilt,
- mounting contact,
- pin seats.

## D6 Long/short wooden Kumpf fasteners
Treat as first-class mechanical components.

Generate and compare hypotheses:
- paired long/short canonical mounting,
- geometry-setting pair,
- securing-only pair,
- repair-history variants.

Model curvature/head/shaft form from current photographs.
Do not finalize function before Saturday evidence.

## D7 Paddles
Model:
- actual board geometry,
- orientation,
- connection to rim/Kumpf context,
- phase around circumference.

## D8 Bearings / Radstatt / frame
This is mandatory, not decorative context.

Reconstruct:
- bearing stands,
- bearing supports,
- major cross beams,
- lower frames,
- braces,
- side frames,
- walk/work boards,
- trough support,
- channel support.

Use historical Radstatt drawings + current photos together.

## D9 Trough / Rinne
Model:
- collection trough,
- inlet geometry,
- discharge channel,
- relative height to top Kumpf,
- support structure.

---

# Phase E — Site and water model

Build the wheel as a machine in its real operating environment.

Required:
- river surface,
- bank/context geometry,
- plausible water level,
- flow direction,
- wheel immersion,
- Radstatt relation to water,
- trough/rinne discharge path.

Do not pretend full CFD.

But provide a physically plausible real-time functional simulation:
- wheel rotation,
- Kumpf path,
- fill state approximation,
- lifting,
- tipping/discharge window,
- water transfer to trough,
- trough/rinne flow visualization,
- flow direction,
- configurable speed/water level.

Astra may use particles/shaders/mesh-water techniques for presentation, provided the simulation is clearly labeled as functional visualization rather than measured fluid dynamics.

Target: the viewer should make the operating principle immediately understandable.

---

# Phase F — Technical drawing system

This phase is mandatory before the final field PDF.

Read and obey `docs/DRAWING-LANGUAGE.md`.

## Absolute rule
No final operational page may use the current primitive schematic sketches.

Every operational visual must be either:

### 1. Real photo + technical overlay
Use for real installed context.

or

### 2. Technical projection from reconstructed geometry
Use for geometry, parts, joints, sections and measurements.

or

### 3. Comparative candidate drawing
Use for unresolved geometry.

Required drawing families:
- KS-00 system/site,
- KS-10 shaft/arms,
- KS-20 rim/Krümmlinge,
- KS-30 Kumpf + long/short wooden fasteners,
- KS-40 paddle,
- KS-50 bearings/Radstatt/trough/channel,
- KS-60 assembly/exploded,
- KS-70 Saturday dismantling capture.

Include real:
- orthographic views,
- sections,
- details,
- exploded views,
- measurement endpoints,
- photo directions,
- partner relationships.

No emoji arrows.
No Unicode decorative symbols standing in for technical drafting.
Use SVG/vector technical symbols.

---

# Phase G — Rebuild the field pack from those drawings

The current 12-sheet concept may remain compact, but every sheet must be visually useful.

Goal:
- 8–12 A3 sheets,
- large technical visual area,
- minimal prose,
- obvious measurement/photo locations,
- handwriting space,
- STOPP only for irreversible loss.

Use the Saturday capture plan as operational truth.

A craftsman should understand the requested action by looking at the page before reading paragraphs.

---

# Phase H — UX recovery from the original reference stylekit

Do not preserve the currently deployed composition merely because it exists.

Use the source reference:
`https://thorstenhalsch.github.io/Webpage-preview/`

Reinspect its real CSS/tokens and visual rhythm.

## Required UX principles

### Language
All human-facing UI is German.

No:
- Research,
- Evidence,
- Claims,
- Conflict Matrix,
- Field Pack,
- Hypothesis,
- internal TASK/COMP/CLAIM IDs,
unless inside explicitly technical/developer detail views.

### Icons
- no emojis,
- no Unicode arrows as interface decoration,
- use a consistent SVG icon set,
- technical arrows are SVG/vector drafting marks.

### Color
The current tannengrün dominance is rejected.

Astra may retune the palette beyond the source tokens.

Retain the reference page's family resemblance through:
- typography,
- paper/white hierarchy,
- soft surfaces,
- fine borders,
- restrained radius,
- rhythm.

Use deep green only as a controlled identity accent if it still works.

For 3D components, build a **separate technical component palette**:
- wood/sand/oak families,
- graphite/metal,
- muted blue-gray for water/scan,
- restrained amber for unresolved geometry,
- selected highlight distinct from semantic status.

Do not color the entire application according to the component palette.

### Start page
Must be substantially shorter than the current product.

Purpose:
1. pride/history,
2. one strong explanation of what is being preserved,
3. three obvious paths.

No duplicate project status.
No long uncertainty list.
No field workflow repeated on the story page.

### Werkstatt
Model first.

Above fold:
- compact identity/navigation,
- model/site viewer,
- very small set of obvious actions.

Do not expose advanced scan transforms, variant controls, data capture forms and research detail at once.

Use progressive disclosure.

### Vor Ort
One physical job at a time.

Primary:
- annotated photo or technical drawing,
- current action,
- capture/measurement,
- next.

Do not present a dashboard.

---

# Phase I — High-fidelity interactive viewer

Build a polished scene hierarchy.

Required modes:
- Gesamtanlage,
- Radkörper,
- Tragwerk,
- Welle/Arme,
- Kranz,
- Kumpf/Schaufel,
- Lager,
- Trog/Rinne,
- Betrieb,
- Exploded,
- Schnitt,
- Evidenz,
- Scan-Abgleich.

But do not expose all modes as equal permanent buttons.

Use context-aware mode selection.

Interactions:
- smooth camera transitions,
- part isolation,
- ghost surrounding structure,
- cut plane,
- exploded factor,
- candidate geometry switch,
- current/historical/synthetic comparison,
- water/rotation toggle,
- labels only when useful.

---

# Phase J — QA / adversarial visual audit

Automated tests are necessary but not sufficient.

Required visual QA:
- desktop,
- iPhone 13 class,
- 320 px,
- 200 % text,
- workshop with scan,
- workshop with exploded/cut,
- field task with photo overlay,
- field task with technical drawing,
- all A3 pages rendered to PNG contact sheet.

Adversarial audit questions:
- Is any English visible to a craftsman?
- Is any emoji visible?
- Is any internal ID visible by default?
- Is there any duplicate information?
- Is there any large empty marketing card?
- Is green dominating?
- Can the main action be identified in <3 seconds?
- Does every field visual refer to real geometry/evidence?
- Can scan mode be turned on/off without breaking model navigation?
- Are technical drawings actually construction-level, not decorative?

Materialize screenshots and audit results in the repository.

---

# Phase K — stop gate

Do not stop after "functionality implemented".

Stop only when all of these pass:

## GEOMETRY
- coherent complete system model,
- primitive placeholders removed from primary view,
- new evidence incorporated,
- candidate hidden joinery ranked.

## SCAN
- dedicated coherent scan workflow,
- no drifting/half-overlay confusion,
- explicit registration state.

## DRAWINGS
- **TECHNICAL DRAWING QUALITY PASS**,
- no primitive final sketches,
- real photo overlays or geometry-derived drawings.

## UX
- **HUMAN UX QUALITY PASS**,
- German only in normal UI,
- no emoji,
- no cockpit,
- no dominant tannengrün,
- source-stylekit family resemblance,
- compact start page,
- model-first workshop,
- action-first field mode.

## FUNCTION
- working rotation/water visualization,
- water pickup/discharge understandable,
- site/Radstatt context present.

## TRACEABILITY
- evidence/current/historical/synthetic/alternative/unknown remain distinct.

Final gate:

# **BRUTE-FORCE FUNCTIONAL RECONSTRUCTION READY**

At the gate, provide:
- exact commit,
- full validation report,
- screenshots,
- technical drawing contact sheet,
- remaining Saturday-only unknowns,
- explicit recommendation whether to deploy.
