v1, v2 = map(int, input().split())
v3 = [0 for v4 in range(v2)]
v5 = [0 for v4 in range(v2)]
for v6 in range(v2):
    v3[v6], v5[v6] = map(int, input().split())
v7 = [[0 for v4 in range(v1 + 1)] for v4 in range(v2 + 1)]
for v8 in range(v1 + 1):
    v7[0][v8] = float('inf')
for v6 in range(1, v2 + 1):
    for v8 in range(1, v1 + 1):
        v7[v6][v8] = min(v7[v6 - 1][v8], v7[v6][max(v8 - v3[v6 - 1], 0)] + v5[v6 - 1])
print(v7[v2][v1])
