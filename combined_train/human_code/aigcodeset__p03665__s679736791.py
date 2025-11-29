from operator import mul
from functools import reduce

def f1(a1, a2):
    a2 = min(a1 - a2, a2)
    if a2 == 0:
        return 1
    v2 = reduce(mul, range(a1, a1 - a2, -1))
    v3 = reduce(mul, range(1, a2 + 1))
    return v2 // v3
v1, v2 = map(int, input().split())
v3 = list(map(int, input().split()))
v4 = sum([a % 2 == 0 for v5 in v3])
v6 = sum([v5 % 2 != 0 for v5 in v3])
v7 = 0
if v2 == 0:
    v7 += 1
for v8 in range(1, v1 + 1):
    for v9 in range(0, v8 + 1):
        v10 = v8 - v9
        if v9 > v4 or v10 > v6:
            continue
        if v2 == 0 and v10 % 2 == 0:
            v7 += f1(v4, v9) * f1(v6, v10)
        elif v2 == 1 and v10 % 2 == 1:
            v7 += f1(v4, v9) * f1(v6, v10)
print(v7)
