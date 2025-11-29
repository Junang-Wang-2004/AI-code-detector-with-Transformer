v1 = 998244353
v2, v3 = map(int, input().split())
v4 = []
v5 = []
for v6 in range(v3):
    v7, v8 = map(int, input().split())
    v4.append([v7, v8])
    v5.append(1 if v7 <= 1 <= v8 else 0)
v9 = [0] * (v2 * 2)
v9[1] = 1
for v10 in range(2, v2 + 1):
    v9[v10] = sum(v5) % v1
    for v11 in range(v3):
        v7, v8 = v4[v11]
        v5[v11] = (v5[v11] + v9[v10 - v7 + 1] - v9[v10 - v8]) % v1
print(v9[v2])
