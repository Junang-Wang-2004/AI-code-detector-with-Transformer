v1, v2, v3 = map(int, input().split())
v4 = []
v5 = []
for v6 in range(v1):
    v7, v8 = map(int, input().split())
    v4.append(v7)
    v5.append(v8)
v9 = 0
for v6 in range(v1):
    if v5[v6] > 0:
        v10 = (v5[v6] + v3 - 1) // v3
        v9 += v10
        for v11 in range(v6 + 1, v1):
            if v4[v11] <= v4[v6] + v2:
                v5[v11] -= v10 * v3
                if v5[v11] <= 0:
                    v5[v11] = 0
print(v9)
