v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    v3.append([v5, v6])
v3.sort()
import math
v7 = [10 ** 20 for v4 in range(v1 + 1)]
v7[0] = 0
for v4 in range(v2):
    for v8 in range(v1 + 1):
        if v8 - v3[v4][0] >= 0:
            v7[v8] = min(v7[v8], v7[v8 - v3[v4][0]] + v3[v4][1])
print(v7[v1])
