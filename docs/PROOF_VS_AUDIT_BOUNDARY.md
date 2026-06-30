# Proof vs Audit Boundary

## Written proof

The written proof is the only place where a classification-free theorem candidate can be established.

## Audit scripts

The scripts provide deterministic exact-arithmetic checks for:

- Cartan construction;
- symmetrizer correctness;
- positive-definiteness sanity checks;
- Schur complement sanity checks;
- stress-test rejection of invalid inputs;
- manifest reproducibility.

## What the scripts are good for

They help reviewers reproduce calculations quickly and detect accidental file drift.

## What the scripts cannot do

They cannot substitute for a proof that the logic works uniformly for all valid subspaces and ranks.
