"""Necessary-condition screen for additive maximal-entanglement EA codes.

SAT means that the enumerator constraints are feasible.  It does not prove a
code exists.  Requires z3-solver.
"""

import json
import math
import sys
import time

import z3


TABLE_II_EXTRA = [
    (18, 4, 12), (18, 5, 11), (18, 6, 10), (18, 7, 9), (18, 8, 9),
    (18, 9, 8), (18, 10, 7), (18, 11, 6), (19, 3, 14), (19, 4, 13),
    (19, 6, 11), (19, 7, 9), (19, 8, 9), (19, 11, 7), (19, 12, 6),
    (20, 6, 12), (20, 7, 10), (20, 8, 9), (20, 8, 10), (20, 9, 9),
    (20, 10, 8), (20, 11, 7), (20, 12, 7), (20, 13, 6),
]
EARLIER = [
    (12, 6, 6), (14, 5, 8), (14, 6, 7), (15, 4, 10), (15, 6, 8),
    (15, 7, 7), (16, 7, 8), (16, 8, 7), (17, 5, 10), (17, 6, 9),
    (17, 7, 8), (17, 8, 8), (17, 9, 7), (17, 13, 4),
]


def krawtchouk(n, j, weight):
    return sum((-1) ** s * 3 ** (j - s) * math.comb(weight, s) * math.comb(n - weight, j - s)
               for s in range(max(0, j - n + weight), min(weight, j) + 1))


def screen(n, k, distance):
    a = [z3.Int(f"a{i}") for i in range(n + 1)]
    b = [z3.Int(f"b{i}") for i in range(n + 1)]
    solver = z3.Solver()
    solver.set(timeout=15_000)
    solver.add(a[0] == 1, b[0] == 1, z3.Sum(a) == 4 ** k, z3.Sum(b) == 4 ** (n - k))
    solver.add(*[a[i] == 0 for i in range(1, distance)])
    for i in range(1, n + 1):
        solver.add(a[i] >= 0, b[i] >= 0, a[i] + b[i] <= math.comb(n, i) * 3 ** i)
    for j in range(n + 1):
        solver.add(4 ** k * b[j] == z3.Sum(krawtchouk(n, j, i) * a[i] for i in range(n + 1)))

    gauss_sum = z3.Sum((-1) ** i * a[i] for i in range(n + 1))
    solver.add(z3.Or(gauss_sum == 2 ** k, gauss_sum == -2 ** k))
    for j in range(1, n + 1):
        ambient = math.comb(n, j) * 3 ** j
        even_projection_count = z3.Int(f"p{j}")
        signed = z3.Sum((-1) ** i * krawtchouk(n, j, i) * a[i] for i in range(n + 1))
        solver.add(signed == 2 ** k * z3.If(gauss_sum > 0, 2 * even_projection_count - ambient,
                                             ambient - 2 * even_projection_count))
        solver.add(even_projection_count >= b[j] + (a[j] if j % 2 == 0 else 0))
        solver.add(ambient - even_projection_count >= (a[j] if j % 2 else 0))

    started = time.time()
    status = solver.check()
    result = {"n": n, "k": k, "d": distance, "status": str(status),
              "seconds": round(time.time() - started, 3)}
    if status == z3.sat:
        model = solver.model()
        result["A"] = [model.eval(x).as_long() for x in a]
        result["B"] = [model.eval(x).as_long() for x in b]
    return result


if __name__ == "__main__":
    parameters = TABLE_II_EXTRA if "--table-ii-extra" in sys.argv else EARLIER
    results = [screen(*parameter) for parameter in parameters]
    print(json.dumps({"warning": "SAT is only enumerator feasibility.", "results": results}, indent=2))
