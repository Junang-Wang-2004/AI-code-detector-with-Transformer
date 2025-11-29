import math
import itertools
v1 = int(input())
v2 = []
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    v2.append((v4, v5))
v6 = 0
for v7 in itertools.permutations(range(v1)):
    v8 = 0
    for v9 in range(v1 - 1):
        v10, v11 = v2[v7[v9]]
        v12, v13 = v2[v7[v9 + 1]]
        v8 += math.sqrt((v10 - v12) ** 2 + (v11 - v13) ** 2)
    v6 += v8
v14 = v6 / math.factorial(v1)
print(v14)
