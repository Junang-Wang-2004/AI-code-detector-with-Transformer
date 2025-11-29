import math
v1, v2, v3, v4 = map(int, input().split())
v5 = v2 // v3 - v1 // v3
v6 = v2 // v4 - v1 // v4
if v1 % v3 == 0:
    v5 += 1
if v1 % v4 == 0:
    v6 += 1
v7 = v3 * v4 // math.gcd(v3, v4)
v8 = v2 // v7 - v1 // v7
if v1 % v7 == 0:
    v8 += 1
v9 = v2 - v1 + 1 - (v5 + v6 - v8)
print(int(v9))
