v1 = 10 ** 9 + 7
v2, v3 = map(int, input().split())
v4 = 0
v5 = [0] * (v3 + 1)
for v6 in range(v3, 0, -1):
    v7 = v3 // v6
    v8 = pow(v7, v2, v1)
    v9 = 2
    while v6 * v9 <= v3:
        v8 -= v5[v6 * v9]
        v9 += 1
    v5[v6] = v8
    v4 += v6 * v8
    v4 %= v1
print(v4)
