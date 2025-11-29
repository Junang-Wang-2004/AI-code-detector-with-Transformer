v1, v2, v3 = map(int, input().split())
v4 = [0 for v5 in range(v1)]
v6 = [0 for v5 in range(v2)]
for v7 in range(v3):
    v8, v9 = map(int, input().split())
    v4[v8 - 1] = v4[v8 - 1] + 1
    v6[v9 - 1] = v6[v9 - 1] + 1
v4.sort()
v6.sort()
print(v4[v1 - 1] + v6[v2 - 1])
