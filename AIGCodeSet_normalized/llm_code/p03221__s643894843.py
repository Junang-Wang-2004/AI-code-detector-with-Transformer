v1, v2 = map(int, input().split())
v3 = []
for v4 in range(v2):
    v3.append([int(i) for v5 in input().split()])
v6 = sorted(v3)
for v5 in range(v2):
    v7 = v6.index(v3[v5])
    v8 = 0
    for v9 in range(0, v7)[::-1]:
        if v6[v9][0] != v6[v7][0]:
            v8 = v9
            break
    if v8 == 0:
        v10 = v7 - v8 + 1
    else:
        v10 = v7 - v8
    print(str(v3[v5][0]).zfill(6) + str(v10).zfill(6))
