v1, v2 = list(map(int, input().split()))
v3 = [list(map(int, input().split())) for v4 in range(10)]
v5 = [list(map(int, input().split())) for v4 in range(v1)]
v6 = 0
for v4 in v5:
    for v7 in v4:
        if v7 != -1:
            v6 += v3[v7][1]
print(int(v6))
