# Referee Q&A Quick Responses

## Q: Is this a peer-reviewed theorem?

No. It is a solution-candidate referee package. External review is pending.

## Q: Does the code prove OPAC-018?

No. The code provides exact-arithmetic audit support. The written proof must carry the theorem.

## Q: Is the proof classification-free?

That is the central claim to be reviewed. See `docs/CLASSIFICATION_FREE_DEPENDENCY_TABLE.md`.

## Q: Does the proof claim kappa stays uniformly away from 2 as rank grows?

No. The margin may shrink with rank. See `docs/ASYMPTOTIC_MARGIN_CORRECTION.md`.

## Q: How are B_n and C_n handled?

By using a metric symmetrizer before Schur complement analysis. See `docs/NON_SIMPLY_LACED_METRIC_SYMMETRIZER.md`.

## Q: Can facets leak outside even if vertices are controlled?

No after vertex containment is established, because linear maps commute with convex hull. See `docs/CONVEX_HULL_CONTAINMENT_BRIDGE.md`.
