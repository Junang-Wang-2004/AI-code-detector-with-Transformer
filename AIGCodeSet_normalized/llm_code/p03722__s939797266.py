v1, v2 = map(int, input().split())
v3 = 10 ** 13
from collections import defaultdict
v4 = defaultdict(set)
for v5 in range(v2):
    v6, v7, v8 = map(int, input().split())
    v4[v6].add((v7, v8))

def f1(a1, a2, a3, a4):
    if a1 == v1:
        return max(a2, a4)
    if len(v4[a1]) == 0:
        return a4
    for v1, v2 in v4[a1]:
        if a4 > v3:
            return a4
        if v1 in a3:
            return float('inf')
        a4 = f1(v1, a2 + v2, a3 | {a1}, a4)
    return a4
print(f1(1, 0, set(), -1 * float('inf')))
