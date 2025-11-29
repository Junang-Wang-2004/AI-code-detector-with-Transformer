v1 = int(input())
v2 = list(map(int, input().split()))
import math
from itertools import permutations
v3 = [0] * v1
for v4 in range(v1):
    v3[v4] = v4
v5 = math.factorial(v1)
v6 = [0] * v5
v4 = 0
for v7 in permutations(v3, v1):
    v8 = 0
    for v9 in range(v1):
        v8 += abs(v7[v9] - v9) * v2[v9]
    v6[v4] = v8
    v4 += 1
print(max(v6))
