import math
v1 = int(input())
v2 = [[] for v3 in range(v1)]
for v3 in range(v1 - 1):
    v4, v5 = map(lambda x: int(x) - 1, input().split())
    v2[v4].append(v5)
    v2[v5].append(v4)
v6 = [[0] * v1 for v3 in range(2)]

def f1(a1, a2, a3, a4=0):
    for v1 in v2[a2]:
        if v1 != a3:
            v6[a4][v1] = a1
            f1(a1 + 1, v1, a2, a4)
f1(1, 0, -1, 0)
f1(1, v1 - 1, -1, 1)
v7 = 0
for v8, v9 in zip(v6[0], v6[1]):
    if v8 <= v9:
        v7 += 1
print('Fennec' if v7 * 2 > v1 else 'Snuke')
