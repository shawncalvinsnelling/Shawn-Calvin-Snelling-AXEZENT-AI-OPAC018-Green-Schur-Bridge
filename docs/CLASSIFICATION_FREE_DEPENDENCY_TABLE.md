# Classification-Free Dependency Table

The purpose of this table is to separate structural proof ingredients from finite-type computational sanity checks.

| Proof component | Intended role | Uses classification? | File |
|---|---|---:|---|
| Convexity and projection linearity | Shows projection commutes with convex hull | No | `docs/CONVEX_HULL_CONTAINMENT_BRIDGE.md` |
| Crystallographic integrality | Controls allowed Cartan/coroot values | No | `paper/main.tex` |
| Green ratio lemma | Local candidate inequality | Must be no | `paper/main.tex` |
| Schur complement step | Hyperplane reduction candidate | Must be no | `docs/SCHUR_COMPLEMENT_BOUND_CAVEATS.md` |
| Cellini-Marietti transfer | Connects local/projection structure to OPAC target | Literature-dependent | `docs/CELLINI_MARIETTI_TRANSFER_CHECKLIST.md` |
| Infinite classical families | Checks rank-growth wording and margins | No enumeration as proof | `docs/ASYMPTOTIC_MARGIN_CORRECTION.md` |
| 32 finite Cartan audit | Reproducibility/sanity check | Yes, as audit only | `pure_python_exact_audit.py` |

## Reviewer warning handled here

A finite audit of root types can be useful, but a classification-free proof cannot depend on that finite enumeration as its logical core.

Therefore:

```text
Finite audit = sanity check
Written structural proof = theorem candidate
External referee review = required
```
