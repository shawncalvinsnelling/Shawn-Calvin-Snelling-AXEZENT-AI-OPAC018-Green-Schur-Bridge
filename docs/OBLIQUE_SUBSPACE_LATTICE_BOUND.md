# Oblique Subspace Lattice Bound

## Reviewer attack

A Phi-subspace `U` may not be aligned with the displayed simple-root coordinate blocks. A reviewer may ask what happens when `U` cuts through the root lattice obliquely and creates dense fractional-looking projection coordinates.

## Safe response

The written proof must not depend on the subspace being a coordinate subspace in a chosen Dynkin diagram ordering.

The structural route should use:

1. `Phi cap U` spans `U` by the definition of Phi-subspace;
2. orthogonal projection is defined by the invariant Euclidean form, not by coordinates;
3. projected roots are controlled by root-system pairings/coroot pairings;
4. coordinate density in one basis does not imply uncontrolled geometry in the invariant metric;
5. any block representation must be justified after choosing a basis adapted to `Phi cap U` and its complement.

## Proof obligation

The manuscript should contain a lemma of the following kind:

```text
Adapted-basis lemma:
For every Phi-subspace U, one may express the projection problem using a basis adapted to Phi cap U and its orthogonal complement, and the resulting coefficient bounds depend only on crystallographic root-system pairings, not on the accidental coordinate density of U in the original simple-root basis.
```

## Audit boundary

The finite audit checks standard Cartan forms and representative Schur-block conditions. It is not a complete enumeration of all oblique Phi-subspaces.

That is why the adapted-basis lemma is a proof obligation in the manuscript.
