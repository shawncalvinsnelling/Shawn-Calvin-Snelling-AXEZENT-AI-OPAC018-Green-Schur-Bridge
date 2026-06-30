# Uniform Rank Bound Lemma - Safe Form

## Important correction

The package must **not** claim a fixed rank-independent gap:

```text
kappa(Phi_n, U_n) <= 2 - epsilon
```

with one constant `epsilon > 0` for every rank.

The OPAC context allows the maximum to approach 2 as rank grows.

## Safe form

The safe finite-rank target is:

```text
For every finite rank n and every valid Phi-subspace U,
kappa(Phi_n, U) < 2.
```

The margin may shrink with rank:

```text
2 - kappa(Phi_n, U) may be O(1/n).
```

## Why this matters

A reviewer will reject any argument that accidentally proves the stronger false-looking claim that the gap stays uniformly away from 2 for all ranks.

## Proof obligation

The candidate proof should identify a rank-dependent positive margin:

```text
epsilon_n(Phi, U) > 0
```

such that:

```text
kappa(Phi_n, U) <= 2 - epsilon_n(Phi, U)
```

with no requirement that `epsilon_n` has a positive limit.

## Audit relation

The audit can check finite ranks and exact finite-type invariants. It cannot prove the infinite-rank statement by itself.
