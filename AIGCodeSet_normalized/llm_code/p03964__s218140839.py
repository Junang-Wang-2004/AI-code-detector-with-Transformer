import math
v1 = int(input())
v2, v3 = list(map(int, input().split()))
v4 = v2 + v3
v5 = v2
v6 = v3
for v7 in range(1, v1):
    v2, v3 = list(map(int, input().split()))
    v8 = max(math.ceil(v4 / (v2 + v3)), math.ceil(v5 / v2), math.ceil(v6 / v3))
    v9 = v8 * (v2 + v3)
    v5 = v8 * v2
    v6 = v8 * v3
print(v9)
