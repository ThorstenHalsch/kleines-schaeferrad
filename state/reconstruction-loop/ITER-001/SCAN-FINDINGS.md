# Available scan review — ITER-001

Read the archived `Scaniverse 2026-10-07 173556.ply` and `.glb`; re-ran the binary audit. PLY: 75,619 points (74,405 unique positions), finite coordinates. GLB: 56,117 vertices, 78,043 triangles, 30,775 boundary edges, no reported nonmanifold edges or zero-area faces in the existing audit method. The scan is visibly partial, not a closed mechanical survey.

The point cloud/mesh provides local surface and visibility context. A separate dedicated paddle scan and a nail point cloud reported by Thorsten are **not identified in this repository**. That is an availability finding, not a claim that they do not exist elsewhere. No current field distances, signed side confirmation or mechanical registration are present. `data/scan-transforms.json` remains unchanged.

Orthographic and spatial inspection shows mixed thin boards, frame members and partial vessel regions. Assigning one sparse surface patch to a particular blade face and measuring its angle to a fitted rim without correspondence would create false precision. This iteration therefore does not claim a blade plane measurement or an overlap dimension from the scan. The photo/expert constraint remains active. See `sources/scan-review.png` in the output package.

Next decisive input: identify the dedicated scan filename or capture three labeled installed blade neighborhoods, with shaft direction and rim plane together. Capture long/short nail paths and three adjacent vessels before separation. These are source-limited decisions, not algorithmically measured geometry in this iteration.
