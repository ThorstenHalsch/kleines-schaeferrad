# Animation transport recovery

All ITER-001 artifacts are preserved. The GitHub connector rejects requests above 16 MiB, so the original 22,216,599-byte GIF is stored losslessly as three binary parts. No model or rendering was regenerated.

Run from any working directory:

```sh
python output/calibration/ITER-001/operation/restore-full-cycle.py
```

The script verifies each part and the complete SHA-256, then restores `full-cycle.gif` beside the parts. Afterwards the existing review page animation links and package validator work unchanged. The repository does not contain the assembled GIF until this step is run. Static phase images remain directly available.

Original local commit: `924a647d4425ec18e2be13578c8683381be57b62`. All other 121 changed paths are byte-identical. The connector recovery commit has a different tree solely for this documented transport representation and recovery instructions. No merge or deployment.
