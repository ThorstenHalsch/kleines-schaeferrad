# ITER-001 — Baseline V3 calibration

Branch: `work/model-calibration-loop-v3-20261008`  
Starting head: `22c29d1b737e507da947182f690c470e771d6e81`  
Evidence baseline: `558626019c6f85c6061467727f54122a793b15bd`  
Protocol: `state/reconstruction-loop/PROTOCOL.md`  
No merge; no deployment; no field geometry promotion.

## Result

The reference Kumpf is materially rebuilt, not merely relabeled. V2's 440 mm bilged body is replaced by a straight tapered twelve-stave reference candidate with a recessed base engaging an actual groove, three flat metal bands and four bored openings. The four new Thorsten photos govern its shape. Installed measurements remain null.

Truth and Brute-Force have separate GLBs, component indexes and all sixteen canonical camera views. Truth renders are deliberately incomplete: they visualize supported construction and historical/observed form, with all display dimensions/poses labeled. Exact nail paths, directed overlap, full 24-copy population, bearing contacts, synthetic site and operation are excluded from Truth. Three reference-layout vessels illustrate the known neighborhood relation; their pose and equivalence to installed parts are **not** truth claims. The authoritative Truth payload is the constraints and per-property provenance, not an implicit claim that every display vertex has been surveyed.

Brute-Force supplies the complete candidate system. It has ranked nail mappings A/B/C, a collision-screened directed overlap pose, radial paddle boards and a geometry-driven water cycle. The task's gate is readiness for criticism, not acceptance of these candidates.

## Deliverables

- [Review index](../../../output/calibration/ITER-001/review.html)
- [32 canonical renders / manifest](../../../output/calibration/ITER-001/canonical-manifest.json)
- [Canonical contact sheet](../../../output/calibration/ITER-001/canonical-contact-sheet.jpg)
- [Truth GLB](../../../output/calibration/ITER-001/truth-ITER-001.glb), [Truth index](../../../output/calibration/ITER-001/truth-index.json)
- [Brute-Force GLB](../../../output/calibration/ITER-001/brute-ITER-001.glb), [Brute-Force index](../../../output/calibration/ITER-001/brute-index.json)
- [Technical contact sheet](../../../output/calibration/ITER-001/technical-contact-sheet.jpg)
- [Full operating cycle](../../../output/calibration/ITER-001/operation/full-cycle.gif)
- [Pickup / lift / discharge / channel](../../../output/calibration/ITER-001/operation/pickup-lift-discharge-channel.jpg)
- Source-photo plates in `output/calibration/ITER-001/sources/`; five required comparison plates plus A/B/C in `comparisons/`.
- `CONSTRAINT-DELTA.json`, `MODEL-DELTA.json`, `SCORECARD.json`, `CRITIQUE-READY.md`, `ADVERSARIAL-AUDIT.md`, `SATURDAY-QUESTIONS.md`.

## A — Reference vessel

Source identities: PHOTO-1000046420 through PHOTO-1000046423; NARRATIVE-TH-KUMPF-20261008-01/02/03. Original bytes are preserved. All thirty attached files are checked against the archive by hash in `attachment-intake.json`.

The reference appears approximately straight-tapered, with a larger base end and smaller mouth. Ruler readouts support **reference-only estimates**, not direct current installed measurements:

| Property | Display choice | Conservative photo interval | Method / limitation |
|---|---:|---:|---|
| Length | 600 mm | 580–620 mm | Read end positions along folding rule in 6423; zero/end contact and perspective uncertain |
| Base external diameter | 300 mm | 280–320 mm | Ruler chord in 6421; no rectification or proof of a diametral chord |
| Mouth external diameter | 220 mm | 210–240 mm | Approximately 0–22/23 cm along ruler in 6422; perspective / opposite-edge uncertainty |
| Hoop offsets | 100 / 300 / 500 mm | ±15 mm | Seat positions in 6423; selected from mouth end as a candidate convention |
| Hole offsets | 190 / 450 mm | 180–210 / 430–470 mm | Visible shafts near ruler in 6423; exact center and end reference require confirmation |

Twelve equal 30° sectors are an idealized realization of the expert count. Small asymmetric edges, stave widths and joint openings are visible, but their metric correction cannot be separated reliably from perspective. No invented per-stave asymmetry is passed off as observed. 24 mm thickness is a **historical variant candidate**; 22 mm remains selectable. Groove width/depth (14/8 mm), bore radius (12 mm), base setback (45 mm) and exactly opposed drilled-stave indices are construction candidates, not read measurements.

The base geometry physically engages the rebated stave profile. Four cylindrical passages are actual voids, verified by rays through both opposed staves; adjacent timber remains solid. Orthographics, clipped section, groove macro and the isolated two-stave drilling plate are derived from that same mesh.

## B — Nail paths

A maps HA1–HB1 and HA2–HB2. B reverses access/head direction. C cross-pairs the rows and would require oblique holes or a different curved insertion; it is retained for criticism and is not the production choice.

A's endpoints are calculated to a **common candidate inner rim exit plane**, not simply assigned arbitrary unequal lengths. In the chosen tilted-overlap pose the paths are approximately 726 / 595 mm, a 131 mm difference. These are generated candidate lengths, not claimed source measurements. Both centerlines intersect a Krümmling; their samples clear neighboring bodies/paddles during outward withdrawal. Hole clearance is separately tested. The actual Krümmling bores, precise nail curvature, contact force and source correspondence remain unverified. The model does not silently cut guessed bores into Truth.

Unequal reach is geometrically consistent with the selected staggered/tilted overlapping mounting. This does **not** independently prove that it is Thorsten's actual overlap mechanism. His stated function has priority; the exact reconstruction is a critic question. The old tilt-as-primary-purpose hypothesis stays demoted.

## C–E — Neighborhood, paddles and circumference

A three-vessel cluster and a full repeated family use one parameterized construction. Circumferential projected envelope overlap is about 0.047 rad (2.70°) at a 15° expected slot pitch. Overlap in projection is not solid interpenetration. The selected pose passed a conservative envelope screen; subsequent solid/surface samples found no vessel-neighbor, vessel-paddle or vessel-rim penetration. Reversing overlap is an exposed alternative, not a verified second solution.

Candidate mounting sequence for geometric discussion: establish the first reference pose; present the next vessel in the selected circumferential direction with its base/mouth overlap relation visible; thread the paired rows toward their recorded rim partner; close the ring only after checking the last/first neighbor. Actual removal order and restraint must be documented on site, not inferred as a mandatory reverse sequence. Withdrawal tests cover the stated candidate only.

Mechanical coordinates: shaft **X**, wheel plane **YZ**, radial R(a)=(0,−sin a,cos a), tangent T(a)=(0,−cos a,−sin a). V2 board plane spanned X and T, so its normal was R. V3 spans X and R, normal T. **Both are perpendicular to YZ.** Thus the expert's plane statement alone does not determine pitch. Current photos and effective stream-facing area support the radial candidate over the old tangential blade. Local phase changes from 0.5 to 0.45 slot and axial overhang from 150 to 70 mm remove candidate conflicts. Neither these values nor radial pitch are promoted into Truth. See `PADDLE-ORIENTATION.md`.

Production uses 24 expected slots, not 24 identified physical objects. `production.variants[slot]` permits distinct vessel dimensions. Historic/expected graph IDs are retained; no physical instance register is fabricated.

## F — Operating recalibration

The same `vesselPose` controls mesh orientation, mouth position and water behavior. Interior quadrature estimates how much water can lie below the lowest mouth lip; immersion fills, emerging mouth retains only that capacity, decreasing capacity spills. This replaces V2's fixed discharge phase window. Fill is bounded and periodic; a dry river yields zero lift.

After the mouth, the displayed trajectory uses explicit candidate exit velocity plus rigid-body tangential velocity and gravity. It is not bent toward the trough. Trough interception is tested at the receiving plane; misses continue toward the river. The chosen **1.8 m/s outflow speed is synthetic and adjustable** (also 1.0 and 0 in the viewer), not CFD or measured head. Thus successful interception does not verify real operation. The reference run shows top interception roughly 312–344°, as well as emergence/early spill losses. Trog/Rinne continuity is visible, but volume, efficiency and structural adequacy are not asserted.

The V2 trough intersected the new vessel orbit. It and its synthetic supports were moved outside the swept vessel envelope, then checked at 72 rotation steps. The new trough pose is a Brute-Force candidate only. Its significant displacement is an explicit critic item, not an authoritative correction of the historical/site geometry.

## G–J — Separation, presentation and output

Truth's non-metric authority is expert construction knowledge and direct photo form. Historical arms/rims remain marked historical/conventional. The three reference layouts are illustrations with `installedMetric:null` and candidate pose status. Exact nails are absent from Truth geometry; their count/family/function remain in the expert topology payload. Unknown bearings, fixed structure and operation deliberately leave incomplete views.

Brute-Force has real component joints at the reference vessel, flat bands, inspectable wood/metal material status, wet-zone shading, candidate site/water context, full kinematics and a slow ~30 s single-revolution GIF. The visual result is a critic-ready museum-model candidate, not photorealistic restoration or a surveyed digital twin. Remaining visual and evidential quality is recorded separately in the scorecard.

All sixteen views exist in both modes with one frozen camera definition per pair (`data/canonical-cameras.json`). Five comparison plates cover old/new vessel, nails, paddle, isolated/cluster, operating cycle. Additional source plates are explicitly unregistered visual comparisons; no false registered photo/scan overlay is presented.

Eight required technical topics plus four reference orthographics, groove macro and rim exploded detail are supplied. Existing field drawing selectors and text were updated to use the component-level vessel and expert fastening function, rather than the former free-pin/tilt assumption.

## K–L — Audit, limitations and handoff

`ADVERSARIAL-AUDIT.md` records defects corrected during this iteration and evidence-limited P1/P2 questions. `geometry-audit.json`, `contact-audit.json`, `stationary-audit.json`, phase trials and automated tests give scoped evidence. Samples are not continuous collision certificates or dismantling authorization. Source authority remains unchanged.

The critic should focus first on the new vessel proportions and end convention, the exact overlap/nail mechanism, radial paddle interpretation, and the receiving trough/outflow candidate. Do not approve their metric implementation solely because the candidate animates without sampled collisions.

## Validation at handoff

All 26 geometry, mechanics, workbench, calibration and field-kit tests pass. The production/offline build completes. Evidence verification covers 43 historical originals, four contributed originals, ten derivatives, 369 claims and 51 source analyses. Package validation decodes all 66 images (including all 72 animation frames), verifies 32 canonical render hashes and 16 paired cameras, both model provenance hashes and all 30 attachment/archive matches. See `PACKAGE-VALIDATION.json`. Section-plane clipping tolerances were corrected to retain material contours; the detailed reference section uses a 1 μm offset to avoid coinciding triangle edges. No additional metric claim follows from that numerical choice.
