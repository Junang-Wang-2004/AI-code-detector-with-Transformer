v1 = list(input())
v2 = len(v1)
v3 = pow(10, 9) + 7
v4 = pow(10, 5) + 5
v5 = [1] * v4
v6 = [1] * v4
for v7 in range(1, v4):
    v5[v7] = v5[v7 - 1] * 2 % v3
    v6[v7] = v6[v7 - 1] * 3 % v3
v8 = 0
v9 = 0
for v7 in range(v2):
    if v1[v7] == '1':
        v9 += v6[v2 - v7 - 1] * v5[v8] % v3
        v9 %= v3
        v8 += 1
v9 += v5[v8]
v9 %= v3
print(v9)
