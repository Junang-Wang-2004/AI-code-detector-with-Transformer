v1, v2, v3, v4 = map(int, input().split())
v5 = v2 - v1 + 1
v6 = v3 * v4
v7 = v3
v8 = v4
if v7 < v8:
    v7 = v8
    v8 = v3
v9 = v7 % v8
while v9 != 0:
    v7 = v8
    v8 = v9
    v9 = v7 % v8
v6 //= v8
v5 -= v2 // v3 - (v1 - 1) // v3 + v2 // v4 - (v1 - 1) // v4
v5 += v2 // v6 - (v1 - 1) // v6
print(v5)
