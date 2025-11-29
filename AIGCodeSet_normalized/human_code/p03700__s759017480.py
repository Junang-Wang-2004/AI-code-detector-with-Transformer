v1, v2, v3 = map(int, input().split())
v4 = 0
v5 = [int(input()) for v6 in range(v1)]
v7 = 0
v8 = 10 ** 9 + 1
v9 = v2 - v3
while v7 != v8:
    v10 = (v7 + v8) // 2
    v11 = 0
    for v12 in range(v1):
        v13 = v5[v12] - v10 * v3
        if v13 > 0:
            v11 += (v13 - 1) // v9 + 1
    if v11 <= v10:
        v8 = v10
    else:
        v7 = v10 + 1
print(v7)
