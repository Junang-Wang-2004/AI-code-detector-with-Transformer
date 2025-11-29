import bisect
from numpy import cumsum
v1 = 5
v2 = int(input())
v3 = [[int(item) for v4 in input().split()] for v5 in range(v2)]

def f1(a1):
    v1 = [True for v5 in range(a1 + 1)]
    v1[0] = False
    v1[1] = False
    for v2 in range(2, int(a1 ** 0.5) + 1):
        if not v1[v2]:
            continue
        for v3 in range(v2 * 2, a1 + 1, v2):
            v1[v3] = False
    return [v2 for v2 in range(a1 + 1) if v1[v2]]
v6 = f1(10 ** v1)
v7 = [0] * (10 ** v1 + 1)
for v8 in v6:
    if v8 % 4 == 1 or v8 == 3:
        v9 = bisect.bisect_left(v6, (v8 + 1) // 2)
        if v6[v9] == (v8 + 1) // 2:
            v7[v8] = 1
v10 = cumsum(v7)
for v11, v12 in v3:
    print(v10[v12] - v10[v11 - 1])
