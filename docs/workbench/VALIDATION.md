# Validation — Field Reconstruction Workbench Alpha

Date: 2026-10-07. Work branch: work/field-workbench-alpha-20261007.

## Executed locally

- `npm run test:workbench`: 8 passing tests. Continuous arm topology, unique IDs, counts and plane segmentation, A/B difference, stationary explosion behavior, provenance references, measurement validation, lossless media JSON roundtrip and conflicting import rejection.
- `npm run check`: 0 errors, 0 warnings, 0 hints.
- `npm run build`: successful, landing + werkstatt routes; 43 source assets and 5 generated A3 review sheets. Vite reports one >500 kB JS chunk (about 832 kB uncompressed): Three.js and baseline data. Scan GLB remains lazy loaded. No claim of a measured mobile performance budget.
- `python scripts/verify_evidence.py`: 43 originals, 10 baseline derivatives, 355 claims and graph/conflict references verified. Original baseline files unchanged.
- Shared-mesh SVG projections KS-00 and KS-30 were rasterized with PyMuPDF and visually inspected: full page, status, source notes, drawing numbers, A/B and blank measurement fields visible. Five A3 pages combined in KS-Review-A0.pdf. Wireframe projections do not solve hidden-line removal and are not norm-certified manufacturing drawings.

## Browser environment blocker

No browser binary was installed in the local workspace. Playwright Chromium download returned a truncated/invalid ZIP (`End of central directory record signature not found`). A cloud-browser attempt at the local test URL returned `net::ERR_CONNECTION_REFUSED`. The supported static preview runner failed with `bwrap: Can't mount proc on /newroot/proc: Operation not permitted`. The Astro preview path also did not become healthy. These are infrastructure failures, not passing UI tests.

`tests/browser-field.mjs` and `.github/workflows/field-workbench.yml` provide the next execution path in CI. They exercise desktop 1440 px, narrow 320 px, an iPhone 17 Pro touch profile and 200 % root text enlargement. This is device emulation, not physical iPhone/Safari or human testing. It tests a complete simulated measurement + photo → review → save → export → import loop and draft interruption/resume. All test records are explicitly labeled SIMULATION.

## Gate

**PENDING — do not claim FIELD RECONSTRUCTION WORKBENCH ALPHA READY until browser CI evidence has been retrieved and reviewed.**

Missing evidence at this checkpoint: live render/interaction, a full UI capture loop, 320 px / iPhone-format / desktop / 200 % text checks, runtime target sizing and task resumption in a real browser. Source-level controls and unit tests are not substitutes.

No real target users or physical current iPhone were available. Follow HUMAN-PLAN.md after automated testing; real field observations must remain separate from simulated test records.

## Publication approval blocker

Automatic approval review rejected the exact branch push to the existing GitHub remote. No push retry, PR creation or CI run followed. See state/ASTRA-WORK-SESSION-20261007.md. Approval for branch push + draft PR/CI is the next required action; no merge/deployment is included.
