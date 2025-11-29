v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(10)]
v5 = [list(map(int, input().split())) for v4 in range(v1)]
v6 = 0
for v7 in range(v1):
    for v8 in range(v2):
        if v5[v7][v8] != -1:
            v6 += v3[v5[v7][v8]][1]
print(v6)
