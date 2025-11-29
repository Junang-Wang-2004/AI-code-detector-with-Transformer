import itertools
import math
v1 = int(input())
v2 = [list(map(int, input().split())) for v3 in range(v1)]
v4 = 0
for v5 in itertools.permutations(range(v1)):
    v6 = 0
    for v7 in range(v1 - 1):
        v8, v9 = v2[v5[v7]]
        v10, v11 = v2[v5[v7 + 1]]
        v6 += math.sqrt((v8 - v10) ** 2 + (v9 - v11) ** 2)
    v4 += v6
v12 = v4 / math.factorial(v1)
print(v12)
