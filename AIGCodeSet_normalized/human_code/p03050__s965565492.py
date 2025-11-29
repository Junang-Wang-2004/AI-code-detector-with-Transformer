import math
v1 = int(input())
v2 = 0
for v3 in range(1, math.ceil(((1 + 4 * v1) ** 0.5 - 1) / 2)):
    if (v1 - v3) % v3 == 0:
        v2 += (v1 - v3) // v3
print(int(v2))
