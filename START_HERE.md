# Start Here - OPAC-018 Green-Schur Bridge Clean Package

This repository is organized for a referee or outside mathematician to inspect the proof candidate quickly.

## 1. Read the claim boundary first

Open:

```text
CLAIMS_AND_NONCLAIMS.md
```

This file explains what is claimed and what is not claimed.

## 2. Read the referee roadmap

Open:

```text
REFEREE_ROADMAP.md
```

This maps each proof-critical step to the manuscript and supporting documentation.

## 3. Read the manuscript source

Open:

```text
paper/main.tex
```

A convenience PDF is included at:

```text
paper/Green-Schur-Bridge-for-OPAC018-Clean-Referee-Edition-v1_5_0.pdf
```

## 4. Run the audits

```bash
python verify_manifest.py
python pure_python_exact_audit.py
python counterexample_stress_test.py
python verify_manifest.py
```

Optional Sage:

```bash
sage sage/opac18_green_schur_sage_test_fixed.sage
```

## 5. Review the attack-response docs

The main hidden-risk areas are separated into human-readable files:

```text
docs/ASYMPTOTIC_MARGIN_CORRECTION.md
docs/SCHUR_COMPLEMENT_BOUND_CAVEATS.md
docs/NON_SIMPLY_LACED_METRIC_SYMMETRIZER.md
docs/OBLIQUE_SUBSPACE_LATTICE_BOUND.md
docs/CONVEX_HULL_CONTAINMENT_BRIDGE.md
```

## 6. Submit issues using templates

The repository includes issue templates for:

```text
proof_gap_report
computation_repro_report
notation_question
```

## Final reminder

The package is a proof candidate. Passing audits support reproducibility; they do not replace independent mathematical referee review.
