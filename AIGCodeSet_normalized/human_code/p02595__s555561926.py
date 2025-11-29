import math
v1, v2 = (int(x) for v3 in input().split())
v4 = 0
for v5 in range(v1):
    v6, v7 = (int(v3) for v3 in input().split())
    v8 = math.sqrt(v6 * v6 + v7 * v7)
    if v2 >= v8:
        v4 += 1
print(v4)
