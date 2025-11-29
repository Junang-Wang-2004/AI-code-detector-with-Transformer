from fractions import gcd
v1, v2, v3, v4 = map(int, input().split())
v5 = []
for v6 in [v2, v1 - 1]:
    v7 = v6
    v8 = v3 * v4 // gcd(v3, v4)
    v9 = v7 // v3
    v10 = v7 // v4
    v11 = v7 // v8
    v5 += [v7 - v9 - v10 + v11]
print(v5[0] - v5[1])
