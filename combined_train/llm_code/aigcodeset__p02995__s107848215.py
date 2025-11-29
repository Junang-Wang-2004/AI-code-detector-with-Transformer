from math import gcd
v1, v2, v3, v4 = map(int, input().split())
v5 = v2 - v2 % v3
if v1 % v3 != 0:
    v6 = v1 - v1 % v3 + v3
else:
    v6 = v1
v7 = v2 - v2 % v4
if v1 % v4 != 0:
    v8 = v1 - v1 % v4 + v4
else:
    v8 = v1
v9 = v3 * v4 // gcd(v3, v4)
v10 = v2 - v2 % v9
if v1 % v9 != 0:
    v11 = v1 - v1 % v9 + v9
else:
    v11 = v1
v12 = (v5 - v6 + v3) // v3
v13 = (v7 - v8 + v4) // v4
v14 = (v10 - v11 + v9) // v9
v15 = v12 + v13 - v14
v16 = v2 - v1 + 1
print(v16 - v15)
