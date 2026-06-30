# Known Failure Modes

This package documents where the method is expected to fail or become out of scope.

| Case | Expected status | Why |
|---|---|---|
| Non-crystallographic systems | Out of scope | Coroot integrality can fail |
| Affine/degenerate Cartan matrices | Rejected | Positive definiteness fails |
| Arbitrary dense fractional matrices | Rejected | Not root-system Cartan data |
| Missing Phi-subspace condition | Out of scope | Target root polytope may not span U |
| Treating asymmetric Cartan as Gram matrix | Rejected | Non-simply-laced types require symmetrizer |
| Uniform rank-independent gap | Not claimed | OPAC behavior allows approach to 2 |

See also:

```text
counterexample_stress_test.py
docs/ASYMPTOTIC_MARGIN_CORRECTION.md
docs/NON_SIMPLY_LACED_METRIC_SYMMETRIZER.md
```
