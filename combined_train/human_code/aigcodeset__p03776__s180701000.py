from collections import Counter
v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v4.sort(reverse=True)
v5 = Counter(v4)
v6 = sum(v4[:v2]) / v2
v7 = 0
from operator import mul
from functools import reduce

def f1(a1, a2):
    a2 = min(a1 - a2, a2)
    if a2 == 0:
        return 1
    v2 = reduce(mul, range(a1, a1 - a2, -1))
    v3 = reduce(mul, range(1, a2 + 1))
    return v2 // v3
v8 = v4[v2 - 1]
v9 = v5[v8]
v10 = Counter(v4[:v2])
v11 = v10[v8]
for v12 in range(v2 - 1, v3):
    v13 = v4[v12]
    if v12 != v2 - 1:
        if v13 != v4[0]:
            break
    v7 += f1(v9, v12 + 1 - (v2 - v11))
print(v6)
print(v7)
