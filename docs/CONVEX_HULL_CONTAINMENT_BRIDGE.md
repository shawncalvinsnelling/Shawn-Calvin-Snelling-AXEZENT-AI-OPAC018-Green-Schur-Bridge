# Convex Hull Containment Bridge

## Reviewer attack

A proof that bounds individual projected roots must still explain why the entire projected polytope is contained. Referees may ask whether facets or higher-dimensional faces can leak outward.

## Linear projection identity

For a linear map `L` and a finite set `S`:

```text
L(ConvHull(S)) = ConvHull(L(S)).
```

Therefore, for root systems:

```text
pi_U(ConvHull(Phi)) = ConvHull(pi_U(Phi)).
```

## Consequence

If every projected root lies inside a convex target body `K`, then the convex hull of all projected roots also lies inside `K`:

```text
pi_U(alpha) in K for all alpha in Phi
=> ConvHull(pi_U(Phi)) subset K
=> pi_U(ConvHull(Phi)) subset K.
```

## What must be shown

The proof candidate must identify the correct target body:

```text
K = kappa * ConvHull(Phi cap U)
```

and prove projected-root containment into that body under the OPAC hypotheses.

## No facet leakage

Because projection is linear and convex hull is the minimal convex set containing the images of the vertices, facets cannot flex outside the convex hull of projected vertices.

The hard part is not facet leakage after vertex containment. The hard part is proving the correct vertex containment in the first place.
