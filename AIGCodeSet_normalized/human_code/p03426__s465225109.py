v1, v2, v3 = map(int, input().split())
v4 = {}
for v5 in range(v1):
    v6 = list(map(int, input().split()))
    for v7 in range(v2):
        v4[v6[v7] - 1] = (v5, v7)
v8 = [0] * (v1 * v2)
for v5 in range(v1 * v2 - v3):
    v9, v10 = v4[v5]
    v11, v12 = v4[v5 + v3]
    v8[v5 + v3] = v8[v5] + abs(v11 - v9) + abs(v12 - v10)
v13 = int(input())
for v5 in range(v13):
    v14, v15 = map(int, input().split())
    print(v8[v15 - 1] - v8[v14 - 1])
