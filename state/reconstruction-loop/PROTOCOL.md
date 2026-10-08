# Reconstruction Calibration Loop — Protocol V1

Status: canonical iteration protocol  
Baseline: `main@558626019c6f85c6061467727f54122a793b15bd`

## Purpose

Keep two models improving in parallel without allowing synthetic plausibility to silently become truth.

### Model A — Truth Model
Only:
- directly measured current geometry,
- current observed topology,
- local expert construction knowledge for non-metric properties,
- historical local drawings explicitly marked as historical,
- registered scan constraints when actually registered.

### Model B — Brute-Force Functional Model
May include:
- best-ranked hidden-joinery candidates,
- complete Radstatt / frame / trough / river context,
- plausible missing geometry,
- operating kinematics,
- water pickup / discharge visualization,
- material / lighting / environment polish.

Synthetic completion is encouraged here, but every synthetic element keeps provenance/status.

---

# Iteration loop

Each iteration MUST execute these stages in order.

## 1. Evidence Intake
Read every new source since the previous iteration.

Materialize:
- new claims,
- expert corrections,
- current-photo observations,
- measurements,
- scan findings,
- unresolved contradictions.

Do not summarize away source identity.

## 2. Constraint Extraction
Convert evidence into explicit constraints:
- geometry,
- topology,
- assembly,
- function,
- terminology,
- orientation,
- water/kinematics.

Each constraint records:
- source,
- scope,
- confidence,
- whether it constrains Truth Model, Brute-Force Model, or both.

## 3. Truth Model Update
Update only what the evidence authority policy permits.

Promotion priority is defined in:
`data/evidence-authority.json`

Never promote a synthetic metric value because it merely looks plausible.

## 4. Brute-Force Update
Generate / refine the strongest whole-system candidate.

Use:
- Truth Model as hard local anchor,
- local expert knowledge,
- historical construction,
- external analogies only where local evidence is silent,
- collision / assembly / force-path reasoning,
- functional water-wheel reasoning.

For unresolved hidden geometry, maintain ranked alternatives.

## 5. Canonical Render Set
Every iteration produces the same comparison views:

1. Gesamtanlage — Landseite
2. Gesamtanlage — Wasserseite
3. Schräg Land
4. Schräg Wasser
5. axial entlang Welle A
6. axial entlang Welle B
7. Welle/Arme Schnitt
8. Lager Landseite
9. Lager Wasserseite
10. Krümmlingstoß
11. Kumpf + Schaufel + Kumpfnägel
12. drei benachbarte Kümpfe / Überlappung
13. Radstatt Unterbau
14. Trog / Rinne / oberer Übergabepunkt
15. Exploded View
16. Betrieb mit Wasser

Render both:
- Truth Model state
- Brute-Force Model state

Keep camera definitions stable between iterations.

## 6. Adversarial Self-Audit
Before handoff, challenge the new state against:
- current photos,
- historical drawings,
- expert corrections,
- scan,
- dimensional conflicts.

For every mismatch output:
- component,
- canonical view,
- source that contradicts or questions it,
- severity P0/P1/P2,
- proposed next action:
  - correct now,
  - generate alternative,
  - field capture required,
  - leave open.

Do not self-promote disputed geometry into Truth.

## 7. Iteration Package
Write:
- `ITERATION-REPORT.md`
- `CONSTRAINT-DELTA.json`
- `MODEL-DELTA.json`
- `CRITIQUE-READY.md`
- canonical renders
- updated model exports
- next unresolved questions

Stop at:

**CALIBRATION ITERATION READY FOR TRUTH CRITIC**

A separate critic/integrator may then decide what enters the next iteration.

---

# Approximation scorecard

Use 0–5 only as navigation, not false precision.

Track separately:

## Truth Confidence
- shaft
- arms
- rims / Krümmlinge
- Kümpfe
- Kumpfnägel
- paddles
- bearings
- Radstatt
- trough / channel
- scan registration
- waterline / operation

## Synthetic Completeness
- whole-system geometry
- hidden joinery
- site context
- water function
- material realism
- lighting
- animation
- exploded / section views
- technical drawing coverage

Every score change needs a source or implementation reason.

---

# Human Truth Critic

ThorstenHalsch is a high-priority local expert source because he is materially involved with the water-wheel project.

His direct corrections outrank:
- external analogies,
- unsupported synthetic geometry,
- generic water-wheel assumptions.

They do not outrank direct current metric measurement for dimensions.

Use him especially for:
- terminology,
- Kumpf construction,
- Kumpfnagel function,
- overlap logic,
- paddle orientation,
- practical assembly/maintenance knowledge.

Never reinterpret an explicit local correction away merely because the current model or code disagrees.
