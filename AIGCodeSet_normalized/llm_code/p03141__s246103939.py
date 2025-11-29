v1 = int(input())
v2 = [0] * v1
v3 = [0] * v1
v4 = [0] * v1
v5 = [(0, 0)] * v1
v6 = [(0, 0)] * v1
for v7 in range(v1):
    v8, v9 = map(int, input().split())
    v2[v7] = v8
    v3[v7] = v9
    v5[v7] = (-v8, -v9, v7)
    v6[v7] = (-v9, -v8, v7)
v5.sort()
v6.sort()
v10 = 0
v11 = 0
v8 = 0
v9 = 0
for v7 in range(v1):
    if v7 % 2 == 0:
        while True:
            v12, v12, v13 = v5[v8]
            if v4[v13] == 0:
                v10 += v2[v13]
                v4[v13] = 1
                v8 += 1
                break
            else:
                v8 += 1
    else:
        while True:
            v12, v12, v13 = v6[v9]
            if v4[v13] == 0:
                v11 += v3[v13]
                v4[v13] = 1
                v9 += 1
                break
            else:
                v9 += 1
print(v10 - v11)
