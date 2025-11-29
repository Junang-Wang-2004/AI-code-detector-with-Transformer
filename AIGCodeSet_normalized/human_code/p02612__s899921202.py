import math
v1 = int(input())
v2 = 10 ** 6
for v3 in range(1, math.ceil(v1 / 1000) + 1):
    v4 = v1 - v3 * 1000
    if v4 <= 0:
        v2 = min(v2, abs(v4))
print(v2)
