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
v4, v5 = (0, 0)
for v6 in v3:
    if v6 % 2 == 0:
        v4 += 1
    else:
        v5 += 1
v7 = 0
if v2 == 0:
    v7 += 2 ** v4
    for v8 in range(2, v5 + 1, 2):
        v7 += f1(v5, v8)
else:
    v7 += 2 ** v4 * v5
    for v8 in range(1, v5 + 1, 2):
        v7 += f1(v5, v8)
print(v7)
