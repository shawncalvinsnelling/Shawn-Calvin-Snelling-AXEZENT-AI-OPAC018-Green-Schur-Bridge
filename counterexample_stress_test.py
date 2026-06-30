#!/usr/bin/env python3
"""Counterexample and stress-test protocol.

The goal is not to prove OPAC-018, but to document inputs that should be
rejected or treated as outside the theorem hypotheses.
"""
from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json
from typing import List

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "receipts" / "counterexample_stress_test_results.json"


def determinant(A: List[List[Fraction]]) -> Fraction:
    n = len(A)
    M = [row[:] for row in A]
    det = Fraction(1)
    for i in range(n):
        pivot = None
        for r in range(i, n):
            if M[r][i] != 0:
                pivot = r
                break
        if pivot is None:
            return Fraction(0)
        if pivot != i:
            M[i], M[pivot] = M[pivot], M[i]
            det *= -1
        piv = M[i][i]
        det *= piv
        for r in range(i + 1, n):
            factor = M[r][i] / piv
            for c in range(i, n):
                M[r][c] -= factor * M[i][c]
    return det


def is_cartan_like(A: List[List[Fraction]]) -> bool:
    n = len(A)
    if any(len(row) != n for row in A):
        return False
    for i in range(n):
        if A[i][i] != 2:
            return False
        for j in range(n):
            if i == j:
                continue
            if A[i][j] > 0:
                return False
            if A[i][j].denominator != 1:
                return False
            if A[i][j] == 0 and A[j][i] != 0:
                return False
    return True


def positive_definite_rough(A: List[List[Fraction]]) -> bool:
    return all(determinant([row[:k] for row in A[:k]]) > 0 for k in range(1, len(A) + 1))


def run() -> dict:
    cases = []

    tests = [
        {
            "name": "affine_A1_like_degenerate",
            "matrix": [[Fraction(2), Fraction(-2)], [Fraction(-2), Fraction(2)]],
            "expected": "reject_positive_definiteness",
        },
        {
            "name": "dense_fractional_not_cartan",
            "matrix": [[Fraction(2), Fraction(-1, 2), Fraction(-1, 3)], [Fraction(-1, 2), Fraction(2), Fraction(-1, 2)], [Fraction(-1, 3), Fraction(-1, 2), Fraction(2)]],
            "expected": "reject_nonintegral_cartan_entries",
        },
        {
            "name": "positive_off_diagonal_not_root_cartan",
            "matrix": [[Fraction(2), Fraction(1)], [Fraction(-1), Fraction(2)]],
            "expected": "reject_positive_off_diagonal",
        },
        {
            "name": "non_square_input",
            "matrix": [[Fraction(2), Fraction(-1), Fraction(0)], [Fraction(-1), Fraction(2)]],
            "expected": "reject_non_square",
        },
        {
            "name": "missing_crystallographic_integrality_symbolic_H2_like",
            "matrix": "[[2, -phi], [-phi, 2]]",
            "expected": "outside_crystallographic_scope",
        },
    ]

    unexpected_acceptances = []
    for t in tests:
        m = t["matrix"]
        if isinstance(m, str):
            accepted = False
            reason = "symbolic irrational matrix is outside exact crystallographic integer Cartan audit"
        else:
            accepted = is_cartan_like(m) and positive_definite_rough(m)
            reason = "accepted by rough checks" if accepted else "rejected by rough hypothesis checks"
        if accepted:
            unexpected_acceptances.append(t["name"])
        cases.append({
            "name": t["name"],
            "expected": t["expected"],
            "accepted": accepted,
            "reason": reason,
        })

    return {
        "package": "AXEZENT-AI-OPAC018-Green-Schur-Bridge",
        "version": "1.5.0",
        "audit_type": "counterexample_stress_test_protocol",
        "passed": not unexpected_acceptances,
        "total_cases": len(cases),
        "unexpected_acceptances": unexpected_acceptances,
        "cases": cases,
        "truth_boundary": "Stress tests document expected rejection/out-of-scope behavior. They do not prove OPAC-018.",
        "output": "receipts/counterexample_stress_test_results.json",
    }


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    result = run()
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "passed": result["passed"],
        "total_cases": result["total_cases"],
        "unexpected_acceptances": result["unexpected_acceptances"],
        "output": result["output"],
    }, indent=2, sort_keys=True))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
