# SageMath audit script for OPAC-018 Green-Schur package.
# This script mirrors the pure-Python audit at a high level and writes a JSON receipt.
# It is audit support, not a substitute for mathematical referee review.

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "receipts" / "opac18_green_schur_sage_results.json"

QQ = RationalField()

def cartan_A(n):
    A = matrix(QQ, n, n, 0)
    for i in range(n):
        A[i,i] = 2
    for i in range(n-1):
        A[i,i+1] = -1
        A[i+1,i] = -1
    return A, [QQ(1)]*n

def cartan_B(n):
    A, d = cartan_A(n)
    if n >= 2:
        A[n-2,n-1] = -2
        A[n-1,n-2] = -1
        d = [QQ(1)]*(n-1) + [QQ(1)/2]
    return A, d

def cartan_C(n):
    A, d = cartan_A(n)
    if n >= 2:
        A[n-2,n-1] = -1
        A[n-1,n-2] = -2
        d = [QQ(1)]*(n-1) + [QQ(2)]
    return A, d

def cartan_D(n):
    A = matrix(QQ, n, n, 0)
    for i in range(n):
        A[i,i] = 2
    for i in range(n-3):
        A[i,i+1] = -1
        A[i+1,i] = -1
    branch = n-3
    A[branch,n-2] = A[n-2,branch] = -1
    A[branch,n-1] = A[n-1,branch] = -1
    return A, [QQ(1)]*n

def simply_laced(n, edges):
    A = matrix(QQ, n, n, 0)
    for i in range(n):
        A[i,i] = 2
    for i,j in edges:
        A[i,j] = A[j,i] = -1
    return A, [QQ(1)]*n

def audit_set():
    items = []
    for n in range(1,9):
        A,d = cartan_A(n); items.append((f"A{n}", A, d))
    for n in range(2,9):
        A,d = cartan_B(n); items.append((f"B{n}", A, d))
    for n in range(2,9):
        A,d = cartan_C(n); items.append((f"C{n}", A, d))
    for n in range(4,9):
        A,d = cartan_D(n); items.append((f"D{n}", A, d))
    extras = [
        ("E6", simply_laced(6, [(0,2),(1,2),(2,3),(3,4),(4,5)])),
        ("E7", simply_laced(7, [(0,2),(1,2),(2,3),(3,4),(4,5),(5,6)])),
        ("E8", simply_laced(8, [(0,2),(1,2),(2,3),(3,4),(4,5),(5,6),(6,7)])),
    ]
    for name, pair in extras:
        A,d = pair; items.append((name,A,d))
    F = matrix(QQ, 4, 4, 0)
    for i in range(4): F[i,i] = 2
    F[0,1] = F[1,0] = -1
    F[1,2] = -2; F[2,1] = -1
    F[2,3] = F[3,2] = -1
    items.append(("F4", F, [QQ(1), QQ(1), QQ(1)/2, QQ(1)/2]))
    G = matrix(QQ, [[2,-3],[-1,2]])
    items.append(("G2", G, [QQ(1), QQ(1)/3]))
    return items

def frac_str(x):
    return str(x.numerator()) if x.denominator() == 1 else f"{x.numerator()}/{x.denominator()}"

def leading_pd(M):
    return all(M[:k,:k].det() > 0 for k in range(1, M.nrows()+1))

def diag_right(A, d):
    D = diagonal_matrix(QQ, d)
    return A * D

systems = []
failures = []
for name, A, d in audit_set():
    G = diag_right(A,d)
    sym = (G == G.transpose())
    pd = leading_pd(G)
    if (not sym) or (not pd):
        failures.append({"type": name, "metric_symmetric": bool(sym), "metric_positive_definite": bool(pd)})
    systems.append({
        "type": name,
        "rank": int(A.nrows()),
        "cartan_det": frac_str(A.det()),
        "metric_det": frac_str(G.det()),
        "metric_symmetric": bool(sym),
        "metric_positive_definite": bool(pd),
        "symmetrizer_d_epsilon": [frac_str(x) for x in d],
    })

result = {
    "package": "AXEZENT-AI-OPAC018-Green-Schur-Bridge",
    "version": "1.5.0",
    "audit_type": "sage_exact_arithmetic_sanity_audit",
    "passed": len(failures) == 0,
    "total_types": len(systems),
    "failures": failures,
    "systems": systems,
    "truth_boundary": "Sage audit support only; not a substitute for independent proof review.",
    "output": "receipts/opac18_green_schur_sage_results.json",
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
print(json.dumps({"passed": result["passed"], "total_types": result["total_types"], "failures": result["failures"], "output": result["output"]}, indent=2, sort_keys=True))
if not result["passed"]:
    raise SystemExit(1)
