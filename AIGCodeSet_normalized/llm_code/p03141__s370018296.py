v1 = int(input())
v2 = []
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2.append(v5)
    v3.append(v6)
import math

def f1(a1, a2):
    if a2 == 0 or a2 > len(a1):
        return []
    v1 = []
    f2(a1, a2, 0, [], v1)
    return v1

def f2(a1, a2, a3, a4, a5):
    if a2 == 0:
        a5.append(a4)
        return
    for v1 in range(a3, len(a1)):
        f2(a1, a2 - 1, v1 + 1, a4 + [a1[v1]], a5)
v7 = f1(range(v1), math.ceil(v1 / 2))
v8 = 0
for v9 in v7:
    v10 = 0
    v11 = 0
    for v12 in range(v1):
        if v12 in v9:
            v10 += v2[v12]
        else:
            v11 += v3[v12]
    if v8 < v10 - v11:
        v8 = v10 - v11
print(v8)
