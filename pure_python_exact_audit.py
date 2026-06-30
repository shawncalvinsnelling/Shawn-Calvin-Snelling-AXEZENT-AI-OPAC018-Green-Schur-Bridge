#!/usr/bin/env python3
"""Pure-Python exact arithmetic audit for the OPAC-018 Green-Schur package.

This script intentionally avoids Sage, NumPy, SymPy, and root-system libraries.
It checks deterministic Cartan/symmetrizer/Schur-complement sanity conditions
for a 32-system finite audit set.

Important: this is an audit, not a substitute for the written proof.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
from typing import List, Tuple, Dict, Any

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "receipts" / "opac18_green_schur_pure_python_results.json"

Matrix = List[List[Fraction]]


def f(x: int | Fraction) -> Fraction:
    return x if isinstance(x, Fraction) else Fraction(x, 1)


def identity(n: int) -> Matrix:
    return [[Fraction(1 if i == j else 0, 1) for j in range(n)] for i in range(n)]


def transpose(A: Matrix) -> Matrix:
    return [list(row) for row in zip(*A)]


def matmul(A: Matrix, B: Matrix) -> Matrix:
    if not A or not B:
        return []
    m, k, n = len(A), len(A[0]), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(n)] for i in range(m)]


def submatrix(A: Matrix, rows: List[int], cols: List[int]) -> Matrix:
    return [[A[i][j] for j in cols] for i in rows]


def mat_sub(A: Matrix, B: Matrix) -> Matrix:
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def determinant(A: Matrix) -> Fraction:
    n = len(A)
    if n == 0:
        return Fraction(1, 1)
    M = [row[:] for row in A]
    det = Fraction(1, 1)
    for i in range(n):
        pivot = None
        for r in range(i, n):
            if M[r][i] != 0:
                pivot = r
                break
        if pivot is None:
            return Fraction(0, 1)
        if pivot != i:
            M[i], M[pivot] = M[pivot], M[i]
            det *= -1
        piv = M[i][i]
        det *= piv
        for r in range(i + 1, n):
            factor = M[r][i] / piv
            if factor:
                for c in range(i, n):
                    M[r][c] -= factor * M[i][c]
    return det


def inverse(A: Matrix) -> Matrix:
    n = len(A)
    M = [A[i][:] + identity(n)[i] for i in range(n)]
    for i in range(n):
        pivot = None
        for r in range(i, n):
            if M[r][i] != 0:
                pivot = r
                break
        if pivot is None:
            raise ValueError("singular matrix")
        if pivot != i:
            M[i], M[pivot] = M[pivot], M[i]
        piv = M[i][i]
        M[i] = [x / piv for x in M[i]]
        for r in range(n):
            if r == i:
                continue
            factor = M[r][i]
            if factor:
                M[r] = [M[r][c] - factor * M[i][c] for c in range(2 * n)]
    return [row[n:] for row in M]


def is_symmetric(A: Matrix) -> bool:
    return all(A[i][j] == A[j][i] for i in range(len(A)) for j in range(len(A)))


def leading_principal_minors_positive(A: Matrix) -> bool:
    return all(determinant(submatrix(A, list(range(k)), list(range(k)))) > 0 for k in range(1, len(A) + 1))


def diag_right(A: Matrix, d: List[Fraction]) -> Matrix:
    return [[A[i][j] * d[j] for j in range(len(A))] for i in range(len(A))]


def cartan_A(n: int) -> Tuple[Matrix, List[Fraction]]:
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][i] = 2
    for i in range(n - 1):
        A[i][i + 1] = -1
        A[i + 1][i] = -1
    return A, [Fraction(1) for _ in range(n)]


def cartan_B(n: int) -> Tuple[Matrix, List[Fraction]]:
    A, d = cartan_A(n)
    if n >= 2:
        A[n - 2][n - 1] = -2
        A[n - 1][n - 2] = -1
        d = [Fraction(1) for _ in range(n - 1)] + [Fraction(1, 2)]
    return A, d


def cartan_C(n: int) -> Tuple[Matrix, List[Fraction]]:
    A, d = cartan_A(n)
    if n >= 2:
        A[n - 2][n - 1] = -1
        A[n - 1][n - 2] = -2
        d = [Fraction(1) for _ in range(n - 1)] + [Fraction(2)]
    return A, d


def cartan_D(n: int) -> Tuple[Matrix, List[Fraction]]:
    if n < 4:
        raise ValueError("D_n requires n >= 4")
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][i] = 2
    for i in range(n - 3):
        A[i][i + 1] = -1
        A[i + 1][i] = -1
    branch = n - 3
    A[branch][n - 2] = A[n - 2][branch] = -1
    A[branch][n - 1] = A[n - 1][branch] = -1
    return A, [Fraction(1) for _ in range(n)]


def cartan_E6() -> Tuple[Matrix, List[Fraction]]:
    # Bourbaki-like tree: 1-3-4-5-6 and 2-3
    n = 6
    edges = [(0,2),(1,2),(2,3),(3,4),(4,5)]
    return simply_laced_from_edges(n, edges)


def cartan_E7() -> Tuple[Matrix, List[Fraction]]:
    n = 7
    edges = [(0,2),(1,2),(2,3),(3,4),(4,5),(5,6)]
    return simply_laced_from_edges(n, edges)


def cartan_E8() -> Tuple[Matrix, List[Fraction]]:
    n = 8
    edges = [(0,2),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7)]
    return simply_laced_from_edges(n, edges)


def simply_laced_from_edges(n: int, edges: List[Tuple[int, int]]) -> Tuple[Matrix, List[Fraction]]:
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][i] = 2
    for i, j in edges:
        A[i][j] = A[j][i] = -1
    return A, [Fraction(1) for _ in range(n)]


def cartan_F4() -> Tuple[Matrix, List[Fraction]]:
    A = [[Fraction(0) for _ in range(4)] for _ in range(4)]
    for i in range(4):
        A[i][i] = 2
    A[0][1] = A[1][0] = -1
    A[1][2] = -2
    A[2][1] = -1
    A[2][3] = A[3][2] = -1
    d = [Fraction(1), Fraction(1), Fraction(1, 2), Fraction(1, 2)]
    return A, d


def cartan_G2() -> Tuple[Matrix, List[Fraction]]:
    A = [[Fraction(2), Fraction(-3)], [Fraction(-1), Fraction(2)]]
    d = [Fraction(1), Fraction(1, 3)]
    return A, d


def audit_set() -> List[Tuple[str, Matrix, List[Fraction]]]:
    items: List[Tuple[str, Matrix, List[Fraction]]] = []
    for n in range(1, 9):
        A, d = cartan_A(n); items.append((f"A{n}", A, d))
    for n in range(2, 9):
        A, d = cartan_B(n); items.append((f"B{n}", A, d))
    for n in range(2, 9):
        A, d = cartan_C(n); items.append((f"C{n}", A, d))
    for n in range(4, 9):
        A, d = cartan_D(n); items.append((f"D{n}", A, d))
    for name, fn in [("E6", cartan_E6), ("E7", cartan_E7), ("E8", cartan_E8), ("F4", cartan_F4), ("G2", cartan_G2)]:
        A, d = fn(); items.append((name, A, d))
    assert len(items) == 32, len(items)
    return items


def frac_str(x: Fraction | int) -> str:
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def matrix_summary(A: Matrix) -> Dict[str, Any]:
    return {
        "rank": len(A),
        "determinant": frac_str(determinant(A)),
        "max_abs_entry": frac_str(max(abs(x) for row in A for x in row)),
    }


def schur_single_deletion_checks(G: Matrix) -> List[Dict[str, Any]]:
    n = len(G)
    checks = []
    for remove in range(n):
        keep = [i for i in range(n) if i != remove]
        if not keep:
            checks.append({"removed_node": remove + 1, "skipped_rank_one": True})
            continue
        GUU = submatrix(G, keep, keep)
        GUW = submatrix(G, keep, [remove])
        GWU = submatrix(G, [remove], keep)
        GWW = submatrix(G, [remove], [remove])
        invGWW = inverse(GWW)
        correction = matmul(matmul(GUW, invGWW), GWU)
        S = mat_sub(GUU, correction)
        checks.append({
            "removed_node": remove + 1,
            "pivot_positive": GWW[0][0] > 0,
            "correction_max_abs_entry": frac_str(max(abs(x) for row in correction for x in row)) if correction else "0",
            "schur_positive_definite": leading_principal_minors_positive(S),
            "schur_det": frac_str(determinant(S)),
        })
    return checks


def validate_cartan(A: Matrix) -> List[str]:
    errors = []
    n = len(A)
    for i in range(n):
        if A[i][i] != 2:
            errors.append(f"diagonal {i+1} is not 2")
        for j in range(n):
            if i == j:
                continue
            if A[i][j] > 0:
                errors.append(f"off diagonal {i+1},{j+1} positive")
            if A[i][j].denominator != 1:
                errors.append(f"off diagonal {i+1},{j+1} non-integral")
    return errors


def run_audit() -> Dict[str, Any]:
    failures = []
    systems = []
    for name, A, d in audit_set():
        errors = validate_cartan(A)
        G = diag_right(A, d)
        sym = is_symmetric(G)
        pd = leading_principal_minors_positive(G)
        schur = schur_single_deletion_checks(G)
        if errors or not sym or not pd or not all(c.get("schur_positive_definite", True) for c in schur):
            failures.append({
                "type": name,
                "errors": errors,
                "metric_symmetric": sym,
                "metric_positive_definite": pd,
                "schur_failures": [c for c in schur if not c.get("schur_positive_definite", True)],
            })
        systems.append({
            "type": name,
            "rank": len(A),
            "cartan": matrix_summary(A),
            "symmetrizer_d_epsilon": [frac_str(x) for x in d],
            "metric_G_equals_A_times_D_epsilon": matrix_summary(G),
            "metric_symmetric": sym,
            "metric_positive_definite": pd,
            "non_simply_laced": any(x != 1 for x in d),
            "finite_rank_margin_model_note": "No uniform asymptotic gap is claimed; strict finite-rank bounds are the theorem target.",
            "schur_single_deletion_checks": schur,
        })
    return {
        "package": "AXEZENT-AI-OPAC018-Green-Schur-Bridge",
        "version": "1.5.0",
        "audit_type": "pure_python_exact_arithmetic_sanity_audit",
        "library_dependencies": [],
        "passed": len(failures) == 0,
        "total_types": len(systems),
        "failures": failures,
        "systems": systems,
        "truth_boundary": "This audit supports reproducibility and exact arithmetic sanity checks. It does not replace independent proof review.",
        "output": "receipts/opac18_green_schur_pure_python_results.json",
    }


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result = run_audit()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "passed": result["passed"],
        "total_types": result["total_types"],
        "failures": result["failures"],
        "output": result["output"],
    }, indent=2, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
