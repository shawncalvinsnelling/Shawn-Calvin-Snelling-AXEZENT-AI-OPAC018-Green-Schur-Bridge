# Referee Roadmap

This file is meant to make the package inspectable in under ten minutes.

## Central question

OPAC-018 asks for a uniform, classification-free proof that:

```text
kappa(Phi, U) < 2
```

for root-polytope projections.

## Main proof route

| Step | What to inspect | File |
|---|---|---|
| Definitions and theorem boundary | Exact statement and hypotheses | `paper/main.tex`, `CLAIMS_AND_NONCLAIMS.md` |
| Classification-free dependency audit | Whether the proof secretly enumerates types | `docs/CLASSIFICATION_FREE_DEPENDENCY_TABLE.md` |
| Local Green-Schur mechanism | Inverse-Cartan/Schur complement candidate | `paper/main.tex`, `docs/SCHUR_COMPLEMENT_BOUND_CAVEATS.md` |
| Infinite classical families | Rank growth and shrinking margin | `docs/UNIFORM_RANK_BOUND_LEMMA.md`, `docs/ASYMPTOTIC_MARGIN_CORRECTION.md` |
| Non-simply-laced systems | Long-root/short-root scaling | `docs/NON_SIMPLY_LACED_METRIC_SYMMETRIZER.md` |
| Oblique subspaces | Non-coordinate projections | `docs/OBLIQUE_SUBSPACE_LATTICE_BOUND.md` |
| Convex hull containment | Vertex bounds to polytope containment | `docs/CONVEX_HULL_CONTAINMENT_BRIDGE.md` |
| Cellini-Marietti transfer | Reduction-step checklist | `docs/CELLINI_MARIETTI_TRANSFER_CHECKLIST.md` |
| Computation support | Exact arithmetic audit | `pure_python_exact_audit.py`, `sage/opac18_green_schur_sage_test_fixed.sage` |
| Failure modes | What breaks outside hypotheses | `docs/KNOWN_FAILURE_MODES.md`, `counterexample_stress_test.py` |

## Referee attack points addressed

1. **Is the proof secretly case-by-case?**  
   See `docs/CLASSIFICATION_FREE_DEPENDENCY_TABLE.md`.

2. **Does the margin falsely stay uniformly away from 2?**  
   See `docs/ASYMPTOTIC_MARGIN_CORRECTION.md`.

3. **Do non-simply-laced types break the Schur argument?**  
   See `docs/NON_SIMPLY_LACED_METRIC_SYMMETRIZER.md`.

4. **Can convex-hull facets leak even if vertices are bounded?**  
   See `docs/CONVEX_HULL_CONTAINMENT_BRIDGE.md`.

5. **Can an oblique Phi-subspace make dense fractional blocks that break the argument?**  
   See `docs/OBLIQUE_SUBSPACE_LATTICE_BOUND.md`.

## What the audits prove

The audits prove that the included deterministic exact-arithmetic checks reproduce the expected package-level invariants.

## What the audits do not prove

They do not replace the written proof. They also do not certify journal acceptance or community acceptance.
