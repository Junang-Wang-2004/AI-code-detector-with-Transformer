v1 = int(input())
v2, v3 = ([0] * v1, [0] * v1)
for v4 in range(v1):
    v5, v6 = map(int, input().split())
    v2[v4] = v5
    v3[v4] = v6
v7, v8, v9, v10 = (-1, float('inf'), -1, float('inf'))
for v4 in range(v1):
    v11 = v2[v4] + v3[v4]
    v12 = v2[v4] - v3[v4]
    v7 = max(v7, v11)
    v8 = min(v8, v11)
    v9 = max(v9, v12)
    v10 = min(v10, v12)
v13 = max(v7 - v8, v9 - v10)
print(v13)
