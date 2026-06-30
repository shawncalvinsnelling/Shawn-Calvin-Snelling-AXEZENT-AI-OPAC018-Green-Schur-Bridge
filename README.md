# AXEZENT-AI-OPAC018-Green-Schur-Bridge

**Clean Referee Edition v1.5.0**

Author: **Shawn Calvin Snelling**  
Affiliation: **Axezent AI Research Lab**

## Status

This repository is a clean-room, reviewer-facing package for the OPAC-018 Green-Schur Bridge proof candidate.

**Current truth label:** `SOLUTION-CANDIDATE / EXTERNAL REVIEW PENDING`

This package includes:

- a referee roadmap;
- a candidate manuscript source;
- exact-arithmetic pure-Python audits;
- a SageMath audit script;
- counterexample/stress-test documentation;
- classification-free dependency tables;
- asymptotic margin safety notes;
- non-simply-laced metric-symmetrizer notes;
- Cellini-Marietti convex-hull transfer checklist;
- GitHub Actions workflows;
- a GitHub Pages-ready website (`index.html`).

## Core claim boundary

The package studies the OPAC-018 root-polytope projection bound:

```text
kappa(Phi, U) < 2
```

for crystallographic root systems and Phi-subspaces, with a proposed Green-Schur route through inverse-Cartan Green ratios, Schur complements, and Cellini-Marietti reduction.

## Truth boundary

This repository does **not** claim:

- journal acceptance;
- arXiv acceptance;
- independent referee verification;
- P vs NP;
- the Riemann Hypothesis;
- Traveling Salesman Problem breakthroughs;
- historical recognition;
- any result outside OPAC-018.

The included Python and Sage scripts are exact-arithmetic audits and reproducibility checks. They are **not** substitutes for a line-by-line mathematical referee review.

## Run the audits

From the repository root:

```bash
python verify_manifest.py
python pure_python_exact_audit.py
python counterexample_stress_test.py
python verify_manifest.py
```

Optional Sage audit, if SageMath is installed:

```bash
sage sage/opac18_green_schur_sage_test_fixed.sage
```

Expected pure-Python summary:

```json
{
  "passed": true,
  "total_types": 32,
  "failures": [],
  "output": "receipts/opac18_green_schur_pure_python_results.json"
}
```

Expected counterexample/stress-test summary:

```json
{
  "passed": true,
  "total_cases": 5,
  "unexpected_acceptances": [],
  "output": "receipts/counterexample_stress_test_results.json"
}
```

## Main reviewer files

Start here:

```text
START_HERE.md
REFEREE_ROADMAP.md
CLAIMS_AND_NONCLAIMS.md
paper/main.tex
paper/Green-Schur-Bridge-for-OPAC018-Clean-Referee-Edition-v1_5_0.pdf
```

Important support docs:

```text
docs/CLASSIFICATION_FREE_DEPENDENCY_TABLE.md
docs/UNIFORM_RANK_BOUND_LEMMA.md
docs/ASYMPTOTIC_MARGIN_CORRECTION.md
docs/SCHUR_COMPLEMENT_BOUND_CAVEATS.md
docs/NON_SIMPLY_LACED_METRIC_SYMMETRIZER.md
docs/OBLIQUE_SUBSPACE_LATTICE_BOUND.md
docs/CONVEX_HULL_CONTAINMENT_BRIDGE.md
docs/CELLINI_MARIETTI_TRANSFER_CHECKLIST.md
docs/KNOWN_FAILURE_MODES.md
```

## Website

This repository includes a static website:

```text
index.html
assets/site.css
```

To publish it, use GitHub Pages from branch `main`, folder `/root`.

## Recommended public wording

```text
OPAC-018 Green-Schur Bridge v1.5.0 is a clean solution-candidate referee package with exact-arithmetic audits, classification-free proof-roadmap documentation, asymptotic safety notes, non-simply-laced metric-symmetrizer notes, and a GitHub Pages-ready website. External mathematical review remains pending.
```
