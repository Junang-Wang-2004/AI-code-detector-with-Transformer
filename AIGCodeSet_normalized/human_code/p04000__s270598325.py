from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
v1, v2, v3 = [int(item) for v4 in input().split()]
v5 = defaultdict(int)
for v6 in range(v3):
    v7, v8 = [int(v4) - 1 for v4 in input().split()]
    for v9 in range(-1, 2):
        for v10 in range(-1, 2):
            v5[v7 + v9, v8 + v10] += 1
v11 = [0] * 10
for v12 in v5.keys():
    if v12[0] < 1 or v12[1] < 1 or v12[0] >= v1 - 1 or (v12[1] >= v2 - 1):
        continue
    v11[v5[v12]] += 1
v13 = (v2 - 2) * (v1 - 2)
v11[0] = v13 - sum(v11)
for v4 in v11:
    print(v4)
