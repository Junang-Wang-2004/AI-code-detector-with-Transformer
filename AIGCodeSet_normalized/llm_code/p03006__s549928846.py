v1 = int(input())
v2 = [[int(i) for v3 in input().split()] for v4 in range(v1)]
v5 = []
v6 = []
for v3 in range(v1):
    for v7 in range(v3 + 1, v1):
        v5.append([v2[v3][0] - v2[v7][0], v2[v3][1] - v2[v7][1]])
for v8, v9 in v5:
    v10 = 0
    for v3 in range(v1):
        if v3 == 0:
            v10 += 1
        elif v2[v3][0] - v2[v3 - 1][0] == v8 and v2[v3][1] - v2[v3 - 1][1] == v9:
            v10 += 0
        else:
            v10 += 1
    v6.append(v10)
print(min(v6))
