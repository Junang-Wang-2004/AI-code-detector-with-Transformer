v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v4 = sorted(v4)[::-1]

def f1(a1):
    v1 = 0
    for v2 in range(v1):
        v1 += v4[v2] - a1
        if v2 - 1 <= v2 and v2 <= v3 - 1 and (v1 >= 0):
            return True
    return False
v5 = 0
v6 = 10 ** 15 + 1
for v7 in range(10 ** 5):
    v8 = (v5 + v6) / 2
    if f1(v8):
        v5 = v8
    else:
        v6 = v8
print(v5)
import math

def f2(a1, a2):
    return math.factorial(a1) // (math.factorial(a1 - a2) * math.factorial(a2))
v9 = 0
from collections import Counter
v10 = Counter(v4)
for v11 in range(v2, v3 + 1):
    v12 = v5 * v11
    v13 = []
    for v7 in range(v11):
        v13.append(v4[v7])
    if sum(v13) != v12:
        continue
    v14 = 1
    v15 = Counter(v13)
    for v16 in v15.keys():
        v14 *= f2(v10[v16], v15[v16])
    v9 += v14
print(v9)
