v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v5 = list(map(int, input().split()))
v6 = [map(int, input().split()) for v7 in range(v3)]
v8 = min(v4) + min(v5)
for v9 in range(v3):
    v10, v11, v12 = v6[v9]
    v13 = v4[v10 - 1] + v5[v11 - 1] - v12
    if v8 > v13:
        v8 = v13
print(v8)
