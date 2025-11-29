import math
v1, v2 = map(int, input().split())
v3 = {}
v4 = 0
v5 = 10 ** 9 + 7
for v6 in range(v2):
    v7 = v2 - v6
    if v7 > v2 / 2:
        v3[v7] = 1
        v4 += v7
    else:
        v8 = pow(v2 // v7, v1, v5)
        v9 = 2
        while v9 * v7 <= v2:
            v8 -= v3[v9 * v7]
            v9 += 1
        v3[v7] = v8 % v5
        v4 = (v4 + v8 * v7 % v5) % v5
print(v4)
