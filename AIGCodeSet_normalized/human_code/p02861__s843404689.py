import math
import itertools
v1 = int(input())
v2 = {}
for v3 in range(v1):
    v2[v3] = list(map(int, input().split()))
v4 = [v2[x] for v5 in range(len(v2))]
v6 = list(itertools.permutations(v4))

def f1(a1):
    v1 = 0
    for v2 in range(len(a1) - 1):
        v1 += math.sqrt(pow(a1[v2][0] - a1[v2 + 1][0], 2) + pow(a1[v2][1] - a1[v2 + 1][1], 2))
    return v1
v7 = 0
for v8 in v6:
    v7 += f1(v8)
print(v7 / len(v6))
