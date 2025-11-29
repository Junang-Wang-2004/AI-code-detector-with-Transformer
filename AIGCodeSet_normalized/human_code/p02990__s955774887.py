from operator import mul
from functools import reduce

def f1(a1, a2):
    if a2 > a1:
        return 0
    a2 = min(a1 - a2, a2)
    if a2 == 0:
        return 1
    v2 = reduce(mul, range(a1, a1 - a2, -1))
    v3 = reduce(mul, range(1, a2 + 1))
    return v2 // v3
v1, v2 = map(int, input().split())
v3 = v1 - v2
for v4 in range(v2):
    v5 = f1(v2 - 1, v4)
    v6 = f1(v3 + 1, v4 + 1)
    v7 = v6 * v5 % (10 ** 9 + 7)
    print(v7)
