v1, v2 = map(int, input().split())
v3 = []
v4 = [0]
for v5 in range(1, v1 + 1):
    v6 = [0] + list(map(int, input().split()))
    v7 = []
    for v8 in range(1, v2 + 1):
        if len(v7) == 2:
            v3.append([v5, v8 - 1, v5, v8])
        if v6[v8] % 2 == 1:
            v7 += [v5, v8]
            if len(v7) == 4:
                v7 = []
    if len(v7) == 2:
        v4.append(1)
    else:
        v4.append(0)
v7 = []
for v5 in range(1, v1 + 1):
    if len(v7) == 2:
        v3.append([v5 - 1, v2, v5, v2])
    if v4[v5] % 2 == 1:
        v7 += [v5, v8]
        if len(v7) == 4:
            v7 = []
v9 = len(v3)
print(v9)
for v5 in range(v9):
    print(v3[v5][0], v3[v5][1], v3[v5][2], v3[v5][3])
