import sys
sys.setrecursionlimit(10 ** 9)
v1, v2 = map(int, input().split())
v3 = [[] for v4 in range(v1)]
for v4 in range(v1 - 1):
    v5, v6 = map(lambda x: int(x) - 1, input().split())
    v3[v5].append(v6)
    v3[v6].append(v5)
v7 = [len(E) for v8 in v3]
v9 = 10 ** 9 + 7
v5 = 10 ** 5 + 1
v10 = [1] * (v5 + 1)
for v4 in range(1, len(v10)):
    v10[v4] = v10[v4 - 1] * v4 % v9
v11 = [1] * (v5 + 1)
v11[v5] = pow(v10[v5], v9 - 2, v9)
for v4 in range(v5 - 1, 0, -1):
    v11[v4] = v11[v4 + 1] * (v4 + 1) % v9

def f1(a1, a2):
    if a2 < 0 or a1 < a2:
        return 0
    return v10[a1] * v11[a1 - a2] % v9

def f2(a1, a2=None):
    if a2 is None:
        v1 = f1(v2, v7[a1] + 1)
    else:
        v1 = f1(v2 - 2, v7[a1] - 1)
    for v2 in v3[a1]:
        if v2 == a2:
            continue
        v1 *= f2(v2, parent=a1)
        v1 %= v9
    return v1
v12 = f2(0, parent=None)
print(v12)
