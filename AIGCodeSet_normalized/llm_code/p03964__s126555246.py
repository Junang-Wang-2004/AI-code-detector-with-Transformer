from math import gcd
from math import ceil
v1 = int(input())
v2 = [0] * v1
v3 = [0] * v1
for v4 in range(v1):
    v2[v4], v3[v4] = map(int, input().split())
v5 = 2
v6, v7 = (v2[0], v3[0])
for v4 in range(1, v1):
    v8, v9 = (v2[v4], v3[v4])
    v10, v11 = (ceil(v6 / v8), ceil(v7 / v9))
    v12 = max(v10, v11)
    v6, v7 = (v12 * v8, v12 * v9)
print(v6 + v7)
