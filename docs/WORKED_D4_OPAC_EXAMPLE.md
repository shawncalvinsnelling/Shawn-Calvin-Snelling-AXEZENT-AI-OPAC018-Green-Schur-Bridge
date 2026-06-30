# Worked D4 OPAC Example

This file records the standard OPAC-018 example in reviewer-friendly form.

Let:

```text
Phi = D4 = { +/- (e_i - e_j), +/- (e_i + e_j) : 1 <= i < j <= 4 }.
```

Use simple roots:

```text
alpha_1 = e_1 - e_2
alpha_2 = e_2 - e_3
alpha_3 = e_3 - e_4
alpha_4 = e_3 + e_4
```

Let:

```text
U = span_R { alpha_1, alpha_3, alpha_4 }.
```

Then `U` is orthogonal to:

```text
omega_2 = e_1 + e_2.
```

The projection of `alpha_2` is:

```text
pi_U(alpha_2)
= alpha_2 - <alpha_2, omega_2>/<omega_2, omega_2> omega_2
= -1/2 alpha_1 - 1/2 alpha_3 - 1/2 alpha_4.
```

The projected root set is the 14-point set described in the OPAC problem statement, while:

```text
Phi cap U = { +/- alpha_1, +/- alpha_3, +/- alpha_4 }.
```

Thus the target base polytope is an octahedron and the projected polytope is a rhombic dodecahedron. The known value in this example is:

```text
kappa(Phi, U) = 3/2.
```

## Why this example matters

Any proposed proof should reproduce this example and explain it in its own notation.
