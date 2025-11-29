v1 = int(input())
v2 = list(map(int, input().split()))
v3 = 10 ** 9 + 7
v4 = [[0] * 3 for v5 in range(v1 + 1)]
v6 = 1
for v7 in range(v1):
    v8 = v2[v7]
    v9 = v4[v7]
    v10 = 0
    v4[v7 + 1] = v9[:]
    for v11, v12 in enumerate(v9):
        if v8 == v12:
            v10 += 1
            if v10 == 1:
                v4[v7 + 1][v11] = v8 + 1
    if v10 == 0:
        print(0)
        break
    v6 = v6 * v10 % v3
print(v6)
