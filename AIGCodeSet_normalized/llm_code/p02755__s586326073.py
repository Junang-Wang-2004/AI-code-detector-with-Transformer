import math
v1, v2 = map(int, input().split())
v3 = -1
for v4 in range(1, 10000):
    if math.floor(v4 * 0.08) == v1 and math.floor(v4 * 0.1) == v2:
        v3 = v4
        break
print(v3)
