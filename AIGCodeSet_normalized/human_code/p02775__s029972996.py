v1 = input()
v2 = len(v1)
v3 = [[0 for v4 in range(2)] for v5 in range(v2)]
v6 = int(v1[v2 - 1])
v3[0][0] = v6
v3[0][1] = 10 - v6
if v2 > 1:
    for v7 in range(1, v2):
        v6 = int(v1[v2 - 1 - v7])
        v3[v7][0] = min(v3[v7 - 1][0] + v6, v3[v7 - 1][1] + v6 + 1)
        v3[v7][1] = min(v3[v7 - 1][0] + 10 - v6, v3[v7 - 1][1] + 10 - v6 - 1)
print(min(v3[v2 - 1][0], v3[v2 - 1][1] + 1))
