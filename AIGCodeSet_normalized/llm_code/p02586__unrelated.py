from collections import defaultdict
v1, v2, v3 = map(int, input().split())
v4 = defaultdict(list)
for v5 in range(v3):
    v6, v7, v8 = map(int, input().split())
    v4[v6].append((v7, v8))
v9 = [[0 for v5 in range(v2 + 1)] for v5 in range(v1 + 1)]
for v10 in range(1, v1 + 1):
    for v11 in range(1, v2 + 1):
        v9[v10][v11] = max(v9[v10 - 1][v11], v9[v10][v11 - 1])
        for v7, v8 in sorted(v4[v10], reverse=True):
            if v7 <= v11 and len(v4[v10]) <= 3:
                v9[v10][v11] = max(v9[v10][v11], v9[v10][v7 - 1] + v8)
print(v9[v1][v2])
