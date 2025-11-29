v1, v2, v3 = map(int, input().split())
v4 = [-1] * (v3 + 1)
v5 = [0]
v6 = v2
v7 = 0
for v8 in range(1, v1 + 1):
    v7 += v6
    v4[v6] = v8
    v5.append(v6)
    v6 = v6 ** 2 % v3
    if v4[v6] != -1:
        v9 = v8 - v4[v6]
        v10 = v1 - v8
        break
v7 += sum(v5[v4[v6] + 1:v4[v6] + v9 + 1]) * (v10 // v9)
v7 += sum(v5[v4[v6] + 1:v4[v6] + v10 % v9 + 1])
print(v7)
