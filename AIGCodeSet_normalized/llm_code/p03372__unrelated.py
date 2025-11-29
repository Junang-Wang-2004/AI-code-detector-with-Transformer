v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v3.append((v5, v6))
v3.sort(key=lambda x: v5[0])
v7 = [0] * (v1 + 1)
for v8 in range(v1):
    for v9 in range(v8 + 1, v1 + 1):
        v10 = v3[v9 - 1][0] - v3[v8][0]
        if v10 > v2:
            break
        v7[v9] = max(v7[v9], v7[v8] + v3[v9 - 1][1] - v10)
print(v7[v1])
