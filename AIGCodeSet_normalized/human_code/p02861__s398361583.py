import itertools
import math
v1 = int(input())
v2 = []
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    v2.append([v4, v5])
v6 = itertools.permutations(v2, v1)
v7 = 0
for v8 in v6:
    for v3 in range(v1 - 1):
        v7 += ((v8[v3][0] - v8[v3 + 1][0]) ** 2 + (v8[v3][1] - v8[v3 + 1][1]) ** 2) ** 0.5
print(v7 / math.factorial(v1))
