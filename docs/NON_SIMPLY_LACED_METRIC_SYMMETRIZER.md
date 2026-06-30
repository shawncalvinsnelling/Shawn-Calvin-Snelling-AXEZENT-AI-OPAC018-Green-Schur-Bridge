# Non-Simply-Laced Metric Symmetrizer

## Reviewer attack

Types `B_n`, `C_n`, `F_4`, and `G_2` contain long and short roots. Their Cartan matrices are not symmetric in the ordinary coordinate basis.

A proof that only works for simply-laced types is not enough.

## Convention used in this repository

The audit uses the Cartan convention:

```text
A_ij = 2 (alpha_i, alpha_j) / (alpha_j, alpha_j).
```

With this convention, a diagonal metric/symmetrizer `D_epsilon` with entries:

```text
d_j = (alpha_j, alpha_j)/2
```

satisfies:

```text
G = A D_epsilon
```

and `G` is symmetric.

Different authors may use the transposed Cartan convention, in which case the symmetrizer appears on the other side. The manuscript should state the convention explicitly.

## Schur complement in the metric form

For non-simply-laced systems, the safe Schur analysis should be performed on the symmetric metric matrix:

```text
G = A D_epsilon.
```

Then block it as:

```text
G = [[G_UU, G_UW],
     [G_WU, G_WW]]
```

and use:

```text
S = G_UU - G_UW G_WW^{-1} G_WU.
```

This avoids treating an asymmetric Cartan matrix as if it were an ordinary symmetric Gram matrix.

## What the audit checks

The audit verifies exact symmetrizability for all included non-simply-laced types and checks Schur complements using the symmetric metric form, not the raw asymmetric Cartan matrix.
