# Semantic Reconstruction Contract — DISCUSSION DRAFT

Status: proposal only; no schema migration, geometry change or manufacturing authorization.

## Principle
One real part has a persistent identity; its evidence, engineering definition and experiences are separate, linked records. Do not make GLB triangles the authority for a dimension.

### Evidence Model
source_id, original_file_hash, capture_time, observer, part_instance_id, partner_instance_id, before_after_event, coordinate_frame, measured_property, endpoints, raw_value, unit, tool_resolution, uncertainty, evidence_class, review_state, provenance.

### Engineering Model
part_definition_id, revision, part_instance_id, variant_id, material/species/condition, parametric features, datum references, dimensions and tolerance scheme, connection graph, fit/clearance constraints, assembly dependencies, calculated validation scope, reviewer, release_state.

### Experience Model
experience_id, source_engineering_revision, camera/scene/material/lighting, render_status, simulation assumptions, animation trajectory, audience, captions and evidence overlay. Must not promote visuals into engineering truth.

## Required states
Evidence: CAPTURED_UNREVIEWED → REVIEWED → ACCEPTED / DISPUTED / UNKNOWN.
Engineering: DRAFT → EXPERT_REVIEWED → METRIC_VERIFIED → RELEASED (each property scoped).
Experience: SYNTHETIC / SOURCE_DERIVED / ENGINEERING_DERIVED, with source revision.

## Future outputs (not yet authorized)
- Per-part orthographic/section drawings with dimension chains, material and tolerance data, signed review and revision.
- BOM / physical instance register with reversible trace to original dismantled part and storage location.
- IKEA-like assembly sheets with dependencies, temporary supports, tool access and safe handling reviewed by experienced team.
- Candidate kinematic assembly/disassembly animations; never infer a safe physical procedure solely from collision-free mesh animation.
- Water operation visualization vs validated hydraulics/loads kept separate.
- Future AR/VR, museum and cinematic experiences all link to approved revision.

## Hard gaps
Current metric scan registration absent; hidden joints not surveyed; material moisture/warp, fits, tolerance stack-up, structural loads, support sequence, wear, restoration vs original distinctions unresolved. '100% correct' is not a defensible guarantee. Require explicit fit-for-purpose release and bounded uncertainty.

## Governance
No automatic promotion from expert statement to current installed metric dimensions. No automatic release by passing unit tests. Revisions and partner identities immutable; supersede, do not overwrite provenance.
