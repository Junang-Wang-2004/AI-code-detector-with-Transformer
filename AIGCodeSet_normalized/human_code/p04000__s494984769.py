import collections
import sys
input = sys.stdin.readline
v1, v2, v3 = [int(v) for v4 in input().split()]
v5 = [0 for v6 in range(10)]
v5[0] = (v1 - 2) * (v2 - 2)
v7 = collections.Counter([])
v8 = [[v6, j] for v6 in range(-1, 2) for v9 in range(-1, 2)]

def f1(a1, a2):
    return a1 * 10 ** 9 + a2
for v6 in range(v3):
    v10, v11 = [int(v4) - 1 for v4 in input().split()]
    for v9 in v8:
        v12, v13 = v9
        if 1 <= v12 + v10 <= v1 - 2 and 1 <= v13 + v11 <= v2 - 2:
            v14 = v7[f1(v12 + v10, v13 + v11)]
            v7[f1(v12 + v10, v13 + v11)] += 1
            v5[v14] -= 1
            v5[v14 + 1] += 1
for v6 in v5:
    print(v6)
