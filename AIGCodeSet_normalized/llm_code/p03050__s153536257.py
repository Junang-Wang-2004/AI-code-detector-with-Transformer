import math
from itertools import combinations

def f1(a1):
    v1 = 2
    v2 = []
    while v1 * v1 <= a1:
        while a1 % v1 == 0:
            a1 //= v1
            v2.append(v1)
        v1 = v1 + 1
    if a1 > 1:
        v2.append(a1)
    return v2

def f2(a1):
    v1 = 1
    for v2 in a1:
        v1 *= v2
    return v1
v1 = int(input())
v2 = f1(v1)
v3 = []
for v4 in range(len(v2)):
    v3 += [a for v5 in combinations(v2, v4 + 1)]
v3 = set(v3)
v6 = 0
for v5 in v3:
    v7 = f2(v5)
    if v7 < math.sqrt(v1):
        continue
    v8 = v1 // v7
    v9 = v1 % v7
    if v8 == v9:
        v6 += v7
print(v6)
