import math
import itertools
v1 = int(input())
v2 = []
for v3 in range(v1):
    v4, v5 = map(int, input().split())
    v2.append((v4, v5))
v6 = [[0] * v1 for v7 in range(v1)]
for v3 in range(v1):
    for v8 in range(v3 + 1, v1):
        v9, v10 = v2[v3]
        v11, v12 = v2[v8]
        v13 = math.sqrt((v9 - v11) ** 2 + (v10 - v12) ** 2)
        v6[v3][v8] = v13
        v6[v8][v3] = v13
v14 = 0
for v15 in itertools.permutations(range(v1)):
    for v3 in range(v1 - 1):
        v14 += v6[v15[v3]][v15[v3 + 1]]
v16 = v14 / math.factorial(v1)
print(v16)
