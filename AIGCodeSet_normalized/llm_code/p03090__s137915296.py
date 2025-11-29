v1 = int(input())
if v1 % 2 == 1:
    v2 = v1 // 2
    v3 = [[0] * 2 for v4 in range(v2)]
    v5 = v2 * 4
    v6 = []
    for v7 in range(v2):
        v3[v7][0] = v7 + 1
        v3[v7][1] = v1 - v7
    for v7 in range(v2):
        if v7 == v2 - 1:
            v6.append([v3[v7][0], v3[0][0]])
            v6.append([v3[v7][0], v3[0][1]])
            v6.append([v3[v7][1], v3[0][0]])
            v6.append([v3[v7][1], v3[0][1]])
        else:
            v6.append([v3[v7][0], v3[v7 + 1][0]])
            v6.append([v3[v7][0], v3[v7 + 1][1]])
            v6.append([v3[v7][1], v3[v7 + 1][0]])
            v6.append([v3[v7][1], v3[v7 + 1][1]])
else:
    v2 = v1 // 2
    v3 = [[0] * 2 for v4 in range(v2)]
    v5 = v2 * 4 - 2
    v6 = []
    for v7 in range(v2):
        v3[v7][0] = v7 + 1
        v3[v7][1] = v1 - v7
    for v7 in range(v2):
        if v7 == v2 - 1:
            v6.append([v3[v7][0], v3[0][0]])
            v6.append([v3[v7][1], v3[0][1]])
        else:
            v6.append([v3[v7][0], v3[v7 + 1][0]])
            v6.append([v3[v7][0], v3[v7 + 1][1]])
            v6.append([v3[v7][1], v3[v7 + 1][0]])
            v6.append([v3[v7][1], v3[v7 + 1][1]])
    v6.append([v3[0][0], v3[v2 - 1][1]])
    v6.append([v3[0][1], v3[v2 - 1][0]])
print(v5)
for v8 in range(v5):
    print(v6[v8][0], v6[v8][1])
