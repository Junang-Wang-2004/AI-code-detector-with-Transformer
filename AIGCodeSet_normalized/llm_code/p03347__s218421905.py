v1 = int(input())
v2 = [int(input()) for v3 in range(v1)]
v4 = [0] * 200001
v5 = [0] * 200001
for v6 in range(v1):
    v7 = v6 - v2[v6]
    if v7 < 0:
        print(-1)
        exit()
    v4[v7] = max(v4[v7], v2[v6])
v8 = 0
v9 = 0
for v6 in range(200001):
    v9 = max(v9, v4[v6] + v6)
    v5[v6] = v9
for v6 in range(1, v1):
    if v6 <= v5[v6 - v2[v6] - 1]:
        print(-1)
        exit()
v8 = sum(v4)
print(v8)
