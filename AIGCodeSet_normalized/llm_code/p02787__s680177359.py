import math
v1, v2 = map(int, input().split())
v3 = [math.inf] * (v1 + 1)
v3[0] = 0
for v4 in range(v2):
    v5, v6 = map(int, input().split())
    for v7 in range(v1 - v5 + 1):
        v3[v7] = min(v3[v7], v3[v7 - v5] + v6)
print(v3[v1 - 1])
