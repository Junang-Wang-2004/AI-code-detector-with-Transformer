v1 = int(input())
v2 = []
v3 = []
v4 = []
for v5 in range(v1):
    v6, v7, v8 = map(int, input().split())
    v2.append(v6)
    v3.append(v7)
    v4.append(v8)
v9 = [[0 for v10 in range(3)] for v10 in range(v1 + 1)]
for v5 in range(1, v1 + 1):
    v9[v5][0] = max(v9[v5 - 1][1], v9[v5 - 1][2]) + v2[v5 - 1]
    v9[v5][1] = max(v9[v5 - 1][0], v9[v5 - 1][2]) + v3[v5 - 1]
    v9[v5][2] = max(v9[v5 - 1][0], v9[v5 - 1][1]) + v4[v5 - 1]
print(max(v9[v1][0], v9[v1][1], v9[v1][2]))
