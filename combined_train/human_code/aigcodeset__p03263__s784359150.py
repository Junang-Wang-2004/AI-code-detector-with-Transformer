v1, v2 = map(int, input().split())
v3 = [list(map(int, input().split())) for v4 in range(v1)]
v5 = []
v6 = 0
for v4 in range(v1 - 1):
    for v7 in range(v2):
        if v3[v4][v7] % 2 == 1:
            v3[v4][v7] -= 1
            v3[v4 + 1][v7] += 1
            v5.append([v4 + 1, v7 + 1, v4 + 2, v7 + 1])
            v6 += 1
for v4 in range(v2 - 1):
    if v3[v1 - 1][v4] % 2 == 1:
        v3[v1 - 1][v4] -= 1
        v3[v1 - 1][v4 + 1] += 1
        v5.append([v1, v4 + 1, v1, v4 + 2])
        v6 += 1
print(v6)
for v4 in range(len(v5)):
    for v7 in range(4):
        if v7 != 3:
            print(v5[v4][v7], end=' ')
        else:
            print(v5[v4][v7])
