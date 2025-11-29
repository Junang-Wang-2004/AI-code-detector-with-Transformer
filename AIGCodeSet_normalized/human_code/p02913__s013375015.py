v1 = int(input())
v2 = input()
v3 = [[0] * v1 for v4 in range(v1)]
v5 = 0
for v6 in range(1, v1):
    if v2[v6] == v2[0]:
        v3[0][v6] = 1
        v5 = 1
for v7 in range(1, v1 - 1):
    for v6 in range(v7 + 1, v1):
        if v2[v7] == v2[v6]:
            v3[v7][v6] = min(v3[v7 - 1][v6 - 1] + 1, v6 - v7)
            v5 = max(v3[v7][v6], v5)
        else:
            v3[v7][v6] = 0
print(v5)
