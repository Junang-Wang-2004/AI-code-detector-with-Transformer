import numpy as np
v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 1000000
v4 = [[] for v5 in range(v1 + 1)]
v4[0] = [1000, 0]
for v6 in range(v1):
    for v7 in v4[v6]:
        v4[v6 + 1].append(v7)
        if v7[0] >= v2[v6]:
            v4[v6 + 1].append([v7[0] - v2[v6], v7[1] + 1])
        if v7[1] > 0:
            v4[v6 + 1].append([v7[0] + v7[1] * v2[v6], v7[1] - 1])
v8 = 0
for v6 in v4[v1]:
    if v6[0] > v8:
        v8 = v6[0]
print(v8)
