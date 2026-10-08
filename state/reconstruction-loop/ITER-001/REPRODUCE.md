# Reproduce ITER-001

Runtime: Node 24, repository's pinned Three.js package; Python 3.12 with numpy, Pillow, moderngl 5.13.0 and glcontext 3.0/3.1. Offscreen rendering uses Mesa/EGL; the recorded renderer is llvmpipe. No browser screenshot or image generation substitutes for mesh renders.

```sh
npm ci --ignore-scripts
python -m pip install moderngl==5.13.0 glcontext==3.1.0
npm run test:calibration
npm run prepare:calibration
npm run build
node --test tests/workbench.test.mjs tests/mechanics.test.mjs tests/reconstruction-geometry.test.mjs tests/field-kit.test.mjs
python scripts/verify_evidence.py
python scripts/validate-calibration-package.py
```

The recorded run used glcontext 3.1.0. Rendering inputs under `/tmp/ks-calibration` are disposable. Persistent exports and plates are under `output/calibration/ITER-001`; implementation, parameters, stable cameras and machine-readable audit outputs are committed. Generated image writes are buffered and atomic to avoid partial PNGs; the package integrity validator checks decoded content, hashes and dimensions.

`package-calibration.mjs` optionally verifies supplied session attachments in `../project_sources`; they must not be mistaken for canonical repository source paths. The archived evidence remains authoritative if those session copies are absent. See committed `attachment-intake.json` for this run.

The existing `prepare:model` command intentionally continues to export the retained V2 baseline for old/new comparison. Use `prepare:calibration` for the new **separate** Truth and Brute-Force exports. There is no merge/deployment command in the iteration pipeline.

The browser binary download returned a truncated archive in this environment; no end-to-end browser playback test is claimed. The web bundle build, geometry/state tests and offscreen animation rendered from the same pose calculations provide the stated coverage. Browser UI playback should be checked by the critic before any deployment.
