# Inter-coder reliability of the instrument checklist, and the rebuild of the facet data from the blind full coding.
# Run: py -I research/hs_reliability.py research/hs_coder_a2.json research/hs_coder_b.json
#   prints Krippendorff's alpha on the cells and the correlation of the two coders' distances over the shared regions,
#   writes research/hs_reliability.json, and rewrites facets.json / facets.js with the full coder's checklist.
import json, itertools, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FULL, SECOND = sys.argv[1], sys.argv[2]
F = json.load(open(os.path.join(HERE, "facets.json"), encoding="utf-8"))
A = json.load(open(FULL, encoding="utf-8"))["regions"]; B = json.load(open(SECOND, encoding="utf-8"))["regions"]
T, tree = F["types"], F["tree"]
assert len(A) == 54 and all(set(A[r]) == set(T) and all(A[r][t] in (0, 1) for t in T) for r in A), "full coding incomplete"
assert all(set(B[r]) == set(T) for r in B)
R = sorted(B)
def kalpha(pairs):
    n = 2 * len(pairs); c1 = sum(a + b for a, b in pairs); c0 = n - c1
    return 1 - (sum(a != b for a, b in pairs) / len(pairs)) / (2 * c0 * c1 / (n * (n - 1)))
H = {"root": 1}; H.update({k: v[1] for k, v in tree.items()})
def comp(c):
    k = sum(c.values()); return {t: 1 / k for t in c if c[t]}
def emd(p, q):
    P, Q = {}, {}
    for m, M in ((p, P), (q, Q)):
        for k, w in m.items():
            x = k
            while x != "root": M[x] = M.get(x, 0) + w; x = tree[x][0]
    return sum(((1 if tree[v][0] == "root" else H[tree[v][0]]) - H[v]) * abs(P.get(v, 0) - Q.get(v, 0)) for v in tree) / 2
def corr(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sum((a - mx) ** 2 for a in x) ** .5 * sum((b - my) ** 2 for b in y) ** .5)
pairs = [(A[r][t], B[r][t]) for r in R for t in T]
da, db = [], []
for x, y in itertools.combinations(R, 2):
    da.append(emd(comp(A[x]), comp(A[y]))); db.append(emd(comp(B[x]), comp(B[y])))
res = {"coders": ["A2 (all 54, blind)", "B (18, blind)"], "regions": R, "cells": len(pairs),
       "agreement": round(1 - sum(a != b for a, b in pairs) / len(pairs), 3), "alpha": round(kalpha(pairs), 3),
       "dist_r": round(corr(da, db), 3),
       "present_median": {"A2": sorted(sum(A[r].values()) for r in R)[9], "B": sorted(sum(B[r].values()) for r in R)[9]},
       "disputed": sorted(((t, sum(A[r][t] != B[r][t] for r in R)) for t in T), key=lambda x: -x[1])[:10]}
json.dump(res, open(os.path.join(HERE, "hs_reliability.json"), "w", encoding="utf-8"), indent=1)
print(json.dumps(res, indent=1))
F["hs"] = A; F["hs_source"] = "blind full coding (A2)"; F["hs_rel"] = res["dist_r"]
json.dump(F, open(os.path.join(HERE, "facets.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(HERE, "facets.js"), "w", encoding="utf-8").write("window.FACDATA=" + json.dumps(F, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("facets.js rebuilt with A2")
