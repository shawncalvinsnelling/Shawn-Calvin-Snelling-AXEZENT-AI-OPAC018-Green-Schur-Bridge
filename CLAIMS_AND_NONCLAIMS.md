# Claims and Nonclaims

## Claim type

`SOLUTION-CANDIDATE / EXTERNAL REVIEW PENDING`

This repository presents a candidate classification-free proof route for the OPAC-018 root-polytope projection bound.

## Main mathematical target

For a crystallographic root system `Phi` and a `Phi`-subspace `U`, the target containment is:

```text
pi_U(ConvHull(Phi)) subset kappa * ConvHull(Phi cap U)
```

with:

```text
kappa(Phi, U) < 2.
```

## What is claimed

The package claims to provide:

1. a written proof candidate based on a Green-Schur inverse-Cartan route;
2. exact-arithmetic sanity checks for a finite Cartan audit set;
3. a pure-Python audit independent of Sage, NumPy, SymPy, and root-system libraries;
4. a SageMath-compatible audit script;
5. documentation of known failure modes outside the hypotheses;
6. specific notes for asymptotic margins, non-simply-laced metric scaling, oblique subspaces, and convex-hull containment.

## What is not claimed

This package does **not** claim:

- peer-reviewed acceptance;
- journal acceptance;
- arXiv acceptance;
- official OPAC acceptance;
- a Millennium Prize result;
- P vs NP;
- the Riemann Hypothesis;
- a Traveling Salesman Problem breakthrough;
- a universal exact solver;
- historical recognition.

## Code/proof boundary

The scripts verify deterministic exact-arithmetic invariants and package reproducibility.

They do **not** prove the theorem by themselves.

The proof candidate must stand or fall by the written mathematical argument and outside review.

## Asymptotic caution

The package does **not** claim a rank-independent uniform gap below 2. The relevant safe statement is:

```text
For each finite rank n, kappa(Phi_n, U_n) < 2,
while the margin 2 - kappa may shrink with rank.
```

This matches the OPAC context that the bound can approach 2 asymptotically.
