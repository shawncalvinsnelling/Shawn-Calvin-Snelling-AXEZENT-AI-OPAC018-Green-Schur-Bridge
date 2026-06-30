# Asymptotic Margin Correction

## Do not claim a uniform asymptotic gap

The correct safety rule is:

```text
Strictly below 2 at each finite rank is the target.
A rank-independent distance below 2 is not required and should not be claimed.
```

## Unsafe wording

Avoid:

```text
lim_{n -> infinity} kappa(Phi_n, U_n) < 2
```

unless a specific family and subspace sequence is being studied and the limit is actually proven.

## Safe wording

Use:

```text
For each finite rank n, the proposed argument aims to prove kappa(Phi_n, U_n) < 2.
The available margin may shrink with n, consistent with known OPAC behavior.
```

## Schur complement caution

For classical Cartan matrices, inverse entries can grow with rank in some positions. For example, for type A:

```text
(A_n^{-1})_{ij} = min(i,j)(n+1-max(i,j))/(n+1).
```

Central entries grow on the order of `n`, so one cannot argue that the entire inverse is uniformly bounded in operator norm.

## What must be bounded instead

The proof must bound the specific functional/vector combinations that enter the projection or Green-Schur correction, not the full inverse matrix norm in isolation.

This distinction prevents a false proof route based on an overly strong norm claim.
