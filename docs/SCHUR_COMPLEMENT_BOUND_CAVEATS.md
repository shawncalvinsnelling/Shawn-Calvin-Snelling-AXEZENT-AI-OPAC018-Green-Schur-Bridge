# Schur Complement Bound Caveats

## Reviewer risk

A Schur complement has the form:

```text
S = A - B D^{-1} C.
```

It is tempting to claim that the correction term is uniformly small because `D^{-1}` is harmless. This is not generally safe.

## Safe interpretation

The proof candidate should only use Schur complement bounds in the exact structural context where:

1. `D` is positive definite in the metric induced by the root system;
2. `B` and `C` arise from crystallographic/root-subspace incidence, not arbitrary dense matrices;
3. the controlled quantity is the projected-root functional or Green ratio, not the full operator norm of `D^{-1}`;
4. all denominators remain nonzero under the hypotheses;
5. non-simply-laced scaling is handled by a symmetrizer.

## What the audit checks

The pure-Python audit checks finite exact-arithmetic sanity conditions:

- Cartan integrality;
- symmetrizability;
- positive definiteness of the metric form;
- Schur complement positive-definiteness for single-node deletions;
- non-simply-laced scaling compatibility.

## What the audit does not check

The audit does not prove a classification-free theorem. It cannot replace the manuscript's structural argument.
